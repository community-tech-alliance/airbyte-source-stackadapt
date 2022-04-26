#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from abc import ABC
from datetime import datetime
from math import ceil
from typing import Any, Iterable, List, Mapping, MutableMapping, Optional, Tuple

import requests
from airbyte_cdk.sources.streams.http import HttpStream


# Basic full refresh stream
class StackadaptStream(HttpStream, ABC):
    """
    TODO: Add docs
    """

    url_base = "https://api.stackadapt.com/service/v2/"

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
        current_page = response_body["page"]
        total_objects = response_body[self.TOTAL_RESULTS_COUNT_FIELD]
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
    STATS_END_DATE = datetime.utcnow().strftime("%Y-%m-%d")

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
        TODO: Add Docs
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
        TODO: Add Docs.
        :return an iterable containing each record in the response
        """

        stats_response = response.json()
        if stats_response.get(self.TOTAL_STATS_KEY):
            yield from stats_response.get(self.TOTAL_STATS_KEY)
        yield from stats_response.get(self.TIME_BASED_STATS_KEY, [])


class Campaigns(StackadaptStream):
    """
    TODO: Add Doc to this class
    """

    # Constants and Parameters
    primary_key = "id"
    page_size = 30
    TOTAL_RESULTS_COUNT_FIELD = "total_campaigns"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        """
        TODO: Override this method to define the path this stream corresponds to. E.g. if the url is https://example-api.com/v1/customers then this
        should return "customers". Required.
        """
        return "campaigns"


class LineItems(StackadaptStream):
    """
    TODO: Add Doc to this class
    """

    primary_key = "id"
    page_size = 30
    TOTAL_RESULTS_COUNT_FIELD = "total_line_items"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "line_items"


class Advertisers(StackadaptStream):
    """
    TODO: Add Doc to this class
    """

    primary_key = "id"
    page_size = 30
    TOTAL_RESULTS_COUNT_FIELD = "total_advertisers"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "advertisers"


class ConversionTrackers(StackadaptStream):
    """
    TODO: Add Doc to this class
    """

    primary_key = "id"
    page_size = 30
    TOTAL_RESULTS_COUNT_FIELD = "total_conversion_trackers"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "conversion_trackers"


class NativeAds(StackadaptStream):
    """
    TODO: Add Doc to this class
    """

    primary_key = "id"
    page_size = 60
    TOTAL_RESULTS_COUNT_FIELD = "total_native_ads"

    def path(
        self,
        stream_state: Mapping[str, Any] = None,
        stream_slice: Mapping[str, Any] = None,
        next_page_token: Mapping[str, Any] = None
    ) -> str:
        return "native_ads"


class AccountCampaignsStats(StackadaptStatStream):
    """
    TODO: Add Doc to this class
    """
    # Constants
    primary_key = "campaign_id"
    GROUP_BY_RESOURCE = "campaign"


class AccountLineItemsStats(StackadaptStatStream):
    """
    TODO: Add Doc to this class
    """
    # Constants
    primary_key = "line_item"
    GROUP_BY_RESOURCE = "line_item"


class AccountNativeAdsStats(StackadaptStatStream):
    """
    TODO: Add Doc to this class
    """
    # Constants
    primary_key = "native_ad_id"
    GROUP_BY_RESOURCE = "native_ad"


# Basic incremental stream
# TODO: Make Stats Incremental Streams, Remove these example streams
class IncrementalStackadaptStream(StackadaptStream, ABC):
    """
    TODO fill in details of this class to implement functionality related to incremental syncs for your connector.
         if you do not need to implement incremental sync for any streams, remove this class.
    """

    # TODO: Fill in to checkpoint stream reads after N records. This prevents re-reading of data if the stream fails for any reason.
    state_checkpoint_interval = None

    @property
    def cursor_field(self) -> str:
        """
        TODO
        Override to return the cursor field used by this stream e.g: an API entity might always use created_at as the cursor field. This is
        usually id or date based. This field's presence tells the framework this in an incremental stream. Required for incremental.

        :return str: The name of the cursor field.
        """
        return []

    def get_updated_state(self, current_stream_state: MutableMapping[str, Any], latest_record: Mapping[str, Any]) -> Mapping[str, Any]:
        """
        Override to determine the latest state after reading the latest record. This typically compared the cursor_field from the latest record and
        the current state and picks the 'most' recent cursor. This is how a stream's state is determined. Required for incremental.
        """
        return {}

class Employees(IncrementalStackadaptStream):
    """
    TODO: Change class name to match the table/data source this stream corresponds to.
    """

    # TODO: Fill in the cursor_field. Required.
    cursor_field = "start_date"

    # TODO: Fill in the primary key. Required. This is usually a unique field in the stream, like an ID or a timestamp.
    primary_key = "employee_id"

    def path(self, **kwargs) -> str:
        """
        TODO: Override this method to define the path this stream corresponds to. E.g. if the url is https://example-api.com/v1/employees then this should
        return "single". Required.
        """
        return "employees"

    def stream_slices(self, stream_state: Mapping[str, Any] = None, **kwargs) -> Iterable[Optional[Mapping[str, any]]]:
        """
        TODO: Optionally override this method to define this stream's slices. If slicing is not needed, delete this method.

        Slices control when state is saved. Specifically, state is saved after a slice has been fully read.
        This is useful if the API offers reads by groups or filters, and can be paired with the state object to make reads efficient. See the "concepts"
        section of the docs for more information.

        The function is called before reading any records in a stream. It returns an Iterable of dicts, each containing the
        necessary data to craft a request for a slice. The stream state is usually referenced to determine what slices need to be created.
        This means that data in a slice is usually closely related to a stream's cursor_field and stream_state.

        An HTTP request is made for each returned slice. The same slice can be accessed in the path, request_params and request_header functions to help
        craft that specific request.

        For example, if https://example-api.com/v1/employees offers a date query params that returns data for that particular day, one way to implement
        this would be to consult the stream state object for the last synced date, then return a slice containing each date from the last synced date
        till now. The request_params function would then grab the date from the stream_slice and make it part of the request by injecting it into
        the date query param.
        """
        raise NotImplementedError("Implement stream slices or delete this method!")
