from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_client_node import TopologyClientNode


T = TypeVar("T", bound="TopologyDeviceClients")


@_attrs_define
class TopologyDeviceClients:
    """Clients In Device.

    Attributes:
        client_group (list[TopologyClientNode] | Unset): Client Group.
        dev_mac (str | Unset): Device Mac.
    """

    client_group: list[TopologyClientNode] | Unset = UNSET
    dev_mac: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_group: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_group, Unset):
            client_group = []
            for client_group_item_data in self.client_group:
                client_group_item = client_group_item_data.to_dict()
                client_group.append(client_group_item)

        dev_mac = self.dev_mac

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_group is not UNSET:
            field_dict["clientGroup"] = client_group
        if dev_mac is not UNSET:
            field_dict["devMac"] = dev_mac

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_client_node import TopologyClientNode

        d = dict(src_dict)
        _client_group = d.pop("clientGroup", UNSET)
        client_group: list[TopologyClientNode] | Unset = UNSET
        if _client_group is not UNSET:
            client_group = []
            for client_group_item_data in _client_group:
                client_group_item = TopologyClientNode.from_dict(client_group_item_data)

                client_group.append(client_group_item)

        dev_mac = d.pop("devMac", UNSET)

        topology_device_clients = cls(
            client_group=client_group,
            dev_mac=dev_mac,
        )

        topology_device_clients.additional_properties = d
        return topology_device_clients

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
