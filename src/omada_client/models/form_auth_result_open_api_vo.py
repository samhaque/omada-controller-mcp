from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.form_auth_card_answer_open_api_vo import FormAuthCardAnswerOpenApiVO


T = TypeVar("T", bound="FormAuthResultOpenApiVO")


@_attrs_define
class FormAuthResultOpenApiVO:
    """
    Attributes:
        id (str | Unset): Form result ID
        form_id (str | Unset): This field represents authentication survey ID. Authentication survey can be created
            using 'Create a new authentication survey' interface, and authentication survey ID can be obtained from 'Get
            authentication survey list' interface.
        answers (list[FormAuthCardAnswerOpenApiVO] | Unset): Answers submitted by users.
        time (int | Unset): Authenticated timestamp in ms.
        ssid (str | Unset): Client connected SSID.
        network (str | Unset): Network (exists when wired connection).
    """

    id: str | Unset = UNSET
    form_id: str | Unset = UNSET
    answers: list[FormAuthCardAnswerOpenApiVO] | Unset = UNSET
    time: int | Unset = UNSET
    ssid: str | Unset = UNSET
    network: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        form_id = self.form_id

        answers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.answers, Unset):
            answers = []
            for answers_item_data in self.answers:
                answers_item = answers_item_data.to_dict()
                answers.append(answers_item)

        time = self.time

        ssid = self.ssid

        network = self.network

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if form_id is not UNSET:
            field_dict["formId"] = form_id
        if answers is not UNSET:
            field_dict["answers"] = answers
        if time is not UNSET:
            field_dict["time"] = time
        if ssid is not UNSET:
            field_dict["ssid"] = ssid
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.form_auth_card_answer_open_api_vo import (
            FormAuthCardAnswerOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        form_id = d.pop("formId", UNSET)

        _answers = d.pop("answers", UNSET)
        answers: list[FormAuthCardAnswerOpenApiVO] | Unset = UNSET
        if _answers is not UNSET:
            answers = []
            for answers_item_data in _answers:
                answers_item = FormAuthCardAnswerOpenApiVO.from_dict(answers_item_data)

                answers.append(answers_item)

        time = d.pop("time", UNSET)

        ssid = d.pop("ssid", UNSET)

        network = d.pop("network", UNSET)

        form_auth_result_open_api_vo = cls(
            id=id,
            form_id=form_id,
            answers=answers,
            time=time,
            ssid=ssid,
            network=network,
        )

        form_auth_result_open_api_vo.additional_properties = d
        return form_auth_result_open_api_vo

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
