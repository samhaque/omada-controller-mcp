from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_info_open_api_vo import AuthInfoOpenApiVO


T = TypeVar("T", bound="ClientHistoryInfo")


@_attrs_define
class ClientHistoryInfo:
    """
    Attributes:
        id (str | Unset): Client History ID.
        mac (str | Unset): Client MAC Address.
        download (int | Unset): Downstream traffic (Byte).
        upload (int | Unset): Upstream traffic (Byte).
        duration (int | Unset): Up time (unit: s).
        first_seen (int | Unset): The timestamp (ms) when the client connected.
        last_seen (int | Unset): Last found time, timestamp (ms).
        name (str | Unset): Client Name.
        ssid (str | Unset): (Wireless)  SSID name.
        port (int | Unset): (Wired) Port ID.
        guest (bool | Unset): (Wireless) Whether it is Guest (used to display the wireless Guest client icon).
        device_name (str | Unset): Device name.
        association_time (int | Unset): (Wireless) The time (ms) it takes for the client to connect to SSID.
        ip (str | Unset): IP Address.
        ipv_6_list (list[str] | Unset): IPv6 Address.
        auth_info (list[AuthInfoOpenApiVO] | Unset): Client portal authentication information
    """

    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    download: int | Unset = UNSET
    upload: int | Unset = UNSET
    duration: int | Unset = UNSET
    first_seen: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    name: str | Unset = UNSET
    ssid: str | Unset = UNSET
    port: int | Unset = UNSET
    guest: bool | Unset = UNSET
    device_name: str | Unset = UNSET
    association_time: int | Unset = UNSET
    ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    auth_info: list[AuthInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac = self.mac

        download = self.download

        upload = self.upload

        duration = self.duration

        first_seen = self.first_seen

        last_seen = self.last_seen

        name = self.name

        ssid = self.ssid

        port = self.port

        guest = self.guest

        device_name = self.device_name

        association_time = self.association_time

        ip = self.ip

        ipv_6_list: list[str] | Unset = UNSET
        if not isinstance(self.ipv_6_list, Unset):
            ipv_6_list = self.ipv_6_list

        auth_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.auth_info, Unset):
            auth_info = []
            for auth_info_item_data in self.auth_info:
                auth_info_item = auth_info_item_data.to_dict()
                auth_info.append(auth_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if duration is not UNSET:
            field_dict["duration"] = duration
        if first_seen is not UNSET:
            field_dict["firstSeen"] = first_seen
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if name is not UNSET:
            field_dict["name"] = name
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if port is not UNSET:
            field_dict["port"] = port
        if guest is not UNSET:
            field_dict["guest"] = guest
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if association_time is not UNSET:
            field_dict["associationTime"] = association_time
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if auth_info is not UNSET:
            field_dict["authInfo"] = auth_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_info_open_api_vo import AuthInfoOpenApiVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        duration = d.pop("duration", UNSET)

        first_seen = d.pop("firstSeen", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        name = d.pop("name", UNSET)

        ssid = d.pop("ssid", UNSET)

        port = d.pop("port", UNSET)

        guest = d.pop("guest", UNSET)

        device_name = d.pop("deviceName", UNSET)

        association_time = d.pop("associationTime", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        _auth_info = d.pop("authInfo", UNSET)
        auth_info: list[AuthInfoOpenApiVO] | Unset = UNSET
        if _auth_info is not UNSET:
            auth_info = []
            for auth_info_item_data in _auth_info:
                auth_info_item = AuthInfoOpenApiVO.from_dict(auth_info_item_data)

                auth_info.append(auth_info_item)

        client_history_info = cls(
            id=id,
            mac=mac,
            download=download,
            upload=upload,
            duration=duration,
            first_seen=first_seen,
            last_seen=last_seen,
            name=name,
            ssid=ssid,
            port=port,
            guest=guest,
            device_name=device_name,
            association_time=association_time,
            ip=ip,
            ipv_6_list=ipv_6_list,
            auth_info=auth_info,
        )

        client_history_info.additional_properties = d
        return client_history_info

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
