from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
    from ..models.long_time_value_item_vo import LongTimeValueItemVO


T = TypeVar("T", bound="ClientDataRateSubHealthDetailVO")


@_attrs_define
class ClientDataRateSubHealthDetailVO:
    """Negotiation rate health info and score

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        average_tx_rate (int | Unset):
        average_rx_rate (int | Unset):
        past_tx_rate (list[LongTimeValueItemVO] | Unset):
        past_rx_rate (list[LongTimeValueItemVO] | Unset):
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    average_tx_rate: int | Unset = UNSET
    average_rx_rate: int | Unset = UNSET
    past_tx_rate: list[LongTimeValueItemVO] | Unset = UNSET
    past_rx_rate: list[LongTimeValueItemVO] | Unset = UNSET
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

        average_tx_rate = self.average_tx_rate

        average_rx_rate = self.average_rx_rate

        past_tx_rate: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_tx_rate, Unset):
            past_tx_rate = []
            for past_tx_rate_item_data in self.past_tx_rate:
                past_tx_rate_item = past_tx_rate_item_data.to_dict()
                past_tx_rate.append(past_tx_rate_item)

        past_rx_rate: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_rx_rate, Unset):
            past_rx_rate = []
            for past_rx_rate_item_data in self.past_rx_rate:
                past_rx_rate_item = past_rx_rate_item_data.to_dict()
                past_rx_rate.append(past_rx_rate_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if average_tx_rate is not UNSET:
            field_dict["averageTxRate"] = average_tx_rate
        if average_rx_rate is not UNSET:
            field_dict["averageRxRate"] = average_rx_rate
        if past_tx_rate is not UNSET:
            field_dict["pastTxRate"] = past_tx_rate
        if past_rx_rate is not UNSET:
            field_dict["pastRxRate"] = past_rx_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_count_vo import AnomalyBriefCountVO
        from ..models.long_time_value_item_vo import (
            LongTimeValueItemVO,
        )

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

        average_tx_rate = d.pop("averageTxRate", UNSET)

        average_rx_rate = d.pop("averageRxRate", UNSET)

        _past_tx_rate = d.pop("pastTxRate", UNSET)
        past_tx_rate: list[LongTimeValueItemVO] | Unset = UNSET
        if _past_tx_rate is not UNSET:
            past_tx_rate = []
            for past_tx_rate_item_data in _past_tx_rate:
                past_tx_rate_item = LongTimeValueItemVO.from_dict(
                    past_tx_rate_item_data
                )

                past_tx_rate.append(past_tx_rate_item)

        _past_rx_rate = d.pop("pastRxRate", UNSET)
        past_rx_rate: list[LongTimeValueItemVO] | Unset = UNSET
        if _past_rx_rate is not UNSET:
            past_rx_rate = []
            for past_rx_rate_item_data in _past_rx_rate:
                past_rx_rate_item = LongTimeValueItemVO.from_dict(
                    past_rx_rate_item_data
                )

                past_rx_rate.append(past_rx_rate_item)

        client_data_rate_sub_health_detail_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            average_tx_rate=average_tx_rate,
            average_rx_rate=average_rx_rate,
            past_tx_rate=past_tx_rate,
            past_rx_rate=past_rx_rate,
        )

        client_data_rate_sub_health_detail_vo.additional_properties = d
        return client_data_rate_sub_health_detail_vo

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
