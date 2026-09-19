from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_statistics_score_vo import HealthStatisticsScoreVO


T = TypeVar("T", bound="HealthStatisticsTimeScoreItemVO")


@_attrs_define
class HealthStatisticsTimeScoreItemVO:
    """
    Attributes:
        time (int | Unset): Time(unit:ms)
        score_detail (HealthStatisticsScoreVO | Unset): Client health score detail
    """

    time: int | Unset = UNSET
    score_detail: HealthStatisticsScoreVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        score_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.score_detail, Unset):
            score_detail = self.score_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if score_detail is not UNSET:
            field_dict["scoreDetail"] = score_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.health_statistics_score_vo import (
            HealthStatisticsScoreVO,
        )

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        _score_detail = d.pop("scoreDetail", UNSET)
        score_detail: HealthStatisticsScoreVO | Unset
        if isinstance(_score_detail, Unset):
            score_detail = UNSET
        else:
            score_detail = HealthStatisticsScoreVO.from_dict(_score_detail)

        health_statistics_time_score_item_vo = cls(
            time=time,
            score_detail=score_detail,
        )

        health_statistics_time_score_item_vo.additional_properties = d
        return health_statistics_time_score_item_vo

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
