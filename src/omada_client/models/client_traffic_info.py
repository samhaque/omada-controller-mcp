from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientTrafficInfo")


@_attrs_define
class ClientTrafficInfo:
    """Client traffic info.

    Attributes:
        total_traffic (int | Unset): Total traffic of all clients.
        wired_clients_traffic (int | Unset): Total traffic of all wired clients.
        clients_2_g_traffic (int | Unset): Total traffic of wireless clients in the 2G band.
        clients_5_g_traffic (int | Unset): Total traffic of wireless clients in the 5G band.
        clients_6_g_traffic (int | Unset): Total traffic of wireless clients in the 6G band.
        wired_clients_num (int | Unset): The number of all wired clients.
        clients_2_g_num (int | Unset): The number of wireless clients in the 2G band.
        clients_5_g_num (int | Unset): The number of wireless clients in the 5G band.
        clients_6_g_num (int | Unset): The number of wireless clients in the 6G band.
    """

    total_traffic: int | Unset = UNSET
    wired_clients_traffic: int | Unset = UNSET
    clients_2_g_traffic: int | Unset = UNSET
    clients_5_g_traffic: int | Unset = UNSET
    clients_6_g_traffic: int | Unset = UNSET
    wired_clients_num: int | Unset = UNSET
    clients_2_g_num: int | Unset = UNSET
    clients_5_g_num: int | Unset = UNSET
    clients_6_g_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_traffic = self.total_traffic

        wired_clients_traffic = self.wired_clients_traffic

        clients_2_g_traffic = self.clients_2_g_traffic

        clients_5_g_traffic = self.clients_5_g_traffic

        clients_6_g_traffic = self.clients_6_g_traffic

        wired_clients_num = self.wired_clients_num

        clients_2_g_num = self.clients_2_g_num

        clients_5_g_num = self.clients_5_g_num

        clients_6_g_num = self.clients_6_g_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if wired_clients_traffic is not UNSET:
            field_dict["wiredClientsTraffic"] = wired_clients_traffic
        if clients_2_g_traffic is not UNSET:
            field_dict["clients2gTraffic"] = clients_2_g_traffic
        if clients_5_g_traffic is not UNSET:
            field_dict["clients5gTraffic"] = clients_5_g_traffic
        if clients_6_g_traffic is not UNSET:
            field_dict["clients6gTraffic"] = clients_6_g_traffic
        if wired_clients_num is not UNSET:
            field_dict["wiredClientsNum"] = wired_clients_num
        if clients_2_g_num is not UNSET:
            field_dict["clients2gNum"] = clients_2_g_num
        if clients_5_g_num is not UNSET:
            field_dict["clients5gNum"] = clients_5_g_num
        if clients_6_g_num is not UNSET:
            field_dict["clients6gNum"] = clients_6_g_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_traffic = d.pop("totalTraffic", UNSET)

        wired_clients_traffic = d.pop("wiredClientsTraffic", UNSET)

        clients_2_g_traffic = d.pop("clients2gTraffic", UNSET)

        clients_5_g_traffic = d.pop("clients5gTraffic", UNSET)

        clients_6_g_traffic = d.pop("clients6gTraffic", UNSET)

        wired_clients_num = d.pop("wiredClientsNum", UNSET)

        clients_2_g_num = d.pop("clients2gNum", UNSET)

        clients_5_g_num = d.pop("clients5gNum", UNSET)

        clients_6_g_num = d.pop("clients6gNum", UNSET)

        client_traffic_info = cls(
            total_traffic=total_traffic,
            wired_clients_traffic=wired_clients_traffic,
            clients_2_g_traffic=clients_2_g_traffic,
            clients_5_g_traffic=clients_5_g_traffic,
            clients_6_g_traffic=clients_6_g_traffic,
            wired_clients_num=wired_clients_num,
            clients_2_g_num=clients_2_g_num,
            clients_5_g_num=clients_5_g_num,
            clients_6_g_num=clients_6_g_num,
        )

        client_traffic_info.additional_properties = d
        return client_traffic_info

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
