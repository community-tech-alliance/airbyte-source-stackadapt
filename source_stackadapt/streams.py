#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from datetime import datetime, timedelta
from math import ceil
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional

import requests
from airbyte_cdk.sources.streams.http import HttpStream
from airbyte_cdk.logger import AirbyteLogger

logger = AirbyteLogger()

# Basic full refresh stream
class StackadaptStream(HttpStream, ABC):
    """
    Base StackAdapt stream class. All StackAdapt streams will inherit from this base class.
    Includes logic for authenticating to the stackadapt API, and pagination strategy.
    """

    url_base = "https://api.stackadapt.com/service/v2/"

    @property
    def total_results_count_field(self) -> str:
        """
        Property for storing the name of the field in the API response that contains
        the total number of results.
        """

    def __init__(self, api_key: str, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key

    def request_headers(
        self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, Any] = None, next_page_token: Mapping[str, Any] = None
    ) -> Mapping[str, Any]:
        return {
            "X-Authorization": self.api_key,
            "Content-Type": "application/json"
        }

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        """
        Determines if there are any more pages left to iterate through for request.

        :param response: the most recent response from the API
        :return If there is another page in the result, a mapping (e.g: dict) containing information needed to query the next page in the response.
                If there are no more pages in the result, return None.
        """
        response_body = response.json()
        
        # Determine if there are any more pages left
        current_page = response_body.get("page", 1)
        current_page = current_page if current_page else 1
        
        total_objects = response_body.get(self.total_results_count_field, 0)
        total_objects = total_objects if total_objects else 0

        total_pages = ceil(total_objects/self.page_size)
        
        if current_page < total_pages:
            return {"page": current_page + 1}
        return None

    def request_params(
        self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, any] = None, next_page_token: Mapping[str, Any] = None
    ) -> MutableMapping[str, Any]:
        """
        Only needed params, excluding the 'stats' endpoint, is page number for response. 
        """
        if next_page_token:
            return next_page_token
        return {}

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        """
        Default response parsing for StackAdapt APIs. For all GET methods, excluding 'stats' endpoint, 
        object data will be in the 'data' field of the response.
        
        :return an iterable containing each record in the response
        """

        response_json = response.json()
        yield from response_json.get("data", [])


class StackadaptStatStream(StackadaptStream):
    """
    Base Stream for streams that use the 'stats' StackAdapt endpoint. This endpoint behaves different than other GET endpoints
    and has a seperate class for unique logic. The 'stats' endpoint works by taking in a number of query parameters to retrieve
    statistics. The response object of the endpoint varies by the given parameters. For more information please refer to the 
    StackAdapt Docs - https://docs.stackadapt.com/#!/stats/getStats

    Note: Currently the only supported 'stats' streams set the resource to 'buyer_account' to get stats for all resources the 
    account has access to. The streams are created by using the 'group_by_resource' field to get account wide stats for specific
    resources (campaigns, line items, and native ads).
    """
    # Constants
    ACCOUNT_RESOURCE_TYPE = "buyer_account"  # Default to grab stats for entire account
    GROUP_BY_RESOURCE = ""                   # Resource to group by. One of: campaign, line_item, native_ad
    TIME_BASED_STATS_KEY = "daily_stats"
    TOTAL_STATS_KEY = "individual_total_stats"
    STATS_END_DATE = datetime.utcnow().date() - timedelta(days=1)  # Only gets stats up until previous day. (Current day stats may be incomplete depending on when sync is ran)

    def __init__(self, stat_type: str, start_date: str, **kwargs):
        super().__init__(**kwargs)
        self.stat_type = stat_type
        self.start_date = start_date

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        """
        The 'stats' endpoint does not have any pagination.

        :param response: the most recent response from the API
        :return If there is another page in the result, a mapping (e.g: dict) containing information needed to query the next page in the response.
                If there are no more pages in the result, return None.
        """
        return None
    
    def request_params(
        self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, any] = None, next_page_token: Mapping[str, Any] = None
    ) -> MutableMapping[str, Any]:
        """
        The query params for the 'stat' endpoint are used to request stats for different resources/types. For more
        information check out the Stackadapt docs: https://docs.stackadapt.com/#!/stats/getStats

        Currently, only 'buyer_account' stats that are grouped by campaign, line item, or native ad are supported.
        """
        stats_query_params = {
            "resource": self.ACCOUNT_RESOURCE_TYPE,
            "type": self.stat_type,
            "group_by_resource": self.GROUP_BY_RESOURCE
        }
        # Only add optional params if provided
        if self.start_date:
            stats_query_params["start_date"] = self.start_date
            stats_query_params["end_date"] = self.STATS_END_DATE

        return stats_query_params
    
    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "stats"

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        """
        Depending on the stat 'type', the response objects will be under a different key.
        Time based stat types will have results under the 'daily_stats' key and
        total stat type will have results in the 'individual_total_stats' key.

        :param response: the response object from the most recent API call
        :return an iterable containing each record in the response
        """

        stats_response = response.json()
        if stats_response.get(self.TOTAL_STATS_KEY):
            yield from stats_response.get(self.TOTAL_STATS_KEY)
        yield from stats_response.get(self.TIME_BASED_STATS_KEY, [])


