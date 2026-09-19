from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientQueryFiltersOpenApiVO")


@_attrs_define
class ClientQueryFiltersOpenApiVO:
    """Filters of the query.

    Attributes:
        wireless (bool | Unset): Filter by wireless, This filter will not affect clientStat result.
        ipc_nvr (bool | Unset): Filter by ipcNvr, This filter will not affect clientStat result. true : filter by client
            type IPC or NVR, false or null: NOT filter by client type.
        ip_exist (bool | Unset): Filter by ipExist. true : Filter clients with existing IP addresses, false or null:
            unfiltered client.
        guest (list[bool] | Unset): Filter by guest, effective only when wireless is true.
        radio_id (list[int] | Unset): Filter by radio Id. 0 : 2.4G, 1 : 5G-1, 2 : 5G-2, 3 : 6G
        device_mac (list[str] | Unset): Filter by the mac of connected device.
        device (list[str] | Unset): Filter by the name of connected device.
        device_type (list[str] | Unset): Filter by the type of client.
        model (str | Unset): Filter by the model.
        vendor (list[str] | Unset): Filter by vendor.
        ssid (list[str] | Unset): Filter by ssid.
        network (list[str] | Unset): Filter by lan network name.
        vid (str | Unset): Filter by VLAN id, vid should be a string like 1,100-200.
        time_start (int | Unset): Filter by lastSeen.
        time_end (int | Unset): Filter by lastSeen.
        auth_status (list[int] | Unset): Filter by authStatus, 0: CONNECTED, 1: PENDING, 2: AUTHED, 3: AUTH_FREE
        auth_type (str | Unset): Filter by authentication type
        source_time (int | Unset): Filter by history health data.
        health (int | Unset): Filter by health score, 0:No Data, 1 : poor 2 : fair 3 : good
    """

    wireless: bool | Unset = UNSET
    ipc_nvr: bool | Unset = UNSET
    ip_exist: bool | Unset = UNSET
    guest: list[bool] | Unset = UNSET
    radio_id: list[int] | Unset = UNSET
    device_mac: list[str] | Unset = UNSET
    device: list[str] | Unset = UNSET
    device_type: list[str] | Unset = UNSET
    model: str | Unset = UNSET
    vendor: list[str] | Unset = UNSET
    ssid: list[str] | Unset = UNSET
    network: list[str] | Unset = UNSET
    vid: str | Unset = UNSET
    time_start: int | Unset = UNSET
    time_end: int | Unset = UNSET
    auth_status: list[int] | Unset = UNSET
    auth_type: str | Unset = UNSET
    source_time: int | Unset = UNSET
    health: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wireless = self.wireless

        ipc_nvr = self.ipc_nvr

        ip_exist = self.ip_exist

        guest: list[bool] | Unset = UNSET
        if not isinstance(self.guest, Unset):
            guest = self.guest

        radio_id: list[int] | Unset = UNSET
        if not isinstance(self.radio_id, Unset):
            radio_id = self.radio_id

        device_mac: list[str] | Unset = UNSET
        if not isinstance(self.device_mac, Unset):
            device_mac = self.device_mac

        device: list[str] | Unset = UNSET
        if not isinstance(self.device, Unset):
            device = self.device

        device_type: list[str] | Unset = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type

        model = self.model

        vendor: list[str] | Unset = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor

        ssid: list[str] | Unset = UNSET
        if not isinstance(self.ssid, Unset):
            ssid = self.ssid

        network: list[str] | Unset = UNSET
        if not isinstance(self.network, Unset):
            network = self.network

        vid = self.vid

        time_start = self.time_start

        time_end = self.time_end

        auth_status: list[int] | Unset = UNSET
        if not isinstance(self.auth_status, Unset):
            auth_status = self.auth_status

        auth_type = self.auth_type

        source_time = self.source_time

        health = self.health

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if ipc_nvr is not UNSET:
            field_dict["ipcNvr"] = ipc_nvr
        if ip_exist is not UNSET:
            field_dict["ipExist"] = ip_exist
        if guest is not UNSET:
            field_dict["guest"] = guest
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if device is not UNSET:
            field_dict["device"] = device
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if model is not UNSET:
            field_dict["model"] = model
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if network is not UNSET:
            field_dict["network"] = network
        if vid is not UNSET:
            field_dict["vid"] = vid
        if time_start is not UNSET:
            field_dict["timeStart"] = time_start
        if time_end is not UNSET:
            field_dict["timeEnd"] = time_end
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if source_time is not UNSET:
            field_dict["sourceTime"] = source_time
        if health is not UNSET:
            field_dict["health"] = health

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wireless = d.pop("wireless", UNSET)

        ipc_nvr = d.pop("ipcNvr", UNSET)

        ip_exist = d.pop("ipExist", UNSET)

        guest = cast(list[bool], d.pop("guest", UNSET))

        radio_id = cast(list[int], d.pop("radioId", UNSET))

        device_mac = cast(list[str], d.pop("deviceMac", UNSET))

        device = cast(list[str], d.pop("device", UNSET))

        device_type = cast(list[str], d.pop("deviceType", UNSET))

        model = d.pop("model", UNSET)

        vendor = cast(list[str], d.pop("vendor", UNSET))

        ssid = cast(list[str], d.pop("ssid", UNSET))

        network = cast(list[str], d.pop("network", UNSET))

        vid = d.pop("vid", UNSET)

        time_start = d.pop("timeStart", UNSET)

        time_end = d.pop("timeEnd", UNSET)

        auth_status = cast(list[int], d.pop("authStatus", UNSET))

        auth_type = d.pop("authType", UNSET)

        source_time = d.pop("sourceTime", UNSET)

        health = d.pop("health", UNSET)

        client_query_filters_open_api_vo = cls(
            wireless=wireless,
            ipc_nvr=ipc_nvr,
            ip_exist=ip_exist,
            guest=guest,
            radio_id=radio_id,
            device_mac=device_mac,
            device=device,
            device_type=device_type,
            model=model,
            vendor=vendor,
            ssid=ssid,
            network=network,
            vid=vid,
            time_start=time_start,
            time_end=time_end,
            auth_status=auth_status,
            auth_type=auth_type,
            source_time=source_time,
            health=health,
        )

        client_query_filters_open_api_vo.additional_properties = d
        return client_query_filters_open_api_vo

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
