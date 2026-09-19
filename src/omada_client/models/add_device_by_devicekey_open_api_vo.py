from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddDeviceByDevicekeyOpenApiVO")


@_attrs_define
class AddDeviceByDevicekeyOpenApiVO:
    """add devices list

    Attributes:
        device_key (str | Unset): device key(QR code)
        name (str | Unset): device name(Parameter [name] should be 1 ~ 128 characters)
        username (str | Unset): device username
        password (str | Unset): device password
    """

    device_key: str | Unset = UNSET
    name: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_key = self.device_key

        name = self.name

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_key is not UNSET:
            field_dict["deviceKey"] = device_key
        if name is not UNSET:
            field_dict["name"] = name
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_key = d.pop("deviceKey", UNSET)

        name = d.pop("name", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        add_device_by_devicekey_open_api_vo = cls(
            device_key=device_key,
            name=name,
            username=username,
            password=password,
        )

        add_device_by_devicekey_open_api_vo.additional_properties = d
        return add_device_by_devicekey_open_api_vo

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
