from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EapClientVO")


@_attrs_define
class EapClientVO:
    """
    Attributes:
        name (str | Unset):
        total_clients (int | Unset):
        total_distribution (float | Unset):
        clients2g (int | Unset):
        distribution2g (float | Unset):
        clients5g (int | Unset):
        distribution5g (float | Unset):
        clients6g (int | Unset):
        distribution6g (float | Unset):
        wired_clients (int | Unset):
        wired_distribution (float | Unset):
    """

    name: str | Unset = UNSET
    total_clients: int | Unset = UNSET
    total_distribution: float | Unset = UNSET
    clients2g: int | Unset = UNSET
    distribution2g: float | Unset = UNSET
    clients5g: int | Unset = UNSET
    distribution5g: float | Unset = UNSET
    clients6g: int | Unset = UNSET
    distribution6g: float | Unset = UNSET
    wired_clients: int | Unset = UNSET
    wired_distribution: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        total_clients = self.total_clients

        total_distribution = self.total_distribution

        clients2g = self.clients2g

        distribution2g = self.distribution2g

        clients5g = self.clients5g

        distribution5g = self.distribution5g

        clients6g = self.clients6g

        distribution6g = self.distribution6g

        wired_clients = self.wired_clients

        wired_distribution = self.wired_distribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if total_clients is not UNSET:
            field_dict["totalClients"] = total_clients
        if total_distribution is not UNSET:
            field_dict["totalDistribution"] = total_distribution
        if clients2g is not UNSET:
            field_dict["clients2g"] = clients2g
        if distribution2g is not UNSET:
            field_dict["distribution2g"] = distribution2g
        if clients5g is not UNSET:
            field_dict["clients5g"] = clients5g
        if distribution5g is not UNSET:
            field_dict["distribution5g"] = distribution5g
        if clients6g is not UNSET:
            field_dict["clients6g"] = clients6g
        if distribution6g is not UNSET:
            field_dict["distribution6g"] = distribution6g
        if wired_clients is not UNSET:
            field_dict["wiredClients"] = wired_clients
        if wired_distribution is not UNSET:
            field_dict["wiredDistribution"] = wired_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        total_clients = d.pop("totalClients", UNSET)

        total_distribution = d.pop("totalDistribution", UNSET)

        clients2g = d.pop("clients2g", UNSET)

        distribution2g = d.pop("distribution2g", UNSET)

        clients5g = d.pop("clients5g", UNSET)

        distribution5g = d.pop("distribution5g", UNSET)

        clients6g = d.pop("clients6g", UNSET)

        distribution6g = d.pop("distribution6g", UNSET)

        wired_clients = d.pop("wiredClients", UNSET)

        wired_distribution = d.pop("wiredDistribution", UNSET)

        eap_client_vo = cls(
            name=name,
            total_clients=total_clients,
            total_distribution=total_distribution,
            clients2g=clients2g,
            distribution2g=distribution2g,
            clients5g=clients5g,
            distribution5g=distribution5g,
            clients6g=clients6g,
            distribution6g=distribution6g,
            wired_clients=wired_clients,
            wired_distribution=wired_distribution,
        )

        eap_client_vo.additional_properties = d
        return eap_client_vo

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
