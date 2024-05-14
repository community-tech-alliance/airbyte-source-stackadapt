import json

account_campaigns_stats_schema = json.loads(
"""
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "atos": {
      "type": ["number", "null"],
      "description": "The average time on site"
    },
    "atos_units": {
      "type": ["number", "null"],
      "description": "The average time on site"
    },
    "campaign": {
      "type": ["string", "null"]
    },
    "campaign_custom_fields": {
      "type": ["string", "null"]
    },
    "campaign_id": {
      "type": ["integer", "null"]
    },
    "campaign_type": {
      "type": ["string", "null"]
    },
    "channel": {
      "type": ["string", "null"]
    },
    "click": {
      "type": ["integer", "null"],
      "description": "Clicks"
    },
    "conv": {
      "type": ["integer", "null"],
      "description": "Conversions"
    },
    "conv_click": {
      "type": ["integer", "null"]
    },
    "conv_click_time_avg": {
      "type": ["number", "null"]
    },
    "conv_cookie": {
      "type": ["integer", "null"],
      "description": "Conversion cookie."
    },
    "conv_imp_derived": {
      "type": ["integer", "null"],
      "description": "Conversions attributed from impressions"
    },
    "conv_imp_time_avg": {
      "type": ["number", "null"]
    },
    "conv_ip": {
      "type": ["integer", "null"]
    },
    "cost": {
      "type": ["number", "null"],
      "description": "Media cost"
    },
    "ctr": {
      "type": ["number", "null"],
      "description": "Click-through rate"
    },
    "cvr": {
      "type": ["number", "null"],
      "description": "Conversion rate"
    },
    "date": {
      "type": ["string", "null"],
      "description": "Date"
    },
    "ecpa": {
      "type": ["number", "null"],
      "description": "Effective cost per action"
    },
    "ecpc": {
      "type": ["number", "null"],
      "description": "Effective cost per click"
    },
    "ecpe": {
      "type": ["number", "null"],
      "description": "Effective cost per engagement"
    },
    "ecpm": {
      "type": ["number", "null"],
      "description": "Effective cost per mille"
    },
    "ecpcl": {
      "type": ["number", "null"]
    },
    "ecpv": {
      "type": ["number", "null"],
      "description": "Effective cost per view"
    },
    "end_date": {
      "type": ["string", "null"]
    },
    "imp": {
      "type": ["integer", "null"],
      "description": "Impressions"
    },
    "line_item": {
      "type": ["string", "null"]
    },
    "line_item_id": {
      "type": ["integer", "null"]
    },
    "ltr": {
      "type": ["number", "null"]
    },
    "page_start": {
      "type": ["integer", "null"]
    },
    "page_time": {
      "type": ["integer", "null"],
      "description": "Total time"
    },
    "page_time_15s": {
      "type": ["integer", "null"],
      "description": "Engagements"
    },
    "page_time_units": {
      "type": ["integer", "null"]
    },
    "profit": {
      "type": ["number", "null"]
    },
    "rcpc": {
      "type": ["number", "null"]
    },
    "rcpcl": {
      "type": ["number", "null"]
    },
    "rcpe": {
      "type": ["number", "null"]
    },
    "rcpm": {
      "type": ["number", "null"]
    },
    "revenue": {
      "type": ["number", "null"]
    },
    "roas": {
      "type": ["number", "null"],
      "description": "Return on ad spend"
    },
    "s_conv": {
      "type": ["integer", "null"],
      "description": "Secondary conversions"
    },
    "start_date": {
      "type": ["string", "null"]
    },
    "sub_advertiser": {
      "type": ["string", "null"]
    },
    "sub_advertiser_id": {
      "type": ["integer", "null"]
    },
    "tp_cpm_cost": {
      "type": ["number", "null"],
      "description": "Third-party CPM cost"
    },
    "tp_cpc_cost": {
      "type": ["number", "null"],
      "description": "Third-party CPC cost"
    },
    "unique_conv": {
      "type": ["integer", "null"],
      "description": "Unique conversions"
    },
    "unique_imp": {
      "type": ["integer", "null"],
      "description": "Unique impressions"
    },
    "unique_imp_inverse_rate": {
      "type": ["number", "null"],
      "description": "Frequency"
    },
    "vcomp_0": {
      "type": ["number", "null"]
    },
    "vcomp_25": {
      "type": ["number", "null"]
    },
    "vcomp_50": {
      "type": ["number", "null"]
    },
    "vcomp_75": {
      "type": ["number", "null"]
    },
    "vcomp_95": {
      "type": ["number", "null"]
    },
    "vcomp_rate": {
      "type": ["number", "null"]
    },
    "view_percent": {
      "type": ["number", "null"],
      "description": "Viewability"
    }
  }
}
"""
)

