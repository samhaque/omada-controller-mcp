from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanWeightOpenApiVO")


@_attrs_define
class VirtualWanWeightOpenApiVO:
    """virtual wan load balance

    Attributes:
        virtual_wan_id (str): virtual wan id
        weight (int | Unset): virtual wan weight
        name (str | Unset): virtual wan name
        physical_wan_id (str | Unset): physical wan id
    """

    virtual_wan_id: str
    weight: int | Unset = UNSET
    name: str | Unset = UNSET
    physical_wan_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_wan_id = self.virtual_wan_id

        weight = self.weight

        name = self.name

        physical_wan_id = self.physical_wan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "virtualWanId": virtual_wan_id,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight
        if name is not UNSET:
            field_dict["name"] = name
        if physical_wan_id is not UNSET:
            field_dict["physicalWanId"] = physical_wan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        virtual_wan_id = d.pop("virtualWanId")

        weight = d.pop("weight", UNSET)

        name = d.pop("name", UNSET)

        physical_wan_id = d.pop("physicalWanId", UNSET)

        virtual_wan_weight_open_api_vo = cls(
            virtual_wan_id=virtual_wan_id,
            weight=weight,
            name=name,
            physical_wan_id=physical_wan_id,
        )

        virtual_wan_weight_open_api_vo.additional_properties = d
        return virtual_wan_weight_open_api_vo

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
