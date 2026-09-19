from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.category_traffic_detail_vo import CategoryTrafficDetailVO


T = TypeVar("T", bound="AppCategoryTrafficsVO")


@_attrs_define
class AppCategoryTrafficsVO:
    """
    Attributes:
        categories (list[CategoryTrafficDetailVO] | Unset):
        total_traffic (int | Unset): total traffic
    """

    categories: list[CategoryTrafficDetailVO] | Unset = UNSET
    total_traffic: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        total_traffic = self.total_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categories is not UNSET:
            field_dict["categories"] = categories
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.category_traffic_detail_vo import (
            CategoryTrafficDetailVO,
        )

        d = dict(src_dict)
        _categories = d.pop("categories", UNSET)
        categories: list[CategoryTrafficDetailVO] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = CategoryTrafficDetailVO.from_dict(
                    categories_item_data
                )

                categories.append(categories_item)

        total_traffic = d.pop("totalTraffic", UNSET)

        app_category_traffics_vo = cls(
            categories=categories,
            total_traffic=total_traffic,
        )

        app_category_traffics_vo.additional_properties = d
        return app_category_traffics_vo

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
