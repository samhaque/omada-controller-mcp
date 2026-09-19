from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboxMessage")


@_attrs_define
class InboxMessage:
    """
    Attributes:
        id (int | Unset): Item ID.
        content (str | Unset): Message content.
        time (int | Unset): Time.
        sender (str | Unset): Sender.
        unread (bool | Unset): Unread or not.
    """

    id: int | Unset = UNSET
    content: str | Unset = UNSET
    time: int | Unset = UNSET
    sender: str | Unset = UNSET
    unread: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        content = self.content

        time = self.time

        sender = self.sender

        unread = self.unread

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if content is not UNSET:
            field_dict["content"] = content
        if time is not UNSET:
            field_dict["time"] = time
        if sender is not UNSET:
            field_dict["sender"] = sender
        if unread is not UNSET:
            field_dict["unread"] = unread

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        content = d.pop("content", UNSET)

        time = d.pop("time", UNSET)

        sender = d.pop("sender", UNSET)

        unread = d.pop("unread", UNSET)

        inbox_message = cls(
            id=id,
            content=content,
            time=time,
            sender=sender,
            unread=unread,
        )

        inbox_message.additional_properties = d
        return inbox_message

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
