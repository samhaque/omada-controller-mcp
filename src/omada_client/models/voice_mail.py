from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceMail")


@_attrs_define
class VoiceMail:
    """
    Attributes:
        id (str | Unset): Voice mail ID.
        date (int | Unset): The date or time of voice mail.
        incoming_number (str | Unset): The incoming number of voice mail.
        telephone_number (str | Unset): The telephone number of voice mail.
        duration (int | Unset): The duration of voice mail.
        read (bool | Unset): Whether the voice mail has been read, false-not read, true-read
    """

    id: str | Unset = UNSET
    date: int | Unset = UNSET
    incoming_number: str | Unset = UNSET
    telephone_number: str | Unset = UNSET
    duration: int | Unset = UNSET
    read: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        date = self.date

        incoming_number = self.incoming_number

        telephone_number = self.telephone_number

        duration = self.duration

        read = self.read

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if date is not UNSET:
            field_dict["date"] = date
        if incoming_number is not UNSET:
            field_dict["incomingNumber"] = incoming_number
        if telephone_number is not UNSET:
            field_dict["telephoneNumber"] = telephone_number
        if duration is not UNSET:
            field_dict["duration"] = duration
        if read is not UNSET:
            field_dict["read"] = read

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        date = d.pop("date", UNSET)

        incoming_number = d.pop("incomingNumber", UNSET)

        telephone_number = d.pop("telephoneNumber", UNSET)

        duration = d.pop("duration", UNSET)

        read = d.pop("read", UNSET)

        voice_mail = cls(
            id=id,
            date=date,
            incoming_number=incoming_number,
            telephone_number=telephone_number,
            duration=duration,
            read=read,
        )

        voice_mail.additional_properties = d
        return voice_mail

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
