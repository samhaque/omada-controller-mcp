from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswClientVO")


@_attrs_define
class OswClientVO:
    """Switch downlink clients.

    Attributes:
        mac (str | Unset): Client MAC Address
        name (str | Unset): Client Name, alias
        device_type (str | Unset): Device Type: iPhone, iPod, Android, PC, printer, TV...
        ip (str | Unset): IP Address
        port (int | Unset): (Wired) Port ID
        lag_id (int | Unset): (Wired) LAG ID. Exists only when the client is connected to the LAG
        unit (int | Unset): Unit ID
        standard_port (str | Unset): Standard port
        model (str | Unset): Client Model
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    ip: str | Unset = UNSET
    port: int | Unset = UNSET
    lag_id: int | Unset = UNSET
    unit: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        device_type = self.device_type

        ip = self.ip

        port = self.port

        lag_id = self.lag_id

        unit = self.unit

        standard_port = self.standard_port

        model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if ip is not UNSET:
            field_dict["ip"] = ip
        if port is not UNSET:
            field_dict["port"] = port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if unit is not UNSET:
            field_dict["unit"] = unit
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        device_type = d.pop("deviceType", UNSET)

        ip = d.pop("ip", UNSET)

        port = d.pop("port", UNSET)

        lag_id = d.pop("lagId", UNSET)

        unit = d.pop("unit", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        model = d.pop("model", UNSET)

        osw_client_vo = cls(
            mac=mac,
            name=name,
            device_type=device_type,
            ip=ip,
            port=port,
            lag_id=lag_id,
            unit=unit,
            standard_port=standard_port,
            model=model,
        )

        osw_client_vo.additional_properties = d
        return osw_client_vo

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
