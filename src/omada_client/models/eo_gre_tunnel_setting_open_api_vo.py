from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EoGreTunnelSettingOpenApiVO")


@_attrs_define
class EoGreTunnelSettingOpenApiVO:
    """
    Attributes:
        gre_enable (bool | Unset): EoGRE Tunnel global config status; True: enable, false: disable.
        tunnel_mtu (int | Unset): Maximum Transmission Unit. The value of parameter [tunnelMtu] should be between [850,
            1500].
        interval (int | Unset): EoGRE Tunnel keep interval config(Unit: Seconds); It should be within the range of
            10–600.
        max_count (int | Unset): EoGRE Tunnel max keepalive skip count config; It should be within the range of 3–10.
        primary_address (str | Unset): EoGRE Tunnel primary gateway IP address config
        secondary_address (str | Unset): EoGRE Tunnel secondary gateway IP address config
    """

    gre_enable: bool | Unset = UNSET
    tunnel_mtu: int | Unset = UNSET
    interval: int | Unset = UNSET
    max_count: int | Unset = UNSET
    primary_address: str | Unset = UNSET
    secondary_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gre_enable = self.gre_enable

        tunnel_mtu = self.tunnel_mtu

        interval = self.interval

        max_count = self.max_count

        primary_address = self.primary_address

        secondary_address = self.secondary_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gre_enable is not UNSET:
            field_dict["greEnable"] = gre_enable
        if tunnel_mtu is not UNSET:
            field_dict["tunnelMtu"] = tunnel_mtu
        if interval is not UNSET:
            field_dict["interval"] = interval
        if max_count is not UNSET:
            field_dict["maxCount"] = max_count
        if primary_address is not UNSET:
            field_dict["primaryAddress"] = primary_address
        if secondary_address is not UNSET:
            field_dict["secondaryAddress"] = secondary_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gre_enable = d.pop("greEnable", UNSET)

        tunnel_mtu = d.pop("tunnelMtu", UNSET)

        interval = d.pop("interval", UNSET)

        max_count = d.pop("maxCount", UNSET)

        primary_address = d.pop("primaryAddress", UNSET)

        secondary_address = d.pop("secondaryAddress", UNSET)

        eo_gre_tunnel_setting_open_api_vo = cls(
            gre_enable=gre_enable,
            tunnel_mtu=tunnel_mtu,
            interval=interval,
            max_count=max_count,
            primary_address=primary_address,
            secondary_address=secondary_address,
        )

        eo_gre_tunnel_setting_open_api_vo.additional_properties = d
        return eo_gre_tunnel_setting_open_api_vo

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
