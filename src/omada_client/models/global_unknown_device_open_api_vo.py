from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalUnknownDeviceOpenApiVO")


@_attrs_define
class GlobalUnknownDeviceOpenApiVO:
    """
    Attributes:
        mac (str | Unset): Device MAC
        name (str | Unset): Device name
        type_ (str | Unset): Device type
        subtype (str | Unset): Switch subtype should be a value as follows: smart: Non-Agile Series Switch; es: Agile
            Series Switch.
        device_series_type (int | Unset): Device series type. 0 means basic, 1 means pro.
        model (str | Unset): Device model name
        ip (str | Unset): Device IP
        uptime (str | Unset): Device uptime
        status (int | Unset): Device status should be a value as follows: 0: Disconnected; 1: Connected; 2: Pending; 3:
            Heartbeat Missed; 4: Isolated
        last_seen (int | Unset): Device lastSeen, unit: ms
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    subtype: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    model: str | Unset = UNSET
    ip: str | Unset = UNSET
    uptime: str | Unset = UNSET
    status: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        type_ = self.type_

        subtype = self.subtype

        device_series_type = self.device_series_type

        model = self.model

        ip = self.ip

        uptime = self.uptime

        status = self.status

        last_seen = self.last_seen

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if model is not UNSET:
            field_dict["model"] = model
        if ip is not UNSET:
            field_dict["ip"] = ip
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if status is not UNSET:
            field_dict["status"] = status
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        subtype = d.pop("subtype", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        model = d.pop("model", UNSET)

        ip = d.pop("ip", UNSET)

        uptime = d.pop("uptime", UNSET)

        status = d.pop("status", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        global_unknown_device_open_api_vo = cls(
            mac=mac,
            name=name,
            type_=type_,
            subtype=subtype,
            device_series_type=device_series_type,
            model=model,
            ip=ip,
            uptime=uptime,
            status=status,
            last_seen=last_seen,
        )

        global_unknown_device_open_api_vo.additional_properties = d
        return global_unknown_device_open_api_vo

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
