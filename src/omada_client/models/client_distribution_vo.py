from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientDistributionVO")


@_attrs_define
class ClientDistributionVO:
    """
    Attributes:
        total_clients (int | Unset):
        clients_percent (int | Unset):
        clients2g (int | Unset):
        clients5g (int | Unset):
        clients6g (int | Unset):
    """

    total_clients: int | Unset = UNSET
    clients_percent: int | Unset = UNSET
    clients2g: int | Unset = UNSET
    clients5g: int | Unset = UNSET
    clients6g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_clients = self.total_clients

        clients_percent = self.clients_percent

        clients2g = self.clients2g

        clients5g = self.clients5g

        clients6g = self.clients6g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_clients is not UNSET:
            field_dict["totalClients"] = total_clients
        if clients_percent is not UNSET:
            field_dict["clientsPercent"] = clients_percent
        if clients2g is not UNSET:
            field_dict["clients2g"] = clients2g
        if clients5g is not UNSET:
            field_dict["clients5g"] = clients5g
        if clients6g is not UNSET:
            field_dict["clients6g"] = clients6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_clients = d.pop("totalClients", UNSET)

        clients_percent = d.pop("clientsPercent", UNSET)

        clients2g = d.pop("clients2g", UNSET)

        clients5g = d.pop("clients5g", UNSET)

        clients6g = d.pop("clients6g", UNSET)

        client_distribution_vo = cls(
            total_clients=total_clients,
            clients_percent=clients_percent,
            clients2g=clients2g,
            clients5g=clients5g,
            clients6g=clients6g,
        )

        client_distribution_vo.additional_properties = d
        return client_distribution_vo

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