class Campaigns(StackadaptStream):
    """
    Returns all campaigns from the system that the user has access to.
    https://docs.stackadapt.com/#!/campaign/findCampaigns
    """

    # Constants and Parameters
    primary_key = "id"
    page_size = 30
    total_results_count_field = "total_campaigns"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "campaigns"


class LineItems(StackadaptStream):
    """
    Returns all line items (Campaign Groups) from the system that the user has access to.
    https://docs.stackadapt.com/#!/line_item/findLineItems
    """

    primary_key = "id"
    page_size = 30
    total_results_count_field = "total_line_items"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "line_items"


class Advertisers(StackadaptStream):
    """
    Returns all advertisers from the system that the user has access to.
    https://docs.stackadapt.com/#!/advertiser/findAdvertisers
    """

    primary_key = "id"
    page_size = 30
    total_results_count_field = "total_advertisers"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "advertisers"


class ConversionTrackers(StackadaptStream):
    """
    Returns all conversion trackers from the system that the user has access to.
    https://docs.stackadapt.com/#!/conversion_trackers/findConversionTrackers
    """

    primary_key = "id"
    page_size = 30
    total_results_count_field = "total_conversion_trackers"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "conversion_trackers"


class NativeAds(StackadaptStream):
    """
    Returns all native ads from the system that the user has access to.
    https://docs.stackadapt.com/#!/native_ad/findNativeAds
    """

    primary_key = "id"
    page_size = 60
    total_results_count_field = "total_native_ads"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "native_ads"


