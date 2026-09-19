from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerOpenApiVO")


@_attrs_define
class CustomerOpenApiVO:
    """
    Attributes:
        customer_name (str | Unset): Customer name should contain 1 to 32 characters.
        description (str | Unset): Customer description should contain 1 to 128 characters.
    """

    customer_name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_name = self.customer_name

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        customer_name = d.pop("customerName", UNSET)

        description = d.pop("description", UNSET)

        customer_open_api_vo = cls(
            customer_name=customer_name,
            description=description,
        )

        customer_open_api_vo.additional_properties = d
        return customer_open_api_vo

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
