from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DigitMapProfileInfo")


@_attrs_define
class DigitMapProfileInfo:
    """
    Attributes:
        profile_id (str | Unset): Digit map profile ID
        omadac_id (str | Unset): Omadac ID
        site_id (str | Unset): Site ID
        profile_name (str | Unset): Digit map profile name
        digit_map (str | Unset): Digit map
        default_profile (bool | Unset): Whether the digit map profile is the default one.
    """

    profile_id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    profile_name: str | Unset = UNSET
    digit_map: str | Unset = UNSET
    default_profile: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        omadac_id = self.omadac_id

        site_id = self.site_id

        profile_name = self.profile_name

        digit_map = self.digit_map

        default_profile = self.default_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if digit_map is not UNSET:
            field_dict["digitMap"] = digit_map
        if default_profile is not UNSET:
            field_dict["defaultProfile"] = default_profile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_id = d.pop("profileId", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        profile_name = d.pop("profileName", UNSET)

        digit_map = d.pop("digitMap", UNSET)

        default_profile = d.pop("defaultProfile", UNSET)

        digit_map_profile_info = cls(
            profile_id=profile_id,
            omadac_id=omadac_id,
            site_id=site_id,
            profile_name=profile_name,
            digit_map=digit_map,
            default_profile=default_profile,
        )

        digit_map_profile_info.additional_properties = d
        return digit_map_profile_info

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
