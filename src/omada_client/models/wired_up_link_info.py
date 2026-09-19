from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wired_port_v3dto import WiredPortV3DTO


T = TypeVar("T", bound="WiredUpLinkInfo")


@_attrs_define
class WiredUpLinkInfo:
    """Exists when connected to upper level device via wired connection

    Attributes:
        up_port (WiredPortV3DTO | Unset): Downlink Port
        up_link_port (WiredPortV3DTO | Unset): Downlink Port
        link_speed (int | Unset): Uplink port linkSpeed, linkSpeed should be a value as follows: 0: Auto; 1: 10M; 2:
            100M; 3: 1000M; 4: 2500M; 5: 10G; 6: 5G; 7: 25G, 8: 100G.
        duplex (int | Unset): Duplex mode, should be a value as follows: 0: Auto; 1: Half; 2: Full.
        rx_drop_pkts (int | Unset): Rx Dropped Packets
        tx_drop_pkts (int | Unset): Tx Dropped Packets
        rx_err_pkts (int | Unset): Rx Error Packets
        tx_err_pkts (int | Unset): Tx Error Packets
    """

    up_port: WiredPortV3DTO | Unset = UNSET
    up_link_port: WiredPortV3DTO | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    rx_drop_pkts: int | Unset = UNSET
    tx_drop_pkts: int | Unset = UNSET
    rx_err_pkts: int | Unset = UNSET
    tx_err_pkts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        up_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.up_port, Unset):
            up_port = self.up_port.to_dict()

        up_link_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.up_link_port, Unset):
            up_link_port = self.up_link_port.to_dict()

        link_speed = self.link_speed

        duplex = self.duplex

        rx_drop_pkts = self.rx_drop_pkts

        tx_drop_pkts = self.tx_drop_pkts

        rx_err_pkts = self.rx_err_pkts

        tx_err_pkts = self.tx_err_pkts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if up_port is not UNSET:
            field_dict["upPort"] = up_port
        if up_link_port is not UNSET:
            field_dict["upLinkPort"] = up_link_port
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if rx_drop_pkts is not UNSET:
            field_dict["rxDropPkts"] = rx_drop_pkts
        if tx_drop_pkts is not UNSET:
            field_dict["txDropPkts"] = tx_drop_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wired_port_v3dto import WiredPortV3DTO

        d = dict(src_dict)
        _up_port = d.pop("upPort", UNSET)
        up_port: WiredPortV3DTO | Unset
        if isinstance(_up_port, Unset):
            up_port = UNSET
        else:
            up_port = WiredPortV3DTO.from_dict(_up_port)

        _up_link_port = d.pop("upLinkPort", UNSET)
        up_link_port: WiredPortV3DTO | Unset
        if isinstance(_up_link_port, Unset):
            up_link_port = UNSET
        else:
            up_link_port = WiredPortV3DTO.from_dict(_up_link_port)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        rx_drop_pkts = d.pop("rxDropPkts", UNSET)

        tx_drop_pkts = d.pop("txDropPkts", UNSET)

        rx_err_pkts = d.pop("rxErrPkts", UNSET)

        tx_err_pkts = d.pop("txErrPkts", UNSET)

        wired_up_link_info = cls(
            up_port=up_port,
            up_link_port=up_link_port,
            link_speed=link_speed,
            duplex=duplex,
            rx_drop_pkts=rx_drop_pkts,
            tx_drop_pkts=tx_drop_pkts,
            rx_err_pkts=rx_err_pkts,
            tx_err_pkts=tx_err_pkts,
        )

        wired_up_link_info.additional_properties = d
        return wired_up_link_info

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
