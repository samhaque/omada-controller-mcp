from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseCategoryOtherIdsOpenApiVO")


@_attrs_define
class LicenseCategoryOtherIdsOpenApiVO:
    """Gateway used license

    Attributes:
        license_key_list (list[str] | Unset): License key list
        select_all (bool | Unset): Select all used license
        total (int | Unset): Total select used license
    """

    license_key_list: list[str] | Unset = UNSET
    select_all: bool | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_key_list: list[str] | Unset = UNSET
        if not isinstance(self.license_key_list, Unset):
            license_key_list = self.license_key_list

        select_all = self.select_all

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_key_list is not UNSET:
            field_dict["licenseKeyList"] = license_key_list
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        license_key_list = cast(list[str], d.pop("licenseKeyList", UNSET))

        select_all = d.pop("selectAll", UNSET)

        total = d.pop("total", UNSET)

        license_category_other_ids_open_api_vo = cls(
            license_key_list=license_key_list,
            select_all=select_all,
            total=total,
        )

        license_category_other_ids_open_api_vo.additional_properties = d
        return license_category_other_ids_open_api_vo

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
