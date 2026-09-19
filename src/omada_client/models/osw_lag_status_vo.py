from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO


T = TypeVar("T", bound="OswLagStatusVO")


@_attrs_define
class OswLagStatusVO:
    """Lag Status

    Attributes:
        name (str | Unset): Lag name
        lag_id (int | Unset): Lag ID
        link_status (int | Unset): Link Status should be a value as follows: 1: link up; 0: link down
        link_speed (int | Unset): Link Speed should be a value as follows: 0: auto; 1: 10M; 2: 100M; 3: 1000M; 4: 2.5G;
            5: 10G
        duplex (int | Unset): Duplex should be a value as follows: 0: Auto; 1: Half; 2: Full
        tx (int | Unset): Tx
        rx (int | Unset): Rx
        tx_rate (int | Unset): Tx Rate
        rx_rate (int | Unset): Rx Rate
        lag_type (int | Unset): LagType should be a value as follows: 1: static; 2: LACP
        ports (list[int] | Unset): Ports member
        standard_ports (list[OswStandPortVO] | Unset): Standard Ports
        stp_discarding (bool | Unset): STP Discarding
        blocked_vlans (str | Unset): Blocked Vlans
        blocked_type (int | Unset): Blocked Type
        trunk_state (int | Unset): LACP state
    """

    name: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    link_status: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    lag_type: int | Unset = UNSET
    ports: list[int] | Unset = UNSET
    standard_ports: list[OswStandPortVO] | Unset = UNSET
    stp_discarding: bool | Unset = UNSET
    blocked_vlans: str | Unset = UNSET
    blocked_type: int | Unset = UNSET
    trunk_state: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        lag_id = self.lag_id

        link_status = self.link_status

        link_speed = self.link_speed

        duplex = self.duplex

        tx = self.tx

        rx = self.rx

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        lag_type = self.lag_type

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        standard_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.standard_ports, Unset):
            standard_ports = []
            for standard_ports_item_data in self.standard_ports:
                standard_ports_item = standard_ports_item_data.to_dict()
                standard_ports.append(standard_ports_item)

        stp_discarding = self.stp_discarding

        blocked_vlans = self.blocked_vlans

        blocked_type = self.blocked_type

        trunk_state = self.trunk_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if lag_type is not UNSET:
            field_dict["lagType"] = lag_type
        if ports is not UNSET:
            field_dict["ports"] = ports
        if standard_ports is not UNSET:
            field_dict["standardPorts"] = standard_ports
        if stp_discarding is not UNSET:
            field_dict["stpDiscarding"] = stp_discarding
        if blocked_vlans is not UNSET:
            field_dict["blockedVlans"] = blocked_vlans
        if blocked_type is not UNSET:
            field_dict["blockedType"] = blocked_type
        if trunk_state is not UNSET:
            field_dict["trunkState"] = trunk_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        lag_id = d.pop("lagId", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        lag_type = d.pop("lagType", UNSET)

        ports = cast(list[int], d.pop("ports", UNSET))

        _standard_ports = d.pop("standardPorts", UNSET)
        standard_ports: list[OswStandPortVO] | Unset = UNSET
        if _standard_ports is not UNSET:
            standard_ports = []
            for standard_ports_item_data in _standard_ports:
                standard_ports_item = OswStandPortVO.from_dict(standard_ports_item_data)

                standard_ports.append(standard_ports_item)

        stp_discarding = d.pop("stpDiscarding", UNSET)

        blocked_vlans = d.pop("blockedVlans", UNSET)

        blocked_type = d.pop("blockedType", UNSET)

        trunk_state = d.pop("trunkState", UNSET)

        osw_lag_status_vo = cls(
            name=name,
            lag_id=lag_id,
            link_status=link_status,
            link_speed=link_speed,
            duplex=duplex,
            tx=tx,
            rx=rx,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            lag_type=lag_type,
            ports=ports,
            standard_ports=standard_ports,
            stp_discarding=stp_discarding,
            blocked_vlans=blocked_vlans,
            blocked_type=blocked_type,
            trunk_state=trunk_state,
        )

        osw_lag_status_vo.additional_properties = d
        return osw_lag_status_vo

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
