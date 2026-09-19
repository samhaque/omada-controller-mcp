from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_info_open_api_vo import SiteInfoOpenApiVO


T = TypeVar("T", bound="ExternalUserGroupDetailOpenApiVO")


@_attrs_define
class ExternalUserGroupDetailOpenApiVO:
    """
    Attributes:
        id (str | Unset): External user group ID.
        name (str | Unset): External user group name.
        role_id (str | Unset): Role ID.
        role_name (str | Unset): Role name.
        role_type (int | Unset): Role type. It should be a value as follows: 0: standard, 1: customer, 2: msp.
        all_site (bool | Unset): Whether having all site permissions.
        sites (list[SiteInfoOpenApiVO] | Unset): The sites which can be accessed.
        temporary_enable (bool | Unset): Whether the user wants to enable the temporary worker permissione
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
    all_site: bool | Unset = UNSET
    sites: list[SiteInfoOpenApiVO] | Unset = UNSET
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

        all_site = self.all_site

        sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

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
        if all_site is not UNSET:
            field_dict["allSite"] = all_site
        if sites is not UNSET:
            field_dict["sites"] = sites
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
        from ..models.site_info_open_api_vo import SiteInfoOpenApiVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        role_id = d.pop("roleId", UNSET)

        role_name = d.pop("roleName", UNSET)

        role_type = d.pop("roleType", UNSET)

        all_site = d.pop("allSite", UNSET)

        _sites = d.pop("sites", UNSET)
        sites: list[SiteInfoOpenApiVO] | Unset = UNSET
        if _sites is not UNSET:
            sites = []
            for sites_item_data in _sites:
                sites_item = SiteInfoOpenApiVO.from_dict(sites_item_data)

                sites.append(sites_item)

        temporary_enable = d.pop("temporaryEnable", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        temporary_validity = d.pop("temporaryValidity", UNSET)

        external_user_group_detail_open_api_vo = cls(
            id=id,
            name=name,
            role_id=role_id,
            role_name=role_name,
            role_type=role_type,
            all_site=all_site,
            sites=sites,
            temporary_enable=temporary_enable,
            start_time=start_time,
            end_time=end_time,
            temporary_validity=temporary_validity,
        )

        external_user_group_detail_open_api_vo.additional_properties = d
        return external_user_group_detail_open_api_vo

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
