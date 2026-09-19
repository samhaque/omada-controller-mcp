from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SdWanNetworkMap")


@_attrs_define
class SdWanNetworkMap:
    """A list of the mapped network

    Attributes:
        site_id (str | Unset): The ID of the site
        site_name (str | Unset): The name of the site
        device_name (str | Unset): The name of the device
        lan_network_id (str | Unset): The ID of the original network before mapping
        gateway_subnet (str | Unset): The IP range of the original network before mapping
        mapped_network (str | Unset): mapped network
        network_type (int | Unset): Network type, 0/null: LAN network, 1: custom route
    """

    site_id: str | Unset = UNSET
    site_name: str | Unset = UNSET
    device_name: str | Unset = UNSET
    lan_network_id: str | Unset = UNSET
    gateway_subnet: str | Unset = UNSET
    mapped_network: str | Unset = UNSET
    network_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        site_name = self.site_name

        device_name = self.device_name

        lan_network_id = self.lan_network_id

        gateway_subnet = self.gateway_subnet

        mapped_network = self.mapped_network

        network_type = self.network_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if lan_network_id is not UNSET:
            field_dict["lanNetworkId"] = lan_network_id
        if gateway_subnet is not UNSET:
            field_dict["gatewaySubnet"] = gateway_subnet
        if mapped_network is not UNSET:
            field_dict["mappedNetwork"] = mapped_network
        if network_type is not UNSET:
            field_dict["networkType"] = network_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        device_name = d.pop("deviceName", UNSET)

        lan_network_id = d.pop("lanNetworkId", UNSET)

        gateway_subnet = d.pop("gatewaySubnet", UNSET)

        mapped_network = d.pop("mappedNetwork", UNSET)

        network_type = d.pop("networkType", UNSET)

        sd_wan_network_map = cls(
            site_id=site_id,
            site_name=site_name,
            device_name=device_name,
            lan_network_id=lan_network_id,
            gateway_subnet=gateway_subnet,
            mapped_network=mapped_network,
            network_type=network_type,
        )

        sd_wan_network_map.additional_properties = d
        return sd_wan_network_map

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
