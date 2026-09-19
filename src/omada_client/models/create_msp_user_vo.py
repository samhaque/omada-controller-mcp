from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMspUserVO")


@_attrs_define
class CreateMspUserVO:
    """
    Attributes:
        type_ (int): Type of user should be a value as follows: 0:local user; 1: cloud user
        name (str): User name. When creating cloud user, you should set TP-LINK ID. It should contain 1 to 128 ASCII
            visible characters and start with letters, numbers, and underscores.
        role_id (str): Msp role ID of user
        customer_role_id (str): Msp user's customer role ID when visit customer
        all_customer (bool): Whether msp user has all customer permission, including new created customer.
        password (str | Unset): Password of local user should contain 8 to 128 ASCII visible characters.And password
            must be a combination of uppercase letters, lowercase letters, numbers, and special symbols. Symbols such as ! #
            $ % & * @ ^ are supported.
        email (str | Unset): Email of user
        customers (list[str] | Unset): User customer privilege list
        alert (bool | Unset): Whether this user wants to receive alert, event, and incident emails. Make sure your email
            is not null.
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permission
        start_time (int | Unset): The start time of the user's validity period. time range: start timestamp
            (Millisecond).
        end_time (int | Unset): The end time of the user's validity period. time range: end timestamp (Millisecond).
    """

    type_: int
    name: str
    role_id: str
    customer_role_id: str
    all_customer: bool
    password: str | Unset = UNSET
    email: str | Unset = UNSET
    customers: list[str] | Unset = UNSET
    alert: bool | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        role_id = self.role_id

        customer_role_id = self.customer_role_id

        all_customer = self.all_customer

        password = self.password

        email = self.email

        customers: list[str] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = self.customers

        alert = self.alert

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "roleId": role_id,
                "customerRoleId": customer_role_id,
                "allCustomer": all_customer,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if customers is not UNSET:
            field_dict["customers"] = customers
        if alert is not UNSET:
            field_dict["alert"] = alert
        if temporary_enable is not UNSET:
            field_dict["temporaryEnable"] = temporary_enable
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        role_id = d.pop("roleId")

        customer_role_id = d.pop("customerRoleId")

        all_customer = d.pop("allCustomer")

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        customers = cast(list[str], d.pop("customers", UNSET))

        alert = d.pop("alert", UNSET)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        create_msp_user_vo = cls(
            type_=type_,
            name=name,
            role_id=role_id,
            customer_role_id=customer_role_id,
            all_customer=all_customer,
            password=password,
            email=email,
            customers=customers,
            alert=alert,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
        )

        create_msp_user_vo.additional_properties = d
        return create_msp_user_vo

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
