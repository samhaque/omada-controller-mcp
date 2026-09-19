from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.msp_privilege_open_api_vo import MspPrivilegeOpenApiVO


T = TypeVar("T", bound="MspExternalUserDetailOpenApiVO")


@_attrs_define
class MspExternalUserDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): External user ID.
        name (str | Unset): External user name.
        idp_id (str | Unset): The ID of IdP which is used by this user.
        idp_name (str | Unset): The name of IdP which is used by this user.
        role_id (str | Unset): The ID of role which is used by this user.
        role_name (str | Unset): The name of role which is used by this user.
        customer_role_id (str | Unset): The ID of customer role which is used by this user.
        customer_role_name (str | Unset): The name of customer role which is used by this user.
        msp_privilege (MspPrivilegeOpenApiVO | Unset): The customer's privilege of this user.
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permission
        start_time (int | Unset): The start time of the user's validity period. time range: start timestamp
            (Millisecond).
        end_time (int | Unset): The end time of the user's validity period. time range: end timestamp (Millisecond).
        temporary_validity (int | Unset): Whether the temporary user is still valid
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    idp_id: str | Unset = UNSET
    idp_name: str | Unset = UNSET
    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    customer_role_id: str | Unset = UNSET
    customer_role_name: str | Unset = UNSET
    msp_privilege: MspPrivilegeOpenApiVO | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    temporary_validity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        idp_id = self.idp_id

        idp_name = self.idp_name

        role_id = self.role_id

        role_name = self.role_name

        customer_role_id = self.customer_role_id

        customer_role_name = self.customer_role_name

        msp_privilege: dict[str, Any] | Unset = UNSET
        if not isinstance(self.msp_privilege, Unset):
            msp_privilege = self.msp_privilege.to_dict()

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
        if idp_id is not UNSET:
            field_dict["idpId"] = idp_id
        if idp_name is not UNSET:
            field_dict["idpName"] = idp_name
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if customer_role_id is not UNSET:
            field_dict["customerRoleId"] = customer_role_id
        if customer_role_name is not UNSET:
            field_dict["customerRoleName"] = customer_role_name
        if msp_privilege is not UNSET:
            field_dict["mspPrivilege"] = msp_privilege
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
        from ..models.msp_privilege_open_api_vo import (
            MspPrivilegeOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        idp_id = d.pop("idpId", UNSET)

        idp_name = d.pop("idpName", UNSET)

        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        customer_role_id = d.pop("customerRoleId", UNSET)

        customer_role_name = d.pop("customerRoleName", UNSET)

        _msp_privilege = d.pop("mspPrivilege", UNSET)
        msp_privilege: MspPrivilegeOpenApiVO | Unset
        if isinstance(_msp_privilege, Unset):
            msp_privilege = UNSET
        else:
            msp_privilege = MspPrivilegeOpenApiVO.from_dict(_msp_privilege)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        temporary_validity = d.pop("temporaryValidity", UNSET)

        msp_external_user_detail_open_api_vo = cls(
            id=id,
            name=name,
            idp_id=idp_id,
            idp_name=idp_name,
            role_id=role_id,
            role_name=role_name,
            customer_role_id=customer_role_id,
            customer_role_name=customer_role_name,
            msp_privilege=msp_privilege,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            temporary_validity=temporary_validity,
        )

        msp_external_user_detail_open_api_vo.additional_properties = d
        return msp_external_user_detail_open_api_vo

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
