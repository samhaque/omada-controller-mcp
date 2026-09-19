from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO
    from ..models.form_auth_card_open_api_vo import FormAuthCardOpenApiVO


T = TypeVar("T", bound="FormAuthOpenApiVO")


@_attrs_define
class FormAuthOpenApiVO:
    """
    Attributes:
        id (str | Unset): Auth form ID
        title (str | Unset): Form title (display for the authentication user). It should contain 1-2000 characters.
        name (str | Unset): Form name (display for the controller user). It should contain 1-2000 characters.
        note (str | Unset): Note should contain 1-2000 characters.
        auth_timeout (AuthTimeOpenApiVO | Unset): Authentication timeout time. Display when enabled, otherwise no
            display.
        card_list (list[FormAuthCardOpenApiVO] | Unset): Form card list.
        is_published (bool | Unset): Whether to publish.
        create_time (int | Unset): Created time of the form.
        portals (list[str] | Unset): Portal names corresponding to the bound portal.
        answer_num (int | Unset): The number of form's answers.
    """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    name: str | Unset = UNSET
    note: str | Unset = UNSET
    auth_timeout: AuthTimeOpenApiVO | Unset = UNSET
    card_list: list[FormAuthCardOpenApiVO] | Unset = UNSET
    is_published: bool | Unset = UNSET
    create_time: int | Unset = UNSET
    portals: list[str] | Unset = UNSET
    answer_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        name = self.name

        note = self.note

        auth_timeout: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_timeout, Unset):
            auth_timeout = self.auth_timeout.to_dict()

        card_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.card_list, Unset):
            card_list = []
            for card_list_item_data in self.card_list:
                card_list_item = card_list_item_data.to_dict()
                card_list.append(card_list_item)

        is_published = self.is_published

        create_time = self.create_time

        portals: list[str] | Unset = UNSET
        if not isinstance(self.portals, Unset):
            portals = self.portals

        answer_num = self.answer_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if name is not UNSET:
            field_dict["name"] = name
        if note is not UNSET:
            field_dict["note"] = note
        if auth_timeout is not UNSET:
            field_dict["authTimeout"] = auth_timeout
        if card_list is not UNSET:
            field_dict["cardList"] = card_list
        if is_published is not UNSET:
            field_dict["isPublished"] = is_published
        if create_time is not UNSET:
            field_dict["createTime"] = create_time
        if portals is not UNSET:
            field_dict["portals"] = portals
        if answer_num is not UNSET:
            field_dict["answerNum"] = answer_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO
        from ..models.form_auth_card_open_api_vo import (
            FormAuthCardOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        name = d.pop("name", UNSET)

        note = d.pop("note", UNSET)

        _auth_timeout = d.pop("authTimeout", UNSET)
        auth_timeout: AuthTimeOpenApiVO | Unset
        if isinstance(_auth_timeout, Unset):
            auth_timeout = UNSET
        else:
            auth_timeout = AuthTimeOpenApiVO.from_dict(_auth_timeout)

        _card_list = d.pop("cardList", UNSET)
        card_list: list[FormAuthCardOpenApiVO] | Unset = UNSET
        if _card_list is not UNSET:
            card_list = []
            for card_list_item_data in _card_list:
                card_list_item = FormAuthCardOpenApiVO.from_dict(card_list_item_data)

                card_list.append(card_list_item)

        is_published = d.pop("isPublished", UNSET)

        create_time = d.pop("createTime", UNSET)

        portals = cast(list[str], d.pop("portals", UNSET))

        answer_num = d.pop("answerNum", UNSET)

        form_auth_open_api_vo = cls(
            id=id,
            title=title,
            name=name,
            note=note,
            auth_timeout=auth_timeout,
            card_list=card_list,
            is_published=is_published,
            create_time=create_time,
            portals=portals,
            answer_num=answer_num,
        )

        form_auth_open_api_vo.additional_properties = d
        return form_auth_open_api_vo

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
