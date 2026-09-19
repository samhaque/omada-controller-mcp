from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceOuiModeOpenApiVO")


@_attrs_define
class DeviceOuiModeOpenApiVO:
    """When mode is 1, should configure device info.

    Attributes:
        device_mac (str): Device MAC. E.g. AA-BB-CC-DD-11-22 . When "oldFirmwareDevice" is true, deivce should configure
            in only one OUI Based VLAN rule.
        stack_id (str | Unset): The stack id of the stack device.
        stack_port_list (list[str] | Unset): The stack port list.
        port_list (list[int] | Unset): Device port list.
        lag_list (list[int] | Unset): Device lag list.
    """

    device_mac: str
    stack_id: str | Unset = UNSET
    stack_port_list: list[str] | Unset = UNSET
    port_list: list[int] | Unset = UNSET
    lag_list: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        stack_id = self.stack_id

        stack_port_list: list[str] | Unset = UNSET
        if not isinstance(self.stack_port_list, Unset):
            stack_port_list = self.stack_port_list

        port_list: list[int] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        lag_list: list[int] | Unset = UNSET
        if not isinstance(self.lag_list, Unset):
            lag_list = self.lag_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceMac": device_mac,
            }
        )
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_port_list is not UNSET:
            field_dict["stackPortList"] = stack_port_list
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if lag_list is not UNSET:
            field_dict["lagList"] = lag_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac = d.pop("deviceMac")

        stack_id = d.pop("stackId", UNSET)

        stack_port_list = cast(list[str], d.pop("stackPortList", UNSET))

        port_list = cast(list[int], d.pop("portList", UNSET))

        lag_list = cast(list[int], d.pop("lagList", UNSET))

        device_oui_mode_open_api_vo = cls(
            device_mac=device_mac,
            stack_id=stack_id,
            stack_port_list=stack_port_list,
            port_list=port_list,
            lag_list=lag_list,
        )

        device_oui_mode_open_api_vo.additional_properties = d
        return device_oui_mode_open_api_vo

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
