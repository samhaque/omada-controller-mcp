from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceReplaceSettingVO")


@_attrs_define
class DeviceReplaceSettingVO:
    """
    Attributes:
        destination_device_key (str): Device Key of the device.
        username (str | Unset): User Name.
        password (str | Unset): password.
    """

    destination_device_key: str
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        destination_device_key = self.destination_device_key

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "destinationDeviceKey": destination_device_key,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        destination_device_key = d.pop("destinationDeviceKey")

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        device_replace_setting_vo = cls(
            destination_device_key=destination_device_key,
            username=username,
            password=password,
        )

        device_replace_setting_vo.additional_properties = d
        return device_replace_setting_vo

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
