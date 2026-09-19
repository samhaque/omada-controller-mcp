from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RaSetting")


@_attrs_define
class RaSetting:
    """Ra Setting

    Attributes:
        enable (bool | Unset): The switch of Ra
        preference (int | Unset): Preference should be a value as follows: 0: "low"; 1: "medium"; 2: "high"
        valid_lifetime (int | Unset): ValidLifetime should be larger than PreferredLifetime.
        preferred_lifetime (int | Unset): PreferredLifetime
    """

    enable: bool | Unset = UNSET
    preference: int | Unset = UNSET
    valid_lifetime: int | Unset = UNSET
    preferred_lifetime: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        preference = self.preference

        valid_lifetime = self.valid_lifetime

        preferred_lifetime = self.preferred_lifetime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if preference is not UNSET:
            field_dict["preference"] = preference
        if valid_lifetime is not UNSET:
            field_dict["validLifetime"] = valid_lifetime
        if preferred_lifetime is not UNSET:
            field_dict["preferredLifetime"] = preferred_lifetime

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        preference = d.pop("preference", UNSET)

        valid_lifetime = d.pop("validLifetime", UNSET)

        preferred_lifetime = d.pop("preferredLifetime", UNSET)

        ra_setting = cls(
            enable=enable,
            preference=preference,
            valid_lifetime=valid_lifetime,
            preferred_lifetime=preferred_lifetime,
        )

        ra_setting.additional_properties = d
        return ra_setting

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
