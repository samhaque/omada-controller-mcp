from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.privilege_result_vo import PrivilegeResultVO
    from ..models.role_detail_vo import RoleDetailVO


T = TypeVar("T", bound="ControllerUserAppVO")


@_attrs_define
class ControllerUserAppVO:
    """
    Attributes:
        type_ (int):
        id (str | Unset):
        role_detail (RoleDetailVO | Unset):
        role_type (int | Unset):
        name (str | Unset):
        email (str | Unset):
        omadac_id (str | Unset):
        verified (bool | Unset):
        alert (bool | Unset):
        privilege (PrivilegeResultVO | Unset):
        viewer_parent_user_id (str | Unset):
        parent_user_id (str | Unset):
        show_tree (bool | Unset):
        incident_notification (bool | Unset):
        user_level (int | Unset):
        temporary_enable (bool | Unset):
        start_time (int | Unset):
        end_time (int | Unset):
        temporary_validity (int | Unset):
    """

    type_: int
    id: str | Unset = UNSET
    role_detail: RoleDetailVO | Unset = UNSET
    role_type: int | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    verified: bool | Unset = UNSET
    alert: bool | Unset = UNSET
    privilege: PrivilegeResultVO | Unset = UNSET
    viewer_parent_user_id: str | Unset = UNSET
    parent_user_id: str | Unset = UNSET
    show_tree: bool | Unset = UNSET
    incident_notification: bool | Unset = UNSET
    user_level: int | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    temporary_validity: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        role_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.role_detail, Unset):
            role_detail = self.role_detail.to_dict()

        role_type = self.role_type

        name = self.name

        email = self.email

        omadac_id = self.omadac_id

        verified = self.verified

        alert = self.alert

        privilege: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privilege, Unset):
            privilege = self.privilege.to_dict()

        viewer_parent_user_id = self.viewer_parent_user_id

        parent_user_id = self.parent_user_id

        show_tree = self.show_tree

        incident_notification = self.incident_notification

        user_level = self.user_level

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        temporary_validity = self.temporary_validity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if role_detail is not UNSET:
            field_dict["roleDetail"] = role_detail
        if role_type is not UNSET:
            field_dict["roleType"] = role_type
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if verified is not UNSET:
            field_dict["verified"] = verified
        if alert is not UNSET:
            field_dict["alert"] = alert
        if privilege is not UNSET:
            field_dict["privilege"] = privilege
        if viewer_parent_user_id is not UNSET:
            field_dict["viewerParentUserId"] = viewer_parent_user_id
        if parent_user_id is not UNSET:
            field_dict["parentUserId"] = parent_user_id
        if show_tree is not UNSET:
            field_dict["showTree"] = show_tree
        if incident_notification is not UNSET:
            field_dict["incidentNotification"] = incident_notification
        if user_level is not UNSET:
            field_dict["userLevel"] = user_level
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
        from ..models.privilege_result_vo import PrivilegeResultVO
        from ..models.role_detail_vo import RoleDetailVO

        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id", UNSET)

        _role_detail = d.pop("roleDetail", UNSET)
        role_detail: RoleDetailVO | Unset
        if isinstance(_role_detail, Unset):
            role_detail = UNSET
        else:
            role_detail = RoleDetailVO.from_dict(_role_detail)

        role_type = d.pop("roleType", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        verified = d.pop("verified", UNSET)

        alert = d.pop("alert", UNSET)

        _privilege = d.pop("privilege", UNSET)
        privilege: PrivilegeResultVO | Unset
        if isinstance(_privilege, Unset):
            privilege = UNSET
        else:
            privilege = PrivilegeResultVO.from_dict(_privilege)

        viewer_parent_user_id = d.pop("viewerParentUserId", UNSET)

        parent_user_id = d.pop("parentUserId", UNSET)

        show_tree = d.pop("showTree", UNSET)

        incident_notification = d.pop("incidentNotification", UNSET)

        user_level = d.pop("userLevel", UNSET)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        temporary_validity = d.pop("temporaryValidity", UNSET)

        controller_user_app_vo = cls(
            type_=type_,
            id=id,
            role_detail=role_detail,
            role_type=role_type,
            name=name,
            email=email,
            omadac_id=omadac_id,
            verified=verified,
            alert=alert,
            privilege=privilege,
            viewer_parent_user_id=viewer_parent_user_id,
            parent_user_id=parent_user_id,
            show_tree=show_tree,
            incident_notification=incident_notification,
            user_level=user_level,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            temporary_validity=temporary_validity,
        )

        controller_user_app_vo.additional_properties = d
        return controller_user_app_vo

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
