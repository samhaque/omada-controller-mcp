from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRateLimitProfileOpenApiVO")


@_attrs_define
class UpdateRateLimitProfileOpenApiVO:
    """
    Attributes:
        name (str): Rate limit profile name should contain 1 to 64 characters.
        down_limit_enable (bool): Whether to enable download limit
        up_limit_enable (bool): Whether to enable upload limit
        down_limit (int | Unset): Download limit(Unit: Kbps), this field is required when parameter [downLimitEnable] is
            true.
        up_limit (int | Unset): Upload limit(Unit: Kbps), this field is required when parameter [upLimitEnable] is true.
    """

    name: str
    down_limit_enable: bool
    up_limit_enable: bool
    down_limit: int | Unset = UNSET
    up_limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        down_limit_enable = self.down_limit_enable

        up_limit_enable = self.up_limit_enable

        down_limit = self.down_limit

        up_limit = self.up_limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "downLimitEnable": down_limit_enable,
                "upLimitEnable": up_limit_enable,
            }
        )
        if down_limit is not UNSET:
            field_dict["downLimit"] = down_limit
        if up_limit is not UNSET:
            field_dict["upLimit"] = up_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        down_limit_enable = d.pop("downLimitEnable")

        up_limit_enable = d.pop("upLimitEnable")

        down_limit = d.pop("downLimit", UNSET)

        up_limit = d.pop("upLimit", UNSET)

        update_rate_limit_profile_open_api_vo = cls(
            name=name,
            down_limit_enable=down_limit_enable,
            up_limit_enable=up_limit_enable,
            down_limit=down_limit,
            up_limit=up_limit,
        )

        update_rate_limit_profile_open_api_vo.additional_properties = d
        return update_rate_limit_profile_open_api_vo

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
