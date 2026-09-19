from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceBriefVO")


@_attrs_define
class DeviceBriefVO:
    """The upper device of the port

    Attributes:
        name (str | Unset): Name
        mac (str | Unset): Mac
        model (str | Unset): Model
        model_version (str | Unset): Model version
        type_ (str | Unset): Type
        status_category (int | Unset): Device status category, 0: Disconnected, 1: Connected, 2: Pending,3: Heartbeat
            Missed, 4: Isolated
        ip (str | Unset): IP
        is_client (bool | Unset): It indicates whether the device is client.
        device_type (str | Unset): Only valid when the device is client. It indicates the device type.
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    status_category: int | Unset = UNSET
    ip: str | Unset = UNSET
    is_client: bool | Unset = UNSET
    device_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        status_category = self.status_category

        ip = self.ip

        is_client = self.is_client

        device_type = self.device_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if ip is not UNSET:
            field_dict["ip"] = ip
        if is_client is not UNSET:
            field_dict["isClient"] = is_client
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        ip = d.pop("ip", UNSET)

        is_client = d.pop("isClient", UNSET)

        device_type = d.pop("deviceType", UNSET)

        device_brief_vo = cls(
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            type_=type_,
            status_category=status_category,
            ip=ip,
            is_client=is_client,
            device_type=device_type,
        )

        device_brief_vo.additional_properties = d
        return device_brief_vo

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
