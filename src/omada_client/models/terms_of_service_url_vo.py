from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TermsOfServiceUrlVO")


@_attrs_define
class TermsOfServiceUrlVO:
    """Terms of service url texts, match the termsOfServiceText and turn the matching characters into an openable link, Up
    to 3 entries are allowed for the list.

        Attributes:
            content (str): Terms of service URL content.
            text (str): Terms of service URL title.
            index (int | Unset): Index of hyperlink position.
    """

    content: str
    text: str
    index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content = self.content

        text = self.text

        index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
                "text": text,
            }
        )
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        content = d.pop("content")

        text = d.pop("text")

        index = d.pop("index", UNSET)

        terms_of_service_url_vo = cls(
            content=content,
            text=text,
            index=index,
        )

        terms_of_service_url_vo.additional_properties = d
        return terms_of_service_url_vo

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
