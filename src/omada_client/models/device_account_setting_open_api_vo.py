from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeviceAccountSettingOpenApiVO")


@_attrs_define
class DeviceAccountSettingOpenApiVO:
    """
    Attributes:
        username (str): Device account username should contain 1 to 64 ASCII characters.
        password (str): Device account parameter [password] should contain 10 to 64 ASCII characters. And passwords must
            be a combination of uppercase letters, lowercase letters, numbers, and special symbols. Symbols such as ! # $ %
            & * @ ^ are supported.
            The password should not contain consecutive identical characters.
            Username and Password should not be the same.
    """

    username: str
    password: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        username = d.pop("username")

        password = d.pop("password")

        device_account_setting_open_api_vo = cls(
            username=username,
            password=password,
        )

        device_account_setting_open_api_vo.additional_properties = d
        return device_account_setting_open_api_vo

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
