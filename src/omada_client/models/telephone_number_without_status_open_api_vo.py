from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelephoneNumberWithoutStatusOpenApiVO")


@_attrs_define
class TelephoneNumberWithoutStatusOpenApiVO:
    """The list of telephone number without status.

    Attributes:
        profile_id (str): Provider profile ID used to bind phone numbers.
        number (str): The number of telephone number.
        device_mac (str): Device MAC.
        phone_number_id (str | Unset): The phoneNumber ID of telephone number.
        prefix (str | Unset): The prefix of telephone number. When the provider in the provider profile is 1&1 Internet,
            Vodafone/Arcor, QSC/Q-DSL home, or Telekom, parameter [prefix] is required. When the provider is easybell,
            parameter [prefix] value is always 0049. In other cases, parameter [prefix] value is always null.
        username (str | Unset): Username.
        password (str | Unset): Password.
    """

    profile_id: str
    number: str
    device_mac: str
    phone_number_id: str | Unset = UNSET
    prefix: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        profile_id = self.profile_id

        number = self.number

        device_mac = self.device_mac

        phone_number_id = self.phone_number_id

        prefix = self.prefix

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileId": profile_id,
                "number": number,
                "deviceMac": device_mac,
            }
        )
        if phone_number_id is not UNSET:
            field_dict["phoneNumberId"] = phone_number_id
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        profile_id = d.pop("profileId")

        number = d.pop("number")

        device_mac = d.pop("deviceMac")

        phone_number_id = d.pop("phoneNumberId", UNSET)

        prefix = d.pop("prefix", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        telephone_number_without_status_open_api_vo = cls(
            profile_id=profile_id,
            number=number,
            device_mac=device_mac,
            phone_number_id=phone_number_id,
            prefix=prefix,
            username=username,
            password=password,
        )

        telephone_number_without_status_open_api_vo.additional_properties = d
        return telephone_number_without_status_open_api_vo

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
