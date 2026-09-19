from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MultiLinkEntryDTO")


@_attrs_define
class MultiLinkEntryDTO:
    """Vigi MultiLink In MLO Mode

    Attributes:
        channel (int | Unset): MLO Channel
        radio (int | Unset): MLO Radio
    """

    channel: int | Unset = UNSET
    radio: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        radio = self.radio

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if radio is not UNSET:
            field_dict["radio"] = radio

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        radio = d.pop("radio", UNSET)

        multi_link_entry_dto = cls(
            channel=channel,
            radio=radio,
        )

        multi_link_entry_dto.additional_properties = d
        return multi_link_entry_dto

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
