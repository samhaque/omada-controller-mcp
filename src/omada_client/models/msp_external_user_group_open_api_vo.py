from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspExternalUserGroupOpenApiVO")


@_attrs_define
class MspExternalUserGroupOpenApiVO:
    """
    Attributes:
        name (str): Msp external user group name should contain 1 to 128 characters.
        role_id (str): Msp role ID which can be obtained from 'Get msp role list' interface.
        customer_role_id (str): Customer role ID which can be obtained from 'Get customer list' interface.
        all_customer (bool): Whether having all customer permissions.
        customers (list[str] | Unset): The customer IDs that can be accessed. Effective when allCustomer is false.
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permission
        start_time (int | Unset): The start time of the user's validity period. time range: start timestamp
            (Millisecond).
        end_time (int | Unset): The end time of the user's validity period. time range: end timestamp (Millisecond).
    """

    name: str
    role_id: str
    customer_role_id: str
    all_customer: bool
    customers: list[str] | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        role_id = self.role_id

        customer_role_id = self.customer_role_id

        all_customer = self.all_customer

        customers: list[str] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = self.customers

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "roleId": role_id,
                "customerRoleId": customer_role_id,
                "allCustomer": all_customer,
            }
        )
        if customers is not UNSET:
            field_dict["customers"] = customers
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
        name = d.pop("name")

        role_id = d.pop("roleId")

        customer_role_id = d.pop("customerRoleId")

        all_customer = d.pop("allCustomer")

        customers = cast(list[str], d.pop("customers", UNSET))

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        msp_external_user_group_open_api_vo = cls(
            name=name,
            role_id=role_id,
            customer_role_id=customer_role_id,
            all_customer=all_customer,
            customers=customers,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
        )

        msp_external_user_group_open_api_vo.additional_properties = d
        return msp_external_user_group_open_api_vo

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
