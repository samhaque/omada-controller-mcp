from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_osw_date_by_network_vo_filters import (
        QueryOswDateByNetworkVOFilters,
    )
    from ..models.query_osw_date_by_network_vo_multi_search_map import (
        QueryOswDateByNetworkVOMultiSearchMap,
    )
    from ..models.query_osw_date_by_network_vo_sorts import QueryOswDateByNetworkVOSorts


T = TypeVar("T", bound="QueryOswDateByNetworkVO")


@_attrs_define
class QueryOswDateByNetworkVO:
    """
    Attributes:
        current_page (int | Unset):
        current_page_size (int | Unset):
        sorts (QueryOswDateByNetworkVOSorts | Unset):
        search_key (str | Unset):
        filters (QueryOswDateByNetworkVOFilters | Unset):
        search_field (str | Unset):
        multi_search_map (QueryOswDateByNetworkVOMultiSearchMap | Unset):
        async_columns (str | Unset):
        lan_network_ids (list[str] | Unset):
    """

    current_page: int | Unset = UNSET
    current_page_size: int | Unset = UNSET
    sorts: QueryOswDateByNetworkVOSorts | Unset = UNSET
    search_key: str | Unset = UNSET
    filters: QueryOswDateByNetworkVOFilters | Unset = UNSET
    search_field: str | Unset = UNSET
    multi_search_map: QueryOswDateByNetworkVOMultiSearchMap | Unset = UNSET
    async_columns: str | Unset = UNSET
    lan_network_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        current_page_size = self.current_page_size

        sorts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = self.sorts.to_dict()

        search_key = self.search_key

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        search_field = self.search_field

        multi_search_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.multi_search_map, Unset):
            multi_search_map = self.multi_search_map.to_dict()

        async_columns = self.async_columns

        lan_network_ids: list[str] | Unset = UNSET
        if not isinstance(self.lan_network_ids, Unset):
            lan_network_ids = self.lan_network_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_page_size is not UNSET:
            field_dict["currentPageSize"] = current_page_size
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if filters is not UNSET:
            field_dict["filters"] = filters
        if search_field is not UNSET:
            field_dict["searchField"] = search_field
        if multi_search_map is not UNSET:
            field_dict["multiSearchMap"] = multi_search_map
        if async_columns is not UNSET:
            field_dict["asyncColumns"] = async_columns
        if lan_network_ids is not UNSET:
            field_dict["lanNetworkIds"] = lan_network_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.query_osw_date_by_network_vo_filters import (
            QueryOswDateByNetworkVOFilters,
        )
        from ..models.query_osw_date_by_network_vo_multi_search_map import (
            QueryOswDateByNetworkVOMultiSearchMap,
        )
        from ..models.query_osw_date_by_network_vo_sorts import (
            QueryOswDateByNetworkVOSorts,
        )

        d = dict(src_dict)
        current_page = d.pop("currentPage", UNSET)

        current_page_size = d.pop("currentPageSize", UNSET)

        _sorts = d.pop("sorts", UNSET)
        sorts: QueryOswDateByNetworkVOSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = QueryOswDateByNetworkVOSorts.from_dict(_sorts)

        search_key = d.pop("searchKey", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: QueryOswDateByNetworkVOFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = QueryOswDateByNetworkVOFilters.from_dict(_filters)

        search_field = d.pop("searchField", UNSET)

        _multi_search_map = d.pop("multiSearchMap", UNSET)
        multi_search_map: QueryOswDateByNetworkVOMultiSearchMap | Unset
        if isinstance(_multi_search_map, Unset):
            multi_search_map = UNSET
        else:
            multi_search_map = QueryOswDateByNetworkVOMultiSearchMap.from_dict(
                _multi_search_map
            )

        async_columns = d.pop("asyncColumns", UNSET)

        lan_network_ids = cast(list[str], d.pop("lanNetworkIds", UNSET))

        query_osw_date_by_network_vo = cls(
            current_page=current_page,
            current_page_size=current_page_size,
            sorts=sorts,
            search_key=search_key,
            filters=filters,
            search_field=search_field,
            multi_search_map=multi_search_map,
            async_columns=async_columns,
            lan_network_ids=lan_network_ids,
        )

        query_osw_date_by_network_vo.additional_properties = d
        return query_osw_date_by_network_vo

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
