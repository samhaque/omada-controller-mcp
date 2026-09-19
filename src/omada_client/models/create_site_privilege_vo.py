from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSitePrivilegeVO")


@_attrs_define
class CreateSitePrivilegeVO:
    """User site privileges

    Attributes:
        all_ (bool | Unset): Whether user has all site permission, including new created site.
        sites (list[str] | Unset): User site privilege list
        service_type (int | Unset): Service type should be a value as follows: 1: Omada System.
    """

    all_: bool | Unset = UNSET
    sites: list[str] | Unset = UNSET
    service_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_ = self.all_

        sites: list[str] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = self.sites

        service_type = self.service_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if all_ is not UNSET:
            field_dict["all"] = all_
        if sites is not UNSET:
            field_dict["sites"] = sites
        if service_type is not UNSET:
            field_dict["serviceType"] = service_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        all_ = d.pop("all", UNSET)

        sites = cast(list[str], d.pop("sites", UNSET))

        service_type = d.pop("serviceType", UNSET)

        create_site_privilege_vo = cls(
            all_=all_,
            sites=sites,
            service_type=service_type,
        )

        create_site_privilege_vo.additional_properties = d
        return create_site_privilege_vo

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
