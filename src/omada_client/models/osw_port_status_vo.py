from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswPortStatusVO")


@_attrs_define
class OswPortStatusVO:
    """Port Status

    Attributes:
        port (int | Unset): Port Number
        link_status (int | Unset): LinkStatus should be a value as follows: 0: link down; 1: link up
        link_speed (int | Unset): LinkSpeed should be a value as follows: 1: 10Mbps; 2: 100Mbps; 3: 1000Mbps; 4: 10Gbps
        duplex (int | Unset): Duplex should be a value as follows: 1: Half; 2: Full
        fec_mode (int | Unset): The configured FEC Mode
        fec_real_mode (int | Unset): The actual effective FEC Mode
        poe (bool | Unset): Indicates whether PoE power supply is in use
        poe_power (float | Unset): PoE Power
        tx (int | Unset): Tx, in bytes
        rx (int | Unset): Rx, in bytes
        tx_rate (int | Unset): Tx rate, in bit/s
        rx_rate (int | Unset): Rx rate, in bit/s
        stp (str | Unset): STP Status
        stp_discarding (bool | Unset): STP Discarding
        blocked_vlans (str | Unset): Blocked Vlans
        blocked_type (int | Unset): Blocked Type
        chassis_id_subtype (str | Unset): Chassis ID Subtype
        chassis_id (str | Unset): Chassis ID
        port_id_subtype (str | Unset): Port ID Subtype
        port_id (str | Unset): Port ID
        stk_status (int | Unset): Stk Status
        trunk_state (int | Unset): LACP port state
    """

    port: int | Unset = UNSET
    link_status: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    fec_mode: int | Unset = UNSET
    fec_real_mode: int | Unset = UNSET
    poe: bool | Unset = UNSET
    poe_power: float | Unset = UNSET
    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    stp: str | Unset = UNSET
    stp_discarding: bool | Unset = UNSET
    blocked_vlans: str | Unset = UNSET
    blocked_type: int | Unset = UNSET
    chassis_id_subtype: str | Unset = UNSET
    chassis_id: str | Unset = UNSET
    port_id_subtype: str | Unset = UNSET
    port_id: str | Unset = UNSET
    stk_status: int | Unset = UNSET
    trunk_state: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        link_status = self.link_status

        link_speed = self.link_speed

        duplex = self.duplex

        fec_mode = self.fec_mode

        fec_real_mode = self.fec_real_mode

        poe = self.poe

        poe_power = self.poe_power

        tx = self.tx

        rx = self.rx

        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        stp = self.stp

        stp_discarding = self.stp_discarding

        blocked_vlans = self.blocked_vlans

        blocked_type = self.blocked_type

        chassis_id_subtype = self.chassis_id_subtype

        chassis_id = self.chassis_id

        port_id_subtype = self.port_id_subtype

        port_id = self.port_id

        stk_status = self.stk_status

        trunk_state = self.trunk_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if fec_mode is not UNSET:
            field_dict["fecMode"] = fec_mode
        if fec_real_mode is not UNSET:
            field_dict["fecRealMode"] = fec_real_mode
        if poe is not UNSET:
            field_dict["poe"] = poe
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if stp is not UNSET:
            field_dict["stp"] = stp
        if stp_discarding is not UNSET:
            field_dict["stpDiscarding"] = stp_discarding
        if blocked_vlans is not UNSET:
            field_dict["blockedVlans"] = blocked_vlans
        if blocked_type is not UNSET:
            field_dict["blockedType"] = blocked_type
        if chassis_id_subtype is not UNSET:
            field_dict["chassisIdSubtype"] = chassis_id_subtype
        if chassis_id is not UNSET:
            field_dict["chassisId"] = chassis_id
        if port_id_subtype is not UNSET:
            field_dict["portIdSubtype"] = port_id_subtype
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if stk_status is not UNSET:
            field_dict["stkStatus"] = stk_status
        if trunk_state is not UNSET:
            field_dict["trunkState"] = trunk_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        fec_mode = d.pop("fecMode", UNSET)

        fec_real_mode = d.pop("fecRealMode", UNSET)

        poe = d.pop("poe", UNSET)

        poe_power = d.pop("poePower", UNSET)

        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        stp = d.pop("stp", UNSET)

        stp_discarding = d.pop("stpDiscarding", UNSET)

        blocked_vlans = d.pop("blockedVlans", UNSET)

        blocked_type = d.pop("blockedType", UNSET)

        chassis_id_subtype = d.pop("chassisIdSubtype", UNSET)

        chassis_id = d.pop("chassisId", UNSET)

        port_id_subtype = d.pop("portIdSubtype", UNSET)

        port_id = d.pop("portId", UNSET)

        stk_status = d.pop("stkStatus", UNSET)

        trunk_state = d.pop("trunkState", UNSET)

        osw_port_status_vo = cls(
            port=port,
            link_status=link_status,
            link_speed=link_speed,
            duplex=duplex,
            fec_mode=fec_mode,
            fec_real_mode=fec_real_mode,
            poe=poe,
            poe_power=poe_power,
            tx=tx,
            rx=rx,
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            stp=stp,
            stp_discarding=stp_discarding,
            blocked_vlans=blocked_vlans,
            blocked_type=blocked_type,
            chassis_id_subtype=chassis_id_subtype,
            chassis_id=chassis_id,
            port_id_subtype=port_id_subtype,
            port_id=port_id,
            stk_status=stk_status,
            trunk_state=trunk_state,
        )

        osw_port_status_vo.additional_properties = d
        return osw_port_status_vo

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
