from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PPSKRateLimitSettingVO")


@_attrs_define
class PPSKRateLimitSettingVO:
    """PPSK Profile Rate Limit config.

    Attributes:
        rate_limit_profile_id (str | Unset): This field represents Rate limit profile ID. Rate limit profile can be
            created using 'Create rate limit profile' interface, and Rate limit profile ID can be obtained from 'Get rate
            limit profile list' interface
        down_limit_enable (bool | Unset): Whether to limit downlink speed; This field is required when select custom
            setting. True: enable, false: disable.
        down_limit (int | Unset): Downlink speed limit value. When the value of Parameter [downLimitType] is 0(Kbps),
            downLimit should be within the range of 1–10485760; when the value of Parameter [downLimitType] is 1(Mbps),
            downLimit should be within the range of 1-10240.
        down_limit_type (int | Unset): Downlink speed limit unit config; DownLimitType should be a value as follows: 0:
            Kbps; 1: Mbps.
        up_limit_enable (bool | Unset): Whether to limit uplink speed; This field is required when select custom
            setting. True: enable, false: disable.
        up_limit (int | Unset): Uplink speed limit value. When the value of Parameter [upLimitType] is 0(Kbps), upLimit
            should be within the range of 1–10485760; when the value of Parameter [upLimitType] is 1(Mbps), upLimit should
            be within the range of 1-10240.
        up_limit_type (int | Unset): Uplink speed limit unit config; UpLimitType should be a value as follows: 0: Kbps;
            1: Mbps.
    """

    rate_limit_profile_id: str | Unset = UNSET
    down_limit_enable: bool | Unset = UNSET
    down_limit: int | Unset = UNSET
    down_limit_type: int | Unset = UNSET
    up_limit_enable: bool | Unset = UNSET
    up_limit: int | Unset = UNSET
    up_limit_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rate_limit_profile_id = self.rate_limit_profile_id

        down_limit_enable = self.down_limit_enable

        down_limit = self.down_limit

        down_limit_type = self.down_limit_type

        up_limit_enable = self.up_limit_enable

        up_limit = self.up_limit

        up_limit_type = self.up_limit_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rate_limit_profile_id is not UNSET:
            field_dict["rateLimitProfileId"] = rate_limit_profile_id
        if down_limit_enable is not UNSET:
            field_dict["downLimitEnable"] = down_limit_enable
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if down_limit_type is not UNSET:
            field_dict["downLimitType"] = down_limit_type
        if up_limit_enable is not UNSET:
            field_dict["upLimitEnable"] = up_limit_enable
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if up_limit_type is not UNSET:
            field_dict["upLimitType"] = up_limit_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rate_limit_profile_id = d.pop("rateLimitProfileId", UNSET)

        down_limit_enable = d.pop("downLimitEnable", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        down_limit_type = d.pop("downLimitType", UNSET)

        up_limit_enable = d.pop("upLimitEnable", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        up_limit_type = d.pop("upLimitType", UNSET)

        ppsk_rate_limit_setting_vo = cls(
            rate_limit_profile_id=rate_limit_profile_id,
            down_limit_enable=down_limit_enable,
            down_limit=down_limit,
            down_limit_type=down_limit_type,
            up_limit_enable=up_limit_enable,
            up_limit=up_limit,
            up_limit_type=up_limit_type,
        )

        ppsk_rate_limit_setting_vo.additional_properties = d
        return ppsk_rate_limit_setting_vo

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
