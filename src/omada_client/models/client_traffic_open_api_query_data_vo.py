from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_traffic_filter_open_api_vo import ClientTrafficFilterOpenApiVO
    from ..models.client_traffic_open_api_query_data_vo_filters import (
        ClientTrafficOpenApiQueryDataVOFilters,
    )
    from ..models.client_traffic_open_api_query_data_vo_sorts import (
        ClientTrafficOpenApiQueryDataVOSorts,
    )


T = TypeVar("T", bound="ClientTrafficOpenApiQueryDataVO")


@_attrs_define
class ClientTrafficOpenApiQueryDataVO:
    """
    Attributes:
        page (int): Start from 1.
        page_size (int): It should be within the range of 1–100.
        sorts (ClientTrafficOpenApiQueryDataVOSorts | Unset):
        search_key (str | Unset): Look for a specific piece of data.
        filters (ClientTrafficOpenApiQueryDataVOFilters | Unset):
        search_field (str | Unset):
        start (int | Unset): Start timestamp, in seconds, such as 1682000000
        end (int | Unset): End timestamp, in seconds, such as 1682000000
        client_traffic_filters (list[ClientTrafficFilterOpenApiVO] | Unset): Client traffic filtering condition
    """

    page: int
    page_size: int
    sorts: ClientTrafficOpenApiQueryDataVOSorts | Unset = UNSET
    search_key: str | Unset = UNSET
    filters: ClientTrafficOpenApiQueryDataVOFilters | Unset = UNSET
    search_field: str | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    client_traffic_filters: list[ClientTrafficFilterOpenApiVO] | Unset = UNSET
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

        start = self.start

        end = self.end

        client_traffic_filters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.client_traffic_filters, Unset):
            client_traffic_filters = []
            for client_traffic_filters_item_data in self.client_traffic_filters:
                client_traffic_filters_item = client_traffic_filters_item_data.to_dict()
                client_traffic_filters.append(client_traffic_filters_item)

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
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if client_traffic_filters is not UNSET:
            field_dict["clientTrafficFilters"] = client_traffic_filters

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_traffic_filter_open_api_vo import (
            ClientTrafficFilterOpenApiVO,
        )
        from ..models.client_traffic_open_api_query_data_vo_filters import (
            ClientTrafficOpenApiQueryDataVOFilters,
        )
        from ..models.client_traffic_open_api_query_data_vo_sorts import (
            ClientTrafficOpenApiQueryDataVOSorts,
        )

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("pageSize")

        _sorts = d.pop("sorts", UNSET)
        sorts: ClientTrafficOpenApiQueryDataVOSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = ClientTrafficOpenApiQueryDataVOSorts.from_dict(_sorts)

        search_key = d.pop("searchKey", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: ClientTrafficOpenApiQueryDataVOFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ClientTrafficOpenApiQueryDataVOFilters.from_dict(_filters)

        search_field = d.pop("searchField", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        _client_traffic_filters = d.pop("clientTrafficFilters", UNSET)
        client_traffic_filters: list[ClientTrafficFilterOpenApiVO] | Unset = UNSET
        if _client_traffic_filters is not UNSET:
            client_traffic_filters = []
            for client_traffic_filters_item_data in _client_traffic_filters:
                client_traffic_filters_item = ClientTrafficFilterOpenApiVO.from_dict(
                    client_traffic_filters_item_data
                )

                client_traffic_filters.append(client_traffic_filters_item)

        client_traffic_open_api_query_data_vo = cls(
            page=page,
            page_size=page_size,
            sorts=sorts,
            search_key=search_key,
            filters=filters,
            search_field=search_field,
            start=start,
            end=end,
            client_traffic_filters=client_traffic_filters,
        )

        client_traffic_open_api_query_data_vo.additional_properties = d
        return client_traffic_open_api_query_data_vo

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
