from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_link_vo import PartnerLinkVO


T = TypeVar("T", bound="ApWirelessUplink")


@_attrs_define
class ApWirelessUplink:
    """Wireless uplink info

    Attributes:
        uplink_mac (str | Unset): Uplink AP MAC
        name (str | Unset): Uplink AP name
        channel (int | Unset): Uplink AP channel
        rssi (int | Unset): Uplink AP rssi
        snr (int | Unset): Uplink AP Signal-noise ratio
        tx_rate (str | Unset): Uplink AP txRate
        tx_rate_int (int | Unset): Uplink AP txRateInt; Unit: Mbps
        rx_rate (str | Unset): Uplink AP rxRate
        rx_rate_int (int | Unset): Uplink AP rxRateInt; Unit: Mbps
        up_bytes (int | Unset): Uplink AP upBytes; Unit: Byte
        down_bytes (int | Unset): Uplink AP downBytes; Unit:Byte
        up_packets (int | Unset): Uplink AP upPackets
        down_packets (int | Unset): Uplink AP downPackets
        activity (int | Unset): Uplink AP activity: (change of(downBytes+upBytes))/time
        support_speed_test (bool | Unset): Whether speed measurement is supported.
        model (str | Unset): Device model.(Used to display the device model diagram)
        model_version (str | Unset): Device model version.(Used to display the device model diagram)
        ip (str | Unset): Device IP.
        type_ (str | Unset): Device type.
        uplink_port (str | Unset): Uplink port of current device. To mark that this port cannot be configured.
        partner_links (list[PartnerLinkVO] | Unset): Mlo link Info
    """

    uplink_mac: str | Unset = UNSET
    name: str | Unset = UNSET
    channel: int | Unset = UNSET
    rssi: int | Unset = UNSET
    snr: int | Unset = UNSET
    tx_rate: str | Unset = UNSET
    tx_rate_int: int | Unset = UNSET
    rx_rate: str | Unset = UNSET
    rx_rate_int: int | Unset = UNSET
    up_bytes: int | Unset = UNSET
    down_bytes: int | Unset = UNSET
    up_packets: int | Unset = UNSET
    down_packets: int | Unset = UNSET
    activity: int | Unset = UNSET
    support_speed_test: bool | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    ip: str | Unset = UNSET
    type_: str | Unset = UNSET
    uplink_port: str | Unset = UNSET
    partner_links: list[PartnerLinkVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uplink_mac = self.uplink_mac

        name = self.name

        channel = self.channel

        rssi = self.rssi

        snr = self.snr

        tx_rate = self.tx_rate

        tx_rate_int = self.tx_rate_int

        rx_rate = self.rx_rate

        rx_rate_int = self.rx_rate_int

        up_bytes = self.up_bytes

        down_bytes = self.down_bytes

        up_packets = self.up_packets

        down_packets = self.down_packets

        activity = self.activity

        support_speed_test = self.support_speed_test

        model = self.model

        model_version = self.model_version

        ip = self.ip

        type_ = self.type_

        uplink_port = self.uplink_port

        partner_links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.partner_links, Unset):
            partner_links = []
            for partner_links_item_data in self.partner_links:
                partner_links_item = partner_links_item_data.to_dict()
                partner_links.append(partner_links_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uplink_mac is not UNSET:
            field_dict["uplinkMac"] = uplink_mac
        if name is not UNSET:
            field_dict["name"] = name
        if channel is not UNSET:
            field_dict["channel"] = channel
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if snr is not UNSET:
            field_dict["snr"] = snr
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if tx_rate_int is not UNSET:
            field_dict["txRateInt"] = tx_rate_int
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if rx_rate_int is not UNSET:
            field_dict["rxRateInt"] = rx_rate_int
        if up_bytes is not UNSET:
            field_dict["upBytes"] = up_bytes
        if down_bytes is not UNSET:
            field_dict["downBytes"] = down_bytes
        if up_packets is not UNSET:
            field_dict["upPackets"] = up_packets
        if down_packets is not UNSET:
            field_dict["downPackets"] = down_packets
        if activity is not UNSET:
            field_dict["activity"] = activity
        if support_speed_test is not UNSET:
            field_dict["supportSpeedTest"] = support_speed_test
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if ip is not UNSET:
            field_dict["ip"] = ip
        if type_ is not UNSET:
            field_dict["type"] = type_
        if uplink_port is not UNSET:
            field_dict["uplinkPort"] = uplink_port
        if partner_links is not UNSET:
            field_dict["partnerLinks"] = partner_links

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.partner_link_vo import PartnerLinkVO

        d = dict(src_dict)
        uplink_mac = d.pop("uplinkMac", UNSET)

        name = d.pop("name", UNSET)

        channel = d.pop("channel", UNSET)

        rssi = d.pop("rssi", UNSET)

        snr = d.pop("snr", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        tx_rate_int = d.pop("txRateInt", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        rx_rate_int = d.pop("rxRateInt", UNSET)

        up_bytes = d.pop("upBytes", UNSET)

        down_bytes = d.pop("downBytes", UNSET)

        up_packets = d.pop("upPackets", UNSET)

        down_packets = d.pop("downPackets", UNSET)

        activity = d.pop("activity", UNSET)

        support_speed_test = d.pop("supportSpeedTest", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        ip = d.pop("ip", UNSET)

        type_ = d.pop("type", UNSET)

        uplink_port = d.pop("uplinkPort", UNSET)

        _partner_links = d.pop("partnerLinks", UNSET)
        partner_links: list[PartnerLinkVO] | Unset = UNSET
        if _partner_links is not UNSET:
            partner_links = []
            for partner_links_item_data in _partner_links:
                partner_links_item = PartnerLinkVO.from_dict(partner_links_item_data)

                partner_links.append(partner_links_item)

        ap_wireless_uplink = cls(
            uplink_mac=uplink_mac,
            name=name,
            channel=channel,
            rssi=rssi,
            snr=snr,
            tx_rate=tx_rate,
            tx_rate_int=tx_rate_int,
            rx_rate=rx_rate,
            rx_rate_int=rx_rate_int,
            up_bytes=up_bytes,
            down_bytes=down_bytes,
            up_packets=up_packets,
            down_packets=down_packets,
            activity=activity,
            support_speed_test=support_speed_test,
            model=model,
            model_version=model_version,
            ip=ip,
            type_=type_,
            uplink_port=uplink_port,
            partner_links=partner_links,
        )

        ap_wireless_uplink.additional_properties = d
        return ap_wireless_uplink

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
