from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeInfoVO")


@_attrs_define
class NodeInfoVO:
    """
    Attributes:
        node_name (str | Unset):
        current_node (str | Unset):
        role (str | Unset):
        system_time (int | Unset):
        status (str | Unset):
        managed_sites (int | Unset):
        managed_devices (int | Unset):
    """

    node_name: str | Unset = UNSET
    current_node: str | Unset = UNSET
    role: str | Unset = UNSET
    system_time: int | Unset = UNSET
    status: str | Unset = UNSET
    managed_sites: int | Unset = UNSET
    managed_devices: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_name = self.node_name

        current_node = self.current_node

        role = self.role

        system_time = self.system_time

        status = self.status

        managed_sites = self.managed_sites

        managed_devices = self.managed_devices

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_name is not UNSET:
            field_dict["nodeName"] = node_name
        if current_node is not UNSET:
            field_dict["currentNode"] = current_node
        if role is not UNSET:
            field_dict["role"] = role
        if system_time is not UNSET:
            field_dict["systemTime"] = system_time
        if status is not UNSET:
            field_dict["status"] = status
        if managed_sites is not UNSET:
            field_dict["managedSites"] = managed_sites
        if managed_devices is not UNSET:
            field_dict["managedDevices"] = managed_devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        node_name = d.pop("nodeName", UNSET)

        current_node = d.pop("currentNode", UNSET)

        role = d.pop("role", UNSET)

        system_time = d.pop("systemTime", UNSET)

        status = d.pop("status", UNSET)

        managed_sites = d.pop("managedSites", UNSET)

        managed_devices = d.pop("managedDevices", UNSET)

        node_info_vo = cls(
            node_name=node_name,
            current_node=current_node,
            role=role,
            system_time=system_time,
            status=status,
            managed_sites=managed_sites,
            managed_devices=managed_devices,
        )

        node_info_vo.additional_properties = d
        return node_info_vo

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
