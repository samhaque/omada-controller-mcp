from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WifiCallingTrafficOpenApiVO")


@_attrs_define
class WifiCallingTrafficOpenApiVO:
    """Top k ePDGs based on voice call traffic statistics.

    Attributes:
        client_name (str | Unset): Client name.
        ap_name (str | Unset): The name of the AP device connected to the client.
        ap_mac (str | Unset): Ap MAC.
        client_mac (str | Unset): Client Mac Address
        ip (str | Unset): Client ip or ipv6.
        carrier_name (str | Unset): Carrier name used by the client.
        wifi_calling_profile_name (str | Unset): Wifi calling profile name used by the client.
        priority (int | Unset): Priority of ePDG in the WiFi calling profile.
        ssid (str | Unset): The name of the SSID that the client is connected to.
        band (int | Unset): SSID band. The lowest bit indicates whether 2.4G is included; the second lowest bit
            indicates whether 5G is included; the third lowest bit indicates whether 6G is included; 1 means included while
            0 means not included. For example, 7(111) means that 2G/5G/6G are enabled; 1(001) means that 2G is enabled.
            (When 5G is included，it means 5G/5G1/5G2 are enabled.)
        domain (str | Unset): EPDG domain name or IP.
        total_traffic (int | Unset): Total traffic.
        traffic_down (int | Unset): Downlink traffic related to voice calls.
        traffic_up (int | Unset): Uplink traffic related to voice calls.
        start_time (int | Unset): Start time of the voice call.
        end_time (int | Unset): End time of the voice call.
        call_num (int | Unset): Number of calls on the same client MAC.
        device_type (str | Unset): Client device type.
        model (str | Unset): Client model.
    """

    client_name: str | Unset = UNSET
    ap_name: str | Unset = UNSET
    ap_mac: str | Unset = UNSET
    client_mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    carrier_name: str | Unset = UNSET
    wifi_calling_profile_name: str | Unset = UNSET
    priority: int | Unset = UNSET
    ssid: str | Unset = UNSET
    band: int | Unset = UNSET
    domain: str | Unset = UNSET
    total_traffic: int | Unset = UNSET
    traffic_down: int | Unset = UNSET
    traffic_up: int | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    call_num: int | Unset = UNSET
    device_type: str | Unset = UNSET
    model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client_name = self.client_name

        ap_name = self.ap_name

        ap_mac = self.ap_mac

        client_mac = self.client_mac

        ip = self.ip

        carrier_name = self.carrier_name

        wifi_calling_profile_name = self.wifi_calling_profile_name

        priority = self.priority

        ssid = self.ssid

        band = self.band

        domain = self.domain

        total_traffic = self.total_traffic

        traffic_down = self.traffic_down

        traffic_up = self.traffic_up

        start_time = self.start_time

        end_time = self.end_time

        call_num = self.call_num

        device_type = self.device_type

        model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if ap_name is not UNSET:
            field_dict["apName"] = ap_name
        if ap_mac is not UNSET:
            field_dict["apMac"] = ap_mac
        if client_mac is not UNSET:
            field_dict["clientMac"] = client_mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if carrier_name is not UNSET:
            field_dict["carrierName"] = carrier_name
        if wifi_calling_profile_name is not UNSET:
            field_dict["wifiCallingProfileName"] = wifi_calling_profile_name
        if priority is not UNSET:
            field_dict["priority"] = priority
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if band is not UNSET:
            field_dict["band"] = band
        if domain is not UNSET:
            field_dict["domain"] = domain
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if traffic_down is not UNSET:
            field_dict["trafficDown"] = traffic_down
        if traffic_up is not UNSET:
            field_dict["trafficUp"] = traffic_up
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if call_num is not UNSET:
            field_dict["callNum"] = call_num
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client_name = d.pop("clientName", UNSET)

        ap_name = d.pop("apName", UNSET)

        ap_mac = d.pop("apMac", UNSET)

        client_mac = d.pop("clientMac", UNSET)

        ip = d.pop("ip", UNSET)

        carrier_name = d.pop("carrierName", UNSET)

        wifi_calling_profile_name = d.pop("wifiCallingProfileName", UNSET)

        priority = d.pop("priority", UNSET)

        ssid = d.pop("ssid", UNSET)

        band = d.pop("band", UNSET)

        domain = d.pop("domain", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        traffic_down = d.pop("trafficDown", UNSET)

        traffic_up = d.pop("trafficUp", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        call_num = d.pop("callNum", UNSET)

        device_type = d.pop("deviceType", UNSET)

        model = d.pop("model", UNSET)

        wifi_calling_traffic_open_api_vo = cls(
            client_name=client_name,
            ap_name=ap_name,
            ap_mac=ap_mac,
            client_mac=client_mac,
            ip=ip,
            carrier_name=carrier_name,
            wifi_calling_profile_name=wifi_calling_profile_name,
            priority=priority,
            ssid=ssid,
            band=band,
            domain=domain,
            total_traffic=total_traffic,
            traffic_down=traffic_down,
            traffic_up=traffic_up,
            start_time=start_time,
            end_time=end_time,
            call_num=call_num,
            device_type=device_type,
            model=model,
        )

        wifi_calling_traffic_open_api_vo.additional_properties = d
        return wifi_calling_traffic_open_api_vo

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
