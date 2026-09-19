from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatisticsCountOpenApiVO")


@_attrs_define
class StatisticsCountOpenApiVO:
    """Represents the quantity of statistics for the voucher group, unaffected by search

    Attributes:
        total_unused_count (int | Unset): Unused voucher counts of the voucher group, unaffected by search
        total_in_use_count (int | Unset): In use voucher counts of the voucher group, unaffected by search
        total_expired_count (int | Unset): Expired voucher counts of the voucher group, unaffected by search
        total_statistics_count (int | Unset): Total voucher counts of the voucher group, unaffected by search
    """

    total_unused_count: int | Unset = UNSET
    total_in_use_count: int | Unset = UNSET
    total_expired_count: int | Unset = UNSET
    total_statistics_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_unused_count = self.total_unused_count

        total_in_use_count = self.total_in_use_count

        total_expired_count = self.total_expired_count

        total_statistics_count = self.total_statistics_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_unused_count is not UNSET:
            field_dict["totalUnusedCount"] = total_unused_count
        if total_in_use_count is not UNSET:
            field_dict["totalInUseCount"] = total_in_use_count
        if total_expired_count is not UNSET:
            field_dict["totalExpiredCount"] = total_expired_count
        if total_statistics_count is not UNSET:
            field_dict["totalStatisticsCount"] = total_statistics_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_unused_count = d.pop("totalUnusedCount", UNSET)

        total_in_use_count = d.pop("totalInUseCount", UNSET)

        total_expired_count = d.pop("totalExpiredCount", UNSET)

        total_statistics_count = d.pop("totalStatisticsCount", UNSET)

        statistics_count_open_api_vo = cls(
            total_unused_count=total_unused_count,
            total_in_use_count=total_in_use_count,
            total_expired_count=total_expired_count,
            total_statistics_count=total_statistics_count,
        )

        statistics_count_open_api_vo.additional_properties = d
        return statistics_count_open_api_vo

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
