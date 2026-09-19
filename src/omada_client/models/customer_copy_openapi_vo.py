from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerCopyOpenapiVO")


@_attrs_define
class CustomerCopyOpenapiVO:
    """
    Attributes:
        new_customer_name (str): New Customer name should contain 1 to 31 characters.
        source_customer_id (str): Source customer ID to be copied.
        description (str | Unset): Customer description should contain 1 to 128 characters.
    """

    new_customer_name: str
    source_customer_id: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        new_customer_name = self.new_customer_name

        source_customer_id = self.source_customer_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "newCustomerName": new_customer_name,
                "sourceCustomerId": source_customer_id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        new_customer_name = d.pop("newCustomerName")

        source_customer_id = d.pop("sourceCustomerId")

        description = d.pop("description", UNSET)

        customer_copy_openapi_vo = cls(
            new_customer_name=new_customer_name,
            source_customer_id=source_customer_id,
            description=description,
        )

        customer_copy_openapi_vo.additional_properties = d
        return customer_copy_openapi_vo

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
