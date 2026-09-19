from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentRankingQueryVO")


@_attrs_define
class IncidentRankingQueryVO:
    """
    Attributes:
        start_time (int): Start time in milliseconds
        end_time (int): End time in milliseconds
        anomaly_code (int): For the values of Anomaly event code, refer to section 5.7.2.1 of the Open API Access
            Example: 1001001.
        top_k (int | Unset): Number of top items to return. Defaults to 5 if not provided, maximum to 20.
    """

    start_time: int
    end_time: int
    anomaly_code: int
    top_k: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_time = self.start_time

        end_time = self.end_time

        anomaly_code = self.anomaly_code

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startTime": start_time,
                "endTime": end_time,
                "anomalyCode": anomaly_code,
            }
        )
        if top_k is not UNSET:
            field_dict["topK"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        anomaly_code = d.pop("anomalyCode")

        top_k = d.pop("topK", UNSET)

        incident_ranking_query_vo = cls(
            start_time=start_time,
            end_time=end_time,
            anomaly_code=anomaly_code,
            top_k=top_k,
        )

        incident_ranking_query_vo.additional_properties = d
        return incident_ranking_query_vo

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
