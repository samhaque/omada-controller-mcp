from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ThreatSeverityOpenApiVO")


@_attrs_define
class ThreatSeverityOpenApiVO:
    """
    Attributes:
        critical (int | Unset): 0：Critical, 1：Major, 2：Moderate 3：Minor 4:Low.
        major (int | Unset): Major.
        moderate (int | Unset): Moderate.
        minor (int | Unset): Minor.
        low (int | Unset): Low.
    """

    critical: int | Unset = UNSET
    major: int | Unset = UNSET
    moderate: int | Unset = UNSET
    minor: int | Unset = UNSET
    low: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        critical = self.critical

        major = self.major

        moderate = self.moderate

        minor = self.minor

        low = self.low

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if critical is not UNSET:
            field_dict["critical"] = critical
        if major is not UNSET:
            field_dict["major"] = major
        if moderate is not UNSET:
            field_dict["moderate"] = moderate
        if minor is not UNSET:
            field_dict["minor"] = minor
        if low is not UNSET:
            field_dict["low"] = low

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        critical = d.pop("critical", UNSET)

        major = d.pop("major", UNSET)

        moderate = d.pop("moderate", UNSET)

        minor = d.pop("minor", UNSET)

        low = d.pop("low", UNSET)

        threat_severity_open_api_vo = cls(
            critical=critical,
            major=major,
            moderate=moderate,
            minor=minor,
            low=low,
        )

        threat_severity_open_api_vo.additional_properties = d
        return threat_severity_open_api_vo

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
