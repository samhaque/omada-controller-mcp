from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.license_num_open_api_vo import LicenseNumOpenApiVO


T = TypeVar("T", bound="LicenseAvailableRecycleOpenApiVO")


@_attrs_define
class LicenseAvailableRecycleOpenApiVO:
    """
    Attributes:
        license_num (list[LicenseNumOpenApiVO] | Unset):
    """

    license_num: list[LicenseNumOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        license_num: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.license_num, Unset):
            license_num = []
            for license_num_item_data in self.license_num:
                license_num_item = license_num_item_data.to_dict()
                license_num.append(license_num_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if license_num is not UNSET:
            field_dict["licenseNum"] = license_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.license_num_open_api_vo import (
            LicenseNumOpenApiVO,
        )

        d = dict(src_dict)
        _license_num = d.pop("licenseNum", UNSET)
        license_num: list[LicenseNumOpenApiVO] | Unset = UNSET
        if _license_num is not UNSET:
            license_num = []
            for license_num_item_data in _license_num:
                license_num_item = LicenseNumOpenApiVO.from_dict(license_num_item_data)

                license_num.append(license_num_item)

        license_available_recycle_open_api_vo = cls(
            license_num=license_num,
        )

        license_available_recycle_open_api_vo.additional_properties = d
        return license_available_recycle_open_api_vo

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
