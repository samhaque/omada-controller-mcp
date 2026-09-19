from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverViewSummaryVO")


@_attrs_define
class OverViewSummaryVO:
    """
    Attributes:
        site_health_score (int | Unset): site health score
        wifi_health_score (int | Unset): Wi-Fi health score
        device_health_score (int | Unset): device health score
        client_health_score (int | Unset): client health score
        wan_health_score (int | Unset): wan health score
        total_devices (int | Unset): total number of device
        total_gateways (int | Unset): total number of gateway
        total_switches (int | Unset): total number of switch
        total_aps (int | Unset): total number of ap
        total_olts (int | Unset): total number of olt
        total_nvrs (int | Unset): total number of nvr
        total_ipcs (int | Unset): total number of ipc
        wired_clients (int | Unset): total number of wired client
        wireless_clients (int | Unset): total number of wireless client
        total_clients (int | Unset): total number of client
        total_traffic (int | Unset): total traffic
        wired_traffic (int | Unset): total traffic of wired device
        wireless_traffic (int | Unset): total traffic of wireless device
    """

    site_health_score: int | Unset = UNSET
    wifi_health_score: int | Unset = UNSET
    device_health_score: int | Unset = UNSET
    client_health_score: int | Unset = UNSET
    wan_health_score: int | Unset = UNSET
    total_devices: int | Unset = UNSET
    total_gateways: int | Unset = UNSET
    total_switches: int | Unset = UNSET
    total_aps: int | Unset = UNSET
    total_olts: int | Unset = UNSET
    total_nvrs: int | Unset = UNSET
    total_ipcs: int | Unset = UNSET
    wired_clients: int | Unset = UNSET
    wireless_clients: int | Unset = UNSET
    total_clients: int | Unset = UNSET
    total_traffic: int | Unset = UNSET
    wired_traffic: int | Unset = UNSET
    wireless_traffic: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_health_score = self.site_health_score

        wifi_health_score = self.wifi_health_score

        device_health_score = self.device_health_score

        client_health_score = self.client_health_score

        wan_health_score = self.wan_health_score

        total_devices = self.total_devices

        total_gateways = self.total_gateways

        total_switches = self.total_switches

        total_aps = self.total_aps

        total_olts = self.total_olts

        total_nvrs = self.total_nvrs

        total_ipcs = self.total_ipcs

        wired_clients = self.wired_clients

        wireless_clients = self.wireless_clients

        total_clients = self.total_clients

        total_traffic = self.total_traffic

        wired_traffic = self.wired_traffic

        wireless_traffic = self.wireless_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_health_score is not UNSET:
            field_dict["siteHealthScore"] = site_health_score
        if wifi_health_score is not UNSET:
            field_dict["wifiHealthScore"] = wifi_health_score
        if device_health_score is not UNSET:
            field_dict["deviceHealthScore"] = device_health_score
        if client_health_score is not UNSET:
            field_dict["clientHealthScore"] = client_health_score
        if wan_health_score is not UNSET:
            field_dict["wanHealthScore"] = wan_health_score
        if total_devices is not UNSET:
            field_dict["totalDevices"] = total_devices
        if total_gateways is not UNSET:
            field_dict["totalGateways"] = total_gateways
        if total_switches is not UNSET:
            field_dict["totalSwitches"] = total_switches
        if total_aps is not UNSET:
            field_dict["totalAps"] = total_aps
        if total_olts is not UNSET:
            field_dict["totalOlts"] = total_olts
        if total_nvrs is not UNSET:
            field_dict["totalNvrs"] = total_nvrs
        if total_ipcs is not UNSET:
            field_dict["totalIpcs"] = total_ipcs
        if wired_clients is not UNSET:
            field_dict["wiredClients"] = wired_clients
        if wireless_clients is not UNSET:
            field_dict["wirelessClients"] = wireless_clients
        if total_clients is not UNSET:
            field_dict["totalClients"] = total_clients
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if wired_traffic is not UNSET:
            field_dict["wiredTraffic"] = wired_traffic
        if wireless_traffic is not UNSET:
            field_dict["wirelessTraffic"] = wireless_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_health_score = d.pop("siteHealthScore", UNSET)

        wifi_health_score = d.pop("wifiHealthScore", UNSET)

        device_health_score = d.pop("deviceHealthScore", UNSET)

        client_health_score = d.pop("clientHealthScore", UNSET)

        wan_health_score = d.pop("wanHealthScore", UNSET)

        total_devices = d.pop("totalDevices", UNSET)

        total_gateways = d.pop("totalGateways", UNSET)

        total_switches = d.pop("totalSwitches", UNSET)

        total_aps = d.pop("totalAps", UNSET)

        total_olts = d.pop("totalOlts", UNSET)

        total_nvrs = d.pop("totalNvrs", UNSET)

        total_ipcs = d.pop("totalIpcs", UNSET)

        wired_clients = d.pop("wiredClients", UNSET)

        wireless_clients = d.pop("wirelessClients", UNSET)

        total_clients = d.pop("totalClients", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        wired_traffic = d.pop("wiredTraffic", UNSET)

        wireless_traffic = d.pop("wirelessTraffic", UNSET)

        over_view_summary_vo = cls(
            site_health_score=site_health_score,
            wifi_health_score=wifi_health_score,
            device_health_score=device_health_score,
            client_health_score=client_health_score,
            wan_health_score=wan_health_score,
            total_devices=total_devices,
            total_gateways=total_gateways,
            total_switches=total_switches,
            total_aps=total_aps,
            total_olts=total_olts,
            total_nvrs=total_nvrs,
            total_ipcs=total_ipcs,
            wired_clients=wired_clients,
            wireless_clients=wireless_clients,
            total_clients=total_clients,
            total_traffic=total_traffic,
            wired_traffic=wired_traffic,
            wireless_traffic=wireless_traffic,
        )

        over_view_summary_vo.additional_properties = d
        return over_view_summary_vo

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
