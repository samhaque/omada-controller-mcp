from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_connection_info import ClientConnectionInfo
    from ..models.client_roaming_info import ClientRoamingInfo


T = TypeVar("T", bound="ClientConnectionHistories")


@_attrs_define
class ClientConnectionHistories:
    """
    Attributes:
        connections (list[ClientConnectionInfo] | Unset): Client connection histories
        roamings (list[ClientRoamingInfo] | Unset): Client roaming histories
    """

    connections: list[ClientConnectionInfo] | Unset = UNSET
    roamings: list[ClientRoamingInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        roamings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.roamings, Unset):
            roamings = []
            for roamings_item_data in self.roamings:
                roamings_item = roamings_item_data.to_dict()
                roamings.append(roamings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connections is not UNSET:
            field_dict["connections"] = connections
        if roamings is not UNSET:
            field_dict["roamings"] = roamings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_connection_info import (
            ClientConnectionInfo,
        )
        from ..models.client_roaming_info import ClientRoamingInfo

        d = dict(src_dict)
        _connections = d.pop("connections", UNSET)
        connections: list[ClientConnectionInfo] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = ClientConnectionInfo.from_dict(connections_item_data)

                connections.append(connections_item)

        _roamings = d.pop("roamings", UNSET)
        roamings: list[ClientRoamingInfo] | Unset = UNSET
        if _roamings is not UNSET:
            roamings = []
            for roamings_item_data in _roamings:
                roamings_item = ClientRoamingInfo.from_dict(roamings_item_data)

                roamings.append(roamings_item)

        client_connection_histories = cls(
            connections=connections,
            roamings=roamings,
        )

        client_connection_histories.additional_properties = d
        return client_connection_histories

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
