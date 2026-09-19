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


T = TypeVar("T", bound="TimeRangeProfileOpenApiVO")


@_attrs_define
class TimeRangeProfileOpenApiVO:
    """
    Attributes:
        profile_id (str | Unset): Time range profile ID
        name (str | Unset): Time range profile name should contain 1 to 64 characters.
        day_mode (int | Unset): Time range profile day mode; It should be a value as follows: 0: Every Day, 1: Weekday,
            2: Weekend, 3: Customized
        custom_day_mode (CustomDayModeOpenApiVO | Unset): Time range profile custom day mode, this field is required
            when parameter [dayMode] is 3.
        time_list (list[ScheduleTimeOpenApiVO] | Unset): Time range profile schedule time config
    """

    profile_id: str | Unset = UNSET
    name: str | Unset = UNSET
    day_mode: int | Unset = UNSET
    custom_day_mode: CustomDayModeOpenApiVO | Unset = UNSET
    time_list: list[ScheduleTimeOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        name = self.name

        day_mode = self.day_mode

        custom_day_mode: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_day_mode, Unset):
            custom_day_mode = self.custom_day_mode.to_dict()

        time_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.time_list, Unset):
            time_list = []
            for time_list_item_data in self.time_list:
                time_list_item = time_list_item_data.to_dict()
                time_list.append(time_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if name is not UNSET:
            field_dict["name"] = name
        if day_mode is not UNSET:
            field_dict["dayMode"] = day_mode
        if custom_day_mode is not UNSET:
            field_dict["customDayMode"] = custom_day_mode
        if time_list is not UNSET:
            field_dict["timeList"] = time_list

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
        profile_id = d.pop("profileId", UNSET)

        name = d.pop("name", UNSET)

        day_mode = d.pop("dayMode", UNSET)

        _custom_day_mode = d.pop("customDayMode", UNSET)
        custom_day_mode: CustomDayModeOpenApiVO | Unset
        if isinstance(_custom_day_mode, Unset):
            custom_day_mode = UNSET
        else:
            custom_day_mode = CustomDayModeOpenApiVO.from_dict(_custom_day_mode)

        _time_list = d.pop("timeList", UNSET)
        time_list: list[ScheduleTimeOpenApiVO] | Unset = UNSET
        if _time_list is not UNSET:
            time_list = []
            for time_list_item_data in _time_list:
                time_list_item = ScheduleTimeOpenApiVO.from_dict(time_list_item_data)

                time_list.append(time_list_item)

        time_range_profile_open_api_vo = cls(
            profile_id=profile_id,
            name=name,
            day_mode=day_mode,
            custom_day_mode=custom_day_mode,
            time_list=time_list,
        )

        time_range_profile_open_api_vo.additional_properties = d
        return time_range_profile_open_api_vo

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
