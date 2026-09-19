from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteTemplateBriefOpenApiVO")


@_attrs_define
class SiteTemplateBriefOpenApiVO:
    """
    Attributes:
        id (str | Unset): Site Template ID
        omadac_id (str | Unset): Omada ID
        name (str | Unset): Name of the site template should contain 1 to 64 characters.
        category (str | Unset): The category of the site template
        type_ (int | Unset): The type should be a value as follows: 0:basic; 1:pro.
        settings (list[str] | Unset): The settings of the site template.
    """

    id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    name: str | Unset = UNSET
    category: str | Unset = UNSET
    type_: int | Unset = UNSET
    settings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        omadac_id = self.omadac_id

        name = self.name

        category = self.category

        type_ = self.type_

        settings: list[str] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if name is not UNSET:
            field_dict["name"] = name
        if category is not UNSET:
            field_dict["category"] = category
        if type_ is not UNSET:
            field_dict["type"] = type_
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        name = d.pop("name", UNSET)

        category = d.pop("category", UNSET)

        type_ = d.pop("type", UNSET)

        settings = cast(list[str], d.pop("settings", UNSET))

        site_template_brief_open_api_vo = cls(
            id=id,
            omadac_id=omadac_id,
            name=name,
            category=category,
            type_=type_,
            settings=settings,
        )

        site_template_brief_open_api_vo.additional_properties = d
        return site_template_brief_open_api_vo

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
