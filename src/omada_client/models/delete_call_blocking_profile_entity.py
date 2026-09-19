from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeleteCallBlockingProfileEntity")


@_attrs_define
class DeleteCallBlockingProfileEntity:
    """
    Attributes:
        profile_id (str): Profile ID
        skip_confirm (bool): skipConfirm indicates whether to skip the query of the devices bound to call blocking
            profile. false: Not to skip the query. true: Skip the query and delete the call blocking profile corresponding
            to the profileId.
    """

    profile_id: str
    skip_confirm: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        skip_confirm = self.skip_confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileId": profile_id,
                "skipConfirm": skip_confirm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_id = d.pop("profileId")

        skip_confirm = d.pop("skipConfirm")

        delete_call_blocking_profile_entity = cls(
            profile_id=profile_id,
            skip_confirm=skip_confirm,
        )

        delete_call_blocking_profile_entity.additional_properties = d
        return delete_call_blocking_profile_entity

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
