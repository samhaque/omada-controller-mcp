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


T = TypeVar("T", bound="TransmissionSubHealthInfoDetailVO")


@_attrs_define
class TransmissionSubHealthInfoDetailVO:
    """wireless transmission quality health info and score

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        support (bool | Unset): Sub dimension support
        incidents (list[AnomalyBriefCountVO] | Unset): Incident information for this health dimension, null if no
            incidents
        average_num_tx_retry (int | Unset): Average value of tx retry
        average_num_tx_drop (int | Unset): Average value of tx drop
        past_nums_tx_retry (list[TimeValueItemVO] | Unset): List of tx retry
        past_nums_tx_drop (list[TimeValueItemVO] | Unset): List of tx drop
    """

    summary_score: int | Unset = UNSET
    support: bool | Unset = UNSET
    incidents: list[AnomalyBriefCountVO] | Unset = UNSET
    average_num_tx_retry: int | Unset = UNSET
    average_num_tx_drop: int | Unset = UNSET
    past_nums_tx_retry: list[TimeValueItemVO] | Unset = UNSET
    past_nums_tx_drop: list[TimeValueItemVO] | Unset = UNSET
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

        average_num_tx_retry = self.average_num_tx_retry

        average_num_tx_drop = self.average_num_tx_drop

        past_nums_tx_retry: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_nums_tx_retry, Unset):
            past_nums_tx_retry = []
            for past_nums_tx_retry_item_data in self.past_nums_tx_retry:
                past_nums_tx_retry_item = past_nums_tx_retry_item_data.to_dict()
                past_nums_tx_retry.append(past_nums_tx_retry_item)

        past_nums_tx_drop: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.past_nums_tx_drop, Unset):
            past_nums_tx_drop = []
            for past_nums_tx_drop_item_data in self.past_nums_tx_drop:
                past_nums_tx_drop_item = past_nums_tx_drop_item_data.to_dict()
                past_nums_tx_drop.append(past_nums_tx_drop_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if support is not UNSET:
            field_dict["support"] = support
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if average_num_tx_retry is not UNSET:
            field_dict["averageNumTxRetry"] = average_num_tx_retry
        if average_num_tx_drop is not UNSET:
            field_dict["averageNumTxDrop"] = average_num_tx_drop
        if past_nums_tx_retry is not UNSET:
            field_dict["pastNumsTxRetry"] = past_nums_tx_retry
        if past_nums_tx_drop is not UNSET:
            field_dict["pastNumsTxDrop"] = past_nums_tx_drop

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

        average_num_tx_retry = d.pop("averageNumTxRetry", UNSET)

        average_num_tx_drop = d.pop("averageNumTxDrop", UNSET)

        _past_nums_tx_retry = d.pop("pastNumsTxRetry", UNSET)
        past_nums_tx_retry: list[TimeValueItemVO] | Unset = UNSET
        if _past_nums_tx_retry is not UNSET:
            past_nums_tx_retry = []
            for past_nums_tx_retry_item_data in _past_nums_tx_retry:
                past_nums_tx_retry_item = TimeValueItemVO.from_dict(
                    past_nums_tx_retry_item_data
                )

                past_nums_tx_retry.append(past_nums_tx_retry_item)

        _past_nums_tx_drop = d.pop("pastNumsTxDrop", UNSET)
        past_nums_tx_drop: list[TimeValueItemVO] | Unset = UNSET
        if _past_nums_tx_drop is not UNSET:
            past_nums_tx_drop = []
            for past_nums_tx_drop_item_data in _past_nums_tx_drop:
                past_nums_tx_drop_item = TimeValueItemVO.from_dict(
                    past_nums_tx_drop_item_data
                )

                past_nums_tx_drop.append(past_nums_tx_drop_item)

        transmission_sub_health_info_detail_vo = cls(
            summary_score=summary_score,
            support=support,
            incidents=incidents,
            average_num_tx_retry=average_num_tx_retry,
            average_num_tx_drop=average_num_tx_drop,
            past_nums_tx_retry=past_nums_tx_retry,
            past_nums_tx_drop=past_nums_tx_drop,
        )

        transmission_sub_health_info_detail_vo.additional_properties = d
        return transmission_sub_health_info_detail_vo

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
