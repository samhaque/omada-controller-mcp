from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryCountryThreatListOpenApiVO")


@_attrs_define
class QueryCountryThreatListOpenApiVO:
    """
    Attributes:
        country (str | Unset): Country.
        severity (str | Unset): Displays the number of threats at different levels,0 - very high，1- high, 2- medium，3 -
            low.
        sites (str | Unset): List of siteIds, separated by commas (,). All sites are returned if they are not passed.
        current_page (int | Unset): Current Page.
        current_page_size (int | Unset): Current Page Size.
        search_key (str | Unset): Search Key.
        search_field (str | Unset): Specify the search domain, separated by commas, such as "clientMac,clientName".Can
            be null, in which case the default search domain should be used.
        sorts (str | Unset): sorts.
        start_time (int | Unset): The timestamp for the start time is in milliseconds.
        end_time (int | Unset): End Time.
    """

    country: str | Unset = UNSET
    severity: str | Unset = UNSET
    sites: str | Unset = UNSET
    current_page: int | Unset = UNSET
    current_page_size: int | Unset = UNSET
    search_key: str | Unset = UNSET
    search_field: str | Unset = UNSET
    sorts: str | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        severity = self.severity

        sites = self.sites

        current_page = self.current_page

        current_page_size = self.current_page_size

        search_key = self.search_key

        search_field = self.search_field

        sorts = self.sorts

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if severity is not UNSET:
            field_dict["severity"] = severity
        if sites is not UNSET:
            field_dict["sites"] = sites
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_page_size is not UNSET:
            field_dict["currentPageSize"] = current_page_size
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if search_field is not UNSET:
            field_dict["searchField"] = search_field
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        country = d.pop("country", UNSET)

        severity = d.pop("severity", UNSET)

        sites = d.pop("sites", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_page_size = d.pop("currentPageSize", UNSET)

        search_key = d.pop("searchKey", UNSET)

        search_field = d.pop("searchField", UNSET)

        sorts = d.pop("sorts", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        query_country_threat_list_open_api_vo = cls(
            country=country,
            severity=severity,
            sites=sites,
            current_page=current_page,
            current_page_size=current_page_size,
            search_key=search_key,
            search_field=search_field,
            sorts=sorts,
            start_time=start_time,
            end_time=end_time,
        )

        query_country_threat_list_open_api_vo.additional_properties = d
        return query_country_threat_list_open_api_vo

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
