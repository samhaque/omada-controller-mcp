from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="HealthDistributionVO")


@_attrs_define
class HealthDistributionVO:
    """Health distribution

    Attributes:
        total (int | Unset): Total count
        good (int | Unset): Good count
        average (int | Unset): Average count
        poor (int | Unset): Poor count
        no_data (int | Unset): No data count
    """

    total: int | Unset = UNSET
    good: int | Unset = UNSET
    average: int | Unset = UNSET
    poor: int | Unset = UNSET
    no_data: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        good = self.good

        average = self.average

        poor = self.poor

        no_data = self.no_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if good is not UNSET:
            field_dict["good"] = good
        if average is not UNSET:
            field_dict["average"] = average
        if poor is not UNSET:
            field_dict["poor"] = poor
        if no_data is not UNSET:
            field_dict["noData"] = no_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        good = d.pop("good", UNSET)

        average = d.pop("average", UNSET)

        poor = d.pop("poor", UNSET)

        no_data = d.pop("noData", UNSET)

        health_distribution_vo = cls(
            total=total,
            good=good,
            average=average,
            poor=poor,
            no_data=no_data,
        )

        health_distribution_vo.additional_properties = d
        return health_distribution_vo

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
