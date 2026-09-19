from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteTemplateAllModulesOpenApiVO")


@_attrs_define
class SiteTemplateAllModulesOpenApiVO:
    """
    Attributes:
        pro_settings (list[str] | Unset): Pro setting list for creating site template. This field applies to the Omada
            Pro Controller only.
        basic_settings (list[str] | Unset): Basic setting list for creating site template.
    """

    pro_settings: list[str] | Unset = UNSET
    basic_settings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pro_settings: list[str] | Unset = UNSET
        if not isinstance(self.pro_settings, Unset):
            pro_settings = self.pro_settings

        basic_settings: list[str] | Unset = UNSET
        if not isinstance(self.basic_settings, Unset):
            basic_settings = self.basic_settings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pro_settings is not UNSET:
            field_dict["proSettings"] = pro_settings
        if basic_settings is not UNSET:
            field_dict["basicSettings"] = basic_settings

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        pro_settings = cast(list[str], d.pop("proSettings", UNSET))

        basic_settings = cast(list[str], d.pop("basicSettings", UNSET))

        site_template_all_modules_open_api_vo = cls(
            pro_settings=pro_settings,
            basic_settings=basic_settings,
        )

        site_template_all_modules_open_api_vo.additional_properties = d
        return site_template_all_modules_open_api_vo

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
