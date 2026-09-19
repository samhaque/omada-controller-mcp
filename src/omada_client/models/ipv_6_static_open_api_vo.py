from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Ipv6StaticOpenApiVO")


@_attrs_define
class Ipv6StaticOpenApiVO:
    """It is required when protoType is static

    Attributes:
        address (str):
        prefix_len (int): It should be within the range of 1–128
        default_gateway (str):
        primary_dns (str):
        secondary_dns (str | Unset):
    """

    address: str
    prefix_len: int
    default_gateway: str
    primary_dns: str
    secondary_dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        prefix_len = self.prefix_len

        default_gateway = self.default_gateway

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "prefixLen": prefix_len,
                "defaultGateway": default_gateway,
                "primaryDns": primary_dns,
            }
        )
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        address = d.pop("address")

        prefix_len = d.pop("prefixLen")

        default_gateway = d.pop("defaultGateway")

        primary_dns = d.pop("primaryDns")

        secondary_dns = d.pop("secondaryDns", UNSET)

        ipv_6_static_open_api_vo = cls(
            address=address,
            prefix_len=prefix_len,
            default_gateway=default_gateway,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
        )

        ipv_6_static_open_api_vo.additional_properties = d
        return ipv_6_static_open_api_vo

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
