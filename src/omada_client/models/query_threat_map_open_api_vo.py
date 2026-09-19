from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryThreatMapOpenApiVO")


@_attrs_define
class QueryThreatMapOpenApiVO:
    """
    Attributes:
        start (int | Unset): The timestamp for the start time is in milliseconds.
        end (int | Unset): The timestamp for the end time is in milliseconds.
        severity (str | Unset): Severity.
        country (str | Unset): The country that was attacked.
        sites (str | Unset): Comma separated sites should be explained. If it is not passed, select all.
    """

    start: int | Unset = UNSET
    end: int | Unset = UNSET
    severity: str | Unset = UNSET
    country: str | Unset = UNSET
    sites: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        severity = self.severity

        country = self.country

        sites = self.sites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if severity is not UNSET:
            field_dict["severity"] = severity
        if country is not UNSET:
            field_dict["country"] = country
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        severity = d.pop("severity", UNSET)

        country = d.pop("country", UNSET)

        sites = d.pop("sites", UNSET)

        query_threat_map_open_api_vo = cls(
            start=start,
            end=end,
            severity=severity,
            country=country,
            sites=sites,
        )

        query_threat_map_open_api_vo.additional_properties = d
        return query_threat_map_open_api_vo

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
