from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.omadac_info_open_api_vo import OmadacInfoOpenApiVO


T = TypeVar("T", bound="MspExternalUserGroupDetailOpenApiVO")


@_attrs_define
class MspExternalUserGroupDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): Msp external user group ID.
        name (str | Unset): Msp external user group name.
        role_id (str | Unset): Msp role ID.
        role_name (str | Unset): Msp role name.
        role_type (int | Unset): Msp role type.
        customer_role_id (str | Unset): Customer role ID.
        customer_role_name (str | Unset): Customer role name.
        customer_role_type (int | Unset): Customer role type.
        all_customer (bool | Unset): Whether having all customer permissions.
        customers (list[OmadacInfoOpenApiVO] | Unset): The customers which can be accessed. Required when allCustomer is
            false.
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permission
        start_time (int | Unset): The start time of the user's validity period. time range: start timestamp
            (Millisecond).
        end_time (int | Unset): The end time of the user's validity period. time range: end timestamp (Millisecond).
        temporary_validity (int | Unset): Whether the temporary user is still valid
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    role_type: int | Unset = UNSET
    customer_role_id: str | Unset = UNSET
    customer_role_name: str | Unset = UNSET
    customer_role_type: int | Unset = UNSET
    all_customer: bool | Unset = UNSET
    customers: list[OmadacInfoOpenApiVO] | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    temporary_validity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        role_id = self.role_id

        role_name = self.role_name

        role_type = self.role_type

        customer_role_id = self.customer_role_id

        customer_role_name = self.customer_role_name

        customer_role_type = self.customer_role_type

        all_customer = self.all_customer

        customers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.customers, Unset):
            customers = []
            for customers_item_data in self.customers:
                customers_item = customers_item_data.to_dict()
                customers.append(customers_item)

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        temporary_validity = self.temporary_validity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if role_type is not UNSET:
            field_dict["roleType"] = role_type
        if customer_role_id is not UNSET:
            field_dict["customerRoleId"] = customer_role_id
        if customer_role_name is not UNSET:
            field_dict["customerRoleName"] = customer_role_name
        if customer_role_type is not UNSET:
            field_dict["customerRoleType"] = customer_role_type
        if all_customer is not UNSET:
            field_dict["allCustomer"] = all_customer
        if customers is not UNSET:
            field_dict["customers"] = customers
        if temporary_enable is not UNSET:
            field_dict["temporaryEnable"] = temporary_enable
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if temporary_validity is not UNSET:
            field_dict["temporaryValidity"] = temporary_validity

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.omadac_info_open_api_vo import (
            OmadacInfoOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        role_type = d.pop("roleType", UNSET)

        customer_role_id = d.pop("customerRoleId", UNSET)

        customer_role_name = d.pop("customerRoleName", UNSET)

        customer_role_type = d.pop("customerRoleType", UNSET)

        all_customer = d.pop("allCustomer", UNSET)

        _customers = d.pop("customers", UNSET)
        customers: list[OmadacInfoOpenApiVO] | Unset = UNSET
        if _customers is not UNSET:
            customers = []
            for customers_item_data in _customers:
                customers_item = OmadacInfoOpenApiVO.from_dict(customers_item_data)

                customers.append(customers_item)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        temporary_validity = d.pop("temporaryValidity", UNSET)

        msp_external_user_group_detail_open_api_vo = cls(
            id=id,
            name=name,
            role_id=role_id,
            role_name=role_name,
            role_type=role_type,
            customer_role_id=customer_role_id,
            customer_role_name=customer_role_name,
            customer_role_type=customer_role_type,
            all_customer=all_customer,
            customers=customers,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            temporary_validity=temporary_validity,
        )

        msp_external_user_group_detail_open_api_vo.additional_properties = d
        return msp_external_user_group_detail_open_api_vo

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
