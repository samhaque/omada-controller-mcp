from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwitchSummary")


@_attrs_define
class SwitchSummary:
    """
    Attributes:
        clients (int | Unset): Number of wired clients
        port_utilization (int | Unset): Port occupancy rate (integer)
        connected_switch_num (int | Unset): Number of online switches
        total_traffic (int | Unset): Upstream and downstream traffic and the unit (Byte) of online switches
    """

    clients: int | Unset = UNSET
    port_utilization: int | Unset = UNSET
    connected_switch_num: int | Unset = UNSET
    total_traffic: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        clients = self.clients

        port_utilization = self.port_utilization

        connected_switch_num = self.connected_switch_num

        total_traffic = self.total_traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clients is not UNSET:
            field_dict["clients"] = clients
        if port_utilization is not UNSET:
            field_dict["portUtilization"] = port_utilization
        if connected_switch_num is not UNSET:
            field_dict["connectedSwitchNum"] = connected_switch_num
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        clients = d.pop("clients", UNSET)

        port_utilization = d.pop("portUtilization", UNSET)

        connected_switch_num = d.pop("connectedSwitchNum", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        switch_summary = cls(
            clients=clients,
            port_utilization=port_utilization,
            connected_switch_num=connected_switch_num,
            total_traffic=total_traffic,
        )

        switch_summary.additional_properties = d
        return switch_summary

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
