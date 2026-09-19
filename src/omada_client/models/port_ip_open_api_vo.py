from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortIpOpenApiVO")


@_attrs_define
class PortIpOpenApiVO:
    """WAN IPs. Wan IPs can be obtained from 'Get internet ports config' interface

    Attributes:
        wan_id (str | Unset): This field represents WAN port ID. WAN port ID can be obtained from can be obtained from
            'Get internet basic info' interface.
        ip (str | Unset): IP address
    """

    wan_id: str | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_id = self.wan_id

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wan_id is not UNSET:
            field_dict["wanId"] = wan_id
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        wan_id = d.pop("wanId", UNSET)

        ip = d.pop("ip", UNSET)

        port_ip_open_api_vo = cls(
            wan_id=wan_id,
            ip=ip,
        )

        port_ip_open_api_vo.additional_properties = d
        return port_ip_open_api_vo

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
