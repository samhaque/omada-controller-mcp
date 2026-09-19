from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_site_privilege_vo import CreateSitePrivilegeVO


T = TypeVar("T", bound="ModifyUserVO")


@_attrs_define
class ModifyUserVO:
    """
    Attributes:
        role_id (str): This field represents Role ID. Role can be created using 'Create new role' interface, and Role ID
            can be obtained from 'Get role list' interface.
        name (str): User name should contain 1 to 128 characters and start with letters, numbers, and underscores. When
            creating cloud user, you should set TP-LINK ID.
        all_site (bool): Whether user has all site permission, including new created site.
        password (str | Unset): Password of local user should contain 8 to 128 characters. And password must be a
            combination of uppercase letters, lowercase letters, numbers, and special symbols. Symbols such as ! # $ % & * @
            ^ are supported.
        email (str | Unset): Email of user
        alert (bool | Unset): Whether this user wants to receive alert, event, and incident emails. Make sure your email
            is not null.
        force_modify (bool | Unset): Force modify
        incident_notification (bool | Unset): Incident notification, this field is deprecated, please use alert field
            instead.
        sites (list[str] | Unset): User site privilege list
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permission
        start_time (int | Unset): The start time of the user's validity period. time range: start timestamp
            (Millisecond).
        end_time (int | Unset): The end time of the user's validity period. time range: end timestamp (Millisecond).
        site_privileges (list[CreateSitePrivilegeVO] | Unset): User site privileges
    """

    role_id: str
    name: str
    all_site: bool
    password: str | Unset = UNSET
    email: str | Unset = UNSET
    alert: bool | Unset = UNSET
    force_modify: bool | Unset = UNSET
    incident_notification: bool | Unset = UNSET
    sites: list[str] | Unset = UNSET
    temporary_enable: bool | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    site_privileges: list[CreateSitePrivilegeVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role_id = self.role_id

        name = self.name

        all_site = self.all_site

        password = self.password

        email = self.email

        alert = self.alert

        force_modify = self.force_modify

        incident_notification = self.incident_notification

        sites: list[str] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        temporary_enable = self.temporary_enable

        start_time = self.start_time

        end_time = self.end_time

        site_privileges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.site_privileges, Unset):
            site_privileges = []
            for site_privileges_item_data in self.site_privileges:
                site_privileges_item = site_privileges_item_data.to_dict()
                site_privileges.append(site_privileges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "roleId": role_id,
                "name": name,
                "allSite": all_site,
            }
        )
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if alert is not UNSET:
            field_dict["alert"] = alert
        if force_modify is not UNSET:
            field_dict["forceModify"] = force_modify
        if incident_notification is not UNSET:
            field_dict["incidentNotification"] = incident_notification
        if sites is not UNSET:
            field_dict["sites"] = sites
        if temporary_enable is not UNSET:
            field_dict["temporaryEnable"] = temporary_enable
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if site_privileges is not UNSET:
            field_dict["sitePrivileges"] = site_privileges

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.create_site_privilege_vo import (
            CreateSitePrivilegeVO,
        )

        d = dict(src_dict)
        role_id = d.pop("roleId")

        name = d.pop("name")

        all_site = d.pop("allSite")

        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        alert = d.pop("alert", UNSET)

        force_modify = d.pop("forceModify", UNSET)

        incident_notification = d.pop("incidentNotification", UNSET)

        sites = cast(list[str], d.pop("sites", UNSET))

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        _site_privileges = d.pop("sitePrivileges", UNSET)
        site_privileges: list[CreateSitePrivilegeVO] | Unset = UNSET
        if _site_privileges is not UNSET:
            site_privileges = []
            for site_privileges_item_data in _site_privileges:
                site_privileges_item = CreateSitePrivilegeVO.from_dict(
                    site_privileges_item_data
                )

                site_privileges.append(site_privileges_item)

        modify_user_vo = cls(
            role_id=role_id,
            name=name,
            all_site=all_site,
            password=password,
            email=email,
            alert=alert,
            force_modify=force_modify,
            incident_notification=incident_notification,
            sites=sites,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            site_privileges=site_privileges,
        )

        modify_user_vo.additional_properties = d
        return modify_user_vo

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
