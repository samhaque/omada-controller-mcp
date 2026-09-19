from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IspVO")


@_attrs_define
class IspVO:
    """Isp info detail.

    Attributes:
        port (int | Unset): Port id.
        name (str | Unset): Port name.
        port_uuid (str | Unset): Port uuid.
        max_bandwidth (int | Unset): Port max bandwidth.
        download_speed_set (int | Unset): The set download speed.
        upload_speed_set (int | Unset): The set upload speed.
        download_speed (str | Unset): The current download speed.
        upload_speed (str | Unset): The current upload speed.
        download_percent (float | Unset): Download utilization.
        upload_percent (float | Unset): Upload utilization.
        ip (str | Unset): Port ip.
        load_balance (str | Unset): Port load balance.
        status (int | Unset): Isp status, should be a value as follows:2 : normal ISP1 : primary ISP0 : backup ISP
        on_line_status (int | Unset): onLine status, should be a value as follows:1 : online0 : offline
        ipv_4_proto (str | Unset): WAN IPv4 proto.
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    port_uuid: str | Unset = UNSET
    max_bandwidth: int | Unset = UNSET
    download_speed_set: int | Unset = UNSET
    upload_speed_set: int | Unset = UNSET
    download_speed: str | Unset = UNSET
    upload_speed: str | Unset = UNSET
    download_percent: float | Unset = UNSET
    upload_percent: float | Unset = UNSET
    ip: str | Unset = UNSET
    load_balance: str | Unset = UNSET
    status: int | Unset = UNSET
    on_line_status: int | Unset = UNSET
    ipv_4_proto: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        port_uuid = self.port_uuid

        max_bandwidth = self.max_bandwidth

        download_speed_set = self.download_speed_set

        upload_speed_set = self.upload_speed_set

        download_speed = self.download_speed

        upload_speed = self.upload_speed

        download_percent = self.download_percent

        upload_percent = self.upload_percent

        ip = self.ip

        load_balance = self.load_balance

        status = self.status

        on_line_status = self.on_line_status

        ipv_4_proto = self.ipv_4_proto

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid
        if max_bandwidth is not UNSET:
            field_dict["maxBandwidth"] = max_bandwidth
        if download_speed_set is not UNSET:
            field_dict["downloadSpeedSet"] = download_speed_set
        if upload_speed_set is not UNSET:
            field_dict["uploadSpeedSet"] = upload_speed_set
        if download_speed is not UNSET:
            field_dict["downloadSpeed"] = download_speed
        if upload_speed is not UNSET:
            field_dict["uploadSpeed"] = upload_speed
        if download_percent is not UNSET:
            field_dict["downloadPercent"] = download_percent
        if upload_percent is not UNSET:
            field_dict["uploadPercent"] = upload_percent
        if ip is not UNSET:
            field_dict["ip"] = ip
        if load_balance is not UNSET:
            field_dict["loadBalance"] = load_balance
        if status is not UNSET:
            field_dict["status"] = status
        if on_line_status is not UNSET:
            field_dict["onLineStatus"] = on_line_status
        if ipv_4_proto is not UNSET:
            field_dict["ipv4Proto"] = ipv_4_proto

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        port_uuid = d.pop("portUuid", UNSET)

        max_bandwidth = d.pop("maxBandwidth", UNSET)

        download_speed_set = d.pop("downloadSpeedSet", UNSET)

        upload_speed_set = d.pop("uploadSpeedSet", UNSET)

        download_speed = d.pop("downloadSpeed", UNSET)

        upload_speed = d.pop("uploadSpeed", UNSET)

        download_percent = d.pop("downloadPercent", UNSET)

        upload_percent = d.pop("uploadPercent", UNSET)

        ip = d.pop("ip", UNSET)

        load_balance = d.pop("loadBalance", UNSET)

        status = d.pop("status", UNSET)

        on_line_status = d.pop("onLineStatus", UNSET)

        ipv_4_proto = d.pop("ipv4Proto", UNSET)

        isp_vo = cls(
            port=port,
            name=name,
            port_uuid=port_uuid,
            max_bandwidth=max_bandwidth,
            download_speed_set=download_speed_set,
            upload_speed_set=upload_speed_set,
            download_speed=download_speed,
            upload_speed=upload_speed,
            download_percent=download_percent,
            upload_percent=upload_percent,
            ip=ip,
            load_balance=load_balance,
            status=status,
            on_line_status=on_line_status,
            ipv_4_proto=ipv_4_proto,
        )

        isp_vo.additional_properties = d
        return isp_vo

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
