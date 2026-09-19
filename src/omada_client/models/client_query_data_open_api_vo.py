from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_query_data_open_api_vo_sorts import (
        ClientQueryDataOpenApiVOSorts,
    )
    from ..models.client_query_filters_open_api_vo import ClientQueryFiltersOpenApiVO


T = TypeVar("T", bound="ClientQueryDataOpenApiVO")


@_attrs_define
class ClientQueryDataOpenApiVO:
    """
    Attributes:
        page (int): Start from 1.
        page_size (int): It should be within the range of 1–1000.
        sorts (ClientQueryDataOpenApiVOSorts | Unset): Sort rule, key: sort field, value: sort direction, value
            parameter may be one of asc or desc.Optional parameter.
        search_key (str | Unset): Fuzzy query parameters, support field name, mac, ip.
        filters (ClientQueryFiltersOpenApiVO | Unset): Filters of the query.
        scope (int | Unset): Scope of clients to query, 0: all, 1: online(default), 2:offline, 3:blocked.
    """

    page: int
    page_size: int
    sorts: ClientQueryDataOpenApiVOSorts | Unset = UNSET
    search_key: str | Unset = UNSET
    filters: ClientQueryFiltersOpenApiVO | Unset = UNSET
    scope: int | Unset = UNSET
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

        scope = self.scope

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
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_query_data_open_api_vo_sorts import (
            ClientQueryDataOpenApiVOSorts,
        )
        from ..models.client_query_filters_open_api_vo import (
            ClientQueryFiltersOpenApiVO,
        )

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("pageSize")

        _sorts = d.pop("sorts", UNSET)
        sorts: ClientQueryDataOpenApiVOSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = ClientQueryDataOpenApiVOSorts.from_dict(_sorts)

        search_key = d.pop("searchKey", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: ClientQueryFiltersOpenApiVO | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ClientQueryFiltersOpenApiVO.from_dict(_filters)

        scope = d.pop("scope", UNSET)

        client_query_data_open_api_vo = cls(
            page=page,
            page_size=page_size,
            sorts=sorts,
            search_key=search_key,
            filters=filters,
            scope=scope,
        )

        client_query_data_open_api_vo.additional_properties = d
        return client_query_data_open_api_vo

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
