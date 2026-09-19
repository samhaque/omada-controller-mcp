from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO


T = TypeVar("T", bound="SpeedTestV2SettingVO")


@_attrs_define
class SpeedTestV2SettingVO:
    """
    Attributes:
        auto_speed_test (bool): Whether enable scheduled speed testing.
        timing_type (int | Unset): The timing type of speed test setting: 1:Daily, 2:Weekly, 3:Monthly.
        hour (int | Unset): Start time of speed test(unit: hour); It should be within the range of 0~23.
        minute (int | Unset): Start time of speed test(unit: minute); It should be within the range of 0~59.
        day_of_week (list[int] | Unset): It is required when [timingType] is 2. The value should be within the range of
            0(Sunday)~6(Saturday).
        day_of_month (list[int] | Unset): It is required when [timingType] is 3. The value should be within the range of
            1~31.
        resource (int | Unset): Data Source. Resource should be a value as follows: 0: new created; 1: from template; 2:
            override
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    auto_speed_test: bool
    timing_type: int | Unset = UNSET
    hour: int | Unset = UNSET
    minute: int | Unset = UNSET
    day_of_week: list[int] | Unset = UNSET
    day_of_month: list[int] | Unset = UNSET
    resource: int | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_speed_test = self.auto_speed_test

        timing_type = self.timing_type

        hour = self.hour

        minute = self.minute

        day_of_week: list[int] | Unset = UNSET
        if not isinstance(self.day_of_week, Unset):
            day_of_week = self.day_of_week

        day_of_month: list[int] | Unset = UNSET
        if not isinstance(self.day_of_month, Unset):
            day_of_month = self.day_of_month

        resource = self.resource

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoSpeedTest": auto_speed_test,
            }
        )
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
        if resource is not UNSET:
            field_dict["resource"] = resource
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO

        d = dict(src_dict)
        auto_speed_test = d.pop("autoSpeedTest")

        timing_type = d.pop("timingType", UNSET)

        hour = d.pop("hour", UNSET)

        minute = d.pop("minute", UNSET)

        day_of_week = cast(list[int], d.pop("dayOfWeek", UNSET))

        day_of_month = cast(list[int], d.pop("dayOfMonth", UNSET))

        resource = d.pop("resource", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        speed_test_v2_setting_vo = cls(
            auto_speed_test=auto_speed_test,
            timing_type=timing_type,
            hour=hour,
            minute=minute,
            day_of_week=day_of_week,
            day_of_month=day_of_month,
            resource=resource,
            feature_description=feature_description,
        )

        speed_test_v2_setting_vo.additional_properties = d
        return speed_test_v2_setting_vo

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
