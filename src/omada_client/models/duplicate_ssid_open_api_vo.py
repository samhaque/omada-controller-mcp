from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.duplicate_ssid_open_api_vo_ssid_name_map import (
        DuplicateSsidOpenApiVOSsidNameMap,
    )


T = TypeVar("T", bound="DuplicateSsidOpenApiVO")


@_attrs_define
class DuplicateSsidOpenApiVO:
    """
    Attributes:
        ssid_name_map (DuplicateSsidOpenApiVOSsidNameMap | Unset): The SSIDs that are duplicated by site
        duplicate_ssid_names (list[str] | Unset): The SSID Names that are duplicated by site
        site_id (str | Unset): The site ID
    """

    ssid_name_map: DuplicateSsidOpenApiVOSsidNameMap | Unset = UNSET
    duplicate_ssid_names: list[str] | Unset = UNSET
    site_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_name_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ssid_name_map, Unset):
            ssid_name_map = self.ssid_name_map.to_dict()

        duplicate_ssid_names: list[str] | Unset = UNSET
        if not isinstance(self.duplicate_ssid_names, Unset):
            duplicate_ssid_names = self.duplicate_ssid_names

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid_name_map is not UNSET:
            field_dict["ssidNameMap"] = ssid_name_map
        if duplicate_ssid_names is not UNSET:
            field_dict["duplicateSsidNames"] = duplicate_ssid_names
        if site_id is not UNSET:
            field_dict["siteId"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.duplicate_ssid_open_api_vo_ssid_name_map import (
            DuplicateSsidOpenApiVOSsidNameMap,
        )

        d = dict(src_dict)
        _ssid_name_map = d.pop("ssidNameMap", UNSET)
        ssid_name_map: DuplicateSsidOpenApiVOSsidNameMap | Unset
        if isinstance(_ssid_name_map, Unset):
            ssid_name_map = UNSET
        else:
            ssid_name_map = DuplicateSsidOpenApiVOSsidNameMap.from_dict(_ssid_name_map)

        duplicate_ssid_names = cast(list[str], d.pop("duplicateSsidNames", UNSET))

        site_id = d.pop("siteId", UNSET)

        duplicate_ssid_open_api_vo = cls(
            ssid_name_map=ssid_name_map,
            duplicate_ssid_names=duplicate_ssid_names,
            site_id=site_id,
        )

        duplicate_ssid_open_api_vo.additional_properties = d
        return duplicate_ssid_open_api_vo

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
