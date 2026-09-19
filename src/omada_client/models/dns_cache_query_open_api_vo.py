from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsCacheQueryOpenApiVO")


@_attrs_define
class DnsCacheQueryOpenApiVO:
    """
    Attributes:
        page (int | Unset): Queried page
        page_size (int | Unset): Queried page size
        type_ (int | Unset): Type should be a value as follows: 0: ipv4; 1: ipv6. Default type is ipv4.
    """

    page: int | Unset = UNSET
    page_size: int | Unset = UNSET
    type_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        type_ = d.pop("type", UNSET)

        dns_cache_query_open_api_vo = cls(
            page=page,
            page_size=page_size,
            type_=type_,
        )

        dns_cache_query_open_api_vo.additional_properties = d
        return dns_cache_query_open_api_vo

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
