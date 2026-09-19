from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_card_bucket_vo import ClientCardBucketVO


T = TypeVar("T", bound="ClientCardDataVO")


@_attrs_define
class ClientCardDataVO:
    """SNR distribution card data. Only present when 'snr' is requested.

    Attributes:
        total_count (int | Unset): Total number of clients counted for this card
        buckets (list[ClientCardBucketVO] | Unset): Distribution buckets for this card
    """

    total_count: int | Unset = UNSET
    buckets: list[ClientCardBucketVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if buckets is not UNSET:
            field_dict["buckets"] = buckets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_card_bucket_vo import ClientCardBucketVO

        d = dict(src_dict)
        total_count = d.pop("totalCount", UNSET)

        _buckets = d.pop("buckets", UNSET)
        buckets: list[ClientCardBucketVO] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = ClientCardBucketVO.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        client_card_data_vo = cls(
            total_count=total_count,
            buckets=buckets,
        )

        client_card_data_vo.additional_properties = d
        return client_card_data_vo

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
