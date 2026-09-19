from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoipContactPersonSettings")


@_attrs_define
class VoipContactPersonSettings:
    """
    Attributes:
        first_name (str | Unset): The firstName of contact person. It should contain 0 to 64 characters.
        last_name (str | Unset): The lastName of contact person. It should contain 0 to 64 characters.
        private_phone_number (str | Unset): The privatePhoneNumber of contact person.
        work_phone_number (str | Unset): The workPhoneNumber of contact person.
        mobile_phone_number (str | Unset): The mobilePhoneNumber of contact person.
        speed_dial_enable (bool | Unset): Whether to enable the speedDial.
        speed_dial_number_type (int | Unset): speedDialNumberType should be a value as follows: 0: Private Phone Number;
            1: Work Phone Number; 2: Mobile Phone Number.
        speed_dial_number (str | Unset): The speedDialNumber of contact person.
    """

    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    private_phone_number: str | Unset = UNSET
    work_phone_number: str | Unset = UNSET
    mobile_phone_number: str | Unset = UNSET
    speed_dial_enable: bool | Unset = UNSET
    speed_dial_number_type: int | Unset = UNSET
    speed_dial_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        private_phone_number = self.private_phone_number

        work_phone_number = self.work_phone_number

        mobile_phone_number = self.mobile_phone_number

        speed_dial_enable = self.speed_dial_enable

        speed_dial_number_type = self.speed_dial_number_type

        speed_dial_number = self.speed_dial_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if private_phone_number is not UNSET:
            field_dict["privatePhoneNumber"] = private_phone_number
        if work_phone_number is not UNSET:
            field_dict["workPhoneNumber"] = work_phone_number
        if mobile_phone_number is not UNSET:
            field_dict["mobilePhoneNumber"] = mobile_phone_number
        if speed_dial_enable is not UNSET:
            field_dict["speedDialEnable"] = speed_dial_enable
        if speed_dial_number_type is not UNSET:
            field_dict["speedDialNumberType"] = speed_dial_number_type
        if speed_dial_number is not UNSET:
            field_dict["speedDialNumber"] = speed_dial_number

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        private_phone_number = d.pop("privatePhoneNumber", UNSET)

        work_phone_number = d.pop("workPhoneNumber", UNSET)

        mobile_phone_number = d.pop("mobilePhoneNumber", UNSET)

        speed_dial_enable = d.pop("speedDialEnable", UNSET)

        speed_dial_number_type = d.pop("speedDialNumberType", UNSET)

        speed_dial_number = d.pop("speedDialNumber", UNSET)

        voip_contact_person_settings = cls(
            first_name=first_name,
            last_name=last_name,
            private_phone_number=private_phone_number,
            work_phone_number=work_phone_number,
            mobile_phone_number=mobile_phone_number,
            speed_dial_enable=speed_dial_enable,
            speed_dial_number_type=speed_dial_number_type,
            speed_dial_number=speed_dial_number,
        )

        voip_contact_person_settings.additional_properties = d
        return voip_contact_person_settings

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
