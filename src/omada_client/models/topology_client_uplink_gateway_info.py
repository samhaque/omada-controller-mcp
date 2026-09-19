from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_client_uplink_gateway_port_info import (
        TopologyClientUplinkGatewayPortInfo,
    )


T = TypeVar("T", bound="TopologyClientUplinkGatewayInfo")


@_attrs_define
class TopologyClientUplinkGatewayInfo:
    """Uplink Information while Uplink Device is Gateway.

    Attributes:
        port (TopologyClientUplinkGatewayPortInfo | Unset): Uplink Port Information while Uplink Device is Gateway.
        link_speed (int | Unset): Link Speed, it should be a value as follows: 1:10Mbps, 2:100Mbps, 3:1000Mbps,
            4:2.5Gbps, 5:10Gbps, 6:5Gbps, 7:25Gbps.
        duplex (int | Unset): Duplex, it should be a value as follows: 1:Half Duplex.
        channel (int | Unset): Channel, only for wireless router.
        ssid (str | Unset): Ssid, only for wireless router
        radio (int | Unset): Radio, it should be a value as follows: 0:2G, 1:5G, 2:5G2, 3:6G, only for wireless router
        support5g2 (bool | Unset): Whether the device supports the 5G2 frequency band, only for wireless router.
    """

    port: TopologyClientUplinkGatewayPortInfo | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    channel: int | Unset = UNSET
    ssid: str | Unset = UNSET
    radio: int | Unset = UNSET
    support5g2: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        link_speed = self.link_speed

        duplex = self.duplex

        channel = self.channel

        ssid = self.ssid

        radio = self.radio

        support5g2 = self.support5g2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if radio is not UNSET:
            field_dict["radio"] = radio
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_client_uplink_gateway_port_info import (
            TopologyClientUplinkGatewayPortInfo,
        )

        d = dict(src_dict)
        _port = d.pop("port", UNSET)
        port: TopologyClientUplinkGatewayPortInfo | Unset
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = TopologyClientUplinkGatewayPortInfo.from_dict(_port)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        channel = d.pop("channel", UNSET)

        ssid = d.pop("ssid", UNSET)

        radio = d.pop("radio", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        topology_client_uplink_gateway_info = cls(
            port=port,
            link_speed=link_speed,
            duplex=duplex,
            channel=channel,
            ssid=ssid,
            radio=radio,
            support5g2=support5g2,
        )

        topology_client_uplink_gateway_info.additional_properties = d
        return topology_client_uplink_gateway_info

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
