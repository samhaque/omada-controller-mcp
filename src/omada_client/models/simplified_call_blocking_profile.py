from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SimplifiedCallBlockingProfile")


@_attrs_define
class SimplifiedCallBlockingProfile:
    """
    Attributes:
        call_blocking_profile_id (str | Unset): Call blocking profile id.
        call_blocking_profile_name (str | Unset): Call blocking profile name.
    """

    call_blocking_profile_id: str | Unset = UNSET
    call_blocking_profile_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        call_blocking_profile_id = self.call_blocking_profile_id

        call_blocking_profile_name = self.call_blocking_profile_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if call_blocking_profile_id is not UNSET:
            field_dict["callBlockingProfileId"] = call_blocking_profile_id
        if call_blocking_profile_name is not UNSET:
            field_dict["callBlockingProfileName"] = call_blocking_profile_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        call_blocking_profile_id = d.pop("callBlockingProfileId", UNSET)

        call_blocking_profile_name = d.pop("callBlockingProfileName", UNSET)

        simplified_call_blocking_profile = cls(
            call_blocking_profile_id=call_blocking_profile_id,
            call_blocking_profile_name=call_blocking_profile_name,
        )

        simplified_call_blocking_profile.additional_properties = d
        return simplified_call_blocking_profile

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
