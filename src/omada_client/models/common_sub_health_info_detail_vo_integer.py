from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.time_value_item_vo_integer import TimeValueItemVOInteger


T = TypeVar("T", bound="CommonSubHealthInfoDetailVOInteger")


@_attrs_define
class CommonSubHealthInfoDetailVOInteger:
    """Link error score info (wired clients only)

    Attributes:
        summary_score (int | Unset): Sub dimension health score
        average_num (list[TimeValueItemVOInteger] | Unset): List of common dimension value, such as rssi
    """

    summary_score: int | Unset = UNSET
    average_num: list[TimeValueItemVOInteger] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        summary_score = self.summary_score

        average_num: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.average_num, Unset):
            average_num = []
            for average_num_item_data in self.average_num:
                average_num_item = average_num_item_data.to_dict()
                average_num.append(average_num_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if summary_score is not UNSET:
            field_dict["summaryScore"] = summary_score
        if average_num is not UNSET:
            field_dict["averageNum"] = average_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.time_value_item_vo_integer import (
            TimeValueItemVOInteger,
        )

        d = dict(src_dict)
        summary_score = d.pop("summaryScore", UNSET)

        _average_num = d.pop("averageNum", UNSET)
        average_num: list[TimeValueItemVOInteger] | Unset = UNSET
        if _average_num is not UNSET:
            average_num = []
            for average_num_item_data in _average_num:
                average_num_item = TimeValueItemVOInteger.from_dict(
                    average_num_item_data
                )

                average_num.append(average_num_item)

        common_sub_health_info_detail_vo_integer = cls(
            summary_score=summary_score,
            average_num=average_num,
        )

        common_sub_health_info_detail_vo_integer.additional_properties = d
        return common_sub_health_info_detail_vo_integer

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
