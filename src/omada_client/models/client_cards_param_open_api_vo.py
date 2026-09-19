from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bucket_boundary_vo import BucketBoundaryVO


T = TypeVar("T", bound="ClientCardsParamOpenApiVO")


@_attrs_define
class ClientCardsParamOpenApiVO:
    """client cards to query

    Attributes:
        type_ (str | Unset): Type of the card, e.g. 'rssi', 'snr'
        top_k (str | Unset): TopK parameter of the card.
        buckets (list[BucketBoundaryVO] | Unset): Custom bucket boundaries (ascending by value). If not provided,
            default boundaries for the card type will be used.
    """

    type_: str | Unset = UNSET
    top_k: str | Unset = UNSET
    buckets: list[BucketBoundaryVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        top_k = self.top_k

        buckets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.buckets, Unset):
            buckets = []
            for buckets_item_data in self.buckets:
                buckets_item = buckets_item_data.to_dict()
                buckets.append(buckets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if top_k is not UNSET:
            field_dict["topK"] = top_k
        if buckets is not UNSET:
            field_dict["buckets"] = buckets

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.bucket_boundary_vo import BucketBoundaryVO

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        top_k = d.pop("topK", UNSET)

        _buckets = d.pop("buckets", UNSET)
        buckets: list[BucketBoundaryVO] | Unset = UNSET
        if _buckets is not UNSET:
            buckets = []
            for buckets_item_data in _buckets:
                buckets_item = BucketBoundaryVO.from_dict(buckets_item_data)

                buckets.append(buckets_item)

        client_cards_param_open_api_vo = cls(
            type_=type_,
            top_k=top_k,
            buckets=buckets,
        )

        client_cards_param_open_api_vo.additional_properties = d
        return client_cards_param_open_api_vo

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
