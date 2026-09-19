from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OltDetailDownlinkVO")


@_attrs_define
class OltDetailDownlinkVO:
    """Down-link list

    Attributes:
        port (str | Unset): Port
        name (str | Unset): Name of the device connected to the port
        mac (str | Unset): Mac of the device
        ip (str | Unset): Ip address
        ipv6 (str | Unset): Ipv6
        link_status (int | Unset): Link status should be a value as follows: 0:LINK_DOWN;1:LINK_UP
        speed (int | Unset): Speed
        type_ (str | Unset): Device type
        model (str | Unset): Model of device,for example:EAP225
        model_version (str | Unset): Model version of device,for example:3.0
    """

    port: str | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    ipv6: str | Unset = UNSET
    link_status: int | Unset = UNSET
    speed: int | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        mac = self.mac

        ip = self.ip

        ipv6 = self.ipv6

        link_status = self.link_status

        speed = self.speed

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if speed is not UNSET:
            field_dict["speed"] = speed
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        ipv6 = d.pop("ipv6", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        speed = d.pop("speed", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        olt_detail_downlink_vo = cls(
            port=port,
            name=name,
            mac=mac,
            ip=ip,
            ipv6=ipv6,
            link_status=link_status,
            speed=speed,
            type_=type_,
            model=model,
            model_version=model_version,
        )

        olt_detail_downlink_vo.additional_properties = d
        return olt_detail_downlink_vo

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
