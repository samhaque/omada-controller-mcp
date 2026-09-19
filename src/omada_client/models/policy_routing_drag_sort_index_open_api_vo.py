from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.policy_routing_drag_sort_index_open_api_vo_indexes import (
        PolicyRoutingDragSortIndexOpenApiVOIndexes,
    )


T = TypeVar("T", bound="PolicyRoutingDragSortIndexOpenApiVO")


@_attrs_define
class PolicyRoutingDragSortIndexOpenApiVO:
    """
    Attributes:
        indexes (PolicyRoutingDragSortIndexOpenApiVOIndexes): The order in which items take effect, this object is a
            Map, the key is item ID and the value is the index you want to set.
    """

    indexes: PolicyRoutingDragSortIndexOpenApiVOIndexes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indexes = self.indexes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "indexes": indexes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.policy_routing_drag_sort_index_open_api_vo_indexes import (
            PolicyRoutingDragSortIndexOpenApiVOIndexes,
        )

        d = dict(src_dict)
        indexes = PolicyRoutingDragSortIndexOpenApiVOIndexes.from_dict(d.pop("indexes"))

        policy_routing_drag_sort_index_open_api_vo = cls(
            indexes=indexes,
        )

        policy_routing_drag_sort_index_open_api_vo.additional_properties = d
        return policy_routing_drag_sort_index_open_api_vo

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
