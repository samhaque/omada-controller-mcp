from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_rate_limit_entity import CustomRateLimitEntity


T = TypeVar("T", bound="ClientRateLimitSetting")


@_attrs_define
class ClientRateLimitSetting:
    """Setting of rate limit.

    Attributes:
        mode (int): Rate limit mode should be a value as follows: <br/>0: Custom mode. Apply the given rate limit value
            to the client; <br/>1: Rate limit profile mode. Find the corresponding rate limit file with rate limit ID and
            apply it to the client.
        rate_limit_profile_id (str | Unset): Rate limit profile ID. Required when ratelimit mode is 1
        custom_rate_limit (CustomRateLimitEntity | Unset): Custom configuration rate limit.
    """

    mode: int
    rate_limit_profile_id: str | Unset = UNSET
    custom_rate_limit: CustomRateLimitEntity | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        rate_limit_profile_id = self.rate_limit_profile_id

        custom_rate_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_rate_limit, Unset):
            custom_rate_limit = self.custom_rate_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if rate_limit_profile_id is not UNSET:
            field_dict["rateLimitProfileId"] = rate_limit_profile_id
        if custom_rate_limit is not UNSET:
            field_dict["customRateLimit"] = custom_rate_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_rate_limit_entity import (
            CustomRateLimitEntity,
        )

        d = dict(src_dict)
        mode = d.pop("mode")

        rate_limit_profile_id = d.pop("rateLimitProfileId", UNSET)

        _custom_rate_limit = d.pop("customRateLimit", UNSET)
        custom_rate_limit: CustomRateLimitEntity | Unset
        if isinstance(_custom_rate_limit, Unset):
            custom_rate_limit = UNSET
        else:
            custom_rate_limit = CustomRateLimitEntity.from_dict(_custom_rate_limit)

        client_rate_limit_setting = cls(
            mode=mode,
            rate_limit_profile_id=rate_limit_profile_id,
            custom_rate_limit=custom_rate_limit,
        )

        client_rate_limit_setting.additional_properties = d
        return client_rate_limit_setting

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
