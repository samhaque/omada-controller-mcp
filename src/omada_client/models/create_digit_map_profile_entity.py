from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="CreateDigitMapProfileEntity")


@_attrs_define
class CreateDigitMapProfileEntity:
    """
    Attributes:
        profile_name (str): Digit map profile name
        digit_map (str): Digit map
    """

    profile_name: str
    digit_map: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        digit_map = self.digit_map

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileName": profile_name,
                "digitMap": digit_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_name = d.pop("profileName")

        digit_map = d.pop("digitMap")

        create_digit_map_profile_entity = cls(
            profile_name=profile_name,
            digit_map=digit_map,
        )

        create_digit_map_profile_entity.additional_properties = d
        return create_digit_map_profile_entity

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