account_line_items_stats_schema = json.loads(
"""
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "atos": {
      "type": ["number", "null"],
      "description": "The average time on site"
    },
    "atos_units": {
      "type": ["number", "null"],
      "description": "The average time on site"
    },
    "click": {
      "type": ["integer", "null"],
      "description": "Clicks"
    },
    "conv": {
      "type": ["integer", "null"],
      "description": "Conversions"
    },
    "conv_click": {
      "type": ["integer", "null"]
    },
    "conv_click_time_avg": {
      "type": ["number", "null"]
    },
    "conv_imp_derived": {
      "type": ["integer", "null"],
      "description": "Conversions attributed from impressions"
    },
    "conv_imp_time_avg": {
      "type": ["number", "null"]
    },
    "conv_ip": {
      "type": ["integer", "null"]
    },
    "conv_rev": {
      "type": ["number", "null"],
      "description": "Conversion revenue"
    },
    "cost": {
      "type": ["number", "null"],
      "description": "Media cost"
    },
    "ctr": {
      "type": ["number", "null"],
      "description": "Click-through rate"
    },
    "cvr": {
      "type": ["number", "null"],
      "description": "Conversion rate"
    },
    "date": {
      "type": ["string", "null"],
      "description": "Date"
    },
    "ecpa": {
      "type": ["number", "null"],
      "description": "Effective cost per action"
    },
    "ecpc": {
      "type": ["number", "null"],
      "description": "Effective cost per click"
    },
    "ecpcl": {
      "type": ["number", "null"]
    },
    "ecpe": {
      "type": ["number", "null"],
      "description": "Effective cost per engagement"
    },
    "ecpm": {
      "type": ["number", "null"],
      "description": "Effective cost per mille"
    },
    "ecpv": {
      "type": ["number", "null"],
      "description": "Effective cost per view"
    },
    "engage_rate": {
      "type": ["number", "null"]
    },
    "imp": {
      "type": ["integer", "null"],
      "description": "Impressions"
    },
    "line_item": {
      "type": ["string", "null"]
    },
    "ltr": {
      "type": ["number", "null"]
    },
    "page_start": {
      "type": ["integer", "null"]
    },
    "page_time": {
      "type": ["integer", "null"],
      "description": "Total time"
    },
    "page_time_15s": {
      "type": ["integer", "null"],
      "description": "Engagements"
    },
    "page_time_units": {
      "type": ["integer", "null"]
    },
    "profit": {
      "type": ["number", "null"]
    },
    "rcpc": {
      "type": ["number", "null"]
    },
    "rcpcl": {
      "type": ["number", "null"]
    },
    "rcpe": {
      "type": ["number", "null"]
    },
    "rcpm": {
      "type": ["number", "null"]
    },
    "revenue": {
      "type": ["number", "null"]
    },
    "roas": {
      "type": ["number", "null"],
      "description": "Return on ad spend"
    },
    "s_conv": {
      "type": ["integer", "null"],
      "description": "Secondary conversions"
    },
    "sub_advertiser": {
      "type": ["string", "null"]
    },
    "unique_conv": {
      "type": ["integer", "null"],
      "description": "Unique conversions"
    },
    "tp_cpm_cost": {
      "type": ["number", "null"],
      "description": "Third-party CPM cost"
    },
    "tp_cpc_cost": {
      "type": ["number", "null"],
      "description": "Third-party CPC cost"
    },
    "uniq_conv": {
      "type": ["integer", "null"]
    },
    "uniq_ecpa": {
      "type": ["number", "null"]
    },
    "unique_imp": {
      "type": ["integer", "null"],
      "description": "Unique impressions"
    },
    "unique_imp_inverse_rate": {
      "type": ["number", "null"],
      "description": "Frequency"
    },
    "vcomp_0": {
      "type": ["number", "null"]
    },
    "vcomp_25": {
      "type": ["number", "null"]
    },
    "vcomp_50": {
      "type": ["number", "null"]
    },
    "vcomp_75": {
      "type": ["number", "null"]
    },
    "vcomp_95": {
      "type": ["number", "null"]
    },
    "vcomp_rate": {
      "type": ["number", "null"]
    },
    "view_percent": {
      "type": ["number", "null"],
      "description": "Viewability"
    }
  }
}
"""
)


