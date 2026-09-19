from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.drag_sort_index_template_openapi_vo_indexes import (
        DragSortIndexTemplateOpenapiVOIndexes,
    )


T = TypeVar("T", bound="DragSortIndexTemplateOpenapiVO")


@_attrs_define
class DragSortIndexTemplateOpenapiVO:
    """DragSort index entity template

    Attributes:
        type_ (str): "gateway" or "eap"
        indexes (DragSortIndexTemplateOpenapiVOIndexes): The order in which items take effect, this object is a Map, the
            key is item ID and the value is the index you want to set.
    """

    type_: str
    indexes: DragSortIndexTemplateOpenapiVOIndexes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        indexes = self.indexes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "indexes": indexes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.drag_sort_index_template_openapi_vo_indexes import (
            DragSortIndexTemplateOpenapiVOIndexes,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        indexes = DragSortIndexTemplateOpenapiVOIndexes.from_dict(d.pop("indexes"))

        drag_sort_index_template_openapi_vo = cls(
            type_=type_,
            indexes=indexes,
        )

        drag_sort_index_template_openapi_vo.additional_properties = d
        return drag_sort_index_template_openapi_vo

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
