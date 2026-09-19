from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_profile_open_api_vo_profiles import OswProfileOpenApiVOProfiles


T = TypeVar("T", bound="OswProfileOpenApiVO")


@_attrs_define
class OswProfileOpenApiVO:
    """
    Attributes:
        name (str | Unset): Switch name
        mac (str | Unset): Switch MAC
        profiles (OswProfileOpenApiVOProfiles | Unset): Switch port profiles
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    profiles: OswProfileOpenApiVOProfiles | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        profiles: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profiles, Unset):
            profiles = self.profiles.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if profiles is not UNSET:
            field_dict["profiles"] = profiles

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_profile_open_api_vo_profiles import (
            OswProfileOpenApiVOProfiles,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        _profiles = d.pop("profiles", UNSET)
        profiles: OswProfileOpenApiVOProfiles | Unset
        if isinstance(_profiles, Unset):
            profiles = UNSET
        else:
            profiles = OswProfileOpenApiVOProfiles.from_dict(_profiles)

        osw_profile_open_api_vo = cls(
            name=name,
            mac=mac,
            profiles=profiles,
        )

        osw_profile_open_api_vo.additional_properties = d
        return osw_profile_open_api_vo

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
