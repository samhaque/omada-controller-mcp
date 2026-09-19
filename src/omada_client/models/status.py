from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_content import StatusContent


T = TypeVar("T", bound="Status")


@_attrs_define
class Status:
    """
    Attributes:
        command (str | Unset): To get status information from the router, send a message starting with "LTE Router
            Status", followed by Password/PIN(e.g. LTE Router Status 1234). The password is required for viewing device-
            related Information via SMS.
        content (StatusContent | Unset):
    """

    command: str | Unset = UNSET
    content: StatusContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        command = self.command

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if command is not UNSET:
            field_dict["command"] = command
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.status_content import StatusContent

        d = dict(src_dict)
        command = d.pop("command", UNSET)

        _content = d.pop("content", UNSET)
        content: StatusContent | Unset
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = StatusContent.from_dict(_content)

        status = cls(
            command=command,
            content=content,
        )

        status.additional_properties = d
        return status

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