account_native_ads_stats_schema = json.loads(
"""
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "atos": {
      "type": ["number", "null"],
      "description": "The average time on site"
    },
    "atos_units": {
      "type": ["number", "null"],
      "description": "The average time on site"
    },
    "campaign": {
      "type": ["string", "null"]
    },
    "campaign_id": {
      "type": ["integer", "null"]
    },
    "campaign_type": {
      "type": ["string", "null"]
    },
    "channel": {
      "type": ["string", "null"]
    },
    "click": {
      "type": ["integer", "null"],
      "description": "Clicks"
    },
    "click_url": {
      "type": ["string", "null"]
    },
    "conv": {
      "type": ["integer", "null"],
      "description": "Conversions"
    },
    "conv_click": {
      "type": ["integer", "null"]
    },
    "conv_click_time_avg": {
      "type": ["number", "null"]
    },
    "conv_imp_derived": {
      "type": ["integer", "null"],
      "description": "Conversions attributed from impressions"
    },
    "conv_imp_time_avg": {
      "type": ["number", "null"]
    },
    "conv_ip": {
      "type": ["integer", "null"]
    },
    "cost": {
      "type": ["number", "null"],
      "description": "Media cost"
    },
    "creatives": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "url": {
            "type": ["string", "null"]
          },
          "size": {
            "type": ["string", "null"]
          }
        }
      }
    },
    "ctr": {
      "type": ["number", "null"],
      "description": "Click-through rate"
    },
    "cvr": {
      "type": ["number", "null"],
      "description": "Conversion rate"
    },
    "start_date": {
      "type": ["string", "null"],
      "description": "The date when the campaign will begin."
    },
    "end_date": {
      "type": ["string", "null"]
    },
    "heading": {
      "type": ["string", "null"]
    },
    "date": {
      "type": ["string", "null"],
      "description": "Date"
    },
    "ecpa": {
      "type": ["number", "null"],
      "description": "Effective cost per action"
    },
    "ecpc": {
      "type": ["number", "null"],
      "description": "Effective cost per click"
    },
    "ecpcl": {
      "type": ["number", "null"]
    },
    "ecpe": {
      "type": ["number", "null"],
      "description": "Effective cost per engagement"
    },
    "ecpm": {
      "type": ["number", "null"],
      "description": "Effective cost per mille"
    },
    "ecpv": {
      "type": ["number", "null"],
      "description": "Effective cost per view"
    },
    "engage_rate": {
      "type": ["number", "null"]
    },
    "imp": {
      "type": ["integer", "null"],
      "description": "Impressions"
    },
    "line_item": {
      "type": ["string", "null"]
    },
    "line_item_id": {
      "type": ["integer", "null"]
    },
    "ltr": {
      "type": ["number", "null"]
    },
    "native_ad_id": {
      "type": ["integer", "null"]
    },
    "native_ad_type": {
      "type": ["string", "null"]
    },
    "nativead": {
      "type": ["string", "null"]
    },
    "page_start": {
      "type": ["integer", "null"]
    },
    "page_time": {
      "type": ["integer", "null"],
      "description": "Total time"
    },
    "page_time_15s": {
      "type": ["integer", "null"],
      "description": "Engagements"
    },
    "page_time_units": {
      "type": ["integer", "null"]
    },
    "domain": {
      "type": ["string", "null"],
      "description": "Domain name."
    },
    "full_domain": {
        "type": ["string", "null"],
        "description": "Full domain name."
    },
    "ios_id": {
        "type": ["integer", "null"],
        "description": "iOS ID."
    },
    "is_android": {
        "type": ["boolean", "null"],
        "description": "If the device was an android."
    },
    "is_ios": {
        "type": ["boolean", "null"],
        "description": "If the device was an ios."
    },
    "profit": {
      "type": ["number", "null"]
    },
    "rcpc": {
      "type": ["number", "null"]
    },
    "rcpcl": {
      "type": ["number", "null"]
    },
    "rcpe": {
      "type": ["number", "null"]
    },
    "rcpm": {
      "type": ["number", "null"]
    },
    "revenue": {
      "type": ["number", "null"]
    },
    "roas": {
      "type": ["number", "null"],
      "description": "Return on ad spend"
    },
    "s_conv": {
      "type": ["integer", "null"],
      "description": "Secondary conversions"
    },
    "sub_advertiser": {
      "type": ["string", "null"]
    },
    "sub_advertiser_id": {
      "type": ["integer", "null"]
    },
    "tagline": {
      "type": ["string", "null"]
    },
    "unique_conv": {
      "type": ["integer", "null"],
      "description": "Unique conversions"
    },
    "tp_cpm_cost": {
      "type": ["number", "null"],
      "description": "Third-party CPM cost"
    },
    "tp_cpc_cost": {
      "type": ["number", "null"],
      "description": "Third-party CPC cost"
    },
    "uniq_conv": {
      "type": ["integer", "null"]
    },
    "unique_imp": {
      "type": ["integer", "null"],
      "description": "Unique impressions"
    },
    "unique_imp_inverse_rate": {
      "type": ["number", "null"],
      "description": "Frequency"
    },
    "vcomp_0": {
      "type": ["number", "null"]
    },
    "vcomp_25": {
      "type": ["number", "null"]
    },
    "vcomp_50": {
      "type": ["number", "null"]
    },
    "vcomp_75": {
      "type": ["number", "null"]
    },
    "vcomp_95": {
      "type": ["number", "null"]
    },
    "vcomp_rate": {
      "type": ["number", "null"]
    },
    "view_percent": {
      "type": ["number", "null"],
      "description": "Viewability"
    }
  }
}
"""
)


