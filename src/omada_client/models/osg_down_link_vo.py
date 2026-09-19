from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgDownLinkVO")


@_attrs_define
class OsgDownLinkVO:
    """
    Attributes:
        port (int | Unset):
        name (str | Unset):
        mac (str | Unset):
        device_name (str | Unset):
        speed (int | Unset):
        duplex (int | Unset):
        ip (str | Unset):
        model (str | Unset):
        model_version (str | Unset):
        type_ (str | Unset):
        wireless (bool | Unset):
        stack_id (str | Unset):
        stack_name (str | Unset):
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    ip: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    type_: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        mac = self.mac

        device_name = self.device_name

        speed = self.speed

        duplex = self.duplex

        ip = self.ip

        model = self.model

        model_version = self.model_version

        type_ = self.type_

        wireless = self.wireless

        stack_id = self.stack_id

        stack_name = self.stack_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if speed is not UNSET:
            field_dict["speed"] = speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if ip is not UNSET:
            field_dict["ip"] = ip
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if type_ is not UNSET:
            field_dict["type"] = type_
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        speed = d.pop("speed", UNSET)

        duplex = d.pop("duplex", UNSET)

        ip = d.pop("ip", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        type_ = d.pop("type", UNSET)

        wireless = d.pop("wireless", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        osg_down_link_vo = cls(
            port=port,
            name=name,
            mac=mac,
            device_name=device_name,
            speed=speed,
            duplex=duplex,
            ip=ip,
            model=model,
            model_version=model_version,
            type_=type_,
            wireless=wireless,
            stack_id=stack_id,
            stack_name=stack_name,
        )

        osg_down_link_vo.additional_properties = d
        return osg_down_link_vo

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
