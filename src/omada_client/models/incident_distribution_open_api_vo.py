from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_count_open_api_vo import IncidentCountOpenApiVO


T = TypeVar("T", bound="IncidentDistributionOpenApiVO")


@_attrs_define
class IncidentDistributionOpenApiVO:
    """
    Attributes:
        incident_counts (list[IncidentCountOpenApiVO] | Unset): List of incident count items grouped by severity level
            (critical/error/warning/info) and by function type (category)
    """

    incident_counts: list[IncidentCountOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incident_counts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incident_counts, Unset):
            incident_counts = []
            for incident_counts_item_data in self.incident_counts:
                incident_counts_item = incident_counts_item_data.to_dict()
                incident_counts.append(incident_counts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incident_counts is not UNSET:
            field_dict["incidentCounts"] = incident_counts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_count_open_api_vo import (
            IncidentCountOpenApiVO,
        )

        d = dict(src_dict)
        _incident_counts = d.pop("incidentCounts", UNSET)
        incident_counts: list[IncidentCountOpenApiVO] | Unset = UNSET
        if _incident_counts is not UNSET:
            incident_counts = []
            for incident_counts_item_data in _incident_counts:
                incident_counts_item = IncidentCountOpenApiVO.from_dict(
                    incident_counts_item_data
                )

                incident_counts.append(incident_counts_item)

        incident_distribution_open_api_vo = cls(
            incident_counts=incident_counts,
        )

        incident_distribution_open_api_vo.additional_properties = d
        return incident_distribution_open_api_vo

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
