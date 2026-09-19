from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="BatchProfileOverride")


@_attrs_define
class BatchProfileOverride:
    """
    Attributes:
        port_list (list[int]): Port ID List.
        profile_override_enable (bool): Profile Override Enable.
    """

    port_list: list[int]
    profile_override_enable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_list = self.port_list

        profile_override_enable = self.profile_override_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portList": port_list,
                "profileOverrideEnable": profile_override_enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_list = cast(list[int], d.pop("portList"))

        profile_override_enable = d.pop("profileOverrideEnable")

        batch_profile_override = cls(
            port_list=port_list,
            profile_override_enable=profile_override_enable,
        )

        batch_profile_override.additional_properties = d
        return batch_profile_override

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
