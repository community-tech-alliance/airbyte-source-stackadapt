#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from datetime import datetime, timedelta
from math import ceil
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional

import requests
from airbyte_cdk.models import SyncMode
from airbyte_cdk.sources.streams.core import IncrementalMixin
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
            "X-Authorization": self.api_key
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
    # Use cache so that Stats streams can use cached stream data instead of making another API call
    use_cache = True

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

class DeliveryStatStream(StackadaptStream):
    """
    Base Stream for streams that use the 'delivery' stats StackAdapt endpoint. This endpoint behaves different than other GET endpoints
    and has a seperate class for unique logic. The 'delivery' endpoint works by taking in a number of query parameters to retrieve
    statistics. The response object of the endpoint varies by the given parameters. For more information please refer to the 
    StackAdapt Docs - https://docs.stackadapt.com/#!/Stats/getDeliveryStats

    NOTE: Currently this stream only supports getting delivery stats at the 'Advertiser' level with additional granularity with the 'group_by_resource' argument.
    It will use the Advertisers stream to get stats for all advertiser IDs retrieved from the Advertiser stream. Substreams of this base stream can change the granularity
    by specifying the 'group_by_resource', 'date_range_type', and 'type' parameters.
    """
    # Constants
    DEFAULT_DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, start_date: str, **kwargs):
        super().__init__(**kwargs)
        self.advertisers_stream = Advertisers(**kwargs)
        self.start_date = datetime.strptime(start_date, self.DEFAULT_DATE_FORMAT)
        self.end_date = datetime.utcnow() - timedelta(days=1)  # Only gets stats up until previous day. (Current day stats may be incomplete depending on when sync is ran)
    
    @property
    def resource_type(self):
        """
        Override to change the top level resource type for delivery stats.
        """
        return "advertiser"
    
    @property
    def group_by_resource(self):
        """
        Override to specify what resource type to group by. This will lower the granularity
        that stats are returned by (Line Item, Campaign, or Native Ad level)
        
        Must be one of: 'line_item', 'campaign', 'native_ad'
        """
        return None

    @property
    def stat_type(self):
        """
        Override to specify the 'type' of stats you would like to request. This is to specify
        if you want stats split by daily, hourly, or aggregated total interval.

        Must be one of: 'total', 'daily', 'hourly'
        """
        return "total"
    
    @property
    def date_range_type(self):
        """
        Override to specify the date range type stats should be returned in. This can either be 
        'all_time' - returns stats for given resource that are available for all time
        'custom' - Used to specify that you will pass in a custom date range stats should be returned
                   for. This requires 'start_date' and 'end_date params' to be passed in. 
        
        NOTE: All stats streams will use the 'custom' date_range_type since they are incremental streams
              that will pull data daily. 
        """
        return "all_time"

    def _get_stats_key(self):
        """
        Returns the key in which stats can be found in API response object if stat_type is 'total'.
        If stats type is something other than 'total', then stats will be found directly in the
        top level 'stats' object.
        """
        # If stat type is total, stats will be returned under different keys
        if self.stat_type == "total":
            # If custom date range is given, stats will be returned for every day in given range under 'daily_stats'
            if self.date_range_type == "custom":
                return "daily_stats"
            elif self.group_by_resource:
                return "individual_total_stats"
            else:
                return "total_stats"
        return None

    def stream_slices(
        self, sync_mode: SyncMode, cursor_field: List[str] = None, stream_state: Mapping[str, Any] = None
    ) -> Iterable[Optional[Mapping[str, Any]]]:
        """
        Create Stream Slices for each Advertiser ID.
        """
        for record in self.advertisers_stream.read_records(sync_mode=SyncMode.full_refresh):
            logger.info(f"Slice forAdvertiser ID: {record['id']}")
            yield {
                "advertiser_id": record["id"],
                "start_date": self.start_date.strftime(self.DEFAULT_DATE_FORMAT),
                "end_date": self.end_date.strftime(self.DEFAULT_DATE_FORMAT)
            }


    def next_page_token(self, response: requests.Response) -> Optional[Mapping[str, Any]]:
        """
        The 'delivery' endpoint does not have any pagination.

        :param response: the most recent response from the API
        :return If there is another page in the result, a mapping (e.g: dict) containing information needed to query the next page in the response.
                If there are no more pages in the result, return None.
        """
        return None
    
    def request_params(
        self, stream_state: Mapping[str, Any], stream_slice: Mapping[str, any] = None, next_page_token: Mapping[str, Any] = None
    ) -> MutableMapping[str, Any]:
        """
        The query params for the 'delivery' endpoint are used to request stats for different resources/types. For more
        information check out the Stackadapt docs: https://docs.stackadapt.com/#!/stats/getStats

        Currently, only 'advertiser' level stats that are grouped by campaign, line item, or native ad are supported.
        """
        advertiser_id = stream_slice["advertiser_id"]
        stats_query_params = {
            "resource_type": self.resource_type,
            "type": self.stat_type,
            "id": advertiser_id,
            "date_range_type": self.date_range_type
        }
        # Only add optional params if provided
        if self.date_range_type == "custom":
            stats_query_params["start_date"] = stream_slice.get("start_date")
            stats_query_params["end_date"] = stream_slice.get("end_date")
        if self.group_by_resource:
            stats_query_params["group_by_resource"] = self.group_by_resource

        logger.info(f"Making Request with the following Query Params: {stats_query_params}")

        return stats_query_params
    
    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "delivery"

    def parse_response(self, response: requests.Response, **kwargs) -> Iterable[Mapping]:
        """
        Depending on the stat 'type', the response objects will be under a different key.
        'daily' and 'hourly' stat types will have results directly in the 'stats' object.
        'total' stat type will have results in a nested key that depends on other inputs.
        Note: The API will return 'stats': None if no data was found for given time range.

        :param response: the response object from the most recent API call
        :return an iterable containing each record in the response
        """

        stats_response = response.json()
        stats_key = self._get_stats_key()

        # If stats type is 'total' stats will be nested in 'stats' object
        if stats_key:
            stats = stats_response["stats"].get(stats_key)
            # Make sure stats is an array before yielding
            stats = [stats] if not isinstance(stats, list) else stats
            
        # If stats type is 'daily' or 'hourly', stats will be a list under 'stats' object
        else:
            stats = stats_response["stats"]
        
        # Its possible for 'stats' to be None, if it is yield from empty list
        yield from stats if stats else []


