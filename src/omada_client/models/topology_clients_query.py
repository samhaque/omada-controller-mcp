from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clients_query_mac_and_filter_type import ClientsQueryMacAndFilterType


T = TypeVar("T", bound="TopologyClientsQuery")


@_attrs_define
class TopologyClientsQuery:
    """Topology clients query request body.

    Attributes:
        device_macs (list[ClientsQueryMacAndFilterType] | Unset): Device macs.
    """

    device_macs: list[ClientsQueryMacAndFilterType] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_macs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_macs, Unset):
            device_macs = []
            for device_macs_item_data in self.device_macs:
                device_macs_item = device_macs_item_data.to_dict()
                device_macs.append(device_macs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_macs is not UNSET:
            field_dict["deviceMacs"] = device_macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.clients_query_mac_and_filter_type import (
            ClientsQueryMacAndFilterType,
        )

        d = dict(src_dict)
        _device_macs = d.pop("deviceMacs", UNSET)
        device_macs: list[ClientsQueryMacAndFilterType] | Unset = UNSET
        if _device_macs is not UNSET:
            device_macs = []
            for device_macs_item_data in _device_macs:
                device_macs_item = ClientsQueryMacAndFilterType.from_dict(
                    device_macs_item_data
                )

                device_macs.append(device_macs_item)

        topology_clients_query = cls(
            device_macs=device_macs,
        )

        topology_clients_query.additional_properties = d
        return topology_clients_query

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
