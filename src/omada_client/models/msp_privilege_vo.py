from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer_vo import CustomerVO


T = TypeVar("T", bound="MspPrivilegeVO")


@_attrs_define
class MspPrivilegeVO:
    """
    Attributes:
        last_customer (str | Unset):
        customers (list[CustomerVO] | Unset):
        all_ (bool | Unset):
        favorite_customers (list[str] | Unset):
    """

    last_customer: str | Unset = UNSET
    customers: list[CustomerVO] | Unset = UNSET
    all_: bool | Unset = UNSET
    favorite_customers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_customer = self.last_customer

        customers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = customers_item_data.to_dict()
                customers.append(customers_item)

        all_ = self.all_

        favorite_customers: list[str] | Unset = UNSET
        if not isinstance(self.favorite_customers, Unset):
            favorite_customers = self.favorite_customers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_customer is not UNSET:
            field_dict["lastCustomer"] = last_customer
        if customers is not UNSET:
            field_dict["customers"] = customers
        if all_ is not UNSET:
            field_dict["all"] = all_
        if favorite_customers is not UNSET:
            field_dict["favoriteCustomers"] = favorite_customers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.customer_vo import CustomerVO

        d = dict(src_dict)
        last_customer = d.pop("lastCustomer", UNSET)

        _customers = d.pop("customers", UNSET)
        customers: list[CustomerVO] | Unset = UNSET
        if _customers is not UNSET:
            customers = []
            for customers_item_data in _customers:
                customers_item = CustomerVO.from_dict(customers_item_data)

                customers.append(customers_item)

        all_ = d.pop("all", UNSET)

        favorite_customers = cast(list[str], d.pop("favoriteCustomers", UNSET))

        msp_privilege_vo = cls(
            last_customer=last_customer,
            customers=customers,
            all_=all_,
            favorite_customers=favorite_customers,
        )

        msp_privilege_vo.additional_properties = d
        return msp_privilege_vo

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
