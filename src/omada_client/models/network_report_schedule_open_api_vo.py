from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkReportScheduleOpenApiVO")


@_attrs_define
class NetworkReportScheduleOpenApiVO:
    """ 
        Attributes:
            enable (bool): Whether to enable periodic report generation and sending.
            tab (int): Report tab, 0-summary, 1-wireless summary, 2-wired summary, 3-wireless devices,4-wired devices,
                5-ssid, 6-client.
            report_name (str): Parameter [reportName] should be a string of 1 to 64 characters without any space at the
                beginning or end.
            report_type (int): Type of the file to be exported [0:PDF,1:CSV].
            email_list (list[str]): Email List. Example:["11@qq.com","11@qq.com"]. If 'enable' is false, the parameter must
                be [].
            cards (str): According to the Tab, fill in the cards parameter with the corresponding string. The string is a
                json array whose elements represent a single card. The type and granularity parameters for the cards cannot be
                removed. Only the granularity value can be changed, which can be 0/1/2 [0:5min, 1:hourly,
                2:daily].Summary:"[{\\"type\\":\\"apSummary\\"},{\\"type\\":\\"ssidSummary\\
                "},{\\"type\\":\\"bandSummary\\"},{\\"type\\":\\"switchSummary\\"},{\\"type
                \\":\\"deviceSummary\\"},{\\"type\\":\\"clientsSummary\\"},{\\"type\\":\\"tr
                afficSummary\\",\\"granularity\\":0},{\\"type\\":\\"trafficDistribution\\",
                \\"granularity\\":0},{\\"type\\":\\"alertSummary\\"},{\\"type\\":\\"eventSum
                mary\\"},{\\"type\\":\\"appFlowSummary\\"}]";Wireless
                Summary:"[{\\"type\\":\\"onlineOfflineAp\\",\\"granularity\\":0},{\\"type\\"
                :\\"apSummary\\"},{\\"type\\":\\"ssidSummary\\"},{\\"type\\":\\"bandSummary
                \\"},{\\"type\\":\\"topTrafficAp\\",\\"granularity\\":0},{\\"type\\":\\"topC
                lientNumAp\\",\\"granularity\\":0},{\\"type\\":\\"apAlert\\"},{\\"type\\":\\
                "apRebootTimes\\"},{\\"type\\":\\"wirelessOverview\\"},{\\"type\\":\\"wirele
                ssTxRxTraffic\\",\\"granularity\\":0},{\\"type\\":\\"wirelessBandTraffic\\",
                \\"granularity\\":0},{\\"type\\":\\"wirelessClientsActivities\\",\\"granular
                ity\\":0}]";Wired Summary:"[{\\"type\\":\\"wiredOverview\\"},{\\"type\\":\\"ispLoad\\"},{\\"ty
                pe\\":\\"onlineOfflineSwitch\\",\\"granularity\\":0},{\\"type\\":\\"wiredCli
                entsActivities\\",\\"granularity\\":0},{\\"type\\":\\"switchSummary\\"},{\\"
                type\\":\\"topTrafficSwitch\\",\\"granularity\\":0},{\\"type\\":\\"topPoeUti
                lSwitch\\",\\"granularity\\":0},{\\"type\\":\\"topPoePowerSwitch\\",\\"granu
                larity\\":0},{\\"type\\":\\"topClientNumSwitch\\",\\"granularity\\":0},{\\"t
                ype\\":\\"switchAlert\\"},{\\"type\\":\\"switchRebootTimes\\"}]";Wireless
                Devices:"[{\\"type\\":\\"onlineOfflineAp\\",\\"granularity\\":0},{\\"type\\"
                :\\"apSummary\\"},{\\"type\\":\\"topTrafficAp\\",\\"granularity\\":0},{\\"ty
                pe\\":\\"topCpuUtilAp\\",\\"granularity\\":0},{\\"type\\":\\"topMemUtilAp\\"
                ,\\"granularity\\":0},{\\"type\\":\\"topClientNumAp\\",\\"granularity\\":0},
                {\\"type\\":\\"apAlert\\"},{\\"type\\":\\"apRebootTimes\\"}]";Wired
                Devices:"[{\\"type\\":\\"onlineOfflineSwitch\\",\\"granularity\\":0},{\\"typ
                e\\":\\"switchSummary\\"},{\\"type\\":\\"gatewayCpuMemUtil\\",\\"granularity
                \\":0},{\\"type\\":\\"topTrafficSwitch\\",\\"granularity\\":0},{\\"type\\":
                \\"topCpuUtilSwitch\\",\\"granularity\\":0},{\\"type\\":\\"topMemUtilSwitch
                \\",\\"granularity\\":0},{\\"type\\":\\"topClientNumSwitch\\",\\"granularity
                \\":0},{\\"type\\":\\"switchAlert\\"},{\\"type\\":\\"switchRebootTimes\\"}]"
                ;SSID:"[{\\"type\\":\\"ssidSummary\\"},{\\"type\\":\\"topTrafficSsid\\",\\"g
                ranularity\\":0},{\\"type\\":\\"topClientNumSsid\\",\\"granularity\\":0},{\\
                "type\\":\\"ssidNumActivities\\",\\"granularity\\":0}]";Clients:"[{\\"type\\
                ":\\"clientDistribution\\"},{\\"type\\":\\"clientNumActivities\\",\\"granula
                rity\\":0},{\\"type\\":\\"wirelessClientsActivities\\",\\"granularity\\":0},
                {\\"type\\":\\"guestNumActivities\\",\\"granularity\\":0},{\\"type\\":\\"top
                ClientNumAp\\",\\"granularity\\":0},{\\"type\\":\\"topClientNumSwitch\\",\\"
                granularity\\":0}]";
            timing_type (int): Frequency of executing schedule task Daily(1), Weekly(2), Monthly(3).
            hour (int): The value ranges from 0 to 23.
            minute (int): The value ranges from 0 to 59.
            day_of_week (int | Unset): If timing type is weekly, enter and only enter [dayOfWeek].The value ranges from 0 to
                6.('0' indicate Sunday)
            day_of_month (int | Unset): If timing type is monthly, enter and only enter [dayOfMonth].The value ranges from 1
                to 31. Schedule will fail on the day of the monthif you select 29th,30th,31th but the month doesn't have these
                days.
     """

    enable: bool
    tab: int
    report_name: str
    report_type: int
    email_list: list[str]
    cards: str
    timing_type: int
    hour: int
    minute: int
    day_of_week: int | Unset = UNSET
    day_of_month: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        tab = self.tab

        report_name = self.report_name

        report_type = self.report_type

        email_list = self.email_list

        cards = self.cards

        timing_type = self.timing_type

        hour = self.hour

        minute = self.minute

        day_of_week = self.day_of_week

        day_of_month = self.day_of_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "tab": tab,
                "reportName": report_name,
                "reportType": report_type,
                "emailList": email_list,
                "cards": cards,
                "timingType": timing_type,
                "hour": hour,
                "minute": minute,
            }
        )
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        tab = d.pop("tab")

        report_name = d.pop("reportName")

        report_type = d.pop("reportType")

        email_list = cast(list[str], d.pop("emailList"))

        cards = d.pop("cards")

        timing_type = d.pop("timingType")

        hour = d.pop("hour")

        minute = d.pop("minute")

        day_of_week = d.pop("dayOfWeek", UNSET)

        day_of_month = d.pop("dayOfMonth", UNSET)

        network_report_schedule_open_api_vo = cls(
            enable=enable,
            tab=tab,
            report_name=report_name,
            report_type=report_type,
            email_list=email_list,
            cards=cards,
            timing_type=timing_type,
            hour=hour,
            minute=minute,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
        )

        network_report_schedule_open_api_vo.additional_properties = d
        return network_report_schedule_open_api_vo

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
