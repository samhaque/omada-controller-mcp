from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_statistics_time_score_item_vo import (
        HealthStatisticsTimeScoreItemVO,
    )


T = TypeVar("T", bound="ClientScoreTimelineListVO")


@_attrs_define
class ClientScoreTimelineListVO:
    """
    Attributes:
        scores (list[HealthStatisticsTimeScoreItemVO] | Unset):
    """

    scores: list[HealthStatisticsTimeScoreItemVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scores: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.scores, Unset):
            scores = []
            for scores_item_data in self.scores:
                scores_item = scores_item_data.to_dict()
                scores.append(scores_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scores is not UNSET:
            field_dict["scores"] = scores

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.health_statistics_time_score_item_vo import (
            HealthStatisticsTimeScoreItemVO,
        )

        d = dict(src_dict)
        _scores = d.pop("scores", UNSET)
        scores: list[HealthStatisticsTimeScoreItemVO] | Unset = UNSET
        if _scores is not UNSET:
            scores = []
            for scores_item_data in _scores:
                scores_item = HealthStatisticsTimeScoreItemVO.from_dict(
                    scores_item_data
                )

                scores.append(scores_item)

        client_score_timeline_list_vo = cls(
            scores=scores,
        )

        client_score_timeline_list_vo.additional_properties = d
        return client_score_timeline_list_vo

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
