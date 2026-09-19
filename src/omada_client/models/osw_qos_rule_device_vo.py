from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswQosRuleDeviceVO")


@_attrs_define
class OswQosRuleDeviceVO:
    """List of switch devices to which QoS rule are bound, only for bindType 1

    Attributes:
        mac (str | Unset): The device mac.
        stack_device (bool | Unset): Stack device identifier, true: stack device, false: normal device.
        port_list (list[str] | Unset): The selected standard port ID(unit/slot/port) list.
        lag_list (list[int] | Unset): The selected lag ID list.
    """

    mac: str | Unset = UNSET
    stack_device: bool | Unset = UNSET
    port_list: list[str] | Unset = UNSET
    lag_list: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        stack_device = self.stack_device

        port_list: list[str] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        lag_list: list[int] | Unset = UNSET
        if not isinstance(self.lag_list, Unset):
            lag_list = self.lag_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if stack_device is not UNSET:
            field_dict["stackDevice"] = stack_device
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if lag_list is not UNSET:
            field_dict["lagList"] = lag_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        stack_device = d.pop("stackDevice", UNSET)

        port_list = cast(list[str], d.pop("portList", UNSET))

        lag_list = cast(list[int], d.pop("lagList", UNSET))

        osw_qos_rule_device_vo = cls(
            mac=mac,
            stack_device=stack_device,
            port_list=port_list,
            lag_list=lag_list,
        )

        osw_qos_rule_device_vo.additional_properties = d
        return osw_qos_rule_device_vo

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
