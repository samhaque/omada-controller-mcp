from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpServerRangeVO")


@_attrs_define
class DhcpServerRangeVO:
    """Dhcp Server Ranges

    Attributes:
        start_ip (str | Unset): Start IP
        end_ip (str | Unset): End IP
        available_ip_num (int | Unset): The number of available IP addresses in the server address pool.
    """

    start_ip: str | Unset = UNSET
    end_ip: str | Unset = UNSET
    available_ip_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_ip = self.start_ip

        end_ip = self.end_ip

        available_ip_num = self.available_ip_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if start_ip is not UNSET:
            field_dict["startIp"] = start_ip
        if end_ip is not UNSET:
            field_dict["endIp"] = end_ip
        if available_ip_num is not UNSET:
            field_dict["availableIpNum"] = available_ip_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start_ip = d.pop("startIp", UNSET)

        end_ip = d.pop("endIp", UNSET)

        available_ip_num = d.pop("availableIpNum", UNSET)

        dhcp_server_range_vo = cls(
            start_ip=start_ip,
            end_ip=end_ip,
            available_ip_num=available_ip_num,
        )

        dhcp_server_range_vo.additional_properties = d
        return dhcp_server_range_vo

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
