from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UplinkSwitchInfo")


@_attrs_define
class UplinkSwitchInfo:
    """Uplink switch info, exists when parameter [upDeviceType] is 1.

    Attributes:
        port (int | Unset): Client connected port.
        standard_port (str | Unset): Standard Port of Stack
        lag_id (str | Unset): Lag Id
        link_speed (int | Unset): Port link speed, 1: 10Mbps; 2: 100Mbps; 3: 1000Mbps; 4: 2.5Gbps; 5: 10Gbps.
        duplex (int | Unset): Duplex: 1:Half; 2:Full.
        traffic_down (int | Unset): Downstream traffic (Byte).
        traffic_up (int | Unset): Upstream traffic (Byte).
    """

    port: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    lag_id: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    traffic_down: int | Unset = UNSET
    traffic_up: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        standard_port = self.standard_port

        lag_id = self.lag_id

        link_speed = self.link_speed

        duplex = self.duplex

        traffic_down = self.traffic_down

        traffic_up = self.traffic_up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        lag_id = d.pop("lagId", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        uplink_switch_info = cls(
            port=port,
            standard_port=standard_port,
            lag_id=lag_id,
            link_speed=link_speed,
            duplex=duplex,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
        )

        uplink_switch_info.additional_properties = d
        return uplink_switch_info

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
