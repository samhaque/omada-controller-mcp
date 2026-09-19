from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usb_info import UsbInfo


T = TypeVar("T", bound="VoiceMailSettingResponse")


@_attrs_define
class VoiceMailSettingResponse:
    """
    Attributes:
        omadac_id (str | Unset): Omadac ID.
        site_id (str | Unset): Site ID.
        no_answer_time (int | Unset): The no answer time of telephone number.
        remote_access_pin (str | Unset): Remote access pin.
        voice_mail_in_usb (bool | Unset): Whether voice mail is in USB.
        greeting_for_voice_mail_mode (int | Unset): Parameter [greetingForVoiceMailMode] will be 0 or 1. 0: Default, 1:
            Custom.
        default_greeting_name (str | Unset): Greeting name.
        usb_list (list[UsbInfo] | Unset): USB info list.
        enable (bool | Unset): Whether voice mail is enable.
        remote_access_enable (bool | Unset): Whether voice mail allows remote access.
        duration (int | Unset): Voice mail duration.
    """

    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    no_answer_time: int | Unset = UNSET
    remote_access_pin: str | Unset = UNSET
    voice_mail_in_usb: bool | Unset = UNSET
    greeting_for_voice_mail_mode: int | Unset = UNSET
    default_greeting_name: str | Unset = UNSET
    usb_list: list[UsbInfo] | Unset = UNSET
    enable: bool | Unset = UNSET
    remote_access_enable: bool | Unset = UNSET
    duration: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        omadac_id = self.omadac_id

        site_id = self.site_id

        no_answer_time = self.no_answer_time

        remote_access_pin = self.remote_access_pin

        voice_mail_in_usb = self.voice_mail_in_usb

        greeting_for_voice_mail_mode = self.greeting_for_voice_mail_mode

        default_greeting_name = self.default_greeting_name

        usb_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usb_list, Unset):
            usb_list = []
            for usb_list_item_data in self.usb_list:
                usb_list_item = usb_list_item_data.to_dict()
                usb_list.append(usb_list_item)

        enable = self.enable

        remote_access_enable = self.remote_access_enable

        duration = self.duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        if default_greeting_name is not UNSET:
            field_dict["defaultGreetingName"] = default_greeting_name
        if usb_list is not UNSET:
            field_dict["usbList"] = usb_list
        if enable is not UNSET:
            field_dict["enable"] = enable
        if remote_access_enable is not UNSET:
            field_dict["remoteAccessEnable"] = remote_access_enable
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usb_info import UsbInfo

        d = dict(src_dict)
        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        no_answer_time = d.pop("noAnswerTime", UNSET)

        remote_access_pin = d.pop("remoteAccessPin", UNSET)

        voice_mail_in_usb = d.pop("voiceMailInUsb", UNSET)

        greeting_for_voice_mail_mode = d.pop("greetingForVoiceMailMode", UNSET)

        default_greeting_name = d.pop("defaultGreetingName", UNSET)

        _usb_list = d.pop("usbList", UNSET)
        usb_list: list[UsbInfo] | Unset = UNSET
        if _usb_list is not UNSET:
            usb_list = []
            for usb_list_item_data in _usb_list:
                usb_list_item = UsbInfo.from_dict(usb_list_item_data)

                usb_list.append(usb_list_item)

        enable = d.pop("enable", UNSET)

        remote_access_enable = d.pop("remoteAccessEnable", UNSET)

        duration = d.pop("duration", UNSET)

        voice_mail_setting_response = cls(
            omadac_id=omadac_id,
            site_id=site_id,
            no_answer_time=no_answer_time,
            remote_access_pin=remote_access_pin,
            voice_mail_in_usb=voice_mail_in_usb,
            greeting_for_voice_mail_mode=greeting_for_voice_mail_mode,
            default_greeting_name=default_greeting_name,
            usb_list=usb_list,
            enable=enable,
            remote_access_enable=remote_access_enable,
            duration=duration,
        )

        voice_mail_setting_response.additional_properties = d
        return voice_mail_setting_response

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
