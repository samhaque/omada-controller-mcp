from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QosRuleDeviceInfo")


@_attrs_define
class QosRuleDeviceInfo:
    """List of device information for which QoS rules have been successfully issued.

    Attributes:
        mac (str | Unset): The device mac.
        name (str | Unset): The device name.
        status_category (int | Unset): Device status should be a value as follows: 0: Disconnected; 1: Connected; 2:
            Pending; 3: Heartbeat Missed; 4: Isolated
        model (str | Unset): The device model.
        model_version (str | Unset): The model version of device, for example:3.0
        show_model (str | Unset): The device showModel(model + modelVersion).
        stack_device (bool | Unset): Stack device identifier, true: stack device, false: normal device.
        err_code (int | Unset): The code of the device's response after the QoS rules are issued.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    status_category: int | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    stack_device: bool | Unset = UNSET
    err_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        status_category = self.status_category

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        stack_device = self.stack_device

        err_code = self.err_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if stack_device is not UNSET:
            field_dict["stackDevice"] = stack_device
        if err_code is not UNSET:
            field_dict["errCode"] = err_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        stack_device = d.pop("stackDevice", UNSET)

        err_code = d.pop("errCode", UNSET)

        qos_rule_device_info = cls(
            mac=mac,
            name=name,
            status_category=status_category,
            model=model,
            model_version=model_version,
            show_model=show_model,
            stack_device=stack_device,
            err_code=err_code,
        )

        qos_rule_device_info.additional_properties = d
        return qos_rule_device_info

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
