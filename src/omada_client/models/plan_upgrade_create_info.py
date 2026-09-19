from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plan_upgrade_selected_model import PlanUpgradeSelectedModel


T = TypeVar("T", bound="PlanUpgradeCreateInfo")


@_attrs_define
class PlanUpgradeCreateInfo:
    """
    Attributes:
        sites (list[str]): List of site ID selected by the user
        model_list (list[PlanUpgradeSelectedModel]): List of model selected for planned upgrade
        schedule_type (int): The type of upgrade execution time, where 0 represents now and 1 represents the specified
            time
        year (int | Unset): The year selected by the user
        month_of_year (int | Unset): The month of the year selected by the user, It should be within the range of 1-12
        day_of_month (int | Unset): The day of the month selected by the user, It should be within the range of 1-31
        hour (int | Unset): The hour of the day selected by the user, It should be within the range of 0-23
        minute (int | Unset): The minute in the hour selected by the user, It should be within the range of 0-59
    """

    sites: list[str]
    model_list: list[PlanUpgradeSelectedModel]
    schedule_type: int
    year: int | Unset = UNSET
    month_of_year: int | Unset = UNSET
    day_of_month: int | Unset = UNSET
    hour: int | Unset = UNSET
    minute: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sites = self.sites

        model_list = []
        for model_list_item_data in self.model_list:
            model_list_item = model_list_item_data.to_dict()
            model_list.append(model_list_item)

        schedule_type = self.schedule_type

        year = self.year

        month_of_year = self.month_of_year

        day_of_month = self.day_of_month

        hour = self.hour

        minute = self.minute

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sites": sites,
                "modelList": model_list,
                "scheduleType": schedule_type,
            }
        )
        if year is not UNSET:
            field_dict["year"] = year
        if month_of_year is not UNSET:
            field_dict["monthOfYear"] = month_of_year
        if day_of_month is not UNSET:
            field_dict["dayOfMonth"] = day_of_month
        if hour is not UNSET:
            field_dict["hour"] = hour
        if minute is not UNSET:
            field_dict["minute"] = minute

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.plan_upgrade_selected_model import (
            PlanUpgradeSelectedModel,
        )

        d = dict(src_dict)
        sites = cast(list[str], d.pop("sites"))

        model_list = []
        _model_list = d.pop("modelList")
        for model_list_item_data in _model_list:
            model_list_item = PlanUpgradeSelectedModel.from_dict(model_list_item_data)

            model_list.append(model_list_item)

        schedule_type = d.pop("scheduleType")

        year = d.pop("year", UNSET)

        month_of_year = d.pop("monthOfYear", UNSET)

        day_of_month = d.pop("dayOfMonth", UNSET)

        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        plan_upgrade_create_info = cls(
            sites=sites,
            model_list=model_list,
            schedule_type=schedule_type,
            year=year,
            month_of_year=month_of_year,
            day_of_month=day_of_month,
            hour=hour,
            minute=minute,
        )

        plan_upgrade_create_info.additional_properties = d
        return plan_upgrade_create_info

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
