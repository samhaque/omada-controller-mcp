from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="NoAuthSetting")


@_attrs_define
class NoAuthSetting:
    """No Auth Portal Setting.

    Attributes:
        daily_limit_enable (bool): If enabled, authentication can only be performed once a day.
    """

    daily_limit_enable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        daily_limit_enable = self.daily_limit_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dailyLimitEnable": daily_limit_enable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        daily_limit_enable = d.pop("dailyLimitEnable")

        no_auth_setting = cls(
            daily_limit_enable=daily_limit_enable,
        )

        no_auth_setting.additional_properties = d
        return no_auth_setting

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
