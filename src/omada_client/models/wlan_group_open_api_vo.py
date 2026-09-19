from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WlanGroupOpenApiVO")


@_attrs_define
class WlanGroupOpenApiVO:
    """
    Attributes:
        wlan_id (str | Unset): WLAN group ID, kept for backward compatibility and equivalent to id. This field will be
            removed in a future release; use id instead.
        id (str | Unset): WLAN group ID
        name (str | Unset): WLAN group name should contain 1 to 128 characters.
        primary (bool | Unset): Whether it is the default WLAN group
        clone (bool | Unset): Whether it is cloned
        clone_wlan_id (str | Unset): cloneWlanId
        site (str | Unset): site Id
        resource (int | Unset): resource. 0 is new created, 1 is from template, 2 is override template.
    """

    wlan_id: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    primary: bool | Unset = UNSET
    clone: bool | Unset = UNSET
    clone_wlan_id: str | Unset = UNSET
    site: str | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wlan_id = self.wlan_id

        id = self.id

        name = self.name

        primary = self.primary

        clone = self.clone

        clone_wlan_id = self.clone_wlan_id

        site = self.site

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wlan_id is not UNSET:
            field_dict["wlanId"] = wlan_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if primary is not UNSET:
            field_dict["primary"] = primary
        if clone is not UNSET:
            field_dict["clone"] = clone
        if clone_wlan_id is not UNSET:
            field_dict["cloneWlanId"] = clone_wlan_id
        if site is not UNSET:
            field_dict["site"] = site
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wlan_id = d.pop("wlanId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        primary = d.pop("primary", UNSET)

        clone = d.pop("clone", UNSET)

        clone_wlan_id = d.pop("cloneWlanId", UNSET)

        site = d.pop("site", UNSET)

        resource = d.pop("resource", UNSET)

        wlan_group_open_api_vo = cls(
            wlan_id=wlan_id,
            id=id,
            name=name,
            primary=primary,
            clone=clone,
            clone_wlan_id=clone_wlan_id,
            site=site,
            resource=resource,
        )

        wlan_group_open_api_vo.additional_properties = d
        return wlan_group_open_api_vo

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
