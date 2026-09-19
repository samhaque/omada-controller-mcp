from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceClientVO")


@_attrs_define
class DeviceClientVO:
    """
    Attributes:
        name (str | Unset):
        total_clients (int | Unset):
        total_distribution (float | Unset):
    """

    name: str | Unset = UNSET
    total_clients: int | Unset = UNSET
    total_distribution: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        total_clients = self.total_clients

        total_distribution = self.total_distribution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if total_clients is not UNSET:
            field_dict["totalClients"] = total_clients
        if total_distribution is not UNSET:
            field_dict["totalDistribution"] = total_distribution

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        total_clients = d.pop("totalClients", UNSET)

        total_distribution = d.pop("totalDistribution", UNSET)

        device_client_vo = cls(
            name=name,
            total_clients=total_clients,
            total_distribution=total_distribution,
        )

        device_client_vo.additional_properties = d
        return device_client_vo

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
