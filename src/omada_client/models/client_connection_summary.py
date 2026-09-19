from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientConnectionSummary")


@_attrs_define
class ClientConnectionSummary:
    """Summary of client count statistics.

    Attributes:
        total_clients (int | Unset): Total client number.
        wireless_clients (int | Unset): Total wireless client number.
        wired_clients (int | Unset): Total wired client number.
    """

    total_clients: int | Unset = UNSET
    wireless_clients: int | Unset = UNSET
    wired_clients: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_clients = self.total_clients

        wireless_clients = self.wireless_clients

        wired_clients = self.wired_clients

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        total_clients = d.pop("totalClients", UNSET)

        wireless_clients = d.pop("wirelessClients", UNSET)

        wired_clients = d.pop("wiredClients", UNSET)

        client_connection_summary = cls(
            total_clients=total_clients,
            wireless_clients=wireless_clients,
            wired_clients=wired_clients,
        )

        client_connection_summary.additional_properties = d
        return client_connection_summary

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
