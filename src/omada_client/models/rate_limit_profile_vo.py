from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitProfileVO")


@_attrs_define
class RateLimitProfileVO:
    """
    Attributes:
        name (str): Rate limit profile name.
        down_limit_enable (bool): Down limit enable.
        up_limit_enable (bool): Up limit enable.
        id (str | Unset): Rate limit profile id.
        site (str | Unset): Site ID
        down_limit (int | Unset): Down limit. Unit is Kbps, integer from 1 to 10485760.
        up_limit (int | Unset): Up limit. Unit is Kbps, integer from 1 to 10485760.
        is_default (bool | Unset): Whether it is default profile.
        resource (int | Unset):
    """

    name: str
    down_limit_enable: bool
    up_limit_enable: bool
    id: str | Unset = UNSET
    site: str | Unset = UNSET
    down_limit: int | Unset = UNSET
    up_limit: int | Unset = UNSET
    is_default: bool | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        down_limit_enable = self.down_limit_enable

        up_limit_enable = self.up_limit_enable

        id = self.id

        site = self.site

        down_limit = self.down_limit

        up_limit = self.up_limit

        is_default = self.is_default

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "downLimitEnable": down_limit_enable,
                "upLimitEnable": up_limit_enable,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if site is not UNSET:
            field_dict["site"] = site
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        down_limit_enable = d.pop("downLimitEnable")

        up_limit_enable = d.pop("upLimitEnable")

        id = d.pop("id", UNSET)

        site = d.pop("site", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        is_default = d.pop("isDefault", UNSET)

        resource = d.pop("resource", UNSET)

        rate_limit_profile_vo = cls(
            name=name,
            down_limit_enable=down_limit_enable,
            up_limit_enable=up_limit_enable,
            id=id,
            site=site,
            down_limit=down_limit,
            up_limit=up_limit,
            is_default=is_default,
            resource=resource,
        )

        rate_limit_profile_vo.additional_properties = d
        return rate_limit_profile_vo

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
