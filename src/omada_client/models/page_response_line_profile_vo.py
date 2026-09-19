from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.line_profile_vo import LineProfileVO


T = TypeVar("T", bound="PageResponseLineProfileVO")


@_attrs_define
class PageResponseLineProfileVO:
    """
    Attributes:
        content (list[LineProfileVO] | Unset): Content
        total_elements (int | Unset): Total elements
        total_pages (int | Unset): Total page number
        last (bool | Unset): Whether is in the last page
        number (int | Unset): Number of the current page,starting from 0.
        size (int | Unset): Page size
        number_of_elements (int | Unset): Actual number of current page
        first (bool | Unset): Whether is in the first page
    """

    content: list[LineProfileVO] | Unset = UNSET
    total_elements: int | Unset = UNSET
    total_pages: int | Unset = UNSET
    last: bool | Unset = UNSET
    number: int | Unset = UNSET
    size: int | Unset = UNSET
    number_of_elements: int | Unset = UNSET
    first: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()
                content.append(content_item)

        total_elements = self.total_elements

        total_pages = self.total_pages

        last = self.last

        number = self.number

        size = self.size

        number_of_elements = self.number_of_elements

        first = self.first

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if total_elements is not UNSET:
            field_dict["totalElements"] = total_elements
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if last is not UNSET:
            field_dict["last"] = last
        if number is not UNSET:
            field_dict["number"] = number
        if size is not UNSET:
            field_dict["size"] = size
        if number_of_elements is not UNSET:
            field_dict["numberOfElements"] = number_of_elements
        if first is not UNSET:
            field_dict["first"] = first

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.line_profile_vo import LineProfileVO

        d = dict(src_dict)
        _content = d.pop("content", UNSET)
        content: list[LineProfileVO] | Unset = UNSET
        if _content is not UNSET:
            content = []
            for content_item_data in _content:
                content_item = LineProfileVO.from_dict(content_item_data)

                content.append(content_item)

        total_elements = d.pop("totalElements", UNSET)

        total_pages = d.pop("totalPages", UNSET)

        last = d.pop("last", UNSET)

        number = d.pop("number", UNSET)

        size = d.pop("size", UNSET)

        number_of_elements = d.pop("numberOfElements", UNSET)

        first = d.pop("first", UNSET)

        page_response_line_profile_vo = cls(
            content=content,
            total_elements=total_elements,
            total_pages=total_pages,
            last=last,
            number=number,
            size=size,
            number_of_elements=number_of_elements,
            first=first,
        )

        page_response_line_profile_vo.additional_properties = d
        return page_response_line_profile_vo

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
