from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientCardBucketVO")


@_attrs_define
class ClientCardBucketVO:
    """Distribution buckets for this card

    Attributes:
        label (str | Unset): Bucket label, e.g. '>= -50 dBm' or '[10, 20) dB'
        lower_bound (int | Unset): Lower bound of the bucket, null means negative infinity
        lower_inclusive (bool | Unset): Whether the lower bound is inclusive
        upper_bound (int | Unset): Upper bound of the bucket, null means positive infinity
        upper_inclusive (bool | Unset): Whether the upper bound is inclusive
        count (int | Unset): Total number of clients in this bucket
        percent (int | Unset): Percentage of clients in this bucket (0-100)
        clients2g (int | Unset): Number of 2.4GHz clients in this bucket
        clients5g (int | Unset): Number of 5GHz clients in this bucket
        clients6g (int | Unset): Number of 6GHz clients in this bucket
    """

    label: str | Unset = UNSET
    lower_bound: int | Unset = UNSET
    lower_inclusive: bool | Unset = UNSET
    upper_bound: int | Unset = UNSET
    upper_inclusive: bool | Unset = UNSET
    count: int | Unset = UNSET
    percent: int | Unset = UNSET
    clients2g: int | Unset = UNSET
    clients5g: int | Unset = UNSET
    clients6g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        lower_bound = self.lower_bound

        lower_inclusive = self.lower_inclusive

        upper_bound = self.upper_bound

        upper_inclusive = self.upper_inclusive

        count = self.count

        percent = self.percent

        clients2g = self.clients2g

        clients5g = self.clients5g

        clients6g = self.clients6g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if lower_inclusive is not UNSET:
            field_dict["lowerInclusive"] = lower_inclusive
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound
        if upper_inclusive is not UNSET:
            field_dict["upperInclusive"] = upper_inclusive
        if count is not UNSET:
            field_dict["count"] = count
        if percent is not UNSET:
            field_dict["percent"] = percent
        if clients2g is not UNSET:
            field_dict["clients2g"] = clients2g
        if clients5g is not UNSET:
            field_dict["clients5g"] = clients5g
        if clients6g is not UNSET:
            field_dict["clients6g"] = clients6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        label = d.pop("label", UNSET)

        lower_bound = d.pop("lowerBound", UNSET)

        lower_inclusive = d.pop("lowerInclusive", UNSET)

        upper_bound = d.pop("upperBound", UNSET)

        upper_inclusive = d.pop("upperInclusive", UNSET)

        count = d.pop("count", UNSET)

        percent = d.pop("percent", UNSET)

        clients2g = d.pop("clients2g", UNSET)

        clients5g = d.pop("clients5g", UNSET)

        clients6g = d.pop("clients6g", UNSET)

        client_card_bucket_vo = cls(
            label=label,
            lower_bound=lower_bound,
            lower_inclusive=lower_inclusive,
            upper_bound=upper_bound,
            upper_inclusive=upper_inclusive,
            count=count,
            percent=percent,
            clients2g=clients2g,
            clients5g=clients5g,
            clients6g=clients6g,
        )

        client_card_bucket_vo.additional_properties = d
        return client_card_bucket_vo

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
