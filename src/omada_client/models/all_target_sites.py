from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_basic_info import SiteBasicInfo


T = TypeVar("T", bound="AllTargetSites")


@_attrs_define
class AllTargetSites:
    """
    Attributes:
        target_sites (list[SiteBasicInfo] | Unset):
    """

    target_sites: list[SiteBasicInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target_sites: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.target_sites, Unset):
            target_sites = []
            for target_sites_item_data in self.target_sites:
                target_sites_item = target_sites_item_data.to_dict()
                target_sites.append(target_sites_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_sites is not UNSET:
            field_dict["targetSites"] = target_sites

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_basic_info import SiteBasicInfo

        d = dict(src_dict)
        _target_sites = d.pop("targetSites", UNSET)
        target_sites: list[SiteBasicInfo] | Unset = UNSET
        if _target_sites is not UNSET:
            target_sites = []
            for target_sites_item_data in _target_sites:
                target_sites_item = SiteBasicInfo.from_dict(target_sites_item_data)

                target_sites.append(target_sites_item)

        all_target_sites = cls(
            target_sites=target_sites,
        )

        all_target_sites.additional_properties = d
        return all_target_sites

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
