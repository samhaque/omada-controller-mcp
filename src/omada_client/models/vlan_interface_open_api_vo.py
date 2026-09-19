from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VlanInterfaceOpenApiVO")


@_attrs_define
class VlanInterfaceOpenApiVO:
    """
    Attributes:
        vlan_interface_id (str | Unset): Vlan Interface ID
        vlan_interface_name (str | Unset): Vlan Interface Name
        vlan_id (int | Unset): Vlan ID
    """

    vlan_interface_id: str | Unset = UNSET
    vlan_interface_name: str | Unset = UNSET
    vlan_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan_interface_id = self.vlan_interface_id

        vlan_interface_name = self.vlan_interface_name

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vlan_interface_id is not UNSET:
            field_dict["vlanInterfaceId"] = vlan_interface_id
        if vlan_interface_name is not UNSET:
            field_dict["vlanInterfaceName"] = vlan_interface_name
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vlan_interface_id = d.pop("vlanInterfaceId", UNSET)

        vlan_interface_name = d.pop("vlanInterfaceName", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vlan_interface_open_api_vo = cls(
            vlan_interface_id=vlan_interface_id,
            vlan_interface_name=vlan_interface_name,
            vlan_id=vlan_id,
        )

        vlan_interface_open_api_vo.additional_properties = d
        return vlan_interface_open_api_vo

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
