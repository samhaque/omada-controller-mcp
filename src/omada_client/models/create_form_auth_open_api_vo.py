from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO
    from ..models.form_auth_card_open_api_vo import FormAuthCardOpenApiVO


T = TypeVar("T", bound="CreateFormAuthOpenApiVO")


@_attrs_define
class CreateFormAuthOpenApiVO:
    """Survey authentication

    Attributes:
        title (str): Form title (display for the authentication user). It should contain 1-2000 characters.
        name (str): Form name (display for the controller user). It should contain 1-2000 characters.
        note (str): Note should contain 1-2000 characters.
        auth_timeout (AuthTimeOpenApiVO): Authentication timeout time. Display when enabled, otherwise no display.
        card_list (list[FormAuthCardOpenApiVO]): Form card list.
        published (bool): Whether to publish.
    """

    title: str
    name: str
    note: str
    auth_timeout: AuthTimeOpenApiVO
    card_list: list[FormAuthCardOpenApiVO]
    published: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        name = self.name

        note = self.note

        auth_timeout = self.auth_timeout.to_dict()

        card_list = []
        for card_list_item_data in self.card_list:
            card_list_item = card_list_item_data.to_dict()
            card_list.append(card_list_item)

        published = self.published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
                "name": name,
                "note": note,
                "authTimeout": auth_timeout,
                "cardList": card_list,
                "published": published,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auth_time_open_api_vo import AuthTimeOpenApiVO
        from ..models.form_auth_card_open_api_vo import (
            FormAuthCardOpenApiVO,
        )

        d = dict(src_dict)
        title = d.pop("title")

        name = d.pop("name")

        note = d.pop("note")

        auth_timeout = AuthTimeOpenApiVO.from_dict(d.pop("authTimeout"))

        card_list = []
        _card_list = d.pop("cardList")
        for card_list_item_data in _card_list:
            card_list_item = FormAuthCardOpenApiVO.from_dict(card_list_item_data)

            card_list.append(card_list_item)

        published = d.pop("published")

        create_form_auth_open_api_vo = cls(
            title=title,
            name=name,
            note=note,
            auth_timeout=auth_timeout,
            card_list=card_list,
            published=published,
        )

        create_form_auth_open_api_vo.additional_properties = d
        return create_form_auth_open_api_vo

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
