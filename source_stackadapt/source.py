#
# Copyright (c) 2021 Airbyte, Inc., all rights reserved.
#


from typing import Any, List, Mapping, Tuple

import requests
from airbyte_cdk.sources import AbstractSource
from airbyte_cdk.sources.streams import Stream

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
                stat_type=config["stat_type"],
                start_date=config.get("start_date"),
            ),
            AccountLineItemsStats(
                api_key=config["api_key"],
                stat_type=config["stat_type"],
                start_date=config.get("start_date"),
            ),
            AccountNativeAdsStats(
                api_key=config["api_key"],
                stat_type=config["stat_type"],
                start_date=config.get("start_date"),
            )
        ]
