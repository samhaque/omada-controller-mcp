from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteCopyResultVO")


@_attrs_define
class SiteCopyResultVO:
    """Copy failed customer related information.

    Attributes:
        customer_id (str | Unset): Copying failed customer's customerId.
        customer_name (str | Unset): Copying failed customer's customerName.
        error_code (int | Unset): Copying failed customer's errorCode.
    """

    customer_id: str | Unset = UNSET
    customer_name: str | Unset = UNSET
    error_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        customer_name = self.customer_name

        error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if customer_name is not UNSET:
            field_dict["customerName"] = customer_name
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        customer_id = d.pop("customerId", UNSET)

        customer_name = d.pop("customerName", UNSET)

        error_code = d.pop("errorCode", UNSET)

        site_copy_result_vo = cls(
            customer_id=customer_id,
            customer_name=customer_name,
            error_code=error_code,
        )

        site_copy_result_vo.additional_properties = d
        return site_copy_result_vo

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
