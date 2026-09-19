from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="QueryDhcpLeaseTimeParamVO")


@_attrs_define
class QueryDhcpLeaseTimeParamVO:
    """
    Attributes:
        mac (str): the mac you want to get dhcp-lease-time.
        ip_address (str): the ipAddress you want to get dhcp-lease-time.
    """

    mac: str
    ip_address: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip_address = self.ip_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "ipAddress": ip_address,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        ip_address = d.pop("ipAddress")

        query_dhcp_lease_time_param_vo = cls(
            mac=mac,
            ip_address=ip_address,
        )

        query_dhcp_lease_time_param_vo.additional_properties = d
        return query_dhcp_lease_time_param_vo

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
