from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_client_uplink_switch_port_info import (
        TopologyClientUplinkSwitchPortInfo,
    )


T = TypeVar("T", bound="TopologyClientUplinkSwitchInfo")


@_attrs_define
class TopologyClientUplinkSwitchInfo:
    """Uplink Information while Uplink Device is Switch.

    Attributes:
        port (TopologyClientUplinkSwitchPortInfo | Unset): Uplink Port Information while Uplink Device is Switch.
        link_speed (int | Unset): Link Speed, it should be a value as follows: 1:10Mbps, 2:100Mbps, 3:1000Mbps,
            4:2.5Gbps, 5:10Gbps, 6:5Gbps, 7:25Gbps.
        duplex (int | Unset): Duplex, it should be a value as follows: 1:Half Duplex.
    """

    port: TopologyClientUplinkSwitchPortInfo | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port, Unset):
            port = self.port.to_dict()

        link_speed = self.link_speed

        duplex = self.duplex

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_client_uplink_switch_port_info import (
            TopologyClientUplinkSwitchPortInfo,
        )

        d = dict(src_dict)
        _port = d.pop("port", UNSET)
        port: TopologyClientUplinkSwitchPortInfo | Unset
        if isinstance(_port, Unset):
            port = UNSET
        else:
            port = TopologyClientUplinkSwitchPortInfo.from_dict(_port)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        topology_client_uplink_switch_info = cls(
            port=port,
            link_speed=link_speed,
            duplex=duplex,
        )

        topology_client_uplink_switch_info.additional_properties = d
        return topology_client_uplink_switch_info

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
