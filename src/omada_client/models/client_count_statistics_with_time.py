from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientCountStatisticsWithTime")


@_attrs_define
class ClientCountStatisticsWithTime:
    """Client connection trend with time.

    Attributes:
        time (int | Unset): Timestamp, unit is second.
        total_clients (int | Unset): The number of all clients.
        wireless_clients (int | Unset): The number of all wireless clients.
        wired_clients (int | Unset): The number of all wired clients.
    """

    time: int | Unset = UNSET
    total_clients: int | Unset = UNSET
    wireless_clients: int | Unset = UNSET
    wired_clients: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        total_clients = self.total_clients

        wireless_clients = self.wireless_clients

        wired_clients = self.wired_clients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if total_clients is not UNSET:
            field_dict["totalClients"] = total_clients
        if wireless_clients is not UNSET:
            field_dict["wirelessClients"] = wireless_clients
        if wired_clients is not UNSET:
            field_dict["wiredClients"] = wired_clients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        total_clients = d.pop("totalClients", UNSET)

        wireless_clients = d.pop("wirelessClients", UNSET)

        wired_clients = d.pop("wiredClients", UNSET)

        client_count_statistics_with_time = cls(
            time=time,
            total_clients=total_clients,
            wireless_clients=wireless_clients,
            wired_clients=wired_clients,
        )

        client_count_statistics_with_time.additional_properties = d
        return client_count_statistics_with_time

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