advertisers_schema = json.loads(
"""
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": [
    "id"
  ],
  "properties": {
    "id": {
      "type": ["integer", "null"],
      "description": "The ID of the advertiser."
    },
    "name": {
      "type": ["string", "null"],
      "description": "Name of the advertiser"
    },
    "description": {
      "type": ["string", "null"],
      "description": "The description of the advertiser"
    },
    "all_line_item_ids": {
      "type": "array",
      "description": "Ids of all attached line_items",
      "items": {
        "type": ["integer", "null"]
      }
    }
  }
}
"""
)

campaigns_schema = json.loads(
"""

{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": [
    "id"
  ],
  "properties": {
    "id": {
      "type": ["integer", "null"],
      "description": "The ID of the campaign."
    },
    "advertiser_id": {
      "type": ["integer", "null"],
      "description": "The ID of the campaign's advertiser."
    },
    "line_item_id": {
      "type": ["integer", "null"],
      "description": "The ID of the campaign's line item. This value cannot be modified after it has been set."
    },
    "name": {
      "type": ["string", "null"],
      "description": "The name of the campaign."
    },
    "campaign_type": {
      "type": ["string", "null"],
      "description": "(Deprecated) Legacy Campaign Type. Please use the `channel` parameter."
    },
    "channel": {
      "type": ["string", "null"],
      "description": "The campaign's channel. Currently, only native is supported via API creation"
    },
    "budget": {
      "type": ["number", "null"],
      "description": "The budget of the campaign."
    },
    "weekday_enabled": {
      "type": ["boolean", "null"],
      "description": "Enable day parting in campaigns to select days of the week. It will be converted from boolean, true and false to integers, 1 and 0 respectively"
    },
    "weekday_percents": {
      "type": "array",
      "items": {
        "type": ["boolean", "null"]
      },
      "description": "An array of booleans to describe day parting enabled per day of the week starting from Sunday and end at Saturday. Example: The value [ true, false, false, true, true, false, true] means the budget can be spent for the following days with values True. The array is parsed as Sunday: true, Monday: false, Tuesday: false, Wednesday: true, Thursday: true, Friday: false, Saturday: true. This value is only used if budget is not null and weekday_enabled is set to true."
    },
    "weekday_budgets": {
      "type": "array",
      "items": {
        "type": ["number", "null"]
      },
      "description": "An array of floats to describe budgets per day of the week starting from Sunday and end at Saturday. Example: The value [ 400.0, 100.0, 0.0, 200.0, 400.0, 200.0, 0.0 ] means the specified budget can be spent for the following days Sunday: 400.0, Monday: 100.0, Tuesday: 0.0, Wednesday: 200.0, Thursday: 400.0, Friday: 200.0, Saturday: 0.0. This value is only used if budget is set to null and weekday_enabled is set to true."
    },
    "day_part": {
      "type": ["null", "object"],
      "properties": {
        "enabled": {
          "type": ["boolean", "null"],
          "description": "The hourly parting is enabled."
        },
        "timezone": {
          "type": ["string", "null"],
          "description": "Timezone of ad account"
        },
        "start_hour": {
          "type": ["integer", "null"],
          "description": "The campaign will start spending at this hour. The start_hour will be set to 0 if not defined or defined outside of range 0 to 23."
        },
        "end_hour": {
          "type": ["integer", "null"],
          "description": "The campaign will finish spending at this hour. The end_hour will be set to 0 if not defined or defined outside of range 0 to 23"
        }
      },
      "description": "Enable hourly parting to set hours during the day that campaign can spend"
    },
    "bid_type": {
      "type": ["string", "null"],
      "description": "Type of bid model: cpm (Cost Per Thousand Impressions), cpc (Cost Per Click), cpe (Cost Per Engagement) bid model."
    },
    "bid_amount_total": {
      "type": ["number", "null"],
      "description": "The bid amount of the campaign."
    },
    "optimize_type": {
      "type": ["string", "null"],
      "description": "The type of optimization used for the campaign: ctr (CTR floor), cpc (CPC goal)."
    },
    "optimize_value": {
      "type": ["number", "null"],
      "description": "The value of the optimization. Example: The value is 0.2 for a $0.2 CPC goal, or a 0.2% CTR floor."
    },
    "daily_cap": {
      "type": ["number", "null"],
      "description": "The maximum budget to be spent in a single day. This value is only used if pace_evenly is NULL or false."
    },
    "pace_evenly": {
      "type": ["boolean", "null"],
      "description": "Whether or not to pace the campaign budget evenly over the course of the campaign. This value is only used if a valid end_date is specified."
    },
    "state": {
      "type": ["string", "null"],
      "description": "The state of the campaign."
    },
    "start_date": {
      "type": ["string", "null"],
      "description": "The date when the campaign will begin."
    },
    "end_date": {
      "type": ["string", "null"],
      "description": "The date when the campaign will end."
    },
    "smart_targeting": {
      "type": ["boolean", "null"],
      "description": "(Recommended) Smart Targeting helps you target relevant sites based on your audience targeting selection and historical performance. Overrides category_options."
    },
    "category_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of IAB categories to be included in the campaign."
    },
    "custom_segments_list": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of Custom Segments (and/or StackAdapt Segments) identifiers to attach to a campaign"
    },
    "third_party_segments": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of Third-Party Segment identifiers to attach to a campaign"
    },
    "country_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of ISO 3166-1 alpha-2 country codes to be included in the campaign."
    },
    "us_state_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of ISO 3166-2 US state codes to be included in the campaign."
    },
    "canada_province_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of ISO 3166-2 Canadian province codes to be included in the campaign."
    },
    "uk_county_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of ISO 3166-2 UK county codes to be included in the campaign."
    },
    "other_state_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of states (aside from those in US, UK, or Canada) to be included in the campaign. Pairs in format [country code]:[state code]."
    },
    "city_options": {
      "type": ["string", "null"],
      "description": "The list of city ID objects to be included in the campaign."
    },
    "domain_action": {
      "type": ["string", "null"],
      "description": "Action to be taken on the domain_options list."
    },
    "domain_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of domains or subdomains to be included or excluded in the campaign."
    },
    "device_type_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of device types to be included in the campaign."
    },
    "supply_type_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "The list of mobile supply types to be included in the campaign."
    },
    "supply_source_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "List of supply source id's. See the supply_sources endpoint for a list of supply_source_options"
    },
    "freq_cap_limit": {
      "type": ["integer", "null"],
      "description": "The user frequency cap value, which is the maximum amount of impressions that a unique user can see."
    },
    "freq_cap_time": {
      "type": ["integer", "null"],
      "description": "The length of time in milliseconds when the user frequency cap counter restarts."
    },
    "language_options": {
      "type": "array",
      "items": {
        "type": ["string", "null"]
      },
      "description": "A list of language(s) that are targeted. The campaign will only target sites or users whose language is included in the list."
    },
    "use_dma": {
      "type": ["boolean", "null"],
      "description": "Enable campaign to target city by Designated Market Area (DMA)."
    },
    "allow_iframe_engagement": {
      "type": ["boolean", "null"],
      "description": "Allow engagement tracking by placing add within an iframe"
    },
    "all_native_ads": {
      "type": "array",
      "items": {
        "type": [
          "object", "null"
        ],
        "properties": {
          "id": {
            "type": ["integer", "null"],
            "description": "The ID of the native ad."
          },
          "click_url": {
            "type": ["string", "null"],
            "description": "The click URL of the native ad. Not used for App Install Campaigns, where the click url is on the campaign object."
          },
          "input_data": {
            "type": ["null", "object"],
            "properties": {
              "heading": {
                "type": ["string", "null"],
                "description": "The heading of the ad."
              },
              "tagline": {
                "type": ["string", "null"],
                "description": "The tagline of the ad."
              },
              "vast_xml": {
                "type": ["string", "null"],
                "description": "VAST information in XML format."
              },
              "landing_url": {
                "type": ["string", "null"],
                "description": "URL to redirect after interaction."
              },
              "display_js_creative": {
                "type": ["array", "null"],
                "items": {
                  "type": ["object", "null"],
                  "properties": {
                    "js_code": {
                      "type": ["string", "null"],
                      "description": "JS code for the ad."
                    },
                    "width": {
                      "type": ["string", "null"],
                      "description": "The width of the container that the ad will be displayed in. Check the UI for valid options."
                    },
                    "height": {
                      "type": ["string", "null"],
                      "description": "The height of the container that the ad will be displayed in. Check the UI for valid options."
                    },
                    "img_url": {
                      "type": ["string", "null"],
                      "description": "URL for the image."
                    },
                    "is_expandable": {
                      "type": ["string", "null"],
                      "description": "Indicates whether your ad enlarges on the screen when hovering over it for some time."
                    },
                    "js_code_macro": {
                      "type": ["string", "null"],
                      "description": "Macro code in JS."
                    }
                  }
                }
              },
              "video_creatives": {
                "type": ["array", "null"],
                "items": {
                  "type": ["object", "null"],
                  "properties": {
                    "s3_url": {
                      "type": ["string", "null"],
                      "description": "The S3 URL of the video/audio creative."
                    },
                    "width": {
                      "type": ["string", "null"],
                      "description": "The width of the video/audio creative."
                    },
                    "height": {
                      "type": ["string", "null"],
                      "description": "The height of the video/audio creative."
                    },
                    "file_type": {
                      "type": ["string", "null"],
                      "description": "Video/Audio file type."
                    },
                    "duration": {
                      "type": ["number", "null"],
                      "description": "Duration of the video/audio creative."
                    },
                    "bitrate": {
                      "type": ["integer", "null"],
                      "description": "Bitrate of the video/audio creative."
                    }
                  }
                }
              },
              "audio_creatives": {
                "type": ["array", "null"],
                "items": {
                  "type": ["object", "null"],
                  "properties": {
                    "s3_url": {
                      "type": ["string", "null"],
                      "description": "The S3 URL of the video/audio creative."
                    },
                    "width": {
                      "type": ["string", "null"],
                      "description": "The width of the video/audio creative."
                    },
                    "height": {
                      "type": ["string", "null"],
                      "description": "The height of the video/audio creative."
                    },
                    "file_type": {
                      "type": ["string", "null"],
                      "description": "Video/Audio file type."
                    },
                    "duration": {
                      "type": ["number", "null"],
                      "description": "Duration of the video/audio creative."
                    },
                    "bitrate": {
                      "type": ["integer", "null"],
                      "description": "Bitrate of the video/audio creative."
                    }
                  }
                }
              }
            }
          },
          "audit_status": {
            "type": ["string", "null"],
            "description": "The audit status of the audit."
          },
          "name": {
            "type": ["string", "null"],
            "description": "The name of the native ad"
          },
          "state": {
            "type": ["string", "null"],
            "description": "The state of the campaign."
          },
          "imp_tracker_urls": {
            "type": "array",
            "items": {
              "type": ["string", "null"]
            },
            "description": "List of URLs for impression tracking."
          },
          "vast_trackers": {
            "type": "array",
            "items": {
              "type": [
                "object"
              ],
              "properties": {
                "event_type": {
                  "type": ["string", "null"],
                  "description": "The event to track"
                },
                "url": {
                  "type": ["string", "null"],
                  "description": "URL to track this event"
                }
              }
            },
            "description": "List of VAST trackers; only for video/CTV ads."
          },
          "api_frameworks": {
            "type": "array",
            "items": {
              "type": ["string", "null"]
            },
            "description": "List of supported api frameworks."
          },
          "brandname": {
            "type": ["string", "null"],
            "description": "Brand name associated with the creative."
          },
          "cta_text": {
            "type": ["string", "null"],
            "description": "Call-to-Action Text. Only used on some exchanges. This field is optional."
          },
          "creatives": {
            "type": "array",
            "items": {
              "type": [
                "object"
              ],
              "properties": {
                "id": {
                  "type": ["integer", "null"],
                  "description": "The ID of the image."
                },
                "file_name": {
                  "type": ["string", "null"],
                  "description": "The file name of the image."
                },
                "url": {
                  "type": ["string", "null"],
                  "description": "The s3 URL of where the image is being stored."
                },
                "width": {
                  "type": ["integer", "null"],
                  "description": "The width of the image."
                },
                "height": {
                  "type": ["integer", "null"],
                  "description": "The height of the image."
                }
              }
            }
          },
          "icon": {
            "type": ["null", "object"],
            "properties": {
              "id": {
                "type": ["integer", "null"],
                "description": "The ID of the image."
              },
              "file_name": {
                "type": ["string", "null"],
                "description": "The file name of the image."
              },
              "url": {
                "type": ["string", "null"],
                "description": "The s3 URL of where the image is being stored."
              },
              "width": {
                "type": ["integer", "null"],
                "description": "The width of the image."
              },
              "height": {
                "type": ["integer", "null"],
                "description": "The height of the image."
              }
            }
          },
          "channel": {
            "type": ["string", "null"],
            "description": "Campaign type"
          },
          "created_at": {
            "type": ["string", "null"],
            "description": "The date when the campaign was created."
          },
          "updated_at": {
              "type": ["string", "null"],
              "description": "The date when the campaign was last updated."
          }
        }
      },
      "description": "Native ad model"
    },
    "created_at": {
      "type": ["string", "null"],
      "description": "The date when the campaign was created."
    },
    "updated_at": {
      "type": ["string", "null"],
      "description": "The date when the campaign was last updated."
    },
    "ip_options": {
      "type": ["string", "null"],
      "description": "String of IPs separated by commas."
    },
    "device_os_family_options": {
      "type": "array",
      "items": {
          "type": ["string", "null"]
      },
      "description": "A list of device OS that are targeted."
    },
    "device_os_options": {
      "type": "array",
      "items": {
          "type": ["string", "null"]
      },
      "description": "A list of specific device OS that are targeted."
    },
    "connection_type_options": {
      "type": "array",
      "items": {
          "type": ["string", "null"]
      },
      "description": "A list of connection types that are targeted."
    },
    "timezone": {
      "type": ["string", "null"],
      "description": "Timezone of ad account"
    },
    "conversion_trackers": {
      "type": "array",
      "items": {
        "type": ["object", "null"],
        "properties": {
          "id": {
            "type": ["integer","null"],
            "description": "The ID of the conversion_tracker."
          },
          "name": {
            "type": ["string", "null"],
            "description": "The name of the conversion_tracker."
          },
          "description": {
            "type": ["string", "null"],
            "description": "Some description of the conversion_tracker."
          },
          "user_id": {
            "type": ["integer", "null"],
            "description": "User who owns the conversion_tracker."
          },
          "conv_type": {
            "type": ["string", "null"],
            "description": "Specifies whether the conversion is matched by an impression or a click."
          },
          "post_time": {
            "type": ["integer", "null"],
            "description": "Time till tracker expires for each user. Max: 2592000000 (30 days)"
          },
          "count_type": {
            "type": ["string", "null"],
            "description": "Specifies whether the conversion can be counted multiple times, or only once, by the same user."
          }
        }
      }
    }
  }
}
"""
)

