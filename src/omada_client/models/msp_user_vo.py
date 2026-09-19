from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.msp_privilege_vo import MspPrivilegeVO


T = TypeVar("T", bound="MspUserVO")


@_attrs_define
class MspUserVO:
    """
    Attributes:
        type_ (int):
        name (str):
        id (str | Unset):
        role_id (str | Unset):
        role_name (str | Unset):
        password (str | Unset):
        email (str | Unset):
        omadac_id (str | Unset):
        verified (bool | Unset):
        alert (bool | Unset):
        token (str | Unset):
        viewer_parent_user_id (str | Unset):
        show_tree (bool | Unset):
        parent_user_id (str | Unset):
        force_modify (bool | Unset):
        customer_role_id (str | Unset):
        customer_role_name (str | Unset):
        privilege (MspPrivilegeVO | Unset):
        owner (bool | Unset):
        temporary_enable (bool | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        temporary_validity (int | Unset):
        enable_2fa (bool | Unset):
    """

    type_: int
    name: str
    id: str | Unset = UNSET
    role_id: str | Unset = UNSET
    role_name: str | Unset = UNSET
    password: str | Unset = UNSET
    email: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    verified: bool | Unset = UNSET
    alert: bool | Unset = UNSET
    token: str | Unset = UNSET
    viewer_parent_user_id: str | Unset = UNSET
    show_tree: bool | Unset = UNSET
    parent_user_id: str | Unset = UNSET
    force_modify: bool | Unset = UNSET
    customer_role_id: str | Unset = UNSET
    customer_role_name: str | Unset = UNSET
    privilege: MspPrivilegeVO | Unset = UNSET
    owner: bool | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    temporary_validity: int | Unset = UNSET
    enable_2fa: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        id = self.id

        role_id = self.role_id

        role_name = self.role_name

        password = self.password

        email = self.email

        omadac_id = self.omadac_id

        verified = self.verified

        alert = self.alert

        token = self.token

        viewer_parent_user_id = self.viewer_parent_user_id

        show_tree = self.show_tree

        parent_user_id = self.parent_user_id

        force_modify = self.force_modify

        customer_role_id = self.customer_role_id

        customer_role_name = self.customer_role_name

        privilege: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.to_dict()

        owner = self.owner

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        temporary_validity = self.temporary_validity

        enable_2fa = self.enable_2fa

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if role_id is not UNSET:
            field_dict["roleId"] = role_id
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if verified is not UNSET:
            field_dict["verified"] = verified
        if alert is not UNSET:
            field_dict["alert"] = alert
        if token is not UNSET:
            field_dict["token"] = token
        if viewer_parent_user_id is not UNSET:
            field_dict["viewerParentUserId"] = viewer_parent_user_id
        if show_tree is not UNSET:
            field_dict["showTree"] = show_tree
        if parent_user_id is not UNSET:
            field_dict["parentUserId"] = parent_user_id
        if force_modify is not UNSET:
            field_dict["forceModify"] = force_modify
        if customer_role_id is not UNSET:
            field_dict["customerRoleId"] = customer_role_id
        if customer_role_name is not UNSET:
            field_dict["customerRoleName"] = customer_role_name
        if privilege is not UNSET:
            field_dict["privilege"] = privilege
        if owner is not UNSET:
            field_dict["owner"] = owner
        if temporary_enable is not UNSET:
            field_dict["temporaryEnable"] = temporary_enable
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if temporary_validity is not UNSET:
            field_dict["temporaryValidity"] = temporary_validity
        if enable_2fa is not UNSET:
            field_dict["enable2FA"] = enable_2fa

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.msp_privilege_vo import MspPrivilegeVO

        d = dict(src_dict)
        type_ = d.pop("type")

        name = d.pop("name")

        id = d.pop("id", UNSET)

        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        verified = d.pop("verified", UNSET)

        alert = d.pop("alert", UNSET)

        token = d.pop("token", UNSET)

        viewer_parent_user_id = d.pop("viewerParentUserId", UNSET)

        show_tree = d.pop("showTree", UNSET)

        parent_user_id = d.pop("parentUserId", UNSET)

        force_modify = d.pop("forceModify", UNSET)

        customer_role_id = d.pop("customerRoleId", UNSET)

        customer_role_name = d.pop("customerRoleName", UNSET)

        _privilege = d.pop("privilege", UNSET)
        privilege: MspPrivilegeVO | Unset
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = MspPrivilegeVO.from_dict(_privilege)

        owner = d.pop("owner", UNSET)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        temporary_validity = d.pop("temporaryValidity", UNSET)

        enable_2fa = d.pop("enable2FA", UNSET)

        msp_user_vo = cls(
            type_=type_,
            name=name,
            id=id,
            role_id=role_id,
            role_name=role_name,
            password=password,
            email=email,
            omadac_id=omadac_id,
            verified=verified,
            alert=alert,
            token=token,
            viewer_parent_user_id=viewer_parent_user_id,
            show_tree=show_tree,
            parent_user_id=parent_user_id,
            force_modify=force_modify,
            customer_role_id=customer_role_id,
            customer_role_name=customer_role_name,
            privilege=privilege,
            owner=owner,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            temporary_validity=temporary_validity,
            enable_2fa=enable_2fa,
        )

        msp_user_vo.additional_properties = d
        return msp_user_vo

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
