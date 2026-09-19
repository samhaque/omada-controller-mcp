from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SdWanNatItemConfig")


@_attrs_define
class SdWanNatItemConfig:
    """A list of the network map item

    Attributes:
        site_id (str): The ID of the site
        gateway_subnet (str): The IP range of the original network before mapping
        lan_network_id (str | Unset): The ID of the original network before mapping
        mapped_network (str | Unset): mapped network
        network_type (int | Unset): Network type, 0/null: LAN network, 1: custom route
    """

    site_id: str
    gateway_subnet: str
    lan_network_id: str | Unset = UNSET
    mapped_network: str | Unset = UNSET
    network_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        gateway_subnet = self.gateway_subnet

        lan_network_id = self.lan_network_id

        mapped_network = self.mapped_network

        network_type = self.network_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteId": site_id,
                "gatewaySubnet": gateway_subnet,
            }
        )
        if lan_network_id is not UNSET:
            field_dict["lanNetworkId"] = lan_network_id
        if mapped_network is not UNSET:
            field_dict["mappedNetwork"] = mapped_network
        if network_type is not UNSET:
            field_dict["networkType"] = network_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_id = d.pop("siteId")

        gateway_subnet = d.pop("gatewaySubnet")

        lan_network_id = d.pop("lanNetworkId", UNSET)

        mapped_network = d.pop("mappedNetwork", UNSET)

        network_type = d.pop("networkType", UNSET)

        sd_wan_nat_item_config = cls(
            site_id=site_id,
            gateway_subnet=gateway_subnet,
            lan_network_id=lan_network_id,
            mapped_network=mapped_network,
            network_type=network_type,
        )

        sd_wan_nat_item_config.additional_properties = d
        return sd_wan_nat_item_config

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
