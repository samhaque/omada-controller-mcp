from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.active_pair_open_api_dto import ActivePairOpenApiDTO


T = TypeVar("T", bound="ActiveDeviceOpenApiVO")


@_attrs_define
class ActiveDeviceOpenApiVO:
    """
    Attributes:
        active_pair_list (list[ActivePairOpenApiDTO]):
        category (str): It should be a value as follows: basic; ap; l2Switch; l3Switch; gateway
    """

    active_pair_list: list[ActivePairOpenApiDTO]
    category: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_pair_list = []
        for active_pair_list_item_data in self.active_pair_list:
            active_pair_list_item = active_pair_list_item_data.to_dict()
            active_pair_list.append(active_pair_list_item)

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activePairList": active_pair_list,
                "category": category,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.active_pair_open_api_dto import (
            ActivePairOpenApiDTO,
        )

        d = dict(src_dict)
        active_pair_list = []
        _active_pair_list = d.pop("activePairList")
        for active_pair_list_item_data in _active_pair_list:
            active_pair_list_item = ActivePairOpenApiDTO.from_dict(
                active_pair_list_item_data
            )

            active_pair_list.append(active_pair_list_item)

        category = d.pop("category")

        active_device_open_api_vo = cls(
            active_pair_list=active_pair_list,
            category=category,
        )

        active_device_open_api_vo.additional_properties = d
        return active_device_open_api_vo

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