# Basic incremental stream
class IncrementalStackadaptStatStream(StackadaptStream):
    """
    Base Incremental Stackadapt stream
    """
    # Constants
    DEFAULT_DATE_FORMAT = "%Y-%m-%d"
    TIME_BASED_STATS_KEY = "daily_stats"
    ACCOUNT_RESOURCE_TYPE = "buyer_account"  # Default to grab stats for entire account
    GROUP_BY_RESOURCE = ""                   # Resource to group by. One of: campaign, line_item, native_ad
    STAT_TYPE = "daily"                      # For now only daily stats is available
    STATS_END_DATE = datetime.utcnow().date() - timedelta(days=1)  # Only gets stats up until previous day. (Current day stats may be incomplete depending on when sync is ran)
    
    cursor_field = "date"

    def __init__(self, start_date: str, **kwargs):
        super().__init__(**kwargs)
        self.start_date = datetime.strptime(start_date, self.DEFAULT_DATE_FORMAT)
        self._cursor_value = None

    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, Any]:
        """
        Compares the date of the current record with the date saved on the stream state. 
        If the date on the record is greater than the state, then update state. (Note: this seems to be called after each stream slice)
        """
        # Get date from the stream state if it exists. If it doesnt exists, that means this stream hasnt saved a state yet and 
        # we should use the input 'start_date' for stream state
        current_stream_state = current_stream_state or {}
        current_state_date = self.start_date
        if current_stream_state.get(self.cursor_field):
            current_state_date = datetime.strptime(current_stream_state[self.cursor_field], self.DEFAULT_DATE_FORMAT)

        # Compare the date on the current record and if it is greater than the date on the current stream state,
        # update the stream state date with current record date
        current_stream_state[self.cursor_field] = max(
            datetime.strptime(latest_record[self.cursor_field], self.DEFAULT_DATE_FORMAT),
            current_state_date
        ).strftime(self.DEFAULT_DATE_FORMAT)

        return current_stream_state

    def stream_slices(self, sync_mode, cursor_field: List[str] = None, stream_state: Mapping[str, Any] = None) -> Iterable[Optional[Mapping[str, Any]]]:
        """
        Returns a slice for the date range that data should be pulled. This currently will pull the date from the stream state
        to use as the start date for the slice. End date for the slice will be 'STATS_END_DATE': the day before the sync is ran.
        The thinking behind this is that we should pull daily stats for the current date since they may be incomplete depending on when sync is running.

        This also means that each sync run will result in a single slice and API request. We can modify this to a different strategy,
        but this started running into issues when trying to do daily slices (1 API request per day) for initial load.
        """
        slices = []
        stream_state = stream_state or {}

        # Check to see if there is an existing stream state we should pick up from
        # if not just pull data from 'start_date'
        slice_start_date = self.start_date
        if stream_state.get(self.cursor_field):
            slice_start_date = (
                datetime.strptime(stream_state[self.cursor_field], self.DEFAULT_DATE_FORMAT) + timedelta(days=1)
            )
        
        # To reduce number of requests we are making, only create a single slice with data we have not yet pulled.
        # Basically, pull data from the date in stream state or from 'start_date' if no stream state (hasnt ran yet)
        if slice_start_date.date() <= self.STATS_END_DATE:
            slices.append({
                "start_date": datetime.strftime(slice_start_date, self.DEFAULT_DATE_FORMAT),
                "end_date": datetime.strftime(self.STATS_END_DATE, self.DEFAULT_DATE_FORMAT)
            })
        logger.info(f"Request Stream Slices: {slices}")
        return slices

    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        """
        The 'stats' endpoint does not have any pagination.
        """
        return None
    
    def request_params(
        self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, any] = None, next_page_token: Mapping[str, Any] = None
    ) -> MutableMapping[str, Any]:
        """
        The query params for the 'stat' endpoint are used to request stats for different resources/types. For more
        information check out the Stackadapt docs: https://docs.stackadapt.com/#!/stats/getStats

        Currently, only 'buyer_account' stats that are grouped by campaign, line item, or native ad are supported.
        """
        stats_query_params = {
            "resource": self.ACCOUNT_RESOURCE_TYPE,
            "type": self.STAT_TYPE,
            "group_by_resource": self.GROUP_BY_RESOURCE,
            "start_date": stream_slice["start_date"],
            "end_date": stream_slice["end_date"],
        }
        logger.info(f"Query Params: {stats_query_params}")

        return stats_query_params
    
    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "stats"
    
    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        """
        Parses the response object and yields records if there are returned records from source.
        Note: The API will return 'daily_stat': None if no data was found for given time range.

        :param response: the response object from the most recent API call
        :return an iterable containing each record in the response
        """
        stats_response = response.json()

        # Yield from response only if there is available data
        daily_stats = stats_response.get(self.TIME_BASED_STATS_KEY)
        yield from daily_stats if daily_stats else []

class AccountCampaignsStats(IncrementalStackadaptStatStream):
    """
    Returns stats on all the campaigns a user has access to.
    Stats can be either 'total' stats per campaign, or 'daily' stats for each campaign.
    """
    # Constants
    primary_key = "campaign_id"
    GROUP_BY_RESOURCE = "campaign"

class AccountLineItemsStats(IncrementalStackadaptStatStream):
    """
    Returns stats on all the line items a user has access to.
    Stats can be either 'total' stats per line item, or 'daily' stats for each line item.

    Note: the response schema for this stream does not contain the line_item_id, it only contains name
    """
    # Constants
    primary_key = "line_item"
    GROUP_BY_RESOURCE = "line_item"


class AccountNativeAdsStats(IncrementalStackadaptStatStream):
    """
    Returns stats on all the native ads a user has access to.
    Stats can be either 'total' stats per native ad, or 'daily' stats for each native ad.
    """
    # Constants
    primary_key = "native_ad_id"
    GROUP_BY_RESOURCE = "native_ad"
