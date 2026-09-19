from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DashboardVpnStats")


@_attrs_define
class DashboardVpnStats:
    """
    Attributes:
        site (str | Unset): Site
        name (str | Unset): VPN name
        status (bool | Unset): Whether VPN is enabled
        tunnels (int | Unset): The number of tunnels included in the VPN server
        tx_data (int | Unset): The total tx traffic of the channels included in the server/client, in Byte
        rx_data (int | Unset): The total rx traffic of the tunnels included in the server/client, in Byte
    """

    site: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    tunnels: int | Unset = UNSET
    tx_data: int | Unset = UNSET
    rx_data: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site = self.site

        name = self.name

        status = self.status

        tunnels = self.tunnels

        tx_data = self.tx_data

        rx_data = self.rx_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site is not UNSET:
            field_dict["site"] = site
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if tunnels is not UNSET:
            field_dict["tunnels"] = tunnels
        if tx_data is not UNSET:
            field_dict["txData"] = tx_data
        if rx_data is not UNSET:
            field_dict["rxData"] = rx_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site = d.pop("site", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        tunnels = d.pop("tunnels", UNSET)

        tx_data = d.pop("txData", UNSET)

        rx_data = d.pop("rxData", UNSET)

        dashboard_vpn_stats = cls(
            site=site,
            name=name,
            status=status,
            tunnels=tunnels,
            tx_data=tx_data,
            rx_data=rx_data,
        )

        dashboard_vpn_stats.additional_properties = d
        return dashboard_vpn_stats

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
