from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_brief import LanNetworkBrief
    from ..models.osg_port_stat_brief import OsgPortStatBrief


T = TypeVar("T", bound="SdWanCandidateDevice")


@_attrs_define
class SdWanCandidateDevice:
    """
    Attributes:
        device_name (str | Unset): The name of a SD-WAN candidate device.
        device_mac (str | Unset): The MAC of a SD-WAN candidate device.
        show_model (str | Unset): The showModel of a SD-WAN candidate device.
        type_ (str | Unset): The device type of a SD-WAN candidate device.
        model (str | Unset): The model of a SD-WAN candidate device.
        model_version (str | Unset): The model version of a SD-WAN candidate device.
        site_id (str | Unset): The ID of the site where the a SD-WAN candidate device located.
        site_name (str | Unset): The name of the site where the a SD-WAN candidate device located.
        wan_ip (str | Unset): The wan IP of the a SD-WAN candidate device.
        tunnel_limit (int | Unset): The maximum number of VPN tunnels that can be created.
        capacity_level (int | Unset): The capacity level of a SD-WAN candidate device.
        has_public_ip (bool | Unset): Whether the a SD-WAN candidate has public IP.
        status (int | Unset): The online status of the candidate.
        lan_networks (list[LanNetworkBrief] | Unset): A list of the lan network info for the candidate.
        port_infos (list[OsgPortStatBrief] | Unset): A list of the port info for the candidate.
        support_sd_wan_nat (bool | Unset): Whether the device support SD-WAN NAT.
    """

    device_name: str | Unset = UNSET
    device_mac: str | Unset = UNSET
    show_model: str | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    site_id: str | Unset = UNSET
    site_name: str | Unset = UNSET
    wan_ip: str | Unset = UNSET
    tunnel_limit: int | Unset = UNSET
    capacity_level: int | Unset = UNSET
    has_public_ip: bool | Unset = UNSET
    status: int | Unset = UNSET
    lan_networks: list[LanNetworkBrief] | Unset = UNSET
    port_infos: list[OsgPortStatBrief] | Unset = UNSET
    support_sd_wan_nat: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        device_mac = self.device_mac

        show_model = self.show_model

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        site_id = self.site_id

        site_name = self.site_name

        wan_ip = self.wan_ip

        tunnel_limit = self.tunnel_limit

        capacity_level = self.capacity_level

        has_public_ip = self.has_public_ip

        status = self.status

        lan_networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_networks, Unset):
            lan_networks = []
            for lan_networks_item_data in self.lan_networks:
                lan_networks_item = lan_networks_item_data.to_dict()
                lan_networks.append(lan_networks_item)

        port_infos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_infos, Unset):
            port_infos = []
            for port_infos_item_data in self.port_infos:
                port_infos_item = port_infos_item_data.to_dict()
                port_infos.append(port_infos_item)

        support_sd_wan_nat = self.support_sd_wan_nat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if wan_ip is not UNSET:
            field_dict["wanIp"] = wan_ip
        if tunnel_limit is not UNSET:
            field_dict["tunnelLimit"] = tunnel_limit
        if capacity_level is not UNSET:
            field_dict["capacityLevel"] = capacity_level
        if has_public_ip is not UNSET:
            field_dict["hasPublicIp"] = has_public_ip
        if status is not UNSET:
            field_dict["status"] = status
        if lan_networks is not UNSET:
            field_dict["lanNetworks"] = lan_networks
        if port_infos is not UNSET:
            field_dict["portInfos"] = port_infos
        if support_sd_wan_nat is not UNSET:
            field_dict["supportSdWanNat"] = support_sd_wan_nat

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_brief import LanNetworkBrief
        from ..models.osg_port_stat_brief import OsgPortStatBrief

        d = dict(src_dict)
        device_name = d.pop("deviceName", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        show_model = d.pop("showModel", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        wan_ip = d.pop("wanIp", UNSET)

        tunnel_limit = d.pop("tunnelLimit", UNSET)

        capacity_level = d.pop("capacityLevel", UNSET)

        has_public_ip = d.pop("hasPublicIp", UNSET)

        status = d.pop("status", UNSET)

        _lan_networks = d.pop("lanNetworks", UNSET)
        lan_networks: list[LanNetworkBrief] | Unset = UNSET
        if _lan_networks is not UNSET:
            lan_networks = []
            for lan_networks_item_data in _lan_networks:
                lan_networks_item = LanNetworkBrief.from_dict(lan_networks_item_data)

                lan_networks.append(lan_networks_item)

        _port_infos = d.pop("portInfos", UNSET)
        port_infos: list[OsgPortStatBrief] | Unset = UNSET
        if _port_infos is not UNSET:
            port_infos = []
            for port_infos_item_data in _port_infos:
                port_infos_item = OsgPortStatBrief.from_dict(port_infos_item_data)

                port_infos.append(port_infos_item)

        support_sd_wan_nat = d.pop("supportSdWanNat", UNSET)

        sd_wan_candidate_device = cls(
            device_name=device_name,
            device_mac=device_mac,
            show_model=show_model,
            type_=type_,
            model=model,
            model_version=model_version,
            site_id=site_id,
            site_name=site_name,
            wan_ip=wan_ip,
            tunnel_limit=tunnel_limit,
            capacity_level=capacity_level,
            has_public_ip=has_public_ip,
            status=status,
            lan_networks=lan_networks,
            port_infos=port_infos,
            support_sd_wan_nat=support_sd_wan_nat,
        )

        sd_wan_candidate_device.additional_properties = d
        return sd_wan_candidate_device

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
