from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AdvertisementSetting")


@_attrs_define
class AdvertisementSetting:
    """Advertisement Setting.

    Attributes:
        enable (bool): Advertisement enable.
        picture_ids (list[str] | Unset): Picture ID list, Up to 5 entries are allowed for the pictureIds list.
        total_duration (int | Unset): Advertisement totalDuration, should be within the range of 1–30, time unit is
            second.
        picture_interval (int | Unset): Advertisement picture interval, should be within the range of 1–10, time unit is
            second.
        skip_enable (bool | Unset): Whether allow users to skip the advertisement.
        skip_delay (int | Unset): Skip delay, should be within the range of 1–10, time unit is second.
    """

    enable: bool
    picture_ids: list[str] | Unset = UNSET
    total_duration: int | Unset = UNSET
    picture_interval: int | Unset = UNSET
    skip_enable: bool | Unset = UNSET
    skip_delay: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        picture_ids: list[str] | Unset = UNSET
        if not isinstance(self.picture_ids, Unset):
            picture_ids = self.picture_ids

        total_duration = self.total_duration

        picture_interval = self.picture_interval

        skip_enable = self.skip_enable

        skip_delay = self.skip_delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if picture_ids is not UNSET:
            field_dict["pictureIds"] = picture_ids
        if total_duration is not UNSET:
            field_dict["totalDuration"] = total_duration
        if picture_interval is not UNSET:
            field_dict["pictureInterval"] = picture_interval
        if skip_enable is not UNSET:
            field_dict["skipEnable"] = skip_enable
        if skip_delay is not UNSET:
            field_dict["skipDelay"] = skip_delay

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        picture_ids = cast(list[str], d.pop("pictureIds", UNSET))

        total_duration = d.pop("totalDuration", UNSET)

        picture_interval = d.pop("pictureInterval", UNSET)

        skip_enable = d.pop("skipEnable", UNSET)

        skip_delay = d.pop("skipDelay", UNSET)

        advertisement_setting = cls(
            enable=enable,
            picture_ids=picture_ids,
            total_duration=total_duration,
            picture_interval=picture_interval,
            skip_enable=skip_enable,
            skip_delay=skip_delay,
        )

        advertisement_setting.additional_properties = d
        return advertisement_setting

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
