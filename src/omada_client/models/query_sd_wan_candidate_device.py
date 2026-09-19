from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_sd_wan_candidate_device_filters import (
        QuerySdWanCandidateDeviceFilters,
    )
    from ..models.query_sd_wan_candidate_device_sorts import (
        QuerySdWanCandidateDeviceSorts,
    )


T = TypeVar("T", bound="QuerySdWanCandidateDevice")


@_attrs_define
class QuerySdWanCandidateDevice:
    """
    Attributes:
        page (int): Start from 1.
        page_size (int): It should be within the range of 1–1000.
        tunnel_limit (int): The maximum number of VPN tunnels that can be created. Used to filter devices that meet the
            minimum supported tunnel count. Only those that support a tunnel count greater than the minimum will be listed.
        role (int): The role in SD-WAN Group. 0:Hub,1:Spoke
        sorts (QuerySdWanCandidateDeviceSorts | Unset):
        search_key (str | Unset): Look for a specific piece of data.
        filters (QuerySdWanCandidateDeviceFilters | Unset):
        search_field (str | Unset):
        group_id (str | Unset): The ID of the SD-WAN group.
        exclude_device_macs (list[str] | Unset): A list of exclude Device MAC for the candidate.
    """

    page: int
    page_size: int
    tunnel_limit: int
    role: int
    sorts: QuerySdWanCandidateDeviceSorts | Unset = UNSET
    search_key: str | Unset = UNSET
    filters: QuerySdWanCandidateDeviceFilters | Unset = UNSET
    search_field: str | Unset = UNSET
    group_id: str | Unset = UNSET
    exclude_device_macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        tunnel_limit = self.tunnel_limit

        role = self.role

        sorts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = self.sorts.to_dict()

        search_key = self.search_key

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        search_field = self.search_field

        group_id = self.group_id

        exclude_device_macs: list[str] | Unset = UNSET
        if not isinstance(self.exclude_device_macs, Unset):
            exclude_device_macs = self.exclude_device_macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pageSize": page_size,
                "tunnelLimit": tunnel_limit,
                "role": role,
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
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if exclude_device_macs is not UNSET:
            field_dict["excludeDeviceMacs"] = exclude_device_macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.query_sd_wan_candidate_device_filters import (
            QuerySdWanCandidateDeviceFilters,
        )
        from ..models.query_sd_wan_candidate_device_sorts import (
            QuerySdWanCandidateDeviceSorts,
        )

        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("pageSize")

        tunnel_limit = d.pop("tunnelLimit")

        role = d.pop("role")

        _sorts = d.pop("sorts", UNSET)
        sorts: QuerySdWanCandidateDeviceSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = QuerySdWanCandidateDeviceSorts.from_dict(_sorts)

        search_key = d.pop("searchKey", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: QuerySdWanCandidateDeviceFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = QuerySdWanCandidateDeviceFilters.from_dict(_filters)

        search_field = d.pop("searchField", UNSET)

        group_id = d.pop("groupId", UNSET)

        exclude_device_macs = cast(list[str], d.pop("excludeDeviceMacs", UNSET))

        query_sd_wan_candidate_device = cls(
            page=page,
            page_size=page_size,
            tunnel_limit=tunnel_limit,
            role=role,
            sorts=sorts,
            search_key=search_key,
            filters=filters,
            search_field=search_field,
            group_id=group_id,
            exclude_device_macs=exclude_device_macs,
        )

        query_sd_wan_candidate_device.additional_properties = d
        return query_sd_wan_candidate_device

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
