from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_loopback_interface_vo import OswLoopbackInterfaceVO
    from ..models.osw_network_vo import OswNetworkVO


T = TypeVar("T", bound="OswInterfaceOpenApi")


@_attrs_define
class OswInterfaceOpenApi:
    """
    Attributes:
        interface_type (int): Interface type. 0: Loopback; 1: VLAN.
        name (str | Unset): Interface name.
        interface_id (int | Unset): Interface ID.
        status (int | Unset): Interface status. 0: disable, 1: enable.
        vlan_interface (OswNetworkVO | Unset): VLAN Interface.
        loopback_interface (OswLoopbackInterfaceVO | Unset):
    """

    interface_type: int
    name: str | Unset = UNSET
    interface_id: int | Unset = UNSET
    status: int | Unset = UNSET
    vlan_interface: OswNetworkVO | Unset = UNSET
    loopback_interface: OswLoopbackInterfaceVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_type = self.interface_type

        name = self.name

        interface_id = self.interface_id

        status = self.status

        vlan_interface: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vlan_interface, Unset):
            vlan_interface = self.vlan_interface.to_dict()

        loopback_interface: dict[str, Any] | Unset = UNSET
        if not isinstance(self.loopback_interface, Unset):
            loopback_interface = self.loopback_interface.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaceType": interface_type,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if status is not UNSET:
            field_dict["status"] = status
        if vlan_interface is not UNSET:
            field_dict["vlanInterface"] = vlan_interface
        if loopback_interface is not UNSET:
            field_dict["loopbackInterface"] = loopback_interface

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_loopback_interface_vo import (
            OswLoopbackInterfaceVO,
        )
        from ..models.osw_network_vo import OswNetworkVO

        d = dict(src_dict)
        interface_type = d.pop("interfaceType")

        name = d.pop("name", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        status = d.pop("status", UNSET)

        _vlan_interface = d.pop("vlanInterface", UNSET)
        vlan_interface: OswNetworkVO | Unset
        if isinstance(_vlan_interface, Unset):
            vlan_interface = UNSET
        else:
            vlan_interface = OswNetworkVO.from_dict(_vlan_interface)

        _loopback_interface = d.pop("loopbackInterface", UNSET)
        loopback_interface: OswLoopbackInterfaceVO | Unset
        if isinstance(_loopback_interface, Unset):
            loopback_interface = UNSET
        else:
            loopback_interface = OswLoopbackInterfaceVO.from_dict(_loopback_interface)

        osw_interface_open_api = cls(
            interface_type=interface_type,
            name=name,
            interface_id=interface_id,
            status=status,
            vlan_interface=vlan_interface,
            loopback_interface=loopback_interface,
        )

        osw_interface_open_api.additional_properties = d
        return osw_interface_open_api

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
