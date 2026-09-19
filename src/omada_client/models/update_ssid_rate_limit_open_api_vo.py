from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rate_limit_setting_open_api_vo import RateLimitSettingOpenApiVO


T = TypeVar("T", bound="UpdateSsidRateLimitOpenApiVO")


@_attrs_define
class UpdateSsidRateLimitOpenApiVO:
    """
    Attributes:
        client_rate_limit (RateLimitSettingOpenApiVO | Unset): SSID rate limit config.
        ssid_rate_limit (RateLimitSettingOpenApiVO | Unset): SSID rate limit config.
    """

    client_rate_limit: RateLimitSettingOpenApiVO | Unset = UNSET
    ssid_rate_limit: RateLimitSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_rate_limit, Unset):
            client_rate_limit = self.client_rate_limit.to_dict()

        ssid_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssid_rate_limit, Unset):
            ssid_rate_limit = self.ssid_rate_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_rate_limit is not UNSET:
            field_dict["clientRateLimit"] = client_rate_limit
        if ssid_rate_limit is not UNSET:
            field_dict["ssidRateLimit"] = ssid_rate_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.rate_limit_setting_open_api_vo import (
            RateLimitSettingOpenApiVO,
        )

        d = dict(src_dict)
        _client_rate_limit = d.pop("clientRateLimit", UNSET)
        client_rate_limit: RateLimitSettingOpenApiVO | Unset
        if isinstance(_client_rate_limit, Unset):
            client_rate_limit = UNSET
        else:
            client_rate_limit = RateLimitSettingOpenApiVO.from_dict(_client_rate_limit)

        _ssid_rate_limit = d.pop("ssidRateLimit", UNSET)
        ssid_rate_limit: RateLimitSettingOpenApiVO | Unset
        if isinstance(_ssid_rate_limit, Unset):
            ssid_rate_limit = UNSET
        else:
            ssid_rate_limit = RateLimitSettingOpenApiVO.from_dict(_ssid_rate_limit)

        update_ssid_rate_limit_open_api_vo = cls(
            client_rate_limit=client_rate_limit,
            ssid_rate_limit=ssid_rate_limit,
        )

        update_ssid_rate_limit_open_api_vo.additional_properties = d
        return update_ssid_rate_limit_open_api_vo

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
