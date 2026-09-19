from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnKnownMulticastExceptDeviceVO")


@_attrs_define
class UnKnownMulticastExceptDeviceVO:
    """unknown multicast except device list

    Attributes:
        stack_id (str | Unset): Stack Id
        stack_name (str | Unset): Stack name
        mac (str | Unset): Device mac
        device_name (str | Unset): Device name,default value is the mac address of device
        device_type (str | Unset): Device type:ap、gateway、switch、olt
        device_model (str | Unset): Model of device,for example:EAP225
        device_model_version (str | Unset): Model version of device,for example:3.0
        type_ (int | Unset): UnknownMulticastRule type
    """

    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    device_model: str | Unset = UNSET
    device_model_version: str | Unset = UNSET
    type_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_id = self.stack_id

        stack_name = self.stack_name

        mac = self.mac

        device_name = self.device_name

        device_type = self.device_type

        device_model = self.device_model

        device_model_version = self.device_model_version

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if device_model_version is not UNSET:
            field_dict["deviceModelVersion"] = device_model_version
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        mac = d.pop("mac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        device_model_version = d.pop("deviceModelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        un_known_multicast_except_device_vo = cls(
            stack_id=stack_id,
            stack_name=stack_name,
            mac=mac,
            device_name=device_name,
            device_type=device_type,
            device_model=device_model,
            device_model_version=device_model_version,
            type_=type_,
        )

        un_known_multicast_except_device_vo.additional_properties = d
        return un_known_multicast_except_device_vo

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
