from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_info_vo import FeatureInfoVO


T = TypeVar("T", bound="PolicyRoutingInfo")


@_attrs_define
class PolicyRoutingInfo:
    """
    Attributes:
        name (str): Name, name should contain 1 to 64 characters.
        status (bool): Status
        protocols (list[int]): For the values of protocols, refer to section 5.5.2 of the Open API Access Guide.
        backup_interface (bool): Use another WAN port if the current one is down
        source_type (int): SourceType should be a value as follows: 0: Network; 1: IP Group; 2: IP port Group
        source_ids (list[str]): Source IDs, which depends on sourceType, for example: if sourceType is network,
            sourceIds should be LAN network ID. LAN Network can be created using 'Create LAN network' interface, and LAN
            Network ID can be obtained from 'Get LAN network list' interface.
        destination_type (int): DestinationType should be a value as follows: 0: Network; 1: IP Group; 2: IP port Group
        destination_ids (list[str]): Destination IDs, which depends on destinationType, for example: if destinationType
            is network, destinationIds should be LAN network ID. LAN Network can be created using 'Create LAN network'
            interface, and LAN Network ID can be obtained from 'Get LAN network list' interface.
        id (str | Unset): ID
        index (int | Unset): Index
        interface_type (int | Unset): InterfaceType should be a value as follows: 0: WAN; 2: L2TP; 3: PPTP; 4: multi-
            select WAN or VPN or virtual WAN.
        interface_id (str | Unset): Interface ID
        wan_port_ids (list[str] | Unset): WAN port list. When interfaceType is 4, at least one of the wanPortIds or
            vpnIds or virtualWanIds is not empty.
        vpn_ids (list[str] | Unset): VPN list. When interfaceType is 4, at least one of the wanPortIds or vpnIds or
            virtualWanIds is not empty.
        virtual_wan_ids (list[str] | Unset): Virtual WAN list. When interfaceType is 4, at least one of the wanPortIds
            or vpnIds or virtualWanIds is not empty.
        exist_vpn_client (bool | Unset): Whether the interface option exists VPN client
        exist_virtual_wan (bool | Unset): Whether the interface option exists virtual WAN
        exist_multi (bool | Unset): Whether the interface option exists multi
        exist_location_group_dest (bool | Unset): Whether the destination type exists location group
        exist_domain_group_dest (bool | Unset): Whether the destination type exists domain group
        exist_ip_port_group (bool | Unset): Whether the destination type exists ip port group
        feature_description (list[FeatureInfoVO] | Unset): Gateway Feature Description.
    """

    name: str
    status: bool
    protocols: list[int]
    backup_interface: bool
    source_type: int
    source_ids: list[str]
    destination_type: int
    destination_ids: list[str]
    id: str | Unset = UNSET
    index: int | Unset = UNSET
    interface_type: int | Unset = UNSET
    interface_id: str | Unset = UNSET
    wan_port_ids: list[str] | Unset = UNSET
    vpn_ids: list[str] | Unset = UNSET
    virtual_wan_ids: list[str] | Unset = UNSET
    exist_vpn_client: bool | Unset = UNSET
    exist_virtual_wan: bool | Unset = UNSET
    exist_multi: bool | Unset = UNSET
    exist_location_group_dest: bool | Unset = UNSET
    exist_domain_group_dest: bool | Unset = UNSET
    exist_ip_port_group: bool | Unset = UNSET
    feature_description: list[FeatureInfoVO] | Unset = UNSET
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

        id = self.id

        index = self.index

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

        exist_vpn_client = self.exist_vpn_client

        exist_virtual_wan = self.exist_virtual_wan

        exist_multi = self.exist_multi

        exist_location_group_dest = self.exist_location_group_dest

        exist_domain_group_dest = self.exist_domain_group_dest

        exist_ip_port_group = self.exist_ip_port_group

        feature_description: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.feature_description, Unset):
            feature_description = []
            for feature_description_item_data in self.feature_description:
                feature_description_item = feature_description_item_data.to_dict()
                feature_description.append(feature_description_item)

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
        if id is not UNSET:
            field_dict["id"] = id
        if index is not UNSET:
            field_dict["index"] = index
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
        if exist_vpn_client is not UNSET:
            field_dict["existVpnClient"] = exist_vpn_client
        if exist_virtual_wan is not UNSET:
            field_dict["existVirtualWan"] = exist_virtual_wan
        if exist_multi is not UNSET:
            field_dict["existMulti"] = exist_multi
        if exist_location_group_dest is not UNSET:
            field_dict["existLocationGroupDest"] = exist_location_group_dest
        if exist_domain_group_dest is not UNSET:
            field_dict["existDomainGroupDest"] = exist_domain_group_dest
        if exist_ip_port_group is not UNSET:
            field_dict["existIpPortGroup"] = exist_ip_port_group
        if feature_description is not UNSET:
            field_dict["featureDescription"] = feature_description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.feature_info_vo import FeatureInfoVO

        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        protocols = cast(list[int], d.pop("protocols"))

        backup_interface = d.pop("backupInterface")

        source_type = d.pop("sourceType")

        source_ids = cast(list[str], d.pop("sourceIds"))

        destination_type = d.pop("destinationType")

        destination_ids = cast(list[str], d.pop("destinationIds"))

        id = d.pop("id", UNSET)

        index = d.pop("index", UNSET)

        interface_type = d.pop("interfaceType", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        wan_port_ids = cast(list[str], d.pop("wanPortIds", UNSET))

        vpn_ids = cast(list[str], d.pop("vpnIds", UNSET))

        virtual_wan_ids = cast(list[str], d.pop("virtualWanIds", UNSET))

        exist_vpn_client = d.pop("existVpnClient", UNSET)

        exist_virtual_wan = d.pop("existVirtualWan", UNSET)

        exist_multi = d.pop("existMulti", UNSET)

        exist_location_group_dest = d.pop("existLocationGroupDest", UNSET)

        exist_domain_group_dest = d.pop("existDomainGroupDest", UNSET)

        exist_ip_port_group = d.pop("existIpPortGroup", UNSET)

        _feature_description = d.pop("featureDescription", UNSET)
        feature_description: list[FeatureInfoVO] | Unset = UNSET
        if _feature_description is not UNSET:
            feature_description = []
            for feature_description_item_data in _feature_description:
                feature_description_item = FeatureInfoVO.from_dict(
                    feature_description_item_data
                )

                feature_description.append(feature_description_item)

        policy_routing_info = cls(
            name=name,
            status=status,
            protocols=protocols,
            backup_interface=backup_interface,
            source_type=source_type,
            source_ids=source_ids,
            destination_type=destination_type,
            destination_ids=destination_ids,
            id=id,
            index=index,
            interface_type=interface_type,
            interface_id=interface_id,
            wan_port_ids=wan_port_ids,
            vpn_ids=vpn_ids,
            virtual_wan_ids=virtual_wan_ids,
            exist_vpn_client=exist_vpn_client,
            exist_virtual_wan=exist_virtual_wan,
            exist_multi=exist_multi,
            exist_location_group_dest=exist_location_group_dest,
            exist_domain_group_dest=exist_domain_group_dest,
            exist_ip_port_group=exist_ip_port_group,
            feature_description=feature_description,
        )

        policy_routing_info.additional_properties = d
        return policy_routing_info

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
