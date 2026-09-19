from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_open_api_edge_vo import TopologyOpenApiEdgeVO
    from ..models.topology_open_api_node_vo import TopologyOpenApiNodeVO


T = TypeVar("T", bound="TopologyOpenApiVO")


@_attrs_define
class TopologyOpenApiVO:
    """
    Attributes:
        site_id (str | Unset): Site ID
        topology_nodes (list[TopologyOpenApiNodeVO] | Unset): Topology Nodes
        topology_edges (list[TopologyOpenApiEdgeVO] | Unset): Topology Edges
        last_update_time (int | Unset): Last Update Time
    """

    site_id: str | Unset = UNSET
    topology_nodes: list[TopologyOpenApiNodeVO] | Unset = UNSET
    topology_edges: list[TopologyOpenApiEdgeVO] | Unset = UNSET
    last_update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        topology_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topology_nodes, Unset):
            topology_nodes = []
            for topology_nodes_item_data in self.topology_nodes:
                topology_nodes_item = topology_nodes_item_data.to_dict()
                topology_nodes.append(topology_nodes_item)

        topology_edges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topology_edges, Unset):
            topology_edges = []
            for topology_edges_item_data in self.topology_edges:
                topology_edges_item = topology_edges_item_data.to_dict()
                topology_edges.append(topology_edges_item)

        last_update_time = self.last_update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if topology_nodes is not UNSET:
            field_dict["topologyNodes"] = topology_nodes
        if topology_edges is not UNSET:
            field_dict["topologyEdges"] = topology_edges
        if last_update_time is not UNSET:
            field_dict["lastUpdateTime"] = last_update_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_open_api_edge_vo import (
            TopologyOpenApiEdgeVO,
        )
        from ..models.topology_open_api_node_vo import (
            TopologyOpenApiNodeVO,
        )

        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        _topology_nodes = d.pop("topologyNodes", UNSET)
        topology_nodes: list[TopologyOpenApiNodeVO] | Unset = UNSET
        if _topology_nodes is not UNSET:
            topology_nodes = []
            for topology_nodes_item_data in _topology_nodes:
                topology_nodes_item = TopologyOpenApiNodeVO.from_dict(
                    topology_nodes_item_data
                )

                topology_nodes.append(topology_nodes_item)

        _topology_edges = d.pop("topologyEdges", UNSET)
        topology_edges: list[TopologyOpenApiEdgeVO] | Unset = UNSET
        if _topology_edges is not UNSET:
            topology_edges = []
            for topology_edges_item_data in _topology_edges:
                topology_edges_item = TopologyOpenApiEdgeVO.from_dict(
                    topology_edges_item_data
                )

                topology_edges.append(topology_edges_item)

        last_update_time = d.pop("lastUpdateTime", UNSET)

        topology_open_api_vo = cls(
            site_id=site_id,
            topology_nodes=topology_nodes,
            topology_edges=topology_edges,
            last_update_time=last_update_time,
        )

        topology_open_api_vo.additional_properties = d
        return topology_open_api_vo

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
