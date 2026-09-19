from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_open_api_health_status_vo import (
        TopologyOpenApiHealthStatusVO,
    )
    from ..models.topology_open_api_status_vo import TopologyOpenApiStatusVO
    from ..models.topology_v3_open_api_node_vo import TopologyV3OpenApiNodeVO


T = TypeVar("T", bound="TopologyV3OpenApiVO")


@_attrs_define
class TopologyV3OpenApiVO:
    """
    Attributes:
        topology_array (list[TopologyV3OpenApiNodeVO] | Unset): Topology Nodes
        status (TopologyOpenApiStatusVO | Unset): Topology Related Status
        health_stat (TopologyOpenApiHealthStatusVO | Unset): Topology Health Status
        last_update_time (int | Unset): Last Update Time
    """

    topology_array: list[TopologyV3OpenApiNodeVO] | Unset = UNSET
    status: TopologyOpenApiStatusVO | Unset = UNSET
    health_stat: TopologyOpenApiHealthStatusVO | Unset = UNSET
    last_update_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        topology_array: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topology_array, Unset):
            topology_array = []
            for topology_array_item_data in self.topology_array:
                topology_array_item = topology_array_item_data.to_dict()
                topology_array.append(topology_array_item)

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        health_stat: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health_stat, Unset):
            health_stat = self.health_stat.to_dict()

        last_update_time = self.last_update_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if topology_array is not UNSET:
            field_dict["topologyArray"] = topology_array
        if status is not UNSET:
            field_dict["status"] = status
        if health_stat is not UNSET:
            field_dict["healthStat"] = health_stat
        if last_update_time is not UNSET:
            field_dict["lastUpdateTime"] = last_update_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_open_api_health_status_vo import (
            TopologyOpenApiHealthStatusVO,
        )
        from ..models.topology_open_api_status_vo import (
            TopologyOpenApiStatusVO,
        )
        from ..models.topology_v3_open_api_node_vo import (
            TopologyV3OpenApiNodeVO,
        )

        d = dict(src_dict)
        _topology_array = d.pop("topologyArray", UNSET)
        topology_array: list[TopologyV3OpenApiNodeVO] | Unset = UNSET
        if _topology_array is not UNSET:
            topology_array = []
            for topology_array_item_data in _topology_array:
                topology_array_item = TopologyV3OpenApiNodeVO.from_dict(
                    topology_array_item_data
                )

                topology_array.append(topology_array_item)

        _status = d.pop("status", UNSET)
        status: TopologyOpenApiStatusVO | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = TopologyOpenApiStatusVO.from_dict(_status)

        _health_stat = d.pop("healthStat", UNSET)
        health_stat: TopologyOpenApiHealthStatusVO | Unset
        if isinstance(_health_stat, Unset):
            health_stat = UNSET
        else:
            health_stat = TopologyOpenApiHealthStatusVO.from_dict(_health_stat)

        last_update_time = d.pop("lastUpdateTime", UNSET)

        topology_v3_open_api_vo = cls(
            topology_array=topology_array,
            status=status,
            health_stat=health_stat,
            last_update_time=last_update_time,
        )

        topology_v3_open_api_vo.additional_properties = d
        return topology_v3_open_api_vo

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
