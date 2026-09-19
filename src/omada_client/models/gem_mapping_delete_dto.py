from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gem_mapping_delete_item import GemMappingDeleteItem


T = TypeVar("T", bound="GemMappingDeleteDTO")


@_attrs_define
class GemMappingDeleteDTO:
    """
    Attributes:
        gem_mapping_list (list[GemMappingDeleteItem]): gemMappingList
        line_profile_id (int | Unset): The ID of the associated Line Profile,lineProfileId should be within the range of
            1 to 512.
    """

    gem_mapping_list: list[GemMappingDeleteItem]
    line_profile_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gem_mapping_list = []
        for gem_mapping_list_item_data in self.gem_mapping_list:
            gem_mapping_list_item = gem_mapping_list_item_data.to_dict()
            gem_mapping_list.append(gem_mapping_list_item)

        line_profile_id = self.line_profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gemMappingList": gem_mapping_list,
            }
        )
        if line_profile_id is not UNSET:
            field_dict["lineProfileId"] = line_profile_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.gem_mapping_delete_item import (
            GemMappingDeleteItem,
        )

        d = dict(src_dict)
        gem_mapping_list = []
        _gem_mapping_list = d.pop("gemMappingList")
        for gem_mapping_list_item_data in _gem_mapping_list:
            gem_mapping_list_item = GemMappingDeleteItem.from_dict(
                gem_mapping_list_item_data
            )

            gem_mapping_list.append(gem_mapping_list_item)

        line_profile_id = d.pop("lineProfileId", UNSET)

        gem_mapping_delete_dto = cls(
            gem_mapping_list=gem_mapping_list,
            line_profile_id=line_profile_id,
        )

        gem_mapping_delete_dto.additional_properties = d
        return gem_mapping_delete_dto

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
