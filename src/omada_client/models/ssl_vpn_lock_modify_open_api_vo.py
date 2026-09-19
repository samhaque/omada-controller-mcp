from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SslVpnLockModifyOpenApiVO")


@_attrs_define
class SslVpnLockModifyOpenApiVO:
    """
    Attributes:
        type_ (int): Type of the SSL VPN lock should be a value as follows: 0:username, 1:IP. It can not be modified.
        total_lock_time (int): Total lock time of the SSL VPN lock should be within the range of 1–1080(min).
        username (str | Unset): Username of the SSL VPN lock. It is required when parameter [type] is 0.
        ip (str | Unset): IP of the SSL VPN lock. It is required when parameter [type] is 1.
    """

    type_: int
    total_lock_time: int
    username: str | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        total_lock_time = self.total_lock_time

        username = self.username

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "totalLockTime": total_lock_time,
            }
        )
        if username is not UNSET:
            field_dict["username"] = username
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        total_lock_time = d.pop("totalLockTime")

        username = d.pop("username", UNSET)

        ip = d.pop("ip", UNSET)

        ssl_vpn_lock_modify_open_api_vo = cls(
            type_=type_,
            total_lock_time=total_lock_time,
            username=username,
            ip=ip,
        )

        ssl_vpn_lock_modify_open_api_vo.additional_properties = d
        return ssl_vpn_lock_modify_open_api_vo

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
