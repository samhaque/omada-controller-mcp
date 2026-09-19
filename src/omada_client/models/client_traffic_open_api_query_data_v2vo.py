from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_traffic_filter_open_api_vo import ClientTrafficFilterOpenApiVO
    from ..models.client_traffic_open_api_query_data_v2vo_filters import (
        ClientTrafficOpenApiQueryDataV2VOFilters,
    )
    from ..models.client_traffic_open_api_query_data_v2vo_sorts import (
        ClientTrafficOpenApiQueryDataV2VOSorts,
    )


T = TypeVar("T", bound="ClientTrafficOpenApiQueryDataV2VO")


@_attrs_define
class ClientTrafficOpenApiQueryDataV2VO:
    """
    Attributes:
        page (int): Start from 1.
        page_size (int): It should be within the range of 1–100.
        sorts (ClientTrafficOpenApiQueryDataV2VOSorts | Unset): Sort rule, key: sort field, value: sort direction, value
            parameter may be one of asc or desc.
        filters (ClientTrafficOpenApiQueryDataV2VOFilters | Unset): Filter [family] in the form of Map. When the value
            of the [family] key is empty, return an empty result.
        start (int | Unset): Start timestamp, in seconds, such as 1682000000
        end (int | Unset): End timestamp, in seconds, such as 1682000000
        client_traffic_filters (list[ClientTrafficFilterOpenApiVO] | Unset): Client traffic filtering condition
    """

    page: int
    page_size: int
    sorts: ClientTrafficOpenApiQueryDataV2VOSorts | Unset = UNSET
    filters: ClientTrafficOpenApiQueryDataV2VOFilters | Unset = UNSET
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

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

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
        if filters is not UNSET:
            field_dict["filters"] = filters
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
        from ..models.client_traffic_open_api_query_data_v2vo_filters import (
            ClientTrafficOpenApiQueryDataV2VOFilters,
        )
        from ..models.client_traffic_open_api_query_data_v2vo_sorts import (
            ClientTrafficOpenApiQueryDataV2VOSorts,
        )

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("pageSize")

        _sorts = d.pop("sorts", UNSET)
        sorts: ClientTrafficOpenApiQueryDataV2VOSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = ClientTrafficOpenApiQueryDataV2VOSorts.from_dict(_sorts)

        _filters = d.pop("filters", UNSET)
        filters: ClientTrafficOpenApiQueryDataV2VOFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = ClientTrafficOpenApiQueryDataV2VOFilters.from_dict(_filters)

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

        client_traffic_open_api_query_data_v2vo = cls(
            page=page,
            page_size=page_size,
            sorts=sorts,
            filters=filters,
            start=start,
            end=end,
            client_traffic_filters=client_traffic_filters,
        )

        client_traffic_open_api_query_data_v2vo.additional_properties = d
        return client_traffic_open_api_query_data_v2vo

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
