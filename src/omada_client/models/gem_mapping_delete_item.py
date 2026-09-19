from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="GemMappingDeleteItem")


@_attrs_define
class GemMappingDeleteItem:
    """gemMappingList

    Attributes:
        gem_port_id (int): Gem port ID should be within the range of 1 to 1023
        gem_mapping_id (int): GemMappingId should be within the range of 1 to 8,and should not be null
    """

    gem_port_id: int
    gem_mapping_id: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gem_port_id = self.gem_port_id

        gem_mapping_id = self.gem_mapping_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gemPortId": gem_port_id,
                "gemMappingId": gem_mapping_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gem_port_id = d.pop("gemPortId")

        gem_mapping_id = d.pop("gemMappingId")

        gem_mapping_delete_item = cls(
            gem_port_id=gem_port_id,
            gem_mapping_id=gem_mapping_id,
        )

        gem_mapping_delete_item.additional_properties = d
        return gem_mapping_delete_item

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
