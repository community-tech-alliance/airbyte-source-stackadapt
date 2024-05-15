#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#

from .schemas import (
    account_campaigns_stats_schema,
    account_line_items_stats_schema,
    account_native_ads_stats_schema,
    advertisers_schema,
    campaigns_schema,
    conversion_trackers_schema,
    line_items_schema,
    native_ads_schema
)
from typing import Any, List, Mapping, Tuple

import json
import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream
from airbyte_cdk.logger import AirbyteLogger
from airbyte_cdk.models import (
    AirbyteCatalog,
    AirbyteStream,
)

from source_stackadapt.streams import (
    Campaigns,
    LineItems,
    Advertisers,
    ConversionTrackers,
    NativeAds,
    AccountCampaignsStats,
    AccountLineItemsStats,
    AccountNativeAdsStats
)

# Source
class SourceStackadapt(AbstractSource):
    def check_connection(self, logger, config) -> Tuple[bool, any]:
        """
        Checks to see if a connection to StackAdapt API can be created with given credentials.

        :param config:  the user-input config object conforming to the connector's spec.json
        :param logger:  logger object
        :return Tuple[bool, any]: (True, None) if the input config can be used to connect to the API successfully, (False, error) otherwise.
        """
        connection_url = "https://api.stackadapt.com/service/v2/campaigns"
        headers = {
            "X-Authorization": f"{config['api_key']}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(
                url=connection_url,
                headers=headers
            )
            response.raise_for_status()
            return True, None
        except Exception as e:
            return False, e
        

    def discover(self, logger: AirbyteLogger, config: json) -> AirbyteCatalog:
        """
        Returns an AirbyteCatalog representing the available streams and fields in this integration.
        For example, given valid credentials to a Postgres database,
        returns an Airbyte catalog where each postgres table is a stream, and each table column is a field.

        :param logger: Logging object to display debug/info/error to the logs
            (logs will not be accessible via airbyte UI if they are not passed to this logger)
        :param config: Json object containing the configuration of this source, content of this json is as specified in
        the properties of the spec.json file

        :return: AirbyteCatalog is an object describing a list of all available streams in this source.
            A stream is an AirbyteStream object that includes:
            - its stream name (or table name in the case of Postgres)
            - json_schema providing the specifications of expected schema for this stream (a list of columns described
            by their names and types)
        """
        streams = []

        streams.append(AirbyteStream(name="account_campaigns_stats", json_schema=account_campaigns_stats_schema, supported_sync_modes=["full_refresh","incremental"]))
        streams.append(AirbyteStream(name="account_line_items_stats", json_schema=account_line_items_stats_schema, supported_sync_modes=["full_refresh","incremental"]))
        streams.append(AirbyteStream(name="account_native_ads_stats", json_schema=account_native_ads_stats_schema, supported_sync_modes=["full_refresh","incremental"]))
        streams.append(AirbyteStream(name="advertisers", json_schema=advertisers_schema, supported_sync_modes=["full_refresh"]))
        streams.append(AirbyteStream(name="campaigns", json_schema=campaigns_schema, supported_sync_modes=["full_refresh"]))
        streams.append(AirbyteStream(name="conversion_trackers", json_schema=conversion_trackers_schema, supported_sync_modes=["full_refresh"]))
        streams.append(AirbyteStream(name="line_items", json_schema=line_items_schema, supported_sync_modes=["full_refresh"]))
        streams.append(AirbyteStream(name="native_ads", json_schema=native_ads_schema, supported_sync_modes=["full_refresh"]))

        return AirbyteCatalog(streams=streams)        

    def streams(self, config: Mapping[str, Any]) -> List[Stream]:
        """
        :param config: A Mapping of the user input configuration as defined in the connector spec.
        """
        return [
            Campaigns(api_key=config["api_key"]),
            LineItems(api_key=config["api_key"]),
            Advertisers(api_key=config["api_key"]),
            ConversionTrackers(api_key=config["api_key"]),
            NativeAds(api_key=config["api_key"]),
            AccountCampaignsStats(
                api_key=config["api_key"],
                start_date=config.get("start_date"),
            ),
            AccountLineItemsStats(
                api_key=config["api_key"],
                start_date=config.get("start_date"),
            ),
            AccountNativeAdsStats(
                api_key=config["api_key"],
                start_date=config.get("start_date"),
            )
        ]
