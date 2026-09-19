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


T = TypeVar("T", bound="ChannelSubHealthInfoDetailVO")


@_attrs_define
class ChannelSubHealthInfoDetailVO:
    """Rssi health info and score

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        average_num_2_g (int | Unset): Average value of 2g channel
        average_num_5_g (int | Unset): Average value of 5g channel
        average_num_6_g (int | Unset): Average value of 6g channel
        past_nums_2_g (list[TimeValueItemVO] | Unset): List of 2g channel value
        past_nums_5_g (list[TimeValueItemVO] | Unset): List of 5g channel value
        past_nums_6_g (list[TimeValueItemVO] | Unset): List of 6g channel value
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    average_num_2_g: int | Unset = UNSET
    average_num_5_g: int | Unset = UNSET
    average_num_6_g: int | Unset = UNSET
    past_nums_2_g: list[TimeValueItemVO] | Unset = UNSET
    past_nums_5_g: list[TimeValueItemVO] | Unset = UNSET
    past_nums_6_g: list[TimeValueItemVO] | Unset = UNSET
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

        average_num_2_g = self.average_num_2_g

        average_num_5_g = self.average_num_5_g

        average_num_6_g = self.average_num_6_g

        past_nums_2_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_nums_2_g, Unset):
            past_nums_2_g = []
            for past_nums_2_g_item_data in self.past_nums_2_g:
                past_nums_2_g_item = past_nums_2_g_item_data.to_dict()
                past_nums_2_g.append(past_nums_2_g_item)

        past_nums_5_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_nums_5_g, Unset):
            past_nums_5_g = []
            for past_nums_5_g_item_data in self.past_nums_5_g:
                past_nums_5_g_item = past_nums_5_g_item_data.to_dict()
                past_nums_5_g.append(past_nums_5_g_item)

        past_nums_6_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_nums_6_g, Unset):
            past_nums_6_g = []
            for past_nums_6_g_item_data in self.past_nums_6_g:
                past_nums_6_g_item = past_nums_6_g_item_data.to_dict()
                past_nums_6_g.append(past_nums_6_g_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if average_num_2_g is not UNSET:
            field_dict["averageNum2g"] = average_num_2_g
        if average_num_5_g is not UNSET:
            field_dict["averageNum5g"] = average_num_5_g
        if average_num_6_g is not UNSET:
            field_dict["averageNum6g"] = average_num_6_g
        if past_nums_2_g is not UNSET:
            field_dict["pastNums2g"] = past_nums_2_g
        if past_nums_5_g is not UNSET:
            field_dict["pastNums5g"] = past_nums_5_g
        if past_nums_6_g is not UNSET:
            field_dict["pastNums6g"] = past_nums_6_g

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

        average_num_2_g = d.pop("averageNum2g", UNSET)

        average_num_5_g = d.pop("averageNum5g", UNSET)

        average_num_6_g = d.pop("averageNum6g", UNSET)

        _past_nums_2_g = d.pop("pastNums2g", UNSET)
        past_nums_2_g: list[TimeValueItemVO] | Unset = UNSET
        if _past_nums_2_g is not UNSET:
            past_nums_2_g = []
            for past_nums_2_g_item_data in _past_nums_2_g:
                past_nums_2_g_item = TimeValueItemVO.from_dict(past_nums_2_g_item_data)

                past_nums_2_g.append(past_nums_2_g_item)

        _past_nums_5_g = d.pop("pastNums5g", UNSET)
        past_nums_5_g: list[TimeValueItemVO] | Unset = UNSET
        if _past_nums_5_g is not UNSET:
            past_nums_5_g = []
            for past_nums_5_g_item_data in _past_nums_5_g:
                past_nums_5_g_item = TimeValueItemVO.from_dict(past_nums_5_g_item_data)

                past_nums_5_g.append(past_nums_5_g_item)

        _past_nums_6_g = d.pop("pastNums6g", UNSET)
        past_nums_6_g: list[TimeValueItemVO] | Unset = UNSET
        if _past_nums_6_g is not UNSET:
            past_nums_6_g = []
            for past_nums_6_g_item_data in _past_nums_6_g:
                past_nums_6_g_item = TimeValueItemVO.from_dict(past_nums_6_g_item_data)

                past_nums_6_g.append(past_nums_6_g_item)

        channel_sub_health_info_detail_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            average_num_2_g=average_num_2_g,
            average_num_5_g=average_num_5_g,
            average_num_6_g=average_num_6_g,
            past_nums_2_g=past_nums_2_g,
            past_nums_5_g=past_nums_5_g,
            past_nums_6_g=past_nums_6_g,
        )

        channel_sub_health_info_detail_vo.additional_properties = d
        return channel_sub_health_info_detail_vo

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
