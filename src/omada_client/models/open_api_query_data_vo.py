from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_api_query_data_vo_filters import OpenApiQueryDataVOFilters
    from ..models.open_api_query_data_vo_sorts import OpenApiQueryDataVOSorts


T = TypeVar("T", bound="OpenApiQueryDataVO")


@_attrs_define
class OpenApiQueryDataVO:
    """
    Attributes:
        page (int): Start from 1.
        page_size (int): It should be within the range of 1–1000.
        sorts (OpenApiQueryDataVOSorts | Unset):
        search_key (str | Unset): Look for a specific piece of data.
        filters (OpenApiQueryDataVOFilters | Unset):
        search_field (str | Unset):
    """

    page: int
    page_size: int
    sorts: OpenApiQueryDataVOSorts | Unset = UNSET
    search_key: str | Unset = UNSET
    filters: OpenApiQueryDataVOFilters | Unset = UNSET
    search_field: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        sorts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = self.sorts.to_dict()

        search_key = self.search_key

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        search_field = self.search_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pageSize": page_size,
            }
        )
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if filters is not UNSET:
            field_dict["filters"] = filters
        if search_field is not UNSET:
            field_dict["searchField"] = search_field

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.open_api_query_data_vo_filters import (
            OpenApiQueryDataVOFilters,
        )
        from ..models.open_api_query_data_vo_sorts import (
            OpenApiQueryDataVOSorts,
        )

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("pageSize")

        _sorts = d.pop("sorts", UNSET)
        sorts: OpenApiQueryDataVOSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = OpenApiQueryDataVOSorts.from_dict(_sorts)

        search_key = d.pop("searchKey", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: OpenApiQueryDataVOFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = OpenApiQueryDataVOFilters.from_dict(_filters)

        search_field = d.pop("searchField", UNSET)

        open_api_query_data_vo = cls(
            page=page,
            page_size=page_size,
            sorts=sorts,
            search_key=search_key,
            filters=filters,
            search_field=search_field,
        )

        open_api_query_data_vo.additional_properties = d
        return open_api_query_data_vo

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
