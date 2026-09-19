from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyFilterClientCountDTO")


@_attrs_define
class TopologyFilterClientCountDTO:
    """Each Connection Type Client Count

    Attributes:
        client2g (int | Unset): 2g Client Count
        client5g (int | Unset): 5g Client Count
        client6g (int | Unset): 6g Client Count
        client2g5g (int | Unset): 2g And 5g Client Count
        client2g6g (int | Unset): 2g And 6g Client Count
        client5g6g (int | Unset): 5g And 6g Client Count
        client2g5g6g (int | Unset): 2g, 5g And 6g Client Count
        wired_client (int | Unset): Wired Client Count
    """

    client2g: int | Unset = UNSET
    client5g: int | Unset = UNSET
    client6g: int | Unset = UNSET
    client2g5g: int | Unset = UNSET
    client2g6g: int | Unset = UNSET
    client5g6g: int | Unset = UNSET
    client2g5g6g: int | Unset = UNSET
    wired_client: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client2g = self.client2g

        client5g = self.client5g

        client6g = self.client6g

        client2g5g = self.client2g5g

        client2g6g = self.client2g6g

        client5g6g = self.client5g6g

        client2g5g6g = self.client2g5g6g

        wired_client = self.wired_client

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client2g is not UNSET:
            field_dict["client2g"] = client2g
        if client5g is not UNSET:
            field_dict["client5g"] = client5g
        if client6g is not UNSET:
            field_dict["client6g"] = client6g
        if client2g5g is not UNSET:
            field_dict["client2g5g"] = client2g5g
        if client2g6g is not UNSET:
            field_dict["client2g6g"] = client2g6g
        if client5g6g is not UNSET:
            field_dict["client5g6g"] = client5g6g
        if client2g5g6g is not UNSET:
            field_dict["client2g5g6g"] = client2g5g6g
        if wired_client is not UNSET:
            field_dict["wiredClient"] = wired_client

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        client2g = d.pop("client2g", UNSET)

        client5g = d.pop("client5g", UNSET)

        client6g = d.pop("client6g", UNSET)

        client2g5g = d.pop("client2g5g", UNSET)

        client2g6g = d.pop("client2g6g", UNSET)

        client5g6g = d.pop("client5g6g", UNSET)

        client2g5g6g = d.pop("client2g5g6g", UNSET)

        wired_client = d.pop("wiredClient", UNSET)

        topology_filter_client_count_dto = cls(
            client2g=client2g,
            client5g=client5g,
            client6g=client6g,
            client2g5g=client2g5g,
            client2g6g=client2g6g,
            client5g6g=client5g6g,
            client2g5g6g=client2g5g6g,
            wired_client=wired_client,
        )

        topology_filter_client_count_dto.additional_properties = d
        return topology_filter_client_count_dto

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
