from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GatewayACLStatesEntity")


@_attrs_define
class GatewayACLStatesEntity:
    """Only for Gateway ACL

    Attributes:
        state_new (bool | Unset): Match state new
        established (bool | Unset): Match state established
        related (bool | Unset): Match state related
        invalid (bool | Unset): Match state invalid
    """

    state_new: bool | Unset = UNSET
    established: bool | Unset = UNSET
    related: bool | Unset = UNSET
    invalid: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state_new = self.state_new

        established = self.established

        related = self.related

        invalid = self.invalid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if state_new is not UNSET:
            field_dict["stateNew"] = state_new
        if established is not UNSET:
            field_dict["established"] = established
        if related is not UNSET:
            field_dict["related"] = related
        if invalid is not UNSET:
            field_dict["invalid"] = invalid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        state_new = d.pop("stateNew", UNSET)

        established = d.pop("established", UNSET)

        related = d.pop("related", UNSET)

        invalid = d.pop("invalid", UNSET)

        gateway_acl_states_entity = cls(
            state_new=state_new,
            established=established,
            related=related,
            invalid=invalid,
        )

        gateway_acl_states_entity.additional_properties = d
        return gateway_acl_states_entity

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
