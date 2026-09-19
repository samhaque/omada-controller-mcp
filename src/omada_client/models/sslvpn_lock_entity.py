from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SSLVPNLockEntity")


@_attrs_define
class SSLVPNLockEntity:
    """
    Attributes:
        type_ (int): Type of the SSL VPN lock should be a value as follows: 0:username; 1:IP
        total_lock_time (int): Total lock time of the SSL VPN lock should be within the range of 1–1080(min).
        id (str | Unset): ID of the SSL VPN lock
        username (str | Unset): Username of the SSL VPN lock
        ip (str | Unset): IP of the SSL VPN lock
        left_lock_time (int | Unset): Left lock time(min) of the SSL VPN lock.
    """

    type_: int
    total_lock_time: int
    id: str | Unset = UNSET
    username: str | Unset = UNSET
    ip: str | Unset = UNSET
    left_lock_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        total_lock_time = self.total_lock_time

        id = self.id

        username = self.username

        ip = self.ip

        left_lock_time = self.left_lock_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "totalLockTime": total_lock_time,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if username is not UNSET:
            field_dict["username"] = username
        if ip is not UNSET:
            field_dict["ip"] = ip
        if left_lock_time is not UNSET:
            field_dict["leftLockTime"] = left_lock_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        total_lock_time = d.pop("totalLockTime")

        id = d.pop("id", UNSET)

        username = d.pop("username", UNSET)

        ip = d.pop("ip", UNSET)

        left_lock_time = d.pop("leftLockTime", UNSET)

        sslvpn_lock_entity = cls(
            type_=type_,
            total_lock_time=total_lock_time,
            id=id,
            username=username,
            ip=ip,
            left_lock_time=left_lock_time,
        )

        sslvpn_lock_entity.additional_properties = d
        return sslvpn_lock_entity

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
