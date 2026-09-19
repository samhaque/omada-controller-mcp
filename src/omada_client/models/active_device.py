from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveDevice")


@_attrs_define
class ActiveDevice:
    """Most Active APs devices by traffic

    Attributes:
        status (int | Unset): Status should be a value as follows: 0: Connected; 1: Disconnected.
        name (str | Unset): Device name
        traffic (float | Unset): Traffic measured in GB
        mac (str | Unset): Device MAC address, linked to the device details page
        model (str | Unset): Device model, such as EAP620 HD
        model_version (str | Unset): Model version, such as 3.0
    """

    status: int | Unset = UNSET
    name: str | Unset = UNSET
    traffic: float | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        name = self.name

        traffic = self.traffic

        mac = self.mac

        model = self.model

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        name = d.pop("name", UNSET)

        traffic = d.pop("traffic", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        active_device = cls(
            status=status,
            name=name,
            traffic=traffic,
            mac=mac,
            model=model,
            model_version=model_version,
        )

        active_device.additional_properties = d
        return active_device

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
