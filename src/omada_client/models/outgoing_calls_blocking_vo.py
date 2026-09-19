from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutgoingCallsBlockingVO")


@_attrs_define
class OutgoingCallsBlockingVO:
    """Outgoing calls blocking rules. Rules are valid if and only if parameter [outgoingCallsBlockingEnable] equals true.

    Attributes:
        types (list[int] | Unset): Outgoing calls blocking types. 0 means mobile, 1 means landline, 2 means long
            distance, 3 means international, 4 means calls with specific number prefix.
        prefix_list (list[str] | Unset): Field [prefixList] is required when the value of field [types] contains 4.
    """

    types: list[int] | Unset = UNSET
    prefix_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        types: list[int] | Unset = UNSET
        if not isinstance(self.types, Unset):
            types = self.types

        prefix_list: list[str] | Unset = UNSET
        if not isinstance(self.prefix_list, Unset):
            prefix_list = self.prefix_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if types is not UNSET:
            field_dict["types"] = types
        if prefix_list is not UNSET:
            field_dict["prefixList"] = prefix_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        types = cast(list[int], d.pop("types", UNSET))

        prefix_list = cast(list[str], d.pop("prefixList", UNSET))

        outgoing_calls_blocking_vo = cls(
            types=types,
            prefix_list=prefix_list,
        )

        outgoing_calls_blocking_vo.additional_properties = d
        return outgoing_calls_blocking_vo

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
