from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthStatisticsScoreVO")


@_attrs_define
class HealthStatisticsScoreVO:
    """Client health score detail

    Attributes:
        good_count (int | Unset): The number of good level device or client, whose health score is between 8 and 10
        average_count (int | Unset): The number of average level device or client, whose health score is between 4 and 7
        poor_count (int | Unset): The number of good poor device or client, whose health score is between 1 and 3
        no_data_count (int | Unset): The number of noData level device or client, whose health score is 0
    """

    good_count: int | Unset = UNSET
    average_count: int | Unset = UNSET
    poor_count: int | Unset = UNSET
    no_data_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        good_count = self.good_count

        average_count = self.average_count

        poor_count = self.poor_count

        no_data_count = self.no_data_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if good_count is not UNSET:
            field_dict["goodCount"] = good_count
        if average_count is not UNSET:
            field_dict["averageCount"] = average_count
        if poor_count is not UNSET:
            field_dict["poorCount"] = poor_count
        if no_data_count is not UNSET:
            field_dict["noDataCount"] = no_data_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        good_count = d.pop("goodCount", UNSET)

        average_count = d.pop("averageCount", UNSET)

        poor_count = d.pop("poorCount", UNSET)

        no_data_count = d.pop("noDataCount", UNSET)

        health_statistics_score_vo = cls(
            good_count=good_count,
            average_count=average_count,
            poor_count=poor_count,
            no_data_count=no_data_count,
        )

        health_statistics_score_vo.additional_properties = d
        return health_statistics_score_vo

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
