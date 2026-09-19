from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UsbInfo")


@_attrs_define
class UsbInfo:
    """USB info list.

    Attributes:
        usb_uuid (str | Unset): USB UUID.
        usb_name (str | Unset): USB name.
        voice_mailbox_capacity (int | Unset): The capacity of voice mail box.
        remain_available_capacity (int | Unset): Remain available capacity of voice mail box.
        selected (bool | Unset): Whether selected the USB device.
        custom_greeting_name (str | Unset): Custom greeting name.
    """

    usb_uuid: str | Unset = UNSET
    usb_name: str | Unset = UNSET
    voice_mailbox_capacity: int | Unset = UNSET
    remain_available_capacity: int | Unset = UNSET
    selected: bool | Unset = UNSET
    custom_greeting_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        usb_uuid = self.usb_uuid

        usb_name = self.usb_name

        voice_mailbox_capacity = self.voice_mailbox_capacity

        remain_available_capacity = self.remain_available_capacity

        selected = self.selected

        custom_greeting_name = self.custom_greeting_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if usb_uuid is not UNSET:
            field_dict["usbUuid"] = usb_uuid
        if usb_name is not UNSET:
            field_dict["usbName"] = usb_name
        if voice_mailbox_capacity is not UNSET:
            field_dict["voiceMailboxCapacity"] = voice_mailbox_capacity
        if remain_available_capacity is not UNSET:
            field_dict["remainAvailableCapacity"] = remain_available_capacity
        if selected is not UNSET:
            field_dict["selected"] = selected
        if custom_greeting_name is not UNSET:
            field_dict["customGreetingName"] = custom_greeting_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        usb_uuid = d.pop("usbUuid", UNSET)

        usb_name = d.pop("usbName", UNSET)

        voice_mailbox_capacity = d.pop("voiceMailboxCapacity", UNSET)

        remain_available_capacity = d.pop("remainAvailableCapacity", UNSET)

        selected = d.pop("selected", UNSET)

        custom_greeting_name = d.pop("customGreetingName", UNSET)

        usb_info = cls(
            usb_uuid=usb_uuid,
            usb_name=usb_name,
            voice_mailbox_capacity=voice_mailbox_capacity,
            remain_available_capacity=remain_available_capacity,
            selected=selected,
            custom_greeting_name=custom_greeting_name,
        )

        usb_info.additional_properties = d
        return usb_info

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
