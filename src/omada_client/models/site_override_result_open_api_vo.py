from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_override_open_api_vo import SiteOverrideOpenApiVO


T = TypeVar("T", bound="SiteOverrideResultOpenApiVO")


@_attrs_define
class SiteOverrideResultOpenApiVO:
    """
    Attributes:
        sites (list[SiteOverrideOpenApiVO] | Unset): sites with override module
    """

    sites: list[SiteOverrideOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sites, Unset):
            sites = []
            for sites_item_data in self.sites:
                sites_item = sites_item_data.to_dict()
                sites.append(sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sites is not UNSET:
            field_dict["sites"] = sites

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_override_open_api_vo import (
            SiteOverrideOpenApiVO,
        )

        d = dict(src_dict)
        _sites = d.pop("sites", UNSET)
        sites: list[SiteOverrideOpenApiVO] | Unset = UNSET
        if _sites is not UNSET:
            sites = []
            for sites_item_data in _sites:
                sites_item = SiteOverrideOpenApiVO.from_dict(sites_item_data)

                sites.append(sites_item)

        site_override_result_open_api_vo = cls(
            sites=sites,
        )

        site_override_result_open_api_vo.additional_properties = d
        return site_override_result_open_api_vo

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
