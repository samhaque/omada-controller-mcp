from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.longest_uptime_client_info import LongestUptimeClientInfo
    from ..models.top_traffic_client_info import TopTrafficClientInfo


T = TypeVar("T", bound="TopTrafficAndUptimeClients")


@_attrs_define
class TopTrafficAndUptimeClients:
    """Top traffic and uptime clients.

    Attributes:
        active_clients (list[TopTrafficClientInfo] | Unset): Top traffic clients.
        longest_uptime_clients (list[LongestUptimeClientInfo] | Unset): Longest uptime clients.
    """

    active_clients: list[TopTrafficClientInfo] | Unset = UNSET
    longest_uptime_clients: list[LongestUptimeClientInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active_clients, Unset):
            active_clients = []
            for active_clients_item_data in self.active_clients:
                active_clients_item = active_clients_item_data.to_dict()
                active_clients.append(active_clients_item)

        longest_uptime_clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.longest_uptime_clients, Unset):
            longest_uptime_clients = []
            for longest_uptime_clients_item_data in self.longest_uptime_clients:
                longest_uptime_clients_item = longest_uptime_clients_item_data.to_dict()
                longest_uptime_clients.append(longest_uptime_clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_clients is not UNSET:
            field_dict["activeClients"] = active_clients
        if longest_uptime_clients is not UNSET:
            field_dict["longestUptimeClients"] = longest_uptime_clients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.longest_uptime_client_info import (
            LongestUptimeClientInfo,
        )
        from ..models.top_traffic_client_info import (
            TopTrafficClientInfo,
        )

        d = dict(src_dict)
        _active_clients = d.pop("activeClients", UNSET)
        active_clients: list[TopTrafficClientInfo] | Unset = UNSET
        if _active_clients is not UNSET:
            active_clients = []
            for active_clients_item_data in _active_clients:
                active_clients_item = TopTrafficClientInfo.from_dict(
                    active_clients_item_data
                )

                active_clients.append(active_clients_item)

        _longest_uptime_clients = d.pop("longestUptimeClients", UNSET)
        longest_uptime_clients: list[LongestUptimeClientInfo] | Unset = UNSET
        if _longest_uptime_clients is not UNSET:
            longest_uptime_clients = []
            for longest_uptime_clients_item_data in _longest_uptime_clients:
                longest_uptime_clients_item = LongestUptimeClientInfo.from_dict(
                    longest_uptime_clients_item_data
                )

                longest_uptime_clients.append(longest_uptime_clients_item)

        top_traffic_and_uptime_clients = cls(
            active_clients=active_clients,
            longest_uptime_clients=longest_uptime_clients,
        )

        top_traffic_and_uptime_clients.additional_properties = d
        return top_traffic_and_uptime_clients

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
