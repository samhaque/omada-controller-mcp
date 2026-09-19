from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CardGroupVO")


@_attrs_define
class CardGroupVO:
    """list of card group

    Attributes:
        card_group_name (str | Unset):
        card_list (list[str] | Unset):
    """

    card_group_name: str | Unset = UNSET
    card_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card_group_name = self.card_group_name

        card_list: list[str] | Unset = UNSET
        if not isinstance(self.card_list, Unset):
            card_list = self.card_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if card_group_name is not UNSET:
            field_dict["cardGroupName"] = card_group_name
        if card_list is not UNSET:
            field_dict["cardList"] = card_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        card_group_name = d.pop("cardGroupName", UNSET)

        card_list = cast(list[str], d.pop("cardList", UNSET))

        card_group_vo = cls(
            card_group_name=card_group_name,
            card_list=card_list,
        )

        card_group_vo.additional_properties = d
        return card_group_vo

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
