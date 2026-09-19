from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.topology_open_api_edge_vo import TopologyOpenApiEdgeVO


T = TypeVar("T", bound="TopologyOpenApiStatusVOStpLoops")


@_attrs_define
class TopologyOpenApiStatusVOStpLoops:
    """Stp Loops"""

    additional_properties: dict[str, list[TopologyOpenApiEdgeVO]] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:
                additional_property_item = additional_property_item_data.to_dict()
                field_dict[prop_name].append(additional_property_item)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_open_api_edge_vo import (
            TopologyOpenApiEdgeVO,
        )

        d = dict(src_dict)
        topology_open_api_status_vo_stp_loops = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:
                additional_property_item = TopologyOpenApiEdgeVO.from_dict(
                    additional_property_item_data
                )

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        topology_open_api_status_vo_stp_loops.additional_properties = (
            additional_properties
        )
        return topology_open_api_status_vo_stp_loops

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[TopologyOpenApiEdgeVO]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[TopologyOpenApiEdgeVO]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
