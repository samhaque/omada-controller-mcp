from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DnsCacheQueryOpenApiV2VO")


@_attrs_define
class DnsCacheQueryOpenApiV2VO:
    """
    Attributes:
        current_page (int | Unset): Start page number. Start from 1. This subsection is deprecated.
        current_page_size (int | Unset): Number of entries per page. It should be within the range of 1–100. This
            subsection is deprecated.
        type_ (int | Unset): Type of DNS follows: 0: IPV4; 1: IPV6. This subsection is deprecated.
    """

    current_page: int | Unset = UNSET
    current_page_size: int | Unset = UNSET
    type_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        current_page_size = self.current_page_size

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_page_size is not UNSET:
            field_dict["currentPageSize"] = current_page_size
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        current_page = d.pop("currentPage", UNSET)

        current_page_size = d.pop("currentPageSize", UNSET)

        type_ = d.pop("type", UNSET)

        dns_cache_query_open_api_v2vo = cls(
            current_page=current_page,
            current_page_size=current_page_size,
            type_=type_,
        )

        dns_cache_query_open_api_v2vo.additional_properties = d
        return dns_cache_query_open_api_v2vo

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
