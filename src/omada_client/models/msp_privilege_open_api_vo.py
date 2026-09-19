from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspPrivilegeOpenApiVO")


@_attrs_define
class MspPrivilegeOpenApiVO:
    """The customer's privilege of this user.

    Attributes:
        all_ (bool | Unset): Whether having all customer privilege.
        customers (list[str] | Unset): The IDs of customer that can be accessed by this user.
    """

    all_: bool | Unset = UNSET
    customers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        customers: list[str] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = self.customers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if customers is not UNSET:
            field_dict["customers"] = customers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        customers = cast(list[str], d.pop("customers", UNSET))

        msp_privilege_open_api_vo = cls(
            all_=all_,
            customers=customers,
        )

        msp_privilege_open_api_vo.additional_properties = d
        return msp_privilege_open_api_vo

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
