from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGridIpsThreat")


@_attrs_define
class GetGridIpsThreat:
    """
    Attributes:
        id (str | Unset): IPS threat ID
        time (int | Unset): Timestamp, in seconds, such as 1682000000
        src_country (str | Unset): IPS threat source Country
        service (str | Unset): IPS threat description
        severity (int | Unset): IPS threat severity should be a value as follows: 0: Critical; 1: Major; 2: Moderate; 3:
            Minor; 4: Low
        category (int | Unset): IPS threat category
        classification (str | Unset): Ips threat classification
    """

    id: str | Unset = UNSET
    time: int | Unset = UNSET
    src_country: str | Unset = UNSET
    service: str | Unset = UNSET
    severity: int | Unset = UNSET
    category: int | Unset = UNSET
    classification: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        time = self.time

        src_country = self.src_country

        service = self.service

        severity = self.severity

        category = self.category

        classification = self.classification

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time
        if src_country is not UNSET:
            field_dict["srcCountry"] = src_country
        if service is not UNSET:
            field_dict["service"] = service
        if severity is not UNSET:
            field_dict["severity"] = severity
        if category is not UNSET:
            field_dict["category"] = category
        if classification is not UNSET:
            field_dict["classification"] = classification

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        time = d.pop("time", UNSET)

        src_country = d.pop("srcCountry", UNSET)

        service = d.pop("service", UNSET)

        severity = d.pop("severity", UNSET)

        category = d.pop("category", UNSET)

        classification = d.pop("classification", UNSET)

        get_grid_ips_threat = cls(
            id=id,
            time=time,
            src_country=src_country,
            service=service,
            severity=severity,
            category=category,
            classification=classification,
        )

        get_grid_ips_threat.additional_properties = d
        return get_grid_ips_threat

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
