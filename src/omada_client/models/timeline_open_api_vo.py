from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connect_period_vo import ConnectPeriodVO


T = TypeVar("T", bound="TimelineOpenApiVO")


@_attrs_define
class TimelineOpenApiVO:
    """
    Attributes:
        connections (list[ConnectPeriodVO] | Unset): The collection of device online intervals.
    """

    connections: list[ConnectPeriodVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connections is not UNSET:
            field_dict["connections"] = connections

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.connect_period_vo import ConnectPeriodVO

        d = dict(src_dict)
        _connections = d.pop("connections", UNSET)
        connections: list[ConnectPeriodVO] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = ConnectPeriodVO.from_dict(connections_item_data)

                connections.append(connections_item)

        timeline_open_api_vo = cls(
            connections=connections,
        )

        timeline_open_api_vo.additional_properties = d
        return timeline_open_api_vo

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
