from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UrlFilterGlobalOpenApiVO")


@_attrs_define
class UrlFilterGlobalOpenApiVO:
    """
    Attributes:
        block_page (bool): blockPage should be a value as follows: false: close; true: open.
        safe_search (bool): safeSearch should be a value as follows: false: close; true: open.
        block_page_message (str | Unset): blockPageMessage of blockPage,when blockPage switch is open.
    """

    block_page: bool
    safe_search: bool
    block_page_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        block_page = self.block_page

        safe_search = self.safe_search

        block_page_message = self.block_page_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blockPage": block_page,
                "safeSearch": safe_search,
            }
        )
        if block_page_message is not UNSET:
            field_dict["blockPageMessage"] = block_page_message

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        block_page = d.pop("blockPage")

        safe_search = d.pop("safeSearch")

        block_page_message = d.pop("blockPageMessage", UNSET)

        url_filter_global_open_api_vo = cls(
            block_page=block_page,
            safe_search=safe_search,
            block_page_message=block_page_message,
        )

        url_filter_global_open_api_vo.additional_properties = d
        return url_filter_global_open_api_vo

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
