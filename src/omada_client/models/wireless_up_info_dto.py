from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_link_dto import PartnerLinkDTO


T = TypeVar("T", bound="WirelessUpInfoDTO")


@_attrs_define
class WirelessUpInfoDTO:
    """Wireless UpLink Info

    Attributes:
        tx_rate (str | Unset): Tx Rate
        rx_rate (str | Unset): Rx Rate
        tx (int | Unset): Tx
        rx (int | Unset): Rx
        rssi (int | Unset): Rssi
        rssi_percent (float | Unset): Rssi Percent
        rx_drop_pkts (int | Unset): Rx Dropped Packets
        tx_drop_pkts (int | Unset): Tx Dropped Packets
        rx_err_pkts (int | Unset): Rx Error Packets
        tx_err_pkts (int | Unset): Tx Error Packets
        snr (int | Unset): Wireless P2P Ap Snr
        mesh_radio_id (int | Unset): radio Id used in mesh link
        channel (int | Unset): channel in link
        up_rate (int | Unset): upRate of this radio Id
        down_rate (int | Unset): downRate of this radio Id
        partner_links (list[PartnerLinkDTO] | Unset): partner link info in mlo mesh link
    """

    tx_rate: str | Unset = UNSET
    rx_rate: str | Unset = UNSET
    tx: int | Unset = UNSET
    rx: int | Unset = UNSET
    rssi: int | Unset = UNSET
    rssi_percent: float | Unset = UNSET
    rx_drop_pkts: int | Unset = UNSET
    tx_drop_pkts: int | Unset = UNSET
    rx_err_pkts: int | Unset = UNSET
    tx_err_pkts: int | Unset = UNSET
    snr: int | Unset = UNSET
    mesh_radio_id: int | Unset = UNSET
    channel: int | Unset = UNSET
    up_rate: int | Unset = UNSET
    down_rate: int | Unset = UNSET
    partner_links: list[PartnerLinkDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tx_rate = self.tx_rate

        rx_rate = self.rx_rate

        tx = self.tx

        rx = self.rx

        rssi = self.rssi

        rssi_percent = self.rssi_percent

        rx_drop_pkts = self.rx_drop_pkts

        tx_drop_pkts = self.tx_drop_pkts

        rx_err_pkts = self.rx_err_pkts

        tx_err_pkts = self.tx_err_pkts

        snr = self.snr

        mesh_radio_id = self.mesh_radio_id

        channel = self.channel

        up_rate = self.up_rate

        down_rate = self.down_rate

        partner_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.partner_links, Unset):
            partner_links = []
            for partner_links_item_data in self.partner_links:
                partner_links_item = partner_links_item_data.to_dict()
                partner_links.append(partner_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx is not UNSET:
            field_dict["rx"] = rx
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if rssi_percent is not UNSET:
            field_dict["rssiPercent"] = rssi_percent
        if rx_drop_pkts is not UNSET:
            field_dict["rxDropPkts"] = rx_drop_pkts
        if tx_drop_pkts is not UNSET:
            field_dict["txDropPkts"] = tx_drop_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts
        if snr is not UNSET:
            field_dict["snr"] = snr
        if mesh_radio_id is not UNSET:
            field_dict["meshRadioId"] = mesh_radio_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if up_rate is not UNSET:
            field_dict["upRate"] = up_rate
        if down_rate is not UNSET:
            field_dict["downRate"] = down_rate
        if partner_links is not UNSET:
            field_dict["partnerLinks"] = partner_links

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.partner_link_dto import PartnerLinkDTO

        d = dict(src_dict)
        tx_rate = d.pop("txRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx = d.pop("tx", UNSET)

        rx = d.pop("rx", UNSET)

        rssi = d.pop("rssi", UNSET)

        rssi_percent = d.pop("rssiPercent", UNSET)

        rx_drop_pkts = d.pop("rxDropPkts", UNSET)

        tx_drop_pkts = d.pop("txDropPkts", UNSET)

        rx_err_pkts = d.pop("rxErrPkts", UNSET)

        tx_err_pkts = d.pop("txErrPkts", UNSET)

        snr = d.pop("snr", UNSET)

        mesh_radio_id = d.pop("meshRadioId", UNSET)

        channel = d.pop("channel", UNSET)

        up_rate = d.pop("upRate", UNSET)

        down_rate = d.pop("downRate", UNSET)

        _partner_links = d.pop("partnerLinks", UNSET)
        partner_links: list[PartnerLinkDTO] | Unset = UNSET
        if _partner_links is not UNSET:
            partner_links = []
            for partner_links_item_data in _partner_links:
                partner_links_item = PartnerLinkDTO.from_dict(partner_links_item_data)

                partner_links.append(partner_links_item)

        wireless_up_info_dto = cls(
            tx_rate=tx_rate,
            rx_rate=rx_rate,
            tx=tx,
            rx=rx,
            rssi=rssi,
            rssi_percent=rssi_percent,
            rx_drop_pkts=rx_drop_pkts,
            tx_drop_pkts=tx_drop_pkts,
            rx_err_pkts=rx_err_pkts,
            tx_err_pkts=tx_err_pkts,
            snr=snr,
            mesh_radio_id=mesh_radio_id,
            channel=channel,
            up_rate=up_rate,
            down_rate=down_rate,
            partner_links=partner_links,
        )

        wireless_up_info_dto.additional_properties = d
        return wireless_up_info_dto

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
