from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_split_wired_network import TopologySplitWiredNetwork
    from ..models.topology_ssid import TopologySSID


T = TypeVar("T", bound="TopologyAvailableNetworkAndSSID")


@_attrs_define
class TopologyAvailableNetworkAndSSID:
    """Available Network split by vlan and ssids.

    Attributes:
        split_networks (list[TopologySplitWiredNetwork] | Unset): Networks split by vlan.
        ssids (list[TopologySSID] | Unset): SSID List.
    """

    split_networks: list[TopologySplitWiredNetwork] | Unset = UNSET
    ssids: list[TopologySSID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        split_networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.split_networks, Unset):
            split_networks = []
            for split_networks_item_data in self.split_networks:
                split_networks_item = split_networks_item_data.to_dict()
                split_networks.append(split_networks_item)

        ssids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssids, Unset):
            ssids = []
            for ssids_item_data in self.ssids:
                ssids_item = ssids_item_data.to_dict()
                ssids.append(ssids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if split_networks is not UNSET:
            field_dict["splitNetworks"] = split_networks
        if ssids is not UNSET:
            field_dict["ssids"] = ssids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_split_wired_network import (
            TopologySplitWiredNetwork,
        )
        from ..models.topology_ssid import TopologySSID

        d = dict(src_dict)
        _split_networks = d.pop("splitNetworks", UNSET)
        split_networks: list[TopologySplitWiredNetwork] | Unset = UNSET
        if _split_networks is not UNSET:
            split_networks = []
            for split_networks_item_data in _split_networks:
                split_networks_item = TopologySplitWiredNetwork.from_dict(
                    split_networks_item_data
                )

                split_networks.append(split_networks_item)

        _ssids = d.pop("ssids", UNSET)
        ssids: list[TopologySSID] | Unset = UNSET
        if _ssids is not UNSET:
            ssids = []
            for ssids_item_data in _ssids:
                ssids_item = TopologySSID.from_dict(ssids_item_data)

                ssids.append(ssids_item)

        topology_available_network_and_ssid = cls(
            split_networks=split_networks,
            ssids=ssids,
        )

        topology_available_network_and_ssid.additional_properties = d
        return topology_available_network_and_ssid

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
