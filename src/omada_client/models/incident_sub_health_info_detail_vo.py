from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO


T = TypeVar("T", bound="IncidentSubHealthInfoDetailVO")


@_attrs_define
class IncidentSubHealthInfoDetailVO:
    """Incident health info and score (wireless clients only)

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        incident_num (int | Unset): Number of incident
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    incident_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary_score = self.summary_score

        support = self.support

        incidents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incidents, Unset):
            incidents = []
            for incidents_item_data in self.incidents:
                incidents_item = incidents_item_data.to_dict()
                incidents.append(incidents_item)

        incident_num = self.incident_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if incident_num is not UNSET:
            field_dict["incidentNum"] = incident_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO

        d = dict(src_dict)
        summary_score = d.pop("summaryScore", UNSET)

        support = d.pop("support", UNSET)

        _incidents = d.pop("incidents", UNSET)
        incidents: list[AnomalyBriefCountVO] | Unset = UNSET
        if _incidents is not UNSET:
            incidents = []
            for incidents_item_data in _incidents:
                incidents_item = AnomalyBriefCountVO.from_dict(incidents_item_data)

                incidents.append(incidents_item)

        incident_num = d.pop("incidentNum", UNSET)

        incident_sub_health_info_detail_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            incident_num=incident_num,
        )

        incident_sub_health_info_detail_vo.additional_properties = d
        return incident_sub_health_info_detail_vo

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
