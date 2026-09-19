from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
    from ..models.time_value_item_vo import TimeValueItemVO


T = TypeVar("T", bound="CommonSubHealthInfoDetailVO")


@_attrs_define
class CommonSubHealthInfoDetailVO:
    """Link error score health info and score (wired clients only)

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        average_num (int | Unset): Average value of common dimension, such as cpu、memory
        past_nums (list[TimeValueItemVO] | Unset): List of common dimension value , such as cpu、memory
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    average_num: int | Unset = UNSET
    past_nums: list[TimeValueItemVO] | Unset = UNSET
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

        average_num = self.average_num

        past_nums: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_nums, Unset):
            past_nums = []
            for past_nums_item_data in self.past_nums:
                past_nums_item = past_nums_item_data.to_dict()
                past_nums.append(past_nums_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if average_num is not UNSET:
            field_dict["averageNum"] = average_num
        if past_nums is not UNSET:
            field_dict["pastNums"] = past_nums

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
        from ..models.time_value_item_vo import TimeValueItemVO

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

        average_num = d.pop("averageNum", UNSET)

        _past_nums = d.pop("pastNums", UNSET)
        past_nums: list[TimeValueItemVO] | Unset = UNSET
        if _past_nums is not UNSET:
            past_nums = []
            for past_nums_item_data in _past_nums:
                past_nums_item = TimeValueItemVO.from_dict(past_nums_item_data)

                past_nums.append(past_nums_item)

        common_sub_health_info_detail_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            average_num=average_num,
            past_nums=past_nums,
        )

        common_sub_health_info_detail_vo.additional_properties = d
        return common_sub_health_info_detail_vo

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
