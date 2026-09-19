from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedDigitMapProfile")


@_attrs_define
class SimplifiedDigitMapProfile:
    """
    Attributes:
        digit_map_profile_id (str | Unset): Digit map profile ID.
        digit_map_profile_name (str | Unset): Digit map profile name.
    """

    digit_map_profile_id: str | Unset = UNSET
    digit_map_profile_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        digit_map_profile_id = self.digit_map_profile_id

        digit_map_profile_name = self.digit_map_profile_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digit_map_profile_id is not UNSET:
            field_dict["digitMapProfileId"] = digit_map_profile_id
        if digit_map_profile_name is not UNSET:
            field_dict["digitMapProfileName"] = digit_map_profile_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        digit_map_profile_id = d.pop("digitMapProfileId", UNSET)

        digit_map_profile_name = d.pop("digitMapProfileName", UNSET)

        simplified_digit_map_profile = cls(
            digit_map_profile_id=digit_map_profile_id,
            digit_map_profile_name=digit_map_profile_name,
        )

        simplified_digit_map_profile.additional_properties = d
        return simplified_digit_map_profile

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
