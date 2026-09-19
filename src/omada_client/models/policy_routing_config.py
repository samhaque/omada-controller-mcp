from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolicyRoutingConfig")


@_attrs_define
class PolicyRoutingConfig:
    """
    Attributes:
        name (str): Name, name should contain 1 to 64 characters.
        status (bool): Status
        protocols (list[int]): For the values of protocols, refer to section 5.5.2 of the Open API Access Guide.
        backup_interface (bool): Use the other WAN port if the current one is down
        source_type (int): SourceType should be a value as follows: 0: Network; 1: IP Group; 2: IP port Group
        source_ids (list[str]): Source IDs, which depends on sourceType, for example: if sourceType is network,
            sourceIds should be LAN network ID. LAN Network can be created using 'Create LAN network' interface, and LAN
            Network ID can be obtained from 'Get LAN network list' interface.
        destination_type (int): DestinationType should be a value as follows: 0: Network; 1: IP Group; 2: IP port Group
        destination_ids (list[str]): Destination IDs, which depends on destinationType, for example: if destinationType
            is network, destinationIds should be LAN network ID. LAN Network can be created using 'Create LAN network'
            interface, and LAN Network ID can be obtained from 'Get LAN network list' interface.
        interface_type (int | Unset): InterfaceType should be a value as follows: 0: WAN; 2: L2TP; 3: PPTP; 4: multi-
            select WAN or VPN or virtual WAN.
        interface_id (str | Unset): Interface ID
        wan_port_ids (list[str] | Unset): WAN port list. When interfaceType is 4, at least one of the wanPortIds or
            vpnIds or virtualWanIds is not empty.
        vpn_ids (list[str] | Unset): VPN list. When interfaceType is 4, at least one of the wanPortIds or vpnIds or
            virtualWanIds is not empty.
        virtual_wan_ids (list[str] | Unset): Virtual WAN list. When interfaceType is 4, at least one of the wanPortIds
            or vpnIds or virtualWanIds is not empty.
    """

    name: str
    status: bool
    protocols: list[int]
    backup_interface: bool
    source_type: int
    source_ids: list[str]
    destination_type: int
    destination_ids: list[str]
    interface_type: int | Unset = UNSET
    interface_id: str | Unset = UNSET
    wan_port_ids: list[str] | Unset = UNSET
    vpn_ids: list[str] | Unset = UNSET
    virtual_wan_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        protocols = self.protocols

        backup_interface = self.backup_interface

        source_type = self.source_type

        source_ids = self.source_ids

        destination_type = self.destination_type

        destination_ids = self.destination_ids

        interface_type = self.interface_type

        interface_id = self.interface_id

        wan_port_ids: list[str] | Unset = UNSET
        if not isinstance(self.wan_port_ids, Unset):
            wan_port_ids = self.wan_port_ids

        vpn_ids: list[str] | Unset = UNSET
        if not isinstance(self.vpn_ids, Unset):
            vpn_ids = self.vpn_ids

        virtual_wan_ids: list[str] | Unset = UNSET
        if not isinstance(self.virtual_wan_ids, Unset):
            virtual_wan_ids = self.virtual_wan_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "protocols": protocols,
                "backupInterface": backup_interface,
                "sourceType": source_type,
                "sourceIds": source_ids,
                "destinationType": destination_type,
                "destinationIds": destination_ids,
            }
        )
        if interface_type is not UNSET:
            field_dict["interfaceType"] = interface_type
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if wan_port_ids is not UNSET:
            field_dict["wanPortIds"] = wan_port_ids
        if vpn_ids is not UNSET:
            field_dict["vpnIds"] = vpn_ids
        if virtual_wan_ids is not UNSET:
            field_dict["virtualWanIds"] = virtual_wan_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        protocols = cast(list[int], d.pop("protocols"))

        backup_interface = d.pop("backupInterface")

        source_type = d.pop("sourceType")

        source_ids = cast(list[str], d.pop("sourceIds"))

        destination_type = d.pop("destinationType")

        destination_ids = cast(list[str], d.pop("destinationIds"))

        interface_type = d.pop("interfaceType", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        wan_port_ids = cast(list[str], d.pop("wanPortIds", UNSET))

        vpn_ids = cast(list[str], d.pop("vpnIds", UNSET))

        virtual_wan_ids = cast(list[str], d.pop("virtualWanIds", UNSET))

        policy_routing_config = cls(
            name=name,
            status=status,
            protocols=protocols,
            backup_interface=backup_interface,
            source_type=source_type,
            source_ids=source_ids,
            destination_type=destination_type,
            destination_ids=destination_ids,
            interface_type=interface_type,
            interface_id=interface_id,
            wan_port_ids=wan_port_ids,
            vpn_ids=vpn_ids,
            virtual_wan_ids=virtual_wan_ids,
        )

        policy_routing_config.additional_properties = d
        return policy_routing_config

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
