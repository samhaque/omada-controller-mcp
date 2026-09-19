from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="NetworkReportScheduleLaterOpenApiVO")


@_attrs_define
class NetworkReportScheduleLaterOpenApiVO:
    """ 
        Attributes:
            enable (bool): Whether to enable periodic report generation and sending.
            tab (int): Report tab, 0-summary, 1-wireless summary, 2-wired summary, 3-wireless devices,4-wired devices,
                5-ssid, 6-client.
            cards (str): According to the Tab, fill in the cards parameter with the corresponding json string. The string is
                a json array whose elements represent a single card. The type and granularity parameters for the cards cannot be
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
            report_name (str): Report Name.
            report_type (int): Type of the file to be exported [0:PDF,1:CSV].
            email_list (list[str]): Email List. Example:["11@qq.com","11@qq.com"]
            minute (int): The value ranges from 0 to 59.
            hour (int): The value ranges from 0 to 23.
            time (int): The timestamp of the year, month, and day is generated.
            start (int): The start timestamp of the query for the data needed to generate the report.
            end (int): The end timestamp of the query for the data needed to generate the report.
     """

    enable: bool
    tab: int
    cards: str
    report_name: str
    report_type: int
    email_list: list[str]
    minute: int
    hour: int
    time: int
    start: int
    end: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        tab = self.tab

        cards = self.cards

        report_name = self.report_name

        report_type = self.report_type

        email_list = self.email_list

        minute = self.minute

        hour = self.hour

        time = self.time

        start = self.start

        end = self.end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "tab": tab,
                "cards": cards,
                "reportName": report_name,
                "reportType": report_type,
                "emailList": email_list,
                "minute": minute,
                "hour": hour,
                "time": time,
                "start": start,
                "end": end,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        tab = d.pop("tab")

        cards = d.pop("cards")

        report_name = d.pop("reportName")

        report_type = d.pop("reportType")

        email_list = cast(list[str], d.pop("emailList"))

        minute = d.pop("minute")

        hour = d.pop("hour")

        time = d.pop("time")

        start = d.pop("start")

        end = d.pop("end")

        network_report_schedule_later_open_api_vo = cls(
            enable=enable,
            tab=tab,
            cards=cards,
            report_name=report_name,
            report_type=report_type,
            email_list=email_list,
            minute=minute,
            hour=hour,
            time=time,
            start=start,
            end=end,
        )

        network_report_schedule_later_open_api_vo.additional_properties = d
        return network_report_schedule_later_open_api_vo

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
