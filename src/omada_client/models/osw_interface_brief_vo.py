from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswInterfaceBriefVO")


@_attrs_define
class OswInterfaceBriefVO:
    """
    Attributes:
        type_ (int | Unset): Interface type, 0: Loopback interface; 1: VLAN interface
        id (str | Unset): ID.
        interface_id (int | Unset): Interface ID. For loopback interface, the value is loopbackId. For vlan interface,
            the value is vlan.
        name (str | Unset): Interface Name. Not Null when type is 1.
    """

    type_: int | Unset = UNSET
    id: str | Unset = UNSET
    interface_id: int | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        interface_id = self.interface_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        id = d.pop("id", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        name = d.pop("name", UNSET)

        osw_interface_brief_vo = cls(
            type_=type_,
            id=id,
            interface_id=interface_id,
            name=name,
        )

        osw_interface_brief_vo.additional_properties = d
        return osw_interface_brief_vo

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
