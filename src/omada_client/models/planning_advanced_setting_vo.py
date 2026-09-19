from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exclude_channel_vo import ExcludeChannelVO
    from ..models.power_range_vo import PowerRangeVO
    from ..models.power_threshold_vo import PowerThresholdVO
    from ..models.width_range_vo import WidthRangeVO


T = TypeVar("T", bound="PlanningAdvancedSettingVO")


@_attrs_define
class PlanningAdvancedSettingVO:
    """
    Attributes:
        exclude_5_g_ch_en (bool | Unset): Whether to enable the Excluded 5GHz Channels function.
        exclude_5_g_ch (list[ExcludeChannelVO] | Unset): Excluded 5 GHz channel list.
        power_mode (int | Unset): Power mode. 0: Auto. 1: Custom.
        power_range (PowerRangeVO | Unset): Power range. Parameter [powerRange] should not be null when parameter
            [powerMode] is 1.
        width_select_en (bool | Unset): Whether to enable channel width selection.
        width_range (WidthRangeVO | Unset): Channel width range. Parameter [widthRange] should not be null when
            parameter [widthSelectEn] is true.
        power_threshold (PowerThresholdVO | Unset): Power threshold.
    """

    exclude_5_g_ch_en: bool | Unset = UNSET
    exclude_5_g_ch: list[ExcludeChannelVO] | Unset = UNSET
    power_mode: int | Unset = UNSET
    power_range: PowerRangeVO | Unset = UNSET
    width_select_en: bool | Unset = UNSET
    width_range: WidthRangeVO | Unset = UNSET
    power_threshold: PowerThresholdVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude_5_g_ch_en = self.exclude_5_g_ch_en

        exclude_5_g_ch: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.exclude_5_g_ch, Unset):
            exclude_5_g_ch = []
            for exclude_5_g_ch_item_data in self.exclude_5_g_ch:
                exclude_5_g_ch_item = exclude_5_g_ch_item_data.to_dict()
                exclude_5_g_ch.append(exclude_5_g_ch_item)

        power_mode = self.power_mode

        power_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power_range, Unset):
            power_range = self.power_range.to_dict()

        width_select_en = self.width_select_en

        width_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width_range, Unset):
            width_range = self.width_range.to_dict()

        power_threshold: dict[str, Any] | Unset = UNSET
        if not isinstance(self.power_threshold, Unset):
            power_threshold = self.power_threshold.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude_5_g_ch_en is not UNSET:
            field_dict["exclude5gChEn"] = exclude_5_g_ch_en
        if exclude_5_g_ch is not UNSET:
            field_dict["exclude5gCh"] = exclude_5_g_ch
        if power_mode is not UNSET:
            field_dict["powerMode"] = power_mode
        if power_range is not UNSET:
            field_dict["powerRange"] = power_range
        if width_select_en is not UNSET:
            field_dict["widthSelectEn"] = width_select_en
        if width_range is not UNSET:
            field_dict["widthRange"] = width_range
        if power_threshold is not UNSET:
            field_dict["powerThreshold"] = power_threshold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.exclude_channel_vo import ExcludeChannelVO
        from ..models.power_range_vo import PowerRangeVO
        from ..models.power_threshold_vo import PowerThresholdVO
        from ..models.width_range_vo import WidthRangeVO

        d = dict(src_dict)
        exclude_5_g_ch_en = d.pop("exclude5gChEn", UNSET)

        _exclude_5_g_ch = d.pop("exclude5gCh", UNSET)
        exclude_5_g_ch: list[ExcludeChannelVO] | Unset = UNSET
        if _exclude_5_g_ch is not UNSET:
            exclude_5_g_ch = []
            for exclude_5_g_ch_item_data in _exclude_5_g_ch:
                exclude_5_g_ch_item = ExcludeChannelVO.from_dict(
                    exclude_5_g_ch_item_data
                )

                exclude_5_g_ch.append(exclude_5_g_ch_item)

        power_mode = d.pop("powerMode", UNSET)

        _power_range = d.pop("powerRange", UNSET)
        power_range: PowerRangeVO | Unset
        if isinstance(_power_range, Unset):
            power_range = UNSET
        else:
            power_range = PowerRangeVO.from_dict(_power_range)

        width_select_en = d.pop("widthSelectEn", UNSET)

        _width_range = d.pop("widthRange", UNSET)
        width_range: WidthRangeVO | Unset
        if isinstance(_width_range, Unset):
            width_range = UNSET
        else:
            width_range = WidthRangeVO.from_dict(_width_range)

        _power_threshold = d.pop("powerThreshold", UNSET)
        power_threshold: PowerThresholdVO | Unset
        if isinstance(_power_threshold, Unset):
            power_threshold = UNSET
        else:
            power_threshold = PowerThresholdVO.from_dict(_power_threshold)

        planning_advanced_setting_vo = cls(
            exclude_5_g_ch_en=exclude_5_g_ch_en,
            exclude_5_g_ch=exclude_5_g_ch,
            power_mode=power_mode,
            power_range=power_range,
            width_select_en=width_select_en,
            width_range=width_range,
            power_threshold=power_threshold,
        )

        planning_advanced_setting_vo.additional_properties = d
        return planning_advanced_setting_vo

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
