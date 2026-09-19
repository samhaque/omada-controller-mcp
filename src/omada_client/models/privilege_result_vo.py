from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.privilege_result_vo_sites_item import PrivilegeResultVOSitesItem


T = TypeVar("T", bound="PrivilegeResultVO")


@_attrs_define
class PrivilegeResultVO:
    """
    Attributes:
        sites (list[PrivilegeResultVOSitesItem] | Unset): user site privilege list
        last_visited (str | Unset): user last visited site
        last_site_category (str | Unset):
        all_ (bool | Unset): whether user has all site privilege
        site_num (int | Unset): user site num
        favorites (list[str] | Unset):
        service_type (int | Unset):
    """

    sites: list[PrivilegeResultVOSitesItem] | Unset = UNSET
    last_visited: str | Unset = UNSET
    last_site_category: str | Unset = UNSET
    all_: bool | Unset = UNSET
    site_num: int | Unset = UNSET
    favorites: list[str] | Unset = UNSET
    service_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        last_visited = self.last_visited

        last_site_category = self.last_site_category

        all_ = self.all_

        site_num = self.site_num

        favorites: list[str] | Unset = UNSET
        if not isinstance(self.favorites, Unset):
            favorites = self.favorites

        service_type = self.service_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites
        if last_visited is not UNSET:
            field_dict["last visited"] = last_visited
        if last_site_category is not UNSET:
            field_dict["lastSiteCategory"] = last_site_category
        if all_ is not UNSET:
            field_dict["all"] = all_
        if site_num is not UNSET:
            field_dict["siteNum"] = site_num
        if favorites is not UNSET:
            field_dict["favorites"] = favorites
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.privilege_result_vo_sites_item import (
            PrivilegeResultVOSitesItem,
        )

        d = dict(src_dict)
        _sites = d.pop("sites", UNSET)
        sites: list[PrivilegeResultVOSitesItem] | Unset = UNSET
        if _sites is not UNSET:
            sites = []
            for sites_item_data in _sites:
                sites_item = PrivilegeResultVOSitesItem.from_dict(sites_item_data)

                sites.append(sites_item)

        last_visited = d.pop("last visited", UNSET)

        last_site_category = d.pop("lastSiteCategory", UNSET)

        all_ = d.pop("all", UNSET)

        site_num = d.pop("siteNum", UNSET)

        favorites = cast(list[str], d.pop("favorites", UNSET))

        service_type = d.pop("serviceType", UNSET)

        privilege_result_vo = cls(
            sites=sites,
            last_visited=last_visited,
            last_site_category=last_site_category,
            all_=all_,
            site_num=site_num,
            favorites=favorites,
            service_type=service_type,
        )

        privilege_result_vo.additional_properties = d
        return privilege_result_vo

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
