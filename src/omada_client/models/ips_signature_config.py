from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsSignatureConfig")


@_attrs_define
class IpsSignatureConfig:
    """IPS signature configuration

    Attributes:
        type_ (int): Type should be a value as follow: 0: all traffic; 1: packet tracking Example: 1.
        direction (int | Unset): Direction should be a value as follow: 0: both direction; 1: source direction; 2:
            destination direction Example: 1.
        traffic_type (int | Unset): TrafficType should be a value as follow: 0: ip address; 1: subnet Example: 0.
        ip (str | Unset): IPS signature traffic Source. If parameter [trafficType] is 0, parameter [ip] is needed
            Example: 192.168.0.1.
        subnet (str | Unset): IPS signature traffic Source. If parameter [trafficType] is 1, parameter [subnet] is
            needed Example: 192.168.0.0/24.
    """

    type_: int
    direction: int | Unset = UNSET
    traffic_type: int | Unset = UNSET
    ip: str | Unset = UNSET
    subnet: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        direction = self.direction

        traffic_type = self.traffic_type

        ip = self.ip

        subnet = self.subnet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if traffic_type is not UNSET:
            field_dict["trafficType"] = traffic_type
        if ip is not UNSET:
            field_dict["ip"] = ip
        if subnet is not UNSET:
            field_dict["subnet"] = subnet

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        direction = d.pop("direction", UNSET)

        traffic_type = d.pop("trafficType", UNSET)

        ip = d.pop("ip", UNSET)

        subnet = d.pop("subnet", UNSET)

        ips_signature_config = cls(
            type_=type_,
            direction=direction,
            traffic_type=traffic_type,
            ip=ip,
            subnet=subnet,
        )

        ips_signature_config.additional_properties = d
        return ips_signature_config

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
