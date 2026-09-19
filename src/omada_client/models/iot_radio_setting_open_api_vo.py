from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IotRadioSettingOpenApiVO")


@_attrs_define
class IotRadioSettingOpenApiVO:
    """
    Attributes:
        enable (bool): Bluetooth enable.
        console_mode (int | Unset): Bluetooth consle mode should be a value as follow:[0:auto, 1:on, 2:off].
        passcode (str | Unset): Bluetooth consle passcode.
        transmit_power (int | Unset): Broadcast transmission power.<br />The parameter [transmitPower] should be a value
            as follows:[-20, -18, -15, -12, -10, -9, -6, -5, -3, 0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 20].(0 by
            default)
        aging_time (int | Unset): The system automatically removes a device's registry entry if no data reports are
            received within a predefined aging period.<br/>When format = 0, The parameter aging time should be within the
            range of 30-86400.<br/>When format = 1, The parameter aging time should be within the range of 1-1440.<br/>When
            format = 2, The parameter aging time should be within the range of 1-24.<br/>
        format_ (int | Unset): The parameter [format] should be a value as follows: [0:second 1:minute; 2:hour]
        resource (int | Unset):
    """

    enable: bool
    console_mode: int | Unset = UNSET
    passcode: str | Unset = UNSET
    transmit_power: int | Unset = UNSET
    aging_time: int | Unset = UNSET
    format_: int | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        console_mode = self.console_mode

        passcode = self.passcode

        transmit_power = self.transmit_power

        aging_time = self.aging_time

        format_ = self.format_

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if console_mode is not UNSET:
            field_dict["consoleMode"] = console_mode
        if passcode is not UNSET:
            field_dict["passcode"] = passcode
        if transmit_power is not UNSET:
            field_dict["transmitPower"] = transmit_power
        if aging_time is not UNSET:
            field_dict["agingTime"] = aging_time
        if format_ is not UNSET:
            field_dict["format"] = format_
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        console_mode = d.pop("consoleMode", UNSET)

        passcode = d.pop("passcode", UNSET)

        transmit_power = d.pop("transmitPower", UNSET)

        aging_time = d.pop("agingTime", UNSET)

        format_ = d.pop("format", UNSET)

        resource = d.pop("resource", UNSET)

        iot_radio_setting_open_api_vo = cls(
            enable=enable,
            console_mode=console_mode,
            passcode=passcode,
            transmit_power=transmit_power,
            aging_time=aging_time,
            format_=format_,
            resource=resource,
        )

        iot_radio_setting_open_api_vo.additional_properties = d
        return iot_radio_setting_open_api_vo

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
