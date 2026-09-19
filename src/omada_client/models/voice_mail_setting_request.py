from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoiceMailSettingRequest")


@_attrs_define
class VoiceMailSettingRequest:
    """
    Attributes:
        enable (bool): Whether to enable voice mail settings.
        omadac_id (str | Unset): Omadac ID.
        site_id (str | Unset): Site ID.
        no_answer_time (int | Unset): The no answer time of telephone number. Parameter [noAnswerTime] should be from 5
            to 60
        remote_access_pin (str | Unset): Remote access pin.
        voice_mail_in_usb (bool | Unset): Whether voice mail is in USB.
        greeting_for_voice_mail_mode (int | Unset): Parameter [greetingForVoiceMailMode] should be 0 or 1. 0: Default,
            1: Custom.
        greeting_name (str | Unset): Greeting name.
        usb_uuid (str | Unset): USB UUID.
        voice_mail_capacity (int | Unset): The capacity of voice mail.
        remote_access_enable (bool | Unset): Whether voice mail allows remote access.
        duration (int | Unset): Parameter [duration] should be from 20 to 120.
    """

    enable: bool
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    no_answer_time: int | Unset = UNSET
    remote_access_pin: str | Unset = UNSET
    voice_mail_in_usb: bool | Unset = UNSET
    greeting_for_voice_mail_mode: int | Unset = UNSET
    greeting_name: str | Unset = UNSET
    usb_uuid: str | Unset = UNSET
    voice_mail_capacity: int | Unset = UNSET
    remote_access_enable: bool | Unset = UNSET
    duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        omadac_id = self.omadac_id

        site_id = self.site_id

        no_answer_time = self.no_answer_time

        remote_access_pin = self.remote_access_pin

        voice_mail_in_usb = self.voice_mail_in_usb

        greeting_for_voice_mail_mode = self.greeting_for_voice_mail_mode

        greeting_name = self.greeting_name

        usb_uuid = self.usb_uuid

        voice_mail_capacity = self.voice_mail_capacity

        remote_access_enable = self.remote_access_enable

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if no_answer_time is not UNSET:
            field_dict["noAnswerTime"] = no_answer_time
        if remote_access_pin is not UNSET:
            field_dict["remoteAccessPin"] = remote_access_pin
        if voice_mail_in_usb is not UNSET:
            field_dict["voiceMailInUsb"] = voice_mail_in_usb
        if greeting_for_voice_mail_mode is not UNSET:
            field_dict["greetingForVoiceMailMode"] = greeting_for_voice_mail_mode
        if greeting_name is not UNSET:
            field_dict["greetingName"] = greeting_name
        if usb_uuid is not UNSET:
            field_dict["usbUuid"] = usb_uuid
        if voice_mail_capacity is not UNSET:
            field_dict["voiceMailCapacity"] = voice_mail_capacity
        if remote_access_enable is not UNSET:
            field_dict["remoteAccessEnable"] = remote_access_enable
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        no_answer_time = d.pop("noAnswerTime", UNSET)

        remote_access_pin = d.pop("remoteAccessPin", UNSET)

        voice_mail_in_usb = d.pop("voiceMailInUsb", UNSET)

        greeting_for_voice_mail_mode = d.pop("greetingForVoiceMailMode", UNSET)

        greeting_name = d.pop("greetingName", UNSET)

        usb_uuid = d.pop("usbUuid", UNSET)

        voice_mail_capacity = d.pop("voiceMailCapacity", UNSET)

        remote_access_enable = d.pop("remoteAccessEnable", UNSET)

        duration = d.pop("duration", UNSET)

        voice_mail_setting_request = cls(
            enable=enable,
            omadac_id=omadac_id,
            site_id=site_id,
            no_answer_time=no_answer_time,
            remote_access_pin=remote_access_pin,
            voice_mail_in_usb=voice_mail_in_usb,
            greeting_for_voice_mail_mode=greeting_for_voice_mail_mode,
            greeting_name=greeting_name,
            usb_uuid=usb_uuid,
            voice_mail_capacity=voice_mail_capacity,
            remote_access_enable=remote_access_enable,
            duration=duration,
        )

        voice_mail_setting_request.additional_properties = d
        return voice_mail_setting_request

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
