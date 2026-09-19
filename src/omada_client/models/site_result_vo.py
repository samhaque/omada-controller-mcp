from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteResultVO")


@_attrs_define
class SiteResultVO:
    """
    Attributes:
        success_site_list (list[str] | Unset): Site ID list which executing site maintenance successfully.
    """

    success_site_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success_site_list: list[str] | Unset = UNSET
        if not isinstance(self.success_site_list, Unset):
            success_site_list = self.success_site_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success_site_list is not UNSET:
            field_dict["successSiteList"] = success_site_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        success_site_list = cast(list[str], d.pop("successSiteList", UNSET))

        site_result_vo = cls(
            success_site_list=success_site_list,
        )

        site_result_vo.additional_properties = d
        return site_result_vo

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
