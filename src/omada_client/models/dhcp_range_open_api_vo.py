from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpRangeOpenApiVO")


@_attrs_define
class DhcpRangeOpenApiVO:
    """The list of DHCP Range, which size can't be more than "dhcpRangePoolSize", "dhcpRangePoolSize" can be obtained from
    'Get LAN network list' interface.

        Attributes:
            ipaddr_start (str | Unset): DHCP Range Start IP
            ipaddr_end (str | Unset): DHCP Range End IP
    """

    ipaddr_start: str | Unset = UNSET
    ipaddr_end: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipaddr_start = self.ipaddr_start

        ipaddr_end = self.ipaddr_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ipaddr_start is not UNSET:
            field_dict["ipaddrStart"] = ipaddr_start
        if ipaddr_end is not UNSET:
            field_dict["ipaddrEnd"] = ipaddr_end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ipaddr_start = d.pop("ipaddrStart", UNSET)

        ipaddr_end = d.pop("ipaddrEnd", UNSET)

        dhcp_range_open_api_vo = cls(
            ipaddr_start=ipaddr_start,
            ipaddr_end=ipaddr_end,
        )

        dhcp_range_open_api_vo.additional_properties = d
        return dhcp_range_open_api_vo

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
