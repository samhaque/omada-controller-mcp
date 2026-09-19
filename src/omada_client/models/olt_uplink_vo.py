from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OltUplinkVO")


@_attrs_define
class OltUplinkVO:
    """Up-link device

    Attributes:
        mac (str | Unset): The mac of uplink device
        name (str | Unset): The name of uplink device
        model (str | Unset): The model of uplink device
        hw_version (str | Unset): HwVersion
        model_version (str | Unset): Model Version
        link_speed (int | Unset): Link Speed
        port (str | Unset): Olt port linking with uplink device
        type_ (str | Unset): The type of uplink device
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    model_version: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    port: str | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        model = self.model

        hw_version = self.hw_version

        model_version = self.model_version

        link_speed = self.link_speed

        port = self.port

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if port is not UNSET:
            field_dict["port"] = port
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        port = d.pop("port", UNSET)

        type_ = d.pop("type", UNSET)

        olt_uplink_vo = cls(
            mac=mac,
            name=name,
            model=model,
            hw_version=hw_version,
            model_version=model_version,
            link_speed=link_speed,
            port=port,
            type_=type_,
        )

        olt_uplink_vo.additional_properties = d
        return olt_uplink_vo

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
