from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.url_category_open_api_vo_categories import (
        UrlCategoryOpenApiVOCategories,
    )


T = TypeVar("T", bound="UrlCategoryOpenApiVO")


@_attrs_define
class UrlCategoryOpenApiVO:
    """
    Attributes:
        categories (UrlCategoryOpenApiVOCategories | Unset): categories of the URL filtering 5.15
        protocol_ver (str | Unset): protocolVer of the categories.
    """

    categories: UrlCategoryOpenApiVOCategories | Unset = UNSET
    protocol_ver: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: dict[str, Any] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = self.categories.to_dict()

        protocol_ver = self.protocol_ver

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if protocol_ver is not UNSET:
            field_dict["protocolVer"] = protocol_ver

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.url_category_open_api_vo_categories import (
            UrlCategoryOpenApiVOCategories,
        )

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: UrlCategoryOpenApiVOCategories | Unset
        if isinstance(_categories, Unset):
            categories = UNSET
        else:
            categories = UrlCategoryOpenApiVOCategories.from_dict(_categories)

        protocol_ver = d.pop("protocolVer", UNSET)

        url_category_open_api_vo = cls(
            categories=categories,
            protocol_ver=protocol_ver,
        )

        url_category_open_api_vo.additional_properties = d
        return url_category_open_api_vo

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
