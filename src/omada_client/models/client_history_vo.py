from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_info_vo import AuthInfoVO


T = TypeVar("T", bound="ClientHistoryVO")


@_attrs_define
class ClientHistoryVO:
    """
    Attributes:
        id (str | Unset):
        mac (str | Unset):
        download (int | Unset):
        upload (int | Unset):
        duration (int | Unset):
        last_seen (int | Unset):
        name (str | Unset):
        ssid (str | Unset):
        port (int | Unset):
        vid (int | Unset):
        reason (str | Unset):
        reason_type (int | Unset):
        guest (bool | Unset):
        device_name (str | Unset):
        association_time (int | Unset):
        associated (int | Unset):
        ip (str | Unset):
        ipv_6_list (list[str] | Unset):
        auth_info (list[AuthInfoVO] | Unset):
    """

    id: str | Unset = UNSET
    mac: str | Unset = UNSET
    download: int | Unset = UNSET
    upload: int | Unset = UNSET
    duration: int | Unset = UNSET
    last_seen: int | Unset = UNSET
    name: str | Unset = UNSET
    ssid: str | Unset = UNSET
    port: int | Unset = UNSET
    vid: int | Unset = UNSET
    reason: str | Unset = UNSET
    reason_type: int | Unset = UNSET
    guest: bool | Unset = UNSET
    device_name: str | Unset = UNSET
    association_time: int | Unset = UNSET
    associated: int | Unset = UNSET
    ip: str | Unset = UNSET
    ipv_6_list: list[str] | Unset = UNSET
    auth_info: list[AuthInfoVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        mac = self.mac

        download = self.download

        upload = self.upload

        duration = self.duration

        last_seen = self.last_seen

        name = self.name

        ssid = self.ssid

        port = self.port

        vid = self.vid

        reason = self.reason

        reason_type = self.reason_type

        guest = self.guest

        device_name = self.device_name

        association_time = self.association_time

        associated = self.associated

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
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if name is not UNSET:
            field_dict["name"] = name
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if port is not UNSET:
            field_dict["port"] = port
        if vid is not UNSET:
            field_dict["vid"] = vid
        if reason is not UNSET:
            field_dict["reason"] = reason
        if reason_type is not UNSET:
            field_dict["reasonType"] = reason_type
        if guest is not UNSET:
            field_dict["guest"] = guest
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if association_time is not UNSET:
            field_dict["associationTime"] = association_time
        if associated is not UNSET:
            field_dict["associated"] = associated
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_list is not UNSET:
            field_dict["ipv6List"] = ipv_6_list
        if auth_info is not UNSET:
            field_dict["authInfo"] = auth_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_info_vo import AuthInfoVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        mac = d.pop("mac", UNSET)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        duration = d.pop("duration", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        name = d.pop("name", UNSET)

        ssid = d.pop("ssid", UNSET)

        port = d.pop("port", UNSET)

        vid = d.pop("vid", UNSET)

        reason = d.pop("reason", UNSET)

        reason_type = d.pop("reasonType", UNSET)

        guest = d.pop("guest", UNSET)

        device_name = d.pop("deviceName", UNSET)

        association_time = d.pop("associationTime", UNSET)

        associated = d.pop("associated", UNSET)

        ip = d.pop("ip", UNSET)

        ipv_6_list = cast(list[str], d.pop("ipv6List", UNSET))

        _auth_info = d.pop("authInfo", UNSET)
        auth_info: list[AuthInfoVO] | Unset = UNSET
        if _auth_info is not UNSET:
            auth_info = []
            for auth_info_item_data in _auth_info:
                auth_info_item = AuthInfoVO.from_dict(auth_info_item_data)

                auth_info.append(auth_info_item)

        client_history_vo = cls(
            id=id,
            mac=mac,
            download=download,
            upload=upload,
            duration=duration,
            last_seen=last_seen,
            name=name,
            ssid=ssid,
            port=port,
            vid=vid,
            reason=reason,
            reason_type=reason_type,
            guest=guest,
            device_name=device_name,
            association_time=association_time,
            associated=associated,
            ip=ip,
            ipv_6_list=ipv_6_list,
            auth_info=auth_info,
        )

        client_history_vo.additional_properties = d
        return client_history_vo

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
