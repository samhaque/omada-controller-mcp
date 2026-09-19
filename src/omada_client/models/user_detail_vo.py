from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserDetailVO")


@_attrs_define
class UserDetailVO:
    """
    Attributes:
        id (str | Unset): User ID
        type_ (int | Unset): Type of user, type should be a value as follows: 0:local user; 1: cloud user
        role_id (str | Unset): User role ID
        role_name (str | Unset): User bind role name
        name (str | Unset): User name
        email (str | Unset): User email
        omadac_id (str | Unset): Omada ID
        verified (bool | Unset): Whether this cloud user has verified
        show_tree (bool | Unset): Whether this user has Sub-users.
        alert (bool | Unset): Whether this user wants to receive alert, event, and incident emails. Make sure your email
            is not null.
        all_site (bool | Unset): Whether user has all site permission, including new created site
        site_ids (list[str] | Unset): User site privilege list
        parent_user_id (str | Unset): User's parent user id
        favorites (list[str] | Unset): User favorite site list
        incident_notification (bool | Unset): Incident notification, this field is deprecated, please use alert field
            instead.
        user_level (int | Unset): User level, user level should be a value as follows: 0:standard user; 1:customer user;
            2:msp user
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
    omadac_id: str | Unset = UNSET
    verified: bool | Unset = UNSET
    show_tree: bool | Unset = UNSET
    alert: bool | Unset = UNSET
    all_site: bool | Unset = UNSET
    site_ids: list[str] | Unset = UNSET
    parent_user_id: str | Unset = UNSET
    favorites: list[str] | Unset = UNSET
    incident_notification: bool | Unset = UNSET
    user_level: int | Unset = UNSET
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

        omadac_id = self.omadac_id

        verified = self.verified

        show_tree = self.show_tree

        alert = self.alert

        all_site = self.all_site

        site_ids: list[str] | Unset = UNSET
        if not isinstance(self.site_ids, Unset):
            site_ids = self.site_ids

        parent_user_id = self.parent_user_id

        favorites: list[str] | Unset = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        incident_notification = self.incident_notification

        user_level = self.user_level

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
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if verified is not UNSET:
            field_dict["verified"] = verified
        if show_tree is not UNSET:
            field_dict["showTree"] = show_tree
        if alert is not UNSET:
            field_dict["alert"] = alert
        if all_site is not UNSET:
            field_dict["allSite"] = all_site
        if site_ids is not UNSET:
            field_dict["siteIds"] = site_ids
        if parent_user_id is not UNSET:
            field_dict["parentUserId"] = parent_user_id
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
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
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        verified = d.pop("verified", UNSET)

        show_tree = d.pop("showTree", UNSET)

        alert = d.pop("alert", UNSET)

        all_site = d.pop("allSite", UNSET)

        site_ids = cast(list[str], d.pop("siteIds", UNSET))

        parent_user_id = d.pop("parentUserId", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        incident_notification = d.pop("incidentNotification", UNSET)

        user_level = d.pop("userLevel", UNSET)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        temporary_validity = d.pop("temporaryValidity", UNSET)

        user_detail_vo = cls(
            id=id,
            type_=type_,
            role_id=role_id,
            role_name=role_name,
            name=name,
            email=email,
            omadac_id=omadac_id,
            verified=verified,
            show_tree=show_tree,
            alert=alert,
            all_site=all_site,
            site_ids=site_ids,
            parent_user_id=parent_user_id,
            favorites=favorites,
            incident_notification=incident_notification,
            user_level=user_level,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            temporary_validity=temporary_validity,
        )

        user_detail_vo.additional_properties = d
        return user_detail_vo

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
