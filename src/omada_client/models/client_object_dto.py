from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientObjectDTO")


@_attrs_define
class ClientObjectDTO:
    """
    Attributes:
        name (str | Unset): Client Name, alias.
        device_type (str | Unset): Client type: iPhone, iPod, Android, PC, printer, TV...
        manager (bool | Unset): Whether it is the client currently being managed.
        ip (str | Unset): Client IP address.
        radio_id (int | Unset): (Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2:5GHz-2; 3:
            6GHz.
        port (int | Unset): (Wired) Port ID.
        model (str | Unset): Client model.
        ssid (str | Unset): (Wireless)  SSID name.
    """

    name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    manager: bool | Unset = UNSET
    ip: str | Unset = UNSET
    radio_id: int | Unset = UNSET
    port: int | Unset = UNSET
    model: str | Unset = UNSET
    ssid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        device_type = self.device_type

        manager = self.manager

        ip = self.ip

        radio_id = self.radio_id

        port = self.port

        model = self.model

        ssid = self.ssid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if manager is not UNSET:
            field_dict["manager"] = manager
        if ip is not UNSET:
            field_dict["ip"] = ip
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if port is not UNSET:
            field_dict["port"] = port
        if model is not UNSET:
            field_dict["model"] = model
        if ssid is not UNSET:
            field_dict["ssid"] = ssid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        device_type = d.pop("deviceType", UNSET)

        manager = d.pop("manager", UNSET)

        ip = d.pop("ip", UNSET)

        radio_id = d.pop("radioId", UNSET)

        port = d.pop("port", UNSET)

        model = d.pop("model", UNSET)

        ssid = d.pop("ssid", UNSET)

        client_object_dto = cls(
            name=name,
            device_type=device_type,
            manager=manager,
            ip=ip,
            radio_id=radio_id,
            port=port,
            model=model,
            ssid=ssid,
        )

        client_object_dto.additional_properties = d
        return client_object_dto

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
