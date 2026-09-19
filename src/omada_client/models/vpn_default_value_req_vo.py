from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnDefaultValueReqVO")


@_attrs_define
class VpnDefaultValueReqVO:
    """
    Attributes:
        type_ (int): Parameter [type] should be a value as follows: 0, name; 1, port; 2, tunnelIp.
        usage (int | Unset): Parameter [usage] should not be null when parameter [type] is name. Parameter [usage]
            should be a value as follows: 0, server; 1, client; 2, site-to-site.
        vpn_type (int | Unset): Parameter [vpnType] should not be null when parameter [type] is port. Parameter
            [vpnType] should be a value as follows: 3, Open VPN; 4, Wire Guard; 5, SSL VPN.
    """

    type_: int
    usage: int | Unset = UNSET
    vpn_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        usage = self.usage

        vpn_type = self.vpn_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage
        if vpn_type is not UNSET:
            field_dict["vpnType"] = vpn_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        usage = d.pop("usage", UNSET)

        vpn_type = d.pop("vpnType", UNSET)

        vpn_default_value_req_vo = cls(
            type_=type_,
            usage=usage,
            vpn_type=vpn_type,
        )

        vpn_default_value_req_vo.additional_properties = d
        return vpn_default_value_req_vo

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
