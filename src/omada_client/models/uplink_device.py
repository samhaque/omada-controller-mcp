from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UplinkDevice")


@_attrs_define
class UplinkDevice:
    """The device uplinkDevice

    Attributes:
        mac (str | Unset): The device UplinkDevice mac
        uplink_port (str | Unset): The device UplinkDevice port
        name (str | Unset): The device UplinkDevice name
        device_type (int | Unset): The device UplinkDevice deviceType
        type_ (str | Unset): The device UplinkDevice type.Such as: ap, switch, gateway
        uplink_type (int | Unset): The device link type
        show_model (str | Unset): The device UplinkDevice showModel
        model (str | Unset): The device UplinkDevice model
        model_version (str | Unset): The device UplinkDevice modelVersion
        standard_port (str | Unset): The device Uplink Device standardPort
        port (str | Unset): The device Uplink Device port number
        unit (int | Unset): The device Uplink StackDevice unit
        stack_id (str | Unset): The device Uplink StackDevice StackId
        stack_name (str | Unset): The device Uplink StackDevice StackName
        is_stack (bool | Unset): Whether The device Uplink StackDevice is Stack or not
    """

    mac: str | Unset = UNSET
    uplink_port: str | Unset = UNSET
    name: str | Unset = UNSET
    device_type: int | Unset = UNSET
    type_: str | Unset = UNSET
    uplink_type: int | Unset = UNSET
    show_model: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    standard_port: str | Unset = UNSET
    port: str | Unset = UNSET
    unit: int | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    is_stack: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        uplink_port = self.uplink_port

        name = self.name

        device_type = self.device_type

        type_ = self.type_

        uplink_type = self.uplink_type

        show_model = self.show_model

        model = self.model

        model_version = self.model_version

        standard_port = self.standard_port

        port = self.port

        unit = self.unit

        stack_id = self.stack_id

        stack_name = self.stack_name

        is_stack = self.is_stack

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if uplink_port is not UNSET:
            field_dict["uplinkPort"] = uplink_port
        if name is not UNSET:
            field_dict["name"] = name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uplink_type is not UNSET:
            field_dict["uplinkType"] = uplink_type
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if port is not UNSET:
            field_dict["port"] = port
        if unit is not UNSET:
            field_dict["unit"] = unit
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if is_stack is not UNSET:
            field_dict["isStack"] = is_stack

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        uplink_port = d.pop("uplinkPort", UNSET)

        name = d.pop("name", UNSET)

        device_type = d.pop("deviceType", UNSET)

        type_ = d.pop("type", UNSET)

        uplink_type = d.pop("uplinkType", UNSET)

        show_model = d.pop("showModel", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        port = d.pop("port", UNSET)

        unit = d.pop("unit", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        is_stack = d.pop("isStack", UNSET)

        uplink_device = cls(
            mac=mac,
            uplink_port=uplink_port,
            name=name,
            device_type=device_type,
            type_=type_,
            uplink_type=uplink_type,
            show_model=show_model,
            model=model,
            model_version=model_version,
            standard_port=standard_port,
            port=port,
            unit=unit,
            stack_id=stack_id,
            stack_name=stack_name,
            is_stack=is_stack,
        )

        uplink_device.additional_properties = d
        return uplink_device

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
