from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_group_vo import CardGroupVO


T = TypeVar("T", bound="ReportTab")


@_attrs_define
class ReportTab:
    """
    Attributes:
        tab_id (str | Unset): tab id
        name (str | Unset): tab name
        cards (list[str] | Unset): list of cards in tab
        card_group_list (list[CardGroupVO] | Unset): list of card group
        type_ (int | Unset): tab type, default 0, customize 1
        status (int | Unset): tab status, 0: disable, 1: enable
        rank (int | Unset): tab rank
        default_key (str | Unset): defaultKey
        default_tab (str | Unset): defaultTab
        cancel_cards (list[str] | Unset): cards be cancelled
    """

    tab_id: str | Unset = UNSET
    name: str | Unset = UNSET
    cards: list[str] | Unset = UNSET
    card_group_list: list[CardGroupVO] | Unset = UNSET
    type_: int | Unset = UNSET
    status: int | Unset = UNSET
    rank: int | Unset = UNSET
    default_key: str | Unset = UNSET
    default_tab: str | Unset = UNSET
    cancel_cards: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tab_id = self.tab_id

        name = self.name

        cards: list[str] | Unset = UNSET
        if not isinstance(self.cards, Unset):
            cards = self.cards

        card_group_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.card_group_list, Unset):
            card_group_list = []
            for card_group_list_item_data in self.card_group_list:
                card_group_list_item = card_group_list_item_data.to_dict()
                card_group_list.append(card_group_list_item)

        type_ = self.type_

        status = self.status

        rank = self.rank

        default_key = self.default_key

        default_tab = self.default_tab

        cancel_cards: list[str] | Unset = UNSET
        if not isinstance(self.cancel_cards, Unset):
            cancel_cards = self.cancel_cards

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tab_id is not UNSET:
            field_dict["tabId"] = tab_id
        if name is not UNSET:
            field_dict["name"] = name
        if cards is not UNSET:
            field_dict["cards"] = cards
        if card_group_list is not UNSET:
            field_dict["cardGroupList"] = card_group_list
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if rank is not UNSET:
            field_dict["rank"] = rank
        if default_key is not UNSET:
            field_dict["defaultKey"] = default_key
        if default_tab is not UNSET:
            field_dict["defaultTab"] = default_tab
        if cancel_cards is not UNSET:
            field_dict["cancelCards"] = cancel_cards

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.card_group_vo import CardGroupVO

        d = dict(src_dict)
        tab_id = d.pop("tabId", UNSET)

        name = d.pop("name", UNSET)

        cards = cast(list[str], d.pop("cards", UNSET))

        _card_group_list = d.pop("cardGroupList", UNSET)
        card_group_list: list[CardGroupVO] | Unset = UNSET
        if _card_group_list is not UNSET:
            card_group_list = []
            for card_group_list_item_data in _card_group_list:
                card_group_list_item = CardGroupVO.from_dict(card_group_list_item_data)

                card_group_list.append(card_group_list_item)

        type_ = d.pop("type", UNSET)

        status = d.pop("status", UNSET)

        rank = d.pop("rank", UNSET)

        default_key = d.pop("defaultKey", UNSET)

        default_tab = d.pop("defaultTab", UNSET)

        cancel_cards = cast(list[str], d.pop("cancelCards", UNSET))

        report_tab = cls(
            tab_id=tab_id,
            name=name,
            cards=cards,
            card_group_list=card_group_list,
            type_=type_,
            status=status,
            rank=rank,
            default_key=default_key,
            default_tab=default_tab,
            cancel_cards=cancel_cards,
        )

        report_tab.additional_properties = d
        return report_tab

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
