from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FormAuthCardAnswerOpenApiVO")


@_attrs_define
class FormAuthCardAnswerOpenApiVO:
    """Answers submitted by users.

    Attributes:
        type_ (int | Unset): Type should be a value as follows: 0: single choice; 1: multiple choice; 2: ComboBox; 3:
            input; 4: score; 5: prompt box
        choice_answer (list[int] | Unset): Drop-down menu or answer list for multiple-choice questions (exists if and
            only if cardType is 0, 1, 2)
        input_answer (str | Unset): Answers entered by the user, which corresponds to the question and answer question
            or the scored evaluation, or the input of other options in the multiple-choice question. Determined according to
            the type field. 0, 1, and 2 indicate other options answers, 3 indicates the answer in the input box, and 4
            indicates the scored evaluation. InputAnswer should contain 1-2000 characters
        score (int | Unset): User rating (should be within the range of 1-5), exists when type is 4
        others (str | Unset): Exists when cardType is 0, 1 and the user adds other options. Used to save the option
            answer corresponding to the prompt of other options. Assuming that the user adds two other options, D and E, and
            choiceAnswer contains 3 ( D), 4 (E), then others[0] represents the answer of option D. Others should contain
            1-2000 characters
    """

    type_: int | Unset = UNSET
    choice_answer: list[int] | Unset = UNSET
    input_answer: str | Unset = UNSET
    score: int | Unset = UNSET
    others: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        choice_answer: list[int] | Unset = UNSET
        if not isinstance(self.choice_answer, Unset):
            choice_answer = self.choice_answer

        input_answer = self.input_answer

        score = self.score

        others = self.others

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if choice_answer is not UNSET:
            field_dict["choiceAnswer"] = choice_answer
        if input_answer is not UNSET:
            field_dict["inputAnswer"] = input_answer
        if score is not UNSET:
            field_dict["score"] = score
        if others is not UNSET:
            field_dict["others"] = others

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        choice_answer = cast(list[int], d.pop("choiceAnswer", UNSET))

        input_answer = d.pop("inputAnswer", UNSET)

        score = d.pop("score", UNSET)

        others = d.pop("others", UNSET)

        form_auth_card_answer_open_api_vo = cls(
            type_=type_,
            choice_answer=choice_answer,
            input_answer=input_answer,
            score=score,
            others=others,
        )

        form_auth_card_answer_open_api_vo.additional_properties = d
        return form_auth_card_answer_open_api_vo

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
