from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormAuthCardOpenApiVO")


@_attrs_define
class FormAuthCardOpenApiVO:
    """Form card list.

    Attributes:
        type_ (int): Card type should be a value as follows: 0: single choice (single choice); 1: multiple choice
            (multiple choice); 2: ComboBox (drop-down menu); 3: input (input box); 4: score (score); 5: prompt frame
        required (bool): Indicates whether the card is required (cardType is 5, meaningless in the prompt box).
        title (str): Title should contain 1-2000 characters
        choices (list[str]): Drop-down menu or list of options for multiple-choice questions (exist if and only if
            cardType is 0, 1, 2), excluding questions with other options. Choices should contain 1-2000 characters
        others (str | Unset): The question of the other options. Exists if and only if type is 0, 1. Others should
            contain 1-2000 characters
        score_notes (list[str] | Unset): The prompt text corresponding to different scores of the scoring card. Exists
            when the cardType is 4 and needs to be transmitted in order. The subscript 0 corresponds to the score 1.
    """

    type_: int
    required: bool
    title: str
    choices: list[str]
    others: str | Unset = UNSET
    score_notes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        required = self.required

        title = self.title

        choices = self.choices

        others = self.others

        score_notes: list[str] | Unset = UNSET
        if not isinstance(self.score_notes, Unset):
            score_notes = self.score_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "required": required,
                "title": title,
                "choices": choices,
            }
        )
        if others is not UNSET:
            field_dict["others"] = others
        if score_notes is not UNSET:
            field_dict["scoreNotes"] = score_notes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        required = d.pop("required")

        title = d.pop("title")

        choices = cast(list[str], d.pop("choices"))

        others = d.pop("others", UNSET)

        score_notes = cast(list[str], d.pop("scoreNotes", UNSET))

        form_auth_card_open_api_vo = cls(
            type_=type_,
            required=required,
            title=title,
            choices=choices,
            others=others,
            score_notes=score_notes,
        )

        form_auth_card_open_api_vo.additional_properties = d
        return form_auth_card_open_api_vo

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
