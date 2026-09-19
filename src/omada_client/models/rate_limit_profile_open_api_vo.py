from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitProfileOpenApiVO")


@_attrs_define
class RateLimitProfileOpenApiVO:
    """
    Attributes:
        profile_id (str | Unset): Rate limit profile ID
        name (str | Unset): Rate limit profile name
        down_limit_enable (bool | Unset): Whether to enable download limit
        down_limit (int | Unset): Download limit(Unit: Kbps), this field is required when parameter [downLimitEnable] is
            true.
        up_limit_enable (bool | Unset): Whether to enable upload limit
        up_limit (int | Unset): Upload limit(Unit: Kbps), this field is required when parameter [upLimitEnable] is true.
        default_profile (bool | Unset): Whether it is default profile.
        resource (int | Unset): Data source. Resource should be a value as follows: 0: new created; 1: from template; 2:
            override
    """

    profile_id: str | Unset = UNSET
    name: str | Unset = UNSET
    down_limit_enable: bool | Unset = UNSET
    down_limit: int | Unset = UNSET
    up_limit_enable: bool | Unset = UNSET
    up_limit: int | Unset = UNSET
    default_profile: bool | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        name = self.name

        down_limit_enable = self.down_limit_enable

        down_limit = self.down_limit

        up_limit_enable = self.up_limit_enable

        up_limit = self.up_limit

        default_profile = self.default_profile

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if name is not UNSET:
            field_dict["name"] = name
        if down_limit_enable is not UNSET:
            field_dict["downLimitEnable"] = down_limit_enable
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if up_limit_enable is not UNSET:
            field_dict["upLimitEnable"] = up_limit_enable
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit
        if default_profile is not UNSET:
            field_dict["defaultProfile"] = default_profile
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_id = d.pop("profileId", UNSET)

        name = d.pop("name", UNSET)

        down_limit_enable = d.pop("downLimitEnable", UNSET)

        down_limit = d.pop("downLimit", UNSET)

        up_limit_enable = d.pop("upLimitEnable", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        default_profile = d.pop("defaultProfile", UNSET)

        resource = d.pop("resource", UNSET)

        rate_limit_profile_open_api_vo = cls(
            profile_id=profile_id,
            name=name,
            down_limit_enable=down_limit_enable,
            down_limit=down_limit,
            up_limit_enable=up_limit_enable,
            up_limit=up_limit,
            default_profile=default_profile,
            resource=resource,
        )

        rate_limit_profile_open_api_vo.additional_properties = d
        return rate_limit_profile_open_api_vo

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
