from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswPeerPortVO")


@_attrs_define
class OswPeerPortVO:
    """Downlink Port Info

    Attributes:
        port (int | Unset): Port
        st_port (str | Unset): Standard Port, unit/slot/port
        lag_id (int | Unset): LagId. If it is not null, it indicates that the port is a LAG port
        link_speed (int | Unset): Link Speed
        duplex (int | Unset): Duplex
        rx (int | Unset): Port total rx bytes
        rx_rate (int | Unset): Port rx Rate
        tx (int | Unset): Port total tx bytes
        tx_rate (int | Unset): Port tx Rate
        stp_discarding (bool | Unset): STP Discarding
        blocked_vlans (str | Unset): Blocked Vlans
        blocked_type (int | Unset): Blocked Type
    """

    port: int | Unset = UNSET
    st_port: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    rx: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    stp_discarding: bool | Unset = UNSET
    blocked_vlans: str | Unset = UNSET
    blocked_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        st_port = self.st_port

        lag_id = self.lag_id

        link_speed = self.link_speed

        duplex = self.duplex

        rx = self.rx

        rx_rate = self.rx_rate

        tx = self.tx

        tx_rate = self.tx_rate

        stp_discarding = self.stp_discarding

        blocked_vlans = self.blocked_vlans

        blocked_type = self.blocked_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if st_port is not UNSET:
            field_dict["stPort"] = st_port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if rx is not UNSET:
            field_dict["rx"] = rx
        if rx_rate is not UNSET:
            field_dict["rx Rate"] = rx_rate
        if tx is not UNSET:
            field_dict["tx"] = tx
        if tx_rate is not UNSET:
            field_dict["tx Rate"] = tx_rate
        if stp_discarding is not UNSET:
            field_dict["stpDiscarding"] = stp_discarding
        if blocked_vlans is not UNSET:
            field_dict["blockedVlans"] = blocked_vlans
        if blocked_type is not UNSET:
            field_dict["blockedType"] = blocked_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        st_port = d.pop("stPort", UNSET)

        lag_id = d.pop("lagId", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        rx = d.pop("rx", UNSET)

        rx_rate = d.pop("rx Rate", UNSET)

        tx = d.pop("tx", UNSET)

        tx_rate = d.pop("tx Rate", UNSET)

        stp_discarding = d.pop("stpDiscarding", UNSET)

        blocked_vlans = d.pop("blockedVlans", UNSET)

        blocked_type = d.pop("blockedType", UNSET)

        osw_peer_port_vo = cls(
            port=port,
            st_port=st_port,
            lag_id=lag_id,
            link_speed=link_speed,
            duplex=duplex,
            rx=rx,
            rx_rate=rx_rate,
            tx=tx,
            tx_rate=tx_rate,
            stp_discarding=stp_discarding,
            blocked_vlans=blocked_vlans,
            blocked_type=blocked_type,
        )

        osw_peer_port_vo.additional_properties = d
        return osw_peer_port_vo

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
