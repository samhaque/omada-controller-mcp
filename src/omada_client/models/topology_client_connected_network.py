from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyClientConnectedNetwork")


@_attrs_define
class TopologyClientConnectedNetwork:
    """Network that client connected.

    Attributes:
        network_id (str | Unset): Network ID.
        name (str | Unset): Network name.
        vlan_id (int | Unset): Vlan Id, for vlan or single vlan interface, ranges from 1 to 4090.
        vlan_ids (list[int] | Unset): Vlan Ids, for multiple vlan interface, for network .
    """

    network_id: str | Unset = UNSET
    name: str | Unset = UNSET
    vlan_id: int | Unset = UNSET
    vlan_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        name = self.name

        vlan_id = self.vlan_id

        vlan_ids: list[int] | Unset = UNSET
        if not isinstance(self.vlan_ids, Unset):
            vlan_ids = self.vlan_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if name is not UNSET:
            field_dict["name"] = name
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if vlan_ids is not UNSET:
            field_dict["vlanIds"] = vlan_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_id = d.pop("networkId", UNSET)

        name = d.pop("name", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vlan_ids = cast(list[int], d.pop("vlanIds", UNSET))

        topology_client_connected_network = cls(
            network_id=network_id,
            name=name,
            vlan_id=vlan_id,
            vlan_ids=vlan_ids,
        )

        topology_client_connected_network.additional_properties = d
        return topology_client_connected_network

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
