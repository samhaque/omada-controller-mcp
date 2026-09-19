from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PpskProfileBriefInfo")


@_attrs_define
class PpskProfileBriefInfo:
    """PPSK Profile Brief Info.

    Attributes:
        profile_name (str): PPSK Profile Name, should contain 1 to 64 characters.
        id (str | Unset): PPSK Profile ID
        ssid (list[str] | Unset): SSIDs Bound With PPSK Profile
    """

    profile_name: str
    id: str | Unset = UNSET
    ssid: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_name = self.profile_name

        id = self.id

        ssid: list[str] | Unset = UNSET
        if not isinstance(self.ssid, Unset):
            ssid = self.ssid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileName": profile_name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if ssid is not UNSET:
            field_dict["ssid"] = ssid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_name = d.pop("profileName")

        id = d.pop("id", UNSET)

        ssid = cast(list[str], d.pop("ssid", UNSET))

        ppsk_profile_brief_info = cls(
            profile_name=profile_name,
            id=id,
            ssid=ssid,
        )

        ppsk_profile_brief_info.additional_properties = d
        return ppsk_profile_brief_info

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
