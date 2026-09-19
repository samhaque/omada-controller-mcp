from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStatPortStatusVO")


@_attrs_define
class OswStatPortStatusVO:
    """Port Status

    Attributes:
        link_status (int | Unset): LinkStatus should be a value as follows: 0:link down; 1:link up
        stk_status (int | Unset): Stack Status should be a value as follows: 0:DOWN; 1:AUTHFAIL; 2:IEEE; 3:OK
        link_speed (int | Unset): LinkSpeed should be a value as follows: 1:10Mbps; 2:100Mbps; 3:1000Mbps; 4:10Gbps
        poe (bool | Unset): Indicates whether PoE power supply is in use
        tx (int | Unset): Transmit traffic of the port, in bytes
        rx (int | Unset): Receive traffic of the port, in bytes
        total (int | Unset): Transmit traffic + Receive traffic of the port, in bytes
        stp_discarding (bool | Unset): STP Discarding
    """

    link_status: int | Unset = UNSET
    stk_status: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    poe: bool | Unset = UNSET
    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    total: int | Unset = UNSET
    stp_discarding: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        link_status = self.link_status

        stk_status = self.stk_status

        link_speed = self.link_speed

        poe = self.poe

        tx = self.tx

        rx = self.rx

        total = self.total

        stp_discarding = self.stp_discarding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if stk_status is not UNSET:
            field_dict["stkStatus"] = stk_status
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if poe is not UNSET:
            field_dict["poe"] = poe
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx
        if total is not UNSET:
            field_dict["total"] = total
        if stp_discarding is not UNSET:
            field_dict["stpDiscarding"] = stp_discarding

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        link_status = d.pop("linkStatus", UNSET)

        stk_status = d.pop("stkStatus", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        poe = d.pop("poe", UNSET)

        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        total = d.pop("total", UNSET)

        stp_discarding = d.pop("stpDiscarding", UNSET)

        osw_stat_port_status_vo = cls(
            link_status=link_status,
            stk_status=stk_status,
            link_speed=link_speed,
            poe=poe,
            tx=tx,
            rx=rx,
            total=total,
            stp_discarding=stp_discarding,
        )

        osw_stat_port_status_vo.additional_properties = d
        return osw_stat_port_status_vo

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