conversion_trackers_schema = json.loads(
"""
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": [
    "id",
    "name",
    "conv_type",
    "post_time"
  ],
  "properties": {
    "id": {
      "type": ["integer","null"],
      "description": "The ID of the conversion_tracker."
    },
    "name": {
      "type": ["string", "null"],
      "description": "The name of the conversion_tracker."
    },
    "description": {
      "type": ["string", "null"],
      "description": "Some description of the conversion_tracker."
    },
    "user_id": {
      "type": ["integer", "null"],
      "description": "User who owns the conversion_tracker."
    },
    "conv_type": {
      "type": ["string", "null"],
      "description": "Specifies whether the conversion is matched by an impression or a click."
    },
    "post_time": {
      "type": ["integer", "null"],
      "description": "Time till tracker expires for each user. Max: 2592000000 (30 days)"
    },
    "count_type": {
      "type": ["string", "null"],
      "description": "Specifies whether the conversion can be counted multiple times, or only once, by the same user."
    }
  }
}
"""
)


line_items_schema = json.loads(
"""
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": [
    "id",
    "name"
  ],
  "properties": {
    "id": {
      "type": ["integer", "null"],
      "description": "The ID of the line item."
    },
    "name": {
      "type": ["string", "null"],
      "description": "The name of the line item."
    },
    "state": {
      "type": ["string", "null"],
      "description": "The state of the line item."
    },
    "daily_cap": {
      "type": ["number", "null"],
      "description": "The maximum budget (revenue type) to be spent in a single day. This value is only used if pace_evenly is NULL or false."
    },
    "pace_evenly": {
      "type": ["boolean", "null"],
      "description": "Whether or not to pace the campaign budget evenly over the course of the line item (Campaign Group). This value is only used if a valid end_date is specified."
    },
    "black_list_options": {
      "type": ["string", "null"],
      "description": "The list of domains or subdomains to be excluded in the campaign. domain_action must also be set. Example: www.american-express.com, www.google.com"
    },
    "revenue_type": {
      "type": ["string", "null"],
      "description": "With budget type set to revenue, choose a type of revenue tracking."
    },
    "revenue_value": {
      "type": ["number", "null"],
      "description": "The value of the revenue type. For example, 10 with a revenue type 'margin' would have revenue computed with a 10% margin."
    },
    "purchase_order_number": {
      "type": ["string", "null"],
      "description": "PO numbers can be used to align line_items with your own accounting systems"
    },
    "all_campaign_ids": {
      "type": "array",
      "items": {
        "type": ["integer"]
      }
    },
    "advertiser_id": {
      "type": ["integer", "null"],
      "description": "The ID of the line item's advertiser."
    },
    "start_date": {
      "type": ["string", "null"],
      "description": "The timestamp in UTC when the line item will begin."
    },
    "end_date": {
      "type": ["string", "null"],
      "description": "The timestamp in UTC when the line item will end."
    },
    "budget": {
      "type": ["number", "null"],
      "description": "The budget of the line item."
    }
  }
}
"""
)

