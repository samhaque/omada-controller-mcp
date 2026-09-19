from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_day_mode_open_api_vo import CustomDayModeOpenApiVO
    from ..models.schedule_time_open_api_vo import ScheduleTimeOpenApiVO


T = TypeVar("T", bound="UpdateTimeRangeProfileOpenApiVO")


@_attrs_define
class UpdateTimeRangeProfileOpenApiVO:
    """
    Attributes:
        name (str): Time range profile name should contain 1 to 64 characters.
        day_mode (int): Time range profile day mode; 0: Every Day, 1: Weekday, 2: Weekend, 3: Customized
        time_list (list[ScheduleTimeOpenApiVO]): Time range profile schedule time config
        custom_day_mode (CustomDayModeOpenApiVO | Unset): Time range profile custom day mode, this field is required
            when parameter [dayMode] is 3.
    """

    name: str
    day_mode: int
    time_list: list[ScheduleTimeOpenApiVO]
    custom_day_mode: CustomDayModeOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        day_mode = self.day_mode

        time_list = []
        for time_list_item_data in self.time_list:
            time_list_item = time_list_item_data.to_dict()
            time_list.append(time_list_item)

        custom_day_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_day_mode, Unset):
            custom_day_mode = self.custom_day_mode.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "dayMode": day_mode,
                "timeList": time_list,
            }
        )
        if custom_day_mode is not UNSET:
            field_dict["customDayMode"] = custom_day_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_day_mode_open_api_vo import (
            CustomDayModeOpenApiVO,
        )
        from ..models.schedule_time_open_api_vo import (
            ScheduleTimeOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        day_mode = d.pop("dayMode")

        time_list = []
        _time_list = d.pop("timeList")
        for time_list_item_data in _time_list:
            time_list_item = ScheduleTimeOpenApiVO.from_dict(time_list_item_data)

            time_list.append(time_list_item)

        _custom_day_mode = d.pop("customDayMode", UNSET)
        custom_day_mode: CustomDayModeOpenApiVO | Unset
        if isinstance(_custom_day_mode, Unset):
            custom_day_mode = UNSET
        else:
            custom_day_mode = CustomDayModeOpenApiVO.from_dict(_custom_day_mode)

        update_time_range_profile_open_api_vo = cls(
            name=name,
            day_mode=day_mode,
            time_list=time_list,
            custom_day_mode=custom_day_mode,
        )

        update_time_range_profile_open_api_vo.additional_properties = d
        return update_time_range_profile_open_api_vo

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