class IncrementalDeliveryStatStream(DeliveryStatStream, IncrementalMixin):
    """
    Base Incremental Stream for the StackAdapt `delivery` endpoint. 
    This stream incrementally loads stat by saving the latest 'date' seen
    in a record to state. It will then grab that date from state and only 
    request records newer than that date.
    """

    cursor_field = "date"

    def __init__(self, start_date: str, **kwargs):
        super().__init__(start_date, **kwargs)
        self._cursor_value = None

    @property
    def state(self) -> Mapping[str, Any]:
        if self._cursor_value:
            return {self.cursor_field: self._cursor_value.strftime(self.DEFAULT_DATE_FORMAT)} 
        else:
            return {self.cursor_field: self.start_date.strftime(self.DEFAULT_DATE_FORMAT)}

    @state.setter
    def state(self, value: Mapping[str, Any]):
        self._cursor_value = datetime.strptime(value[self.cursor_field], self.DEFAULT_DATE_FORMAT)
    
    def stream_slices(
        self, sync_mode: SyncMode,
        cursor_field: List[str] = None,
        stream_state: Mapping[str, Any] = None
    ) -> Iterable[Optional[Mapping[str, Any]]]:
        """
        Override the stream slices method to update start_date from stream state
        """
        for record in self.advertisers_stream.read_records(sync_mode=SyncMode.full_refresh):
            # Figure out start_date based on stream_state
            slice_start_date = self.start_date
            # If stream date is not equal to start_date, then it has been incremented and start_date = stream state date
            if stream_state and self.cursor_field in stream_state:
                slice_start_date = (
                    datetime.strptime(stream_state[self.cursor_field], self.DEFAULT_DATE_FORMAT) + timedelta(days=1)
                )
            if slice_start_date <= self.end_date:
                logger.info(f"Slice for Advertiser ID: {record['id']} | Start Date: {slice_start_date} | End Date: {self.end_date}")
                yield {
                    "advertiser_id": record["id"],
                    "start_date": slice_start_date.strftime(self.DEFAULT_DATE_FORMAT),
                    "end_date": self.end_date.strftime(self.DEFAULT_DATE_FORMAT)
                }
    
    def read_records(
        self,
        sync_mode: SyncMode,
        cursor_field: List[str] = None,
        stream_slice: Mapping[str, Any] = None,
        stream_state: Mapping[str, Any] = None,
    ) -> Iterable[Mapping[str, Any]]:
        for record in super().read_records(
            sync_mode=sync_mode, cursor_field=cursor_field, stream_slice=stream_slice, stream_state=stream_state
        ):
            yield record
            # Update State with latest date 
            record_date = datetime.strptime(record[self.cursor_field], self.DEFAULT_DATE_FORMAT)
            stream_state_date = self._cursor_value if self._cursor_value else self.start_date
            self._cursor_value = max(stream_state_date, record_date)
    

class AccountCampaignsStats(IncrementalDeliveryStatStream):
    """
    Returns stats on all the campaigns a user has access to.
    Stats can be either 'total' stats per campaign, or 'daily' stats for each campaign.
    """
    # Constants
    group_by_resource = "campaign"
    stat_type = "daily"
    date_range_type = "custom"
    primary_key = None


class AccountLineItemsStats(IncrementalDeliveryStatStream):
    """
    Returns stats on all the line items a user has access to.
    Stats can be either 'total' stats per line item, or 'daily' stats for each line item.

    Note: the response schema for this stream does not contain the line_item_id, it only contains name
    """
    # Constants
    group_by_resource = "line_item"
    stat_type = "daily"
    date_range_type = "custom"
    primary_key = None


class AccountNativeAdsStats(IncrementalDeliveryStatStream):
    """
    Returns stats on all the native ads a user has access to.
    Stats can be either 'total' stats per native ad, or 'daily' stats for each native ad.
    """
    # Constants
    group_by_resource = "native_ad"
    stat_type = "daily"
    date_range_type = "custom"
    primary_key = None
