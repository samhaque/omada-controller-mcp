from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gateway_custom_acl_add_entity import GatewayCustomACLAddEntity
    from ..models.gateway_custom_acl_modify_entity import GatewayCustomACLModifyEntity


T = TypeVar("T", bound="GatewayCustomACLUpdateEntity")


@_attrs_define
class GatewayCustomACLUpdateEntity:
    """
    Attributes:
        adds (list[GatewayCustomACLAddEntity] | Unset): Added Custom ACLs.
        deletes (list[str] | Unset): Deleted Custom ACLs.
        modifies (list[GatewayCustomACLModifyEntity] | Unset): Modified Custom ACLs.
    """

    adds: list[GatewayCustomACLAddEntity] | Unset = UNSET
    deletes: list[str] | Unset = UNSET
    modifies: list[GatewayCustomACLModifyEntity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        adds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.adds, Unset):
            adds = []
            for adds_item_data in self.adds:
                adds_item = adds_item_data.to_dict()
                adds.append(adds_item)

        deletes: list[str] | Unset = UNSET
        if not isinstance(self.deletes, Unset):
            deletes = self.deletes

        modifies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.modifies, Unset):
            modifies = []
            for modifies_item_data in self.modifies:
                modifies_item = modifies_item_data.to_dict()
                modifies.append(modifies_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if adds is not UNSET:
            field_dict["adds"] = adds
        if deletes is not UNSET:
            field_dict["deletes"] = deletes
        if modifies is not UNSET:
            field_dict["modifies"] = modifies

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.gateway_custom_acl_add_entity import (
            GatewayCustomACLAddEntity,
        )
        from ..models.gateway_custom_acl_modify_entity import (
            GatewayCustomACLModifyEntity,
        )

        d = dict(src_dict)
        _adds = d.pop("adds", UNSET)
        adds: list[GatewayCustomACLAddEntity] | Unset = UNSET
        if _adds is not UNSET:
            adds = []
            for adds_item_data in _adds:
                adds_item = GatewayCustomACLAddEntity.from_dict(adds_item_data)

                adds.append(adds_item)

        deletes = cast(list[str], d.pop("deletes", UNSET))

        _modifies = d.pop("modifies", UNSET)
        modifies: list[GatewayCustomACLModifyEntity] | Unset = UNSET
        if _modifies is not UNSET:
            modifies = []
            for modifies_item_data in _modifies:
                modifies_item = GatewayCustomACLModifyEntity.from_dict(
                    modifies_item_data
                )

                modifies.append(modifies_item)

        gateway_custom_acl_update_entity = cls(
            adds=adds,
            deletes=deletes,
            modifies=modifies,
        )

        gateway_custom_acl_update_entity.additional_properties = d
        return gateway_custom_acl_update_entity

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
