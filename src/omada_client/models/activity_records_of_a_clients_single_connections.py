from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_connection_events import ClientConnectionEvents


T = TypeVar("T", bound="ActivityRecordsOfAClientsSingleConnections")


@_attrs_define
class ActivityRecordsOfAClientsSingleConnections:
    """
    Attributes:
        mac (str | Unset): Client MAC
        start (int | Unset): Start timestamp, unit: millisecond.
        end (int | Unset): End timestamp, unit: millisecond.
        events (list[ClientConnectionEvents] | Unset): Client connection events.
    """

    mac: str | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    events: list[ClientConnectionEvents] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        start = self.start

        end = self.end

        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_connection_events import (
            ClientConnectionEvents,
        )

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        _events = d.pop("events", UNSET)
        events: list[ClientConnectionEvents] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = ClientConnectionEvents.from_dict(events_item_data)

                events.append(events_item)

        activity_records_of_a_clients_single_connections = cls(
            mac=mac,
            start=start,
            end=end,
            events=events,
        )

        activity_records_of_a_clients_single_connections.additional_properties = d
        return activity_records_of_a_clients_single_connections

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
