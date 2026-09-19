from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspUserDetailVO")


@_attrs_define
class MspUserDetailVO:
    """
    Attributes:
        id (str | Unset): User ID
        type_ (int | Unset): Type of user should be a value as follows: 0:local user; 1: cloud user
        role_id (str | Unset): Msp user role ID in MSP
        role_name (str | Unset): User bind role name
        name (str | Unset): User name
        email (str | Unset): User email
        msp_id (str | Unset): MSP ID
        verified (bool | Unset): Whether this cloud user has verified
        alert (bool | Unset): Whether this user wants to receive alert, event, and incident emails. Make sure your email
            is not null.
        parent_user_id (str | Unset): User's parent user ID
        customer_role_id (str | Unset): Msp user's customer role ID when visit customer
        customer_role_name (str | Unset): Msp user's customer role name when visit customer
        customer_ids (list[str] | Unset): User customer privilege list
        show_tree (bool | Unset): Whether msp user has Sub-users.
        all_customer (bool | Unset): Whether msp user has all customer permission, including new created customer
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permission
        start_time (int | Unset): The start time of the user's validity period. time range: start timestamp
            (Millisecond).
        end_time (int | Unset): The end time of the user's validity period. time range: end timestamp (Millisecond).
        temporary_validity (int | Unset): Whether the temporary user is still valid
    """

    id: str | Unset = UNSET
    type_: int | Unset = UNSET
    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    msp_id: str | Unset = UNSET
    verified: bool | Unset = UNSET
    alert: bool | Unset = UNSET
    parent_user_id: str | Unset = UNSET
    customer_role_id: str | Unset = UNSET
    customer_role_name: str | Unset = UNSET
    customer_ids: list[str] | Unset = UNSET
    show_tree: bool | Unset = UNSET
    all_customer: bool | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    temporary_validity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        role_id = self.role_id

        role_name = self.role_name

        name = self.name

        email = self.email

        msp_id = self.msp_id

        verified = self.verified

        alert = self.alert

        parent_user_id = self.parent_user_id

        customer_role_id = self.customer_role_id

        customer_role_name = self.customer_role_name

        customer_ids: list[str] | Unset = UNSET
        if not isinstance(self.customer_ids, Unset):
            customer_ids = self.customer_ids

        show_tree = self.show_tree

        all_customer = self.all_customer

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        temporary_validity = self.temporary_validity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if msp_id is not UNSET:
            field_dict["mspId"] = msp_id
        if verified is not UNSET:
            field_dict["verified"] = verified
        if alert is not UNSET:
            field_dict["alert"] = alert
        if parent_user_id is not UNSET:
            field_dict["parentUserId"] = parent_user_id
        if customer_role_id is not UNSET:
            field_dict["customerRoleId"] = customer_role_id
        if customer_role_name is not UNSET:
            field_dict["customerRoleName"] = customer_role_name
        if customer_ids is not UNSET:
            field_dict["customerIds"] = customer_ids
        if show_tree is not UNSET:
            field_dict["showTree"] = show_tree
        if all_customer is not UNSET:
            field_dict["allCustomer"] = all_customer
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
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        msp_id = d.pop("mspId", UNSET)

        verified = d.pop("verified", UNSET)

        alert = d.pop("alert", UNSET)

        parent_user_id = d.pop("parentUserId", UNSET)

        customer_role_id = d.pop("customerRoleId", UNSET)

        customer_role_name = d.pop("customerRoleName", UNSET)

        customer_ids = cast(list[str], d.pop("customerIds", UNSET))

        show_tree = d.pop("showTree", UNSET)

        all_customer = d.pop("allCustomer", UNSET)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        temporary_validity = d.pop("temporaryValidity", UNSET)

        msp_user_detail_vo = cls(
            id=id,
            type_=type_,
            role_id=role_id,
            role_name=role_name,
            name=name,
            email=email,
            msp_id=msp_id,
            verified=verified,
            alert=alert,
            parent_user_id=parent_user_id,
            customer_role_id=customer_role_id,
            customer_role_name=customer_role_name,
            customer_ids=customer_ids,
            show_tree=show_tree,
            all_customer=all_customer,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            temporary_validity=temporary_validity,
        )

        msp_user_detail_vo.additional_properties = d
        return msp_user_detail_vo

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