native_ads_schema = json.loads(
"""
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": [
    "id",
    "input_data",
    "click_url",
    "name",
    "creatives",
    "brandname",
    "channel"
  ],
  "properties": {
    "id": {
      "type": "integer",
      "description": "The ID of the native ad."
    },
    "click_url": {
      "type": "string",
      "description": "The click URL of the native ad. Not used for App Install Campaigns, where the click url is on the campaign object."
    },
    "input_data": {
      "type": ["null", "object"],
      "properties": {
        "heading": {
          "type": ["string", "null"],
          "description": "The heading of the ad."
        },
        "tagline": {
          "type": ["string", "null"],
          "description": "The tagline of the ad."
        },
        "vast_xml": {
          "type": ["string", "null"],
          "description": "VAST information in XML format."
        },
        "landing_url": {
          "type": ["string", "null"],
          "description": "URL to redirect after interaction."
        },
        "display_js_creative": {
          "type": ["array", "null"],
          "items": {
            "type": ["object", "null"],
            "properties": {
              "js_code": {
                "type": ["string", "null"],
                "description": "JS code for the ad."
              },
              "width": {
                "type": ["integer", "null"],
                "description": "The width of the container that the ad will be displayed in. Check the UI for valid options."
              },
              "height": {
                "type": ["integer", "null"],
                "description": "The height of the container that the ad will be displayed in. Check the UI for valid options."
              },
              "img_url": {
                "type": ["string", "null"],
                "description": "URL for the image."
              },
              "is_expandable": {
                "type": ["string", "null"],
                "description": "Indicates whether your ad enlarges on the screen when hovering over it for some time."
              },
              "js_code_macro": {
                "type": ["string", "null"],
                "description": "Macro code in JS."
              }
            }
          }
        },
        "video_creatives": {
          "type": ["array", "null"],
          "items": {
            "type": ["object", "null"],
            "properties": {
              "s3_url": {
                "type": ["string", "null"],
                "description": "The S3 URL of the video/audio creative."
              },
              "width": {
                "type": ["integer", "null"],
                "description": "The width of the video/audio creative."
              },
              "height": {
                "type": ["integer", "null"],
                "description": "The height of the video/audio creative."
              },
              "file_type": {
                "type": ["string", "null"],
                "description": "Video/Audio file type."
              },
              "duration": {
                "type": ["number", "null"],
                "description": "Duration of the video/audio creative."
              },
              "bitrate": {
                "type": ["integer", "null"],
                "description": "Bitrate of the video/audio creative."
              }
            }
          }
        },
        "audio_creatives": {
          "type": ["array", "null"],
          "items": {
            "type": ["object", "null"],
            "properties": {
              "s3_url": {
                "type": ["string", "null"],
                "description": "The S3 URL of the video/audio creative."
              },
              "width": {
                "type": ["integer", "null"],
                "description": "The width of the video/audio creative."
              },
              "height": {
                "type": ["integer", "null"],
                "description": "The height of the video/audio creative."
              },
              "file_type": {
                "type": ["string", "null"],
                "description": "Video/Audio file type."
              },
              "duration": {
                "type": ["number", "null"],
                "description": "Duration of the video/audio creative."
              },
              "bitrate": {
                "type": ["integer", "null"],
                "description": "Bitrate of the video/audio creative."
              }
            }
          }
        }
      }
    },
    "audit_status": {
      "type": "string",
      "description": "The audit status of the audit."
    },
    "name": {
      "type": "string",
      "description": "The name of the native ad"
    },
    "state": {
      "type": "string",
      "description": "The state of the campaign."
    },
    "imp_tracker_urls": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of URLs for impression tracking."
    },
    "vast_trackers": {
      "type": "array",
      "items": {
        "type": [
          "object"
        ],
        "properties": {
          "event_type": {
            "type": ["string", "null"],
            "description": "The event to track"
          },
          "url": {
            "type": ["string", "null"],
            "description": "URL to track this event"
          }
        }
      },
      "description": "List of VAST trackers; only for video/CTV ads."
    },
    "api_frameworks": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of supported api frameworks."
    },
    "brandname": {
      "type": "string",
      "description": "Brand name associated with the creative."
    },
    "cta_text": {
      "type": "string",
      "description": "Call-to-Action Text. Only used on some exchanges. This field is optional."
    },
    "creatives": {
      "type": "array",
      "items": {
        "type": [
          "object"
        ],
        "properties": {
          "id": {
            "type": ["integer", "null"],
            "description": "The ID of the image."
          },
          "file_name": {
            "type": ["string", "null"],
            "description": "The file name of the image."
          },
          "url": {
            "type": ["string", "null"],
            "description": "The s3 URL of where the image is being stored."
          },
          "width": {
            "type": ["integer", "null"],
            "description": "The width of the image."
          },
          "height": {
            "type": ["integer", "null"],
            "description": "The height of the image."
          }
        }
      }
    },
    "icon": {
      "type": ["null", "object"],
      "properties": {
        "id": {
          "type": ["integer", "null"],
          "description": "The ID of the image."
        },
        "file_name": {
          "type": ["string", "null"],
          "description": "The file name of the image."
        },
        "url": {
          "type": ["string", "null"],
          "description": "The s3 URL of where the image is being stored."
        },
        "width": {
          "type": ["integer", "null"],
          "description": "The width of the image."
        },
        "height": {
          "type": ["integer", "null"],
          "description": "The height of the image."
        }
      }
    },
    "channel": {
      "type": ["string", "null"],
      "description": "Campaign type"
    },
    "created_at": {
      "type": ["string", "null"],
      "description": "The date when the campaign was created."
    },
    "updated_at": {
        "type": ["string", "null"],
        "description": "The date when the campaign was last updated."
    }
  }
}
"""
)