from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkReportScheduleVO")


@_attrs_define
class NetworkReportScheduleVO:
    """
    Attributes:
        enable (bool):
        tab (int | Unset):
        tab_id_list (list[str] | Unset):
        report_name (str | Unset):
        report_type (int | Unset):
        email_list (list[str] | Unset):
        time (int | Unset):
        cards (str | Unset):
        timing_type (int | Unset):
        hour (int | Unset):
        minute (int | Unset):
        day_of_week (int | Unset):
        day_of_month (int | Unset):
        month_of_year (int | Unset):
    """

    enable: bool
    tab: int | Unset = UNSET
    tab_id_list: list[str] | Unset = UNSET
    report_name: str | Unset = UNSET
    report_type: int | Unset = UNSET
    email_list: list[str] | Unset = UNSET
    time: int | Unset = UNSET
    cards: str | Unset = UNSET
    timing_type: int | Unset = UNSET
    hour: int | Unset = UNSET
    minute: int | Unset = UNSET
    day_of_week: int | Unset = UNSET
    day_of_month: int | Unset = UNSET
    month_of_year: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        tab = self.tab

        tab_id_list: list[str] | Unset = UNSET
        if not isinstance(self.tab_id_list, Unset):
            tab_id_list = self.tab_id_list

        report_name = self.report_name

        report_type = self.report_type

        email_list: list[str] | Unset = UNSET
        if not isinstance(self.email_list, Unset):
            email_list = self.email_list

        time = self.time

        cards = self.cards

        timing_type = self.timing_type

        hour = self.hour

        minute = self.minute

        day_of_week = self.day_of_week

        day_of_month = self.day_of_month

        month_of_year = self.month_of_year

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
        if report_name is not UNSET:
            field_dict["reportName"] = report_name
        if report_type is not UNSET:
            field_dict["reportType"] = report_type
        if email_list is not UNSET:
            field_dict["emailList"] = email_list
        if time is not UNSET:
            field_dict["time"] = time
        if cards is not UNSET:
            field_dict["cards"] = cards
        if timing_type is not UNSET:
            field_dict["timingType"] = timing_type
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute
        if day_of_week is not UNSET:
            field_dict["dayOfWeek"] = day_of_week
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if month_of_year is not UNSET:
            field_dict["monthOfYear"] = month_of_year

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        tab = d.pop("tab", UNSET)

        tab_id_list = cast(list[str], d.pop("tabIdList", UNSET))

        report_name = d.pop("reportName", UNSET)

        report_type = d.pop("reportType", UNSET)

        email_list = cast(list[str], d.pop("emailList", UNSET))

        time = d.pop("time", UNSET)

        cards = d.pop("cards", UNSET)

        timing_type = d.pop("timingType", UNSET)

        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        day_of_week = d.pop("dayOfWeek", UNSET)

        day_of_month = d.pop("dayOfMonth", UNSET)

        month_of_year = d.pop("monthOfYear", UNSET)

        network_report_schedule_vo = cls(
            enable=enable,
            tab=tab,
            tab_id_list=tab_id_list,
            report_name=report_name,
            report_type=report_type,
            email_list=email_list,
            time=time,
            cards=cards,
            timing_type=timing_type,
            hour=hour,
            minute=minute,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
            month_of_year=month_of_year,
        )

        network_report_schedule_vo.additional_properties = d
        return network_report_schedule_vo

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
