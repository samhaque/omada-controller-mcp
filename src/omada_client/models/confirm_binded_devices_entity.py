from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ConfirmBindedDevicesEntity")


@_attrs_define
class ConfirmBindedDevicesEntity:
    """
    Attributes:
        profile_ids (list[str]): Provider profile IDs
        skip_confirm (bool): skipConfirm indicates whether to skip the query of the devices bound to provider profiles.
            false: Not to skip the query. true: Skip the query and delete the provider profiles corresponding to the
            profileIds.
    """

    profile_ids: list[str]
    skip_confirm: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_ids = self.profile_ids

        skip_confirm = self.skip_confirm

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileIds": profile_ids,
                "skipConfirm": skip_confirm,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_ids = cast(list[str], d.pop("profileIds"))

        skip_confirm = d.pop("skipConfirm")

        confirm_binded_devices_entity = cls(
            profile_ids=profile_ids,
            skip_confirm=skip_confirm,
        )

        confirm_binded_devices_entity.additional_properties = d
        return confirm_binded_devices_entity

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
