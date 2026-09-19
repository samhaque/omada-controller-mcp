from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_rate_limit_setting_open_api_vo import (
        CustomRateLimitSettingOpenApiVO,
    )


T = TypeVar("T", bound="RateLimitSettingOpenApiVO")


@_attrs_define
class RateLimitSettingOpenApiVO:
    """SSID rate limit config.

    Attributes:
        profile_id (str | Unset): This field represents RateLimit Profile ID. RateLimit Profile can be created using
            Create rate limit profile interface, and RateLimit Profile ID can be obtained from Get rate limit profile list
            interface.(The validity priority is higher than the custom setting)
        custom_setting (CustomRateLimitSettingOpenApiVO | Unset): Rate limit custom setting
    """

    profile_id: str | Unset = UNSET
    custom_setting: CustomRateLimitSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        custom_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_setting, Unset):
            custom_setting = self.custom_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if custom_setting is not UNSET:
            field_dict["customSetting"] = custom_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_rate_limit_setting_open_api_vo import (
            CustomRateLimitSettingOpenApiVO,
        )

        d = dict(src_dict)
        profile_id = d.pop("profileId", UNSET)

        _custom_setting = d.pop("customSetting", UNSET)
        custom_setting: CustomRateLimitSettingOpenApiVO | Unset
        if isinstance(_custom_setting, Unset):
            custom_setting = UNSET
        else:
            custom_setting = CustomRateLimitSettingOpenApiVO.from_dict(_custom_setting)

        rate_limit_setting_open_api_vo = cls(
            profile_id=profile_id,
            custom_setting=custom_setting,
        )

        rate_limit_setting_open_api_vo.additional_properties = d
        return rate_limit_setting_open_api_vo

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
