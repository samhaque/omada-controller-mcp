from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_node_info import ClientNodeInfo
    from ..models.device_node_info import DeviceNodeInfo


T = TypeVar("T", bound="ClientTopologyNodesInfo")


@_attrs_define
class ClientTopologyNodesInfo:
    """
    Attributes:
        node_type (int | Unset): Node type, 0: device; 1: client.
        client_node (ClientNodeInfo | Unset): Client node info.
        device_node (DeviceNodeInfo | Unset): Device Node info.
        client (bool | Unset):
    """

    node_type: int | Unset = UNSET
    client_node: ClientNodeInfo | Unset = UNSET
    device_node: DeviceNodeInfo | Unset = UNSET
    client: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_type = self.node_type

        client_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_node, Unset):
            client_node = self.client_node.to_dict()

        device_node: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_node, Unset):
            device_node = self.device_node.to_dict()

        client = self.client

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_type is not UNSET:
            field_dict["nodeType"] = node_type
        if client_node is not UNSET:
            field_dict["clientNode"] = client_node
        if device_node is not UNSET:
            field_dict["deviceNode"] = device_node
        if client is not UNSET:
            field_dict["client"] = client

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_node_info import ClientNodeInfo
        from ..models.device_node_info import DeviceNodeInfo

        d = dict(src_dict)
        node_type = d.pop("nodeType", UNSET)

        _client_node = d.pop("clientNode", UNSET)
        client_node: ClientNodeInfo | Unset
        if isinstance(_client_node, Unset):
            client_node = UNSET
        else:
            client_node = ClientNodeInfo.from_dict(_client_node)

        _device_node = d.pop("deviceNode", UNSET)
        device_node: DeviceNodeInfo | Unset
        if isinstance(_device_node, Unset):
            device_node = UNSET
        else:
            device_node = DeviceNodeInfo.from_dict(_device_node)

        client = d.pop("client", UNSET)

        client_topology_nodes_info = cls(
            node_type=node_type,
            client_node=client_node,
            device_node=device_node,
            client=client,
        )

        client_topology_nodes_info.additional_properties = d
        return client_topology_nodes_info

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
