from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelephoneNumberWithStatusOpenApiVO")


@_attrs_define
class TelephoneNumberWithStatusOpenApiVO:
    """
    Attributes:
        phone_number_id (str | Unset): The phoneNumber ID of telephone number.
        profile_id (str | Unset): The profile ID of telephone number.
        profile_name (str | Unset): The profile name of telephone number.
        prefix (str | Unset): The prefix of telephone number.
        number (str | Unset): The telephone number.
        status (int | Unset): The status of telephone number.
        device_mac (str | Unset): Device MAC.
        username (str | Unset): Username.
        password (str | Unset): Password.
    """

    phone_number_id: str | Unset = UNSET
    profile_id: str | Unset = UNSET
    profile_name: str | Unset = UNSET
    prefix: str | Unset = UNSET
    number: str | Unset = UNSET
    status: int | Unset = UNSET
    device_mac: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone_number_id = self.phone_number_id

        profile_id = self.profile_id

        profile_name = self.profile_name

        prefix = self.prefix

        number = self.number

        status = self.status

        device_mac = self.device_mac

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone_number_id is not UNSET:
            field_dict["phoneNumberId"] = phone_number_id
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if number is not UNSET:
            field_dict["number"] = number
        if status is not UNSET:
            field_dict["status"] = status
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        phone_number_id = d.pop("phoneNumberId", UNSET)

        profile_id = d.pop("profileId", UNSET)

        profile_name = d.pop("profileName", UNSET)

        prefix = d.pop("prefix", UNSET)

        number = d.pop("number", UNSET)

        status = d.pop("status", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        telephone_number_with_status_open_api_vo = cls(
            phone_number_id=phone_number_id,
            profile_id=profile_id,
            profile_name=profile_name,
            prefix=prefix,
            number=number,
            status=status,
            device_mac=device_mac,
            username=username,
            password=password,
        )

        telephone_number_with_status_open_api_vo.additional_properties = d
        return telephone_number_with_status_open_api_vo

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
