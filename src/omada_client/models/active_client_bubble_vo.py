from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActiveClientBubbleVO")


@_attrs_define
class ActiveClientBubbleVO:
    """
    Attributes:
        name (str | Unset):
        type_ (str | Unset):
        mac (str | Unset):
        ap_name (str | Unset):
        traffic (int | Unset):
        traffic_percent (int | Unset):
        upload (int | Unset):
        upload_percent (int | Unset):
        download (int | Unset):
        download_percent (int | Unset):
        health_score (int | Unset):
        tx_rate (int | Unset):
        snr (int | Unset):
        wifi_protocol (str | Unset):
        rssi (int | Unset):
        signal_level (int | Unset):
        channel (int | Unset):
        radio_id (int | Unset):
        band_width (int | Unset):
        incidents (int | Unset):
    """

    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    ap_name: str | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_percent: int | Unset = UNSET
    upload: int | Unset = UNSET
    upload_percent: int | Unset = UNSET
    download: int | Unset = UNSET
    download_percent: int | Unset = UNSET
    health_score: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    snr: int | Unset = UNSET
    wifi_protocol: str | Unset = UNSET
    rssi: int | Unset = UNSET
    signal_level: int | Unset = UNSET
    channel: int | Unset = UNSET
    radio_id: int | Unset = UNSET
    band_width: int | Unset = UNSET
    incidents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        mac = self.mac

        ap_name = self.ap_name

        traffic = self.traffic

        traffic_percent = self.traffic_percent

        upload = self.upload

        upload_percent = self.upload_percent

        download = self.download

        download_percent = self.download_percent

        health_score = self.health_score

        tx_rate = self.tx_rate

        snr = self.snr

        wifi_protocol = self.wifi_protocol

        rssi = self.rssi

        signal_level = self.signal_level

        channel = self.channel

        radio_id = self.radio_id

        band_width = self.band_width

        incidents = self.incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ap_name is not UNSET:
            field_dict["apName"] = ap_name
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent
        if upload is not UNSET:
            field_dict["upload"] = upload
        if upload_percent is not UNSET:
            field_dict["uploadPercent"] = upload_percent
        if download is not UNSET:
            field_dict["download"] = download
        if download_percent is not UNSET:
            field_dict["downloadPercent"] = download_percent
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if snr is not UNSET:
            field_dict["snr"] = snr
        if wifi_protocol is not UNSET:
            field_dict["wifiProtocol"] = wifi_protocol
        if rssi is not UNSET:
            field_dict["rssi"] = rssi
        if signal_level is not UNSET:
            field_dict["signalLevel"] = signal_level
        if channel is not UNSET:
            field_dict["channel"] = channel
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if band_width is not UNSET:
            field_dict["bandWidth"] = band_width
        if incidents is not UNSET:
            field_dict["incidents"] = incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        ap_name = d.pop("apName", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        upload = d.pop("upload", UNSET)

        upload_percent = d.pop("uploadPercent", UNSET)

        download = d.pop("download", UNSET)

        download_percent = d.pop("downloadPercent", UNSET)

        health_score = d.pop("healthScore", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        snr = d.pop("snr", UNSET)

        wifi_protocol = d.pop("wifiProtocol", UNSET)

        rssi = d.pop("rssi", UNSET)

        signal_level = d.pop("signalLevel", UNSET)

        channel = d.pop("channel", UNSET)

        radio_id = d.pop("radioId", UNSET)

        band_width = d.pop("bandWidth", UNSET)

        incidents = d.pop("incidents", UNSET)

        active_client_bubble_vo = cls(
            name=name,
            type_=type_,
            mac=mac,
            ap_name=ap_name,
            traffic=traffic,
            traffic_percent=traffic_percent,
            upload=upload,
            upload_percent=upload_percent,
            download=download,
            download_percent=download_percent,
            health_score=health_score,
            tx_rate=tx_rate,
            snr=snr,
            wifi_protocol=wifi_protocol,
            rssi=rssi,
            signal_level=signal_level,
            channel=channel,
            radio_id=radio_id,
            band_width=band_width,
            incidents=incidents,
        )

        active_client_bubble_vo.additional_properties = d
        return active_client_bubble_vo

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
