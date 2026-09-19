from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyDigitMapProfileEntity")


@_attrs_define
class ModifyDigitMapProfileEntity:
    """
    Attributes:
        profile_name (str | Unset): Digit map profile name
        digit_map (str | Unset): Digit map
    """

    profile_name: str | Unset = UNSET
    digit_map: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        digit_map = self.digit_map

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if digit_map is not UNSET:
            field_dict["digitMap"] = digit_map

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_name = d.pop("profileName", UNSET)

        digit_map = d.pop("digitMap", UNSET)

        modify_digit_map_profile_entity = cls(
            profile_name=profile_name,
            digit_map=digit_map,
        )

        modify_digit_map_profile_entity.additional_properties = d
        return modify_digit_map_profile_entity

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
