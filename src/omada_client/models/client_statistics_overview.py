from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ssid_distribution import SsidDistribution


T = TypeVar("T", bound="ClientStatisticsOverview")


@_attrs_define
class ClientStatisticsOverview:
    """Client statistics overview.

    Attributes:
        total_clients_num (int | Unset): Total number of all clients.
        clients_2_g_num (int | Unset): Total number of wireless clients in the 2G band.
        clients_5_g_num (int | Unset): Total number of wireless clients in the 5G band.
        clients_6_g_num (int | Unset): Total number of wireless clients in the 6G band.
        wired_clients_num (int | Unset): Total number of all wired clients.
        wireless_clients_num (int | Unset): Total number of all wireless clients.
        average_client_num (int | Unset): Average client number of each day.
        average_client_traffic (int | Unset): Average traffic of each client.
        clients_ssid_distribution (SsidDistribution | Unset): Distribution of the number of clients on SSID.
    """

    total_clients_num: int | Unset = UNSET
    clients_2_g_num: int | Unset = UNSET
    clients_5_g_num: int | Unset = UNSET
    clients_6_g_num: int | Unset = UNSET
    wired_clients_num: int | Unset = UNSET
    wireless_clients_num: int | Unset = UNSET
    average_client_num: int | Unset = UNSET
    average_client_traffic: int | Unset = UNSET
    clients_ssid_distribution: SsidDistribution | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_clients_num = self.total_clients_num

        clients_2_g_num = self.clients_2_g_num

        clients_5_g_num = self.clients_5_g_num

        clients_6_g_num = self.clients_6_g_num

        wired_clients_num = self.wired_clients_num

        wireless_clients_num = self.wireless_clients_num

        average_client_num = self.average_client_num

        average_client_traffic = self.average_client_traffic

        clients_ssid_distribution: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clients_ssid_distribution, Unset):
            clients_ssid_distribution = self.clients_ssid_distribution.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_clients_num is not UNSET:
            field_dict["totalClientsNum"] = total_clients_num
        if clients_2_g_num is not UNSET:
            field_dict["clients2gNum"] = clients_2_g_num
        if clients_5_g_num is not UNSET:
            field_dict["clients5gNum"] = clients_5_g_num
        if clients_6_g_num is not UNSET:
            field_dict["clients6gNum"] = clients_6_g_num
        if wired_clients_num is not UNSET:
            field_dict["wiredClientsNum"] = wired_clients_num
        if wireless_clients_num is not UNSET:
            field_dict["wirelessClientsNum"] = wireless_clients_num
        if average_client_num is not UNSET:
            field_dict["averageClientNum"] = average_client_num
        if average_client_traffic is not UNSET:
            field_dict["averageClientTraffic"] = average_client_traffic
        if clients_ssid_distribution is not UNSET:
            field_dict["clientsSsidDistribution"] = clients_ssid_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ssid_distribution import SsidDistribution

        d = dict(src_dict)
        total_clients_num = d.pop("totalClientsNum", UNSET)

        clients_2_g_num = d.pop("clients2gNum", UNSET)

        clients_5_g_num = d.pop("clients5gNum", UNSET)

        clients_6_g_num = d.pop("clients6gNum", UNSET)

        wired_clients_num = d.pop("wiredClientsNum", UNSET)

        wireless_clients_num = d.pop("wirelessClientsNum", UNSET)

        average_client_num = d.pop("averageClientNum", UNSET)

        average_client_traffic = d.pop("averageClientTraffic", UNSET)

        _clients_ssid_distribution = d.pop("clientsSsidDistribution", UNSET)
        clients_ssid_distribution: SsidDistribution | Unset
        if isinstance(_clients_ssid_distribution, Unset):
            clients_ssid_distribution = UNSET
        else:
            clients_ssid_distribution = SsidDistribution.from_dict(
                _clients_ssid_distribution
            )

        client_statistics_overview = cls(
            total_clients_num=total_clients_num,
            clients_2_g_num=clients_2_g_num,
            clients_5_g_num=clients_5_g_num,
            clients_6_g_num=clients_6_g_num,
            wired_clients_num=wired_clients_num,
            wireless_clients_num=wireless_clients_num,
            average_client_num=average_client_num,
            average_client_traffic=average_client_traffic,
            clients_ssid_distribution=clients_ssid_distribution,
        )

        client_statistics_overview.additional_properties = d
        return client_statistics_overview

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
