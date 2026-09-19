from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.call_log_device_open_api_vo import CallLogDeviceOpenApiVO


T = TypeVar("T", bound="VoipCallLog")


@_attrs_define
class VoipCallLog:
    """
    Attributes:
        entry_id (str | Unset): The entry ID of callLog.
        date_time (int | Unset): The dateTime of callLog.
        status (int | Unset): The status of callLog.
        duration (int | Unset): The duration of callLog.
        number_or_contact (str | Unset): The number or contact person of callLog.
        device_number (str | Unset): The deviceNumber of callLog.
        port (int | Unset): FXS port id of this call log.
        telephony_device (CallLogDeviceOpenApiVO | Unset): The telephonyDevice description of callLog.
    """

    entry_id: str | Unset = UNSET
    date_time: int | Unset = UNSET
    status: int | Unset = UNSET
    duration: int | Unset = UNSET
    number_or_contact: str | Unset = UNSET
    device_number: str | Unset = UNSET
    port: int | Unset = UNSET
    telephony_device: CallLogDeviceOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry_id = self.entry_id

        date_time = self.date_time

        status = self.status

        duration = self.duration

        number_or_contact = self.number_or_contact

        device_number = self.device_number

        port = self.port

        telephony_device: dict[str, Any] | Unset = UNSET
        if not isinstance(self.telephony_device, Unset):
            telephony_device = self.telephony_device.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry_id is not UNSET:
            field_dict["entryId"] = entry_id
        if date_time is not UNSET:
            field_dict["dateTime"] = date_time
        if status is not UNSET:
            field_dict["status"] = status
        if duration is not UNSET:
            field_dict["duration"] = duration
        if number_or_contact is not UNSET:
            field_dict["numberOrContact"] = number_or_contact
        if device_number is not UNSET:
            field_dict["deviceNumber"] = device_number
        if port is not UNSET:
            field_dict["port"] = port
        if telephony_device is not UNSET:
            field_dict["telephonyDevice"] = telephony_device

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.call_log_device_open_api_vo import (
            CallLogDeviceOpenApiVO,
        )

        d = dict(src_dict)
        entry_id = d.pop("entryId", UNSET)

        date_time = d.pop("dateTime", UNSET)

        status = d.pop("status", UNSET)

        duration = d.pop("duration", UNSET)

        number_or_contact = d.pop("numberOrContact", UNSET)

        device_number = d.pop("deviceNumber", UNSET)

        port = d.pop("port", UNSET)

        _telephony_device = d.pop("telephonyDevice", UNSET)
        telephony_device: CallLogDeviceOpenApiVO | Unset
        if isinstance(_telephony_device, Unset):
            telephony_device = UNSET
        else:
            telephony_device = CallLogDeviceOpenApiVO.from_dict(_telephony_device)

        voip_call_log = cls(
            entry_id=entry_id,
            date_time=date_time,
            status=status,
            duration=duration,
            number_or_contact=number_or_contact,
            device_number=device_number,
            port=port,
            telephony_device=telephony_device,
        )

        voip_call_log.additional_properties = d
        return voip_call_log

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
