from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="PolicyRoutingDragSortIndexOpenApiVOIndexes")


@_attrs_define
class PolicyRoutingDragSortIndexOpenApiVOIndexes:
    """The order in which items take effect, this object is a Map, the key is item ID and the value is the index you want
    to set.

    """

    additional_properties: dict[str, int] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        policy_routing_drag_sort_index_open_api_vo_indexes = cls()

        policy_routing_drag_sort_index_open_api_vo_indexes.additional_properties = d
        return policy_routing_drag_sort_index_open_api_vo_indexes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> int:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
