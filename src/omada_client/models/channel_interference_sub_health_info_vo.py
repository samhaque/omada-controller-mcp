from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
    from ..models.time_score_item_vo import TimeScoreItemVO


T = TypeVar("T", bound="ChannelInterferenceSubHealthInfoVO")


@_attrs_define
class ChannelInterferenceSubHealthInfoVO:
    """Channel interference rate score detail info

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        average_interf_2_g (int | Unset): Average 2.4G interference
        average_interf_5_g (int | Unset): Average 5G interference
        average_interf_6_g (int | Unset): Average 6G interference
        average_noise_floor (int | Unset): Average noise floor
        scores (list[TimeScoreItemVO] | Unset): List of time score items
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    average_interf_2_g: int | Unset = UNSET
    average_interf_5_g: int | Unset = UNSET
    average_interf_6_g: int | Unset = UNSET
    average_noise_floor: int | Unset = UNSET
    scores: list[TimeScoreItemVO] | Unset = UNSET
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

        average_interf_2_g = self.average_interf_2_g

        average_interf_5_g = self.average_interf_5_g

        average_interf_6_g = self.average_interf_6_g

        average_noise_floor = self.average_noise_floor

        scores: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scores, Unset):
            scores = []
            for scores_item_data in self.scores:
                scores_item = scores_item_data.to_dict()
                scores.append(scores_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if average_interf_2_g is not UNSET:
            field_dict["averageInterf2g"] = average_interf_2_g
        if average_interf_5_g is not UNSET:
            field_dict["averageInterf5g"] = average_interf_5_g
        if average_interf_6_g is not UNSET:
            field_dict["averageInterf6g"] = average_interf_6_g
        if average_noise_floor is not UNSET:
            field_dict["averageNoiseFloor"] = average_noise_floor
        if scores is not UNSET:
            field_dict["scores"] = scores

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
        from ..models.time_score_item_vo import TimeScoreItemVO

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

        average_interf_2_g = d.pop("averageInterf2g", UNSET)

        average_interf_5_g = d.pop("averageInterf5g", UNSET)

        average_interf_6_g = d.pop("averageInterf6g", UNSET)

        average_noise_floor = d.pop("averageNoiseFloor", UNSET)

        _scores = d.pop("scores", UNSET)
        scores: list[TimeScoreItemVO] | Unset = UNSET
        if _scores is not UNSET:
            scores = []
            for scores_item_data in _scores:
                scores_item = TimeScoreItemVO.from_dict(scores_item_data)

                scores.append(scores_item)

        channel_interference_sub_health_info_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            average_interf_2_g=average_interf_2_g,
            average_interf_5_g=average_interf_5_g,
            average_interf_6_g=average_interf_6_g,
            average_noise_floor=average_noise_floor,
            scores=scores,
        )

        channel_interference_sub_health_info_vo.additional_properties = d
        return channel_interference_sub_health_info_vo

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
