from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_picture_info import PortalPictureInfo


T = TypeVar("T", bound="AdvertisementSettingResOpenApiVO")


@_attrs_define
class AdvertisementSettingResOpenApiVO:
    """Advertisement setting

    Attributes:
        enable (bool | Unset): Whether to enable Advertisement setting
        pictures (list[PortalPictureInfo] | Unset): Advertisement picture list. Up to 5 entries are allowed for the
            pictures list
        total_duration (int | Unset): Total duration of advertisement, should be within the range of 1–30 seconds
        picture_interval (int | Unset): Advertisement picture interval, should be within the range of 1–10 seconds
        skip_enable (bool | Unset): Whether to allow users to skip the advertisement
        skip_delay (int | Unset): Skip delay, should be within the range of 1–10, time unit is second.
    """

    enable: bool | Unset = UNSET
    pictures: list[PortalPictureInfo] | Unset = UNSET
    total_duration: int | Unset = UNSET
    picture_interval: int | Unset = UNSET
    skip_enable: bool | Unset = UNSET
    skip_delay: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        pictures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pictures, Unset):
            pictures = []
            for pictures_item_data in self.pictures:
                pictures_item = pictures_item_data.to_dict()
                pictures.append(pictures_item)

        total_duration = self.total_duration

        picture_interval = self.picture_interval

        skip_enable = self.skip_enable

        skip_delay = self.skip_delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if pictures is not UNSET:
            field_dict["pictures"] = pictures
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
        from ..models.portal_picture_info import PortalPictureInfo

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        _pictures = d.pop("pictures", UNSET)
        pictures: list[PortalPictureInfo] | Unset = UNSET
        if _pictures is not UNSET:
            pictures = []
            for pictures_item_data in _pictures:
                pictures_item = PortalPictureInfo.from_dict(pictures_item_data)

                pictures.append(pictures_item)

        total_duration = d.pop("totalDuration", UNSET)

        picture_interval = d.pop("pictureInterval", UNSET)

        skip_enable = d.pop("skipEnable", UNSET)

        skip_delay = d.pop("skipDelay", UNSET)

        advertisement_setting_res_open_api_vo = cls(
            enable=enable,
            pictures=pictures,
            total_duration=total_duration,
            picture_interval=picture_interval,
            skip_enable=skip_enable,
            skip_delay=skip_delay,
        )

        advertisement_setting_res_open_api_vo.additional_properties = d
        return advertisement_setting_res_open_api_vo

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
