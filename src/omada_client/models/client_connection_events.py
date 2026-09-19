from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_connection_events_attributes import (
        ClientConnectionEventsAttributes,
    )


T = TypeVar("T", bound="ClientConnectionEvents")


@_attrs_define
class ClientConnectionEvents:
    """Client connection events.

    Attributes:
        time (int | Unset): Event timestamp, unit: millisecond.
        event_type (int | Unset): Event type should be a value as follows: <br/>0: CONNECT_WIRELESS // Connected to
            [ap:{dev_mac}] with SSID {ssid_name}; <br/>1: DISCONNECT_WIRELESS // Disconnected from [ap:{dev_mac}]; <br/>2:
            ROAMING // Roaming from [ap:{old_dev_mac}] to [ap:{dev_mac}]; <br/>3: BLOCK_WIRELESS // Blocked by admin
            {admin_name}; <br/>100: CONNECT_WIRED // Connected to [{dev_type}:{dev_mac}]; <br/>101: DISCONNECT_WIRED //
            Disconnected from [{dev_type}:{dev_mac}]; <br/>102: BLOCK_WIRED // Blocked by admin {admin_name}; <br/>200:
            AUTH_SUCCESS // Authorized by {auth_type} with {username}; <br/>201: AUTH_FAIL // Failed Authorized by
            {auth_type} with {username}; <br/>202: UNBLOCK // Unblocked by admin {admin_name};
        content (str | Unset): Client connect event description, such as: Connected to [ap:{dev_mac}] with SSID
            {ssid_name}.
        attributes (ClientConnectionEventsAttributes | Unset): Client connect event attributes map, such as
            [{dev_mac}:{AA-BB-CC-DD-EE-FF}].
    """

    time: int | Unset = UNSET
    event_type: int | Unset = UNSET
    content: str | Unset = UNSET
    attributes: ClientConnectionEventsAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        event_type = self.event_type

        content = self.content

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if content is not UNSET:
            field_dict["content"] = content
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_connection_events_attributes import (
            ClientConnectionEventsAttributes,
        )

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        event_type = d.pop("eventType", UNSET)

        content = d.pop("content", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: ClientConnectionEventsAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = ClientConnectionEventsAttributes.from_dict(_attributes)

        client_connection_events = cls(
            time=time,
            event_type=event_type,
            content=content,
            attributes=attributes,
        )

        client_connection_events.additional_properties = d
        return client_connection_events

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
