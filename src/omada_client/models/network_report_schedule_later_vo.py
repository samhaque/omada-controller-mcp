from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkReportScheduleLaterVO")


@_attrs_define
class NetworkReportScheduleLaterVO:
    """
    Attributes:
        enable (bool):
        tab (int | Unset):
        tab_id_list (list[str] | Unset):
        cards (str | Unset):
        report_name (str | Unset):
        report_type (int | Unset):
        email_list (list[str] | Unset):
        minute (int | Unset):
        hour (int | Unset):
        time (int | Unset):
        start (int | Unset):
        end (int | Unset):
    """

    enable: bool
    tab: int | Unset = UNSET
    tab_id_list: list[str] | Unset = UNSET
    cards: str | Unset = UNSET
    report_name: str | Unset = UNSET
    report_type: int | Unset = UNSET
    email_list: list[str] | Unset = UNSET
    minute: int | Unset = UNSET
    hour: int | Unset = UNSET
    time: int | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        tab = self.tab

        tab_id_list: list[str] | Unset = UNSET
        if not isinstance(self.tab_id_list, Unset):
            tab_id_list = self.tab_id_list

        cards = self.cards

        report_name = self.report_name

        report_type = self.report_type

        email_list: list[str] | Unset = UNSET
        if not isinstance(self.email_list, Unset):
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
            }
        )
        if tab is not UNSET:
            field_dict["tab"] = tab
        if tab_id_list is not UNSET:
            field_dict["tabIdList"] = tab_id_list
        if cards is not UNSET:
            field_dict["cards"] = cards
        if report_name is not UNSET:
            field_dict["reportName"] = report_name
        if report_type is not UNSET:
            field_dict["reportType"] = report_type
        if email_list is not UNSET:
            field_dict["emailList"] = email_list
        if minute is not UNSET:
            field_dict["minute"] = minute
        if hour is not UNSET:
            field_dict["hour"] = hour
        if time is not UNSET:
            field_dict["time"] = time
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        tab = d.pop("tab", UNSET)

        tab_id_list = cast(list[str], d.pop("tabIdList", UNSET))

        cards = d.pop("cards", UNSET)

        report_name = d.pop("reportName", UNSET)

        report_type = d.pop("reportType", UNSET)

        email_list = cast(list[str], d.pop("emailList", UNSET))

        minute = d.pop("minute", UNSET)

        hour = d.pop("hour", UNSET)

        time = d.pop("time", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        network_report_schedule_later_vo = cls(
            enable=enable,
            tab=tab,
            tab_id_list=tab_id_list,
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

        network_report_schedule_later_vo.additional_properties = d
        return network_report_schedule_later_vo

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
