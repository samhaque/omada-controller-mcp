from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
    from ..models.time_float_value_item_vo import TimeFloatValueItemVO
    from ..models.time_value_item_vo import TimeValueItemVO


T = TypeVar("T", bound="WanSubHealthInfoDetailVO")


@_attrs_define
class WanSubHealthInfoDetailVO:
    """WAN health info and score

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        average_latency (int | Unset): Average latency
        average_jitter (int | Unset): Average jitter
        average_pkt_loss (float | Unset): Average packet loss
        average_mos (float | Unset): Average mean opinion score
        latency (list[TimeValueItemVO] | Unset): List of latency
        jitter (list[TimeValueItemVO] | Unset): List of jitter
        pkt_loss (list[TimeFloatValueItemVO] | Unset): List of packet loss
        mos (list[TimeFloatValueItemVO] | Unset): List of mos
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    average_latency: int | Unset = UNSET
    average_jitter: int | Unset = UNSET
    average_pkt_loss: float | Unset = UNSET
    average_mos: float | Unset = UNSET
    latency: list[TimeValueItemVO] | Unset = UNSET
    jitter: list[TimeValueItemVO] | Unset = UNSET
    pkt_loss: list[TimeFloatValueItemVO] | Unset = UNSET
    mos: list[TimeFloatValueItemVO] | Unset = UNSET
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

        average_latency = self.average_latency

        average_jitter = self.average_jitter

        average_pkt_loss = self.average_pkt_loss

        average_mos = self.average_mos

        latency: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.latency, Unset):
            latency = []
            for latency_item_data in self.latency:
                latency_item = latency_item_data.to_dict()
                latency.append(latency_item)

        jitter: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.jitter, Unset):
            jitter = []
            for jitter_item_data in self.jitter:
                jitter_item = jitter_item_data.to_dict()
                jitter.append(jitter_item)

        pkt_loss: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pkt_loss, Unset):
            pkt_loss = []
            for pkt_loss_item_data in self.pkt_loss:
                pkt_loss_item = pkt_loss_item_data.to_dict()
                pkt_loss.append(pkt_loss_item)

        mos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mos, Unset):
            mos = []
            for mos_item_data in self.mos:
                mos_item = mos_item_data.to_dict()
                mos.append(mos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if average_latency is not UNSET:
            field_dict["averageLatency"] = average_latency
        if average_jitter is not UNSET:
            field_dict["averageJitter"] = average_jitter
        if average_pkt_loss is not UNSET:
            field_dict["averagePktLoss"] = average_pkt_loss
        if average_mos is not UNSET:
            field_dict["averageMos"] = average_mos
        if latency is not UNSET:
            field_dict["latency"] = latency
        if jitter is not UNSET:
            field_dict["jitter"] = jitter
        if pkt_loss is not UNSET:
            field_dict["pktLoss"] = pkt_loss
        if mos is not UNSET:
            field_dict["mos"] = mos

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
        from ..models.time_float_value_item_vo import (
            TimeFloatValueItemVO,
        )
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

        average_latency = d.pop("averageLatency", UNSET)

        average_jitter = d.pop("averageJitter", UNSET)

        average_pkt_loss = d.pop("averagePktLoss", UNSET)

        average_mos = d.pop("averageMos", UNSET)

        _latency = d.pop("latency", UNSET)
        latency: list[TimeValueItemVO] | Unset = UNSET
        if _latency is not UNSET:
            latency = []
            for latency_item_data in _latency:
                latency_item = TimeValueItemVO.from_dict(latency_item_data)

                latency.append(latency_item)

        _jitter = d.pop("jitter", UNSET)
        jitter: list[TimeValueItemVO] | Unset = UNSET
        if _jitter is not UNSET:
            jitter = []
            for jitter_item_data in _jitter:
                jitter_item = TimeValueItemVO.from_dict(jitter_item_data)

                jitter.append(jitter_item)

        _pkt_loss = d.pop("pktLoss", UNSET)
        pkt_loss: list[TimeFloatValueItemVO] | Unset = UNSET
        if _pkt_loss is not UNSET:
            pkt_loss = []
            for pkt_loss_item_data in _pkt_loss:
                pkt_loss_item = TimeFloatValueItemVO.from_dict(pkt_loss_item_data)

                pkt_loss.append(pkt_loss_item)

        _mos = d.pop("mos", UNSET)
        mos: list[TimeFloatValueItemVO] | Unset = UNSET
        if _mos is not UNSET:
            mos = []
            for mos_item_data in _mos:
                mos_item = TimeFloatValueItemVO.from_dict(mos_item_data)

                mos.append(mos_item)

        wan_sub_health_info_detail_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            average_latency=average_latency,
            average_jitter=average_jitter,
            average_pkt_loss=average_pkt_loss,
            average_mos=average_mos,
            latency=latency,
            jitter=jitter,
            pkt_loss=pkt_loss,
            mos=mos,
        )

        wan_sub_health_info_detail_vo.additional_properties = d
        return wan_sub_health_info_detail_vo

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
