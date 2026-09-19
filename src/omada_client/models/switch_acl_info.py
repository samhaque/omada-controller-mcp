from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_acl_osw_open_api_vo import CustomAclOswOpenApiVO
    from ..models.switch_acl_ether_type_entity import SwitchACLEtherTypeEntity
    from ..models.switch_acl_port_entity import SwitchACLPortEntity


T = TypeVar("T", bound="SwitchACLInfo")


@_attrs_define
class SwitchACLInfo:
    """
    Attributes:
        id (str): ACL ID
        index (int): Index
        description (str): ACL rule description, description should contain 1 to 512 characters.
        status (bool): Status should be a value as follows: 0: disable; 1: enable
        policy (int): Policy should be a value as follows: 0: drop; 1: allow;
        protocols (list[int]): For the values of protocols, refer to section 5.5 of the Open API Access Guide.
        source_ids (list[str]): Source IDs, which depends on sourceType, for example: if sourceType is network,
            sourceIds should be LAN network ID. LAN Network can be created using 'Create LAN network' interface, and LAN
            Network ID can be obtained from 'Get LAN network list' interface.
        destination_ids (list[str]): Destination IDs, which depends on destinationType, for example: if destinationType
            is network, destinationIds should be LAN network ID. LAN Network can be created using 'Create LAN network'
            interface, and LAN Network ID can be obtained from 'Get LAN network list' interface.
        source_type (int): SourceType should be a value as follows: 0: network; 1: IP Group; 2: IP-Port Group; 4: SSID;
            6: IPv6 Group; 7: IPv6-Port Group
        destination_type (int): DestinationType should be a value as follows: 0: network; 1: IP Group; 2: IP-Port Group;
            6: IPv6 Group; 7: IPv6-Port Group
        binding_type (int): BindingType should be a value as follows: 0: all ports; 1: custom ports; 2: all switch vlan;
            3: custom switch vlan
        ether_type (SwitchACLEtherTypeEntity): Ethertype(4-hex number; 0-9，A-F) is only editable when the Source Type
            and Destination Type are both selected as MAC Group in the Rule.
        custom_acl_ports (list[SwitchACLPortEntity] | Unset): Only for bindingType is custom ports, select the custom
            port or LAG of the device
        network_id (str | Unset): Only for bindingType VLAN
        binding_bridge_vlan (int | Unset): Only for bindingType VLAN and network of bridge VLAN
        custom_acl_osws (list[str] | Unset): Only for bindingType is custom switch vlan, list of selected switch mac
        custom_acl_stacks (list[str] | Unset): Only for bindingType is custom switch vlan, list of selected stack id
        custom_acl_devices (list[CustomAclOswOpenApiVO] | Unset): Only for bindingType is custom switch vlan, list of
            selected device
        time_range_id (str | Unset): Time range profile ID
    """

    id: str
    index: int
    description: str
    status: bool
    policy: int
    protocols: list[int]
    source_ids: list[str]
    destination_ids: list[str]
    source_type: int
    destination_type: int
    binding_type: int
    ether_type: SwitchACLEtherTypeEntity
    custom_acl_ports: list[SwitchACLPortEntity] | Unset = UNSET
    network_id: str | Unset = UNSET
    binding_bridge_vlan: int | Unset = UNSET
    custom_acl_osws: list[str] | Unset = UNSET
    custom_acl_stacks: list[str] | Unset = UNSET
    custom_acl_devices: list[CustomAclOswOpenApiVO] | Unset = UNSET
    time_range_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        index = self.index

        description = self.description

        status = self.status

        policy = self.policy

        protocols = self.protocols

        source_ids = self.source_ids

        destination_ids = self.destination_ids

        source_type = self.source_type

        destination_type = self.destination_type

        binding_type = self.binding_type

        ether_type = self.ether_type.to_dict()

        custom_acl_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_acl_ports, Unset):
            custom_acl_ports = []
            for custom_acl_ports_item_data in self.custom_acl_ports:
                custom_acl_ports_item = custom_acl_ports_item_data.to_dict()
                custom_acl_ports.append(custom_acl_ports_item)

        network_id = self.network_id

        binding_bridge_vlan = self.binding_bridge_vlan

        custom_acl_osws: list[str] | Unset = UNSET
        if not isinstance(self.custom_acl_osws, Unset):
            custom_acl_osws = self.custom_acl_osws

        custom_acl_stacks: list[str] | Unset = UNSET
        if not isinstance(self.custom_acl_stacks, Unset):
            custom_acl_stacks = self.custom_acl_stacks

        custom_acl_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_acl_devices, Unset):
            custom_acl_devices = []
            for custom_acl_devices_item_data in self.custom_acl_devices:
                custom_acl_devices_item = custom_acl_devices_item_data.to_dict()
                custom_acl_devices.append(custom_acl_devices_item)

        time_range_id = self.time_range_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "index": index,
                "description": description,
                "status": status,
                "policy": policy,
                "protocols": protocols,
                "sourceIds": source_ids,
                "destinationIds": destination_ids,
                "sourceType": source_type,
                "destinationType": destination_type,
                "bindingType": binding_type,
                "etherType": ether_type,
            }
        )
        if custom_acl_ports is not UNSET:
            field_dict["customAclPorts"] = custom_acl_ports
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if binding_bridge_vlan is not UNSET:
            field_dict["bindingBridgeVlan"] = binding_bridge_vlan
        if custom_acl_osws is not UNSET:
            field_dict["customAclOsws"] = custom_acl_osws
        if custom_acl_stacks is not UNSET:
            field_dict["customAclStacks"] = custom_acl_stacks
        if custom_acl_devices is not UNSET:
            field_dict["customAclDevices"] = custom_acl_devices
        if time_range_id is not UNSET:
            field_dict["timeRangeId"] = time_range_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_acl_osw_open_api_vo import (
            CustomAclOswOpenApiVO,
        )
        from ..models.switch_acl_ether_type_entity import (
            SwitchACLEtherTypeEntity,
        )
        from ..models.switch_acl_port_entity import SwitchACLPortEntity

        d = dict(src_dict)
        id = d.pop("id")

        index = d.pop("index")

        description = d.pop("description")

        status = d.pop("status")

        policy = d.pop("policy")

        protocols = cast(list[int], d.pop("protocols"))

        source_ids = cast(list[str], d.pop("sourceIds"))

        destination_ids = cast(list[str], d.pop("destinationIds"))

        source_type = d.pop("sourceType")

        destination_type = d.pop("destinationType")

        binding_type = d.pop("bindingType")

        ether_type = SwitchACLEtherTypeEntity.from_dict(d.pop("etherType"))

        _custom_acl_ports = d.pop("customAclPorts", UNSET)
        custom_acl_ports: list[SwitchACLPortEntity] | Unset = UNSET
        if _custom_acl_ports is not UNSET:
            custom_acl_ports = []
            for custom_acl_ports_item_data in _custom_acl_ports:
                custom_acl_ports_item = SwitchACLPortEntity.from_dict(
                    custom_acl_ports_item_data
                )

                custom_acl_ports.append(custom_acl_ports_item)

        network_id = d.pop("networkId", UNSET)

        binding_bridge_vlan = d.pop("bindingBridgeVlan", UNSET)

        custom_acl_osws = cast(list[str], d.pop("customAclOsws", UNSET))

        custom_acl_stacks = cast(list[str], d.pop("customAclStacks", UNSET))

        _custom_acl_devices = d.pop("customAclDevices", UNSET)
        custom_acl_devices: list[CustomAclOswOpenApiVO] | Unset = UNSET
        if _custom_acl_devices is not UNSET:
            custom_acl_devices = []
            for custom_acl_devices_item_data in _custom_acl_devices:
                custom_acl_devices_item = CustomAclOswOpenApiVO.from_dict(
                    custom_acl_devices_item_data
                )

                custom_acl_devices.append(custom_acl_devices_item)

        time_range_id = d.pop("timeRangeId", UNSET)

        switch_acl_info = cls(
            id=id,
            index=index,
            description=description,
            status=status,
            policy=policy,
            protocols=protocols,
            source_ids=source_ids,
            destination_ids=destination_ids,
            source_type=source_type,
            destination_type=destination_type,
            binding_type=binding_type,
            ether_type=ether_type,
            custom_acl_ports=custom_acl_ports,
            network_id=network_id,
            binding_bridge_vlan=binding_bridge_vlan,
            custom_acl_osws=custom_acl_osws,
            custom_acl_stacks=custom_acl_stacks,
            custom_acl_devices=custom_acl_devices,
            time_range_id=time_range_id,
        )

        switch_acl_info.additional_properties = d
        return switch_acl_info

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
