from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkPortsAssociationVO")


@_attrs_define
class NetworkPortsAssociationVO:
    """NetworkPortsAssociationVO

    Attributes:
        id (str | Unset): Network's ID
        name (str | Unset): Network's name
        vlan (int | Unset): VLAN ID
        native_ports (list[int] | Unset): Native ports list
        untagged_ports (list[int] | Unset): Untagged ports list
        tagged_ports (list[int] | Unset): Tagged ports list
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    native_ports: list[int] | Unset = UNSET
    untagged_ports: list[int] | Unset = UNSET
    tagged_ports: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vlan = self.vlan

        native_ports: list[int] | Unset = UNSET
        if not isinstance(self.native_ports, Unset):
            native_ports = self.native_ports

        untagged_ports: list[int] | Unset = UNSET
        if not isinstance(self.untagged_ports, Unset):
            untagged_ports = self.untagged_ports

        tagged_ports: list[int] | Unset = UNSET
        if not isinstance(self.tagged_ports, Unset):
            tagged_ports = self.tagged_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if native_ports is not UNSET:
            field_dict["nativePorts"] = native_ports
        if untagged_ports is not UNSET:
            field_dict["untaggedPorts"] = untagged_ports
        if tagged_ports is not UNSET:
            field_dict["taggedPorts"] = tagged_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vlan = d.pop("vlan", UNSET)

        native_ports = cast(list[int], d.pop("nativePorts", UNSET))

        untagged_ports = cast(list[int], d.pop("untaggedPorts", UNSET))

        tagged_ports = cast(list[int], d.pop("taggedPorts", UNSET))

        network_ports_association_vo = cls(
            id=id,
            name=name,
            vlan=vlan,
            native_ports=native_ports,
            untagged_ports=untagged_ports,
            tagged_ports=tagged_ports,
        )

        network_ports_association_vo.additional_properties = d
        return network_ports_association_vo

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
