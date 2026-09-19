from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_global_search_summary import DeviceGlobalSearchSummary
    from ..models.global_search_result_open_api_vo_site_names import (
        GlobalSearchResultOpenApiVOSiteNames,
    )


T = TypeVar("T", bound="GlobalSearchResultOpenApiVO")


@_attrs_define
class GlobalSearchResultOpenApiVO:
    """
    Attributes:
        site_names (GlobalSearchResultOpenApiVOSiteNames | Unset): site name
        devices (list[DeviceGlobalSearchSummary] | Unset): device list result
    """

    site_names: GlobalSearchResultOpenApiVOSiteNames | Unset = UNSET
    devices: list[DeviceGlobalSearchSummary] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_names: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site_names, Unset):
            site_names = self.site_names.to_dict()

        devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_names is not UNSET:
            field_dict["siteNames"] = site_names
        if devices is not UNSET:
            field_dict["devices"] = devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_global_search_summary import (
            DeviceGlobalSearchSummary,
        )
        from ..models.global_search_result_open_api_vo_site_names import (
            GlobalSearchResultOpenApiVOSiteNames,
        )

        d = dict(src_dict)
        _site_names = d.pop("siteNames", UNSET)
        site_names: GlobalSearchResultOpenApiVOSiteNames | Unset
        if isinstance(_site_names, Unset):
            site_names = UNSET
        else:
            site_names = GlobalSearchResultOpenApiVOSiteNames.from_dict(_site_names)

        _devices = d.pop("devices", UNSET)
        devices: list[DeviceGlobalSearchSummary] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = DeviceGlobalSearchSummary.from_dict(devices_item_data)

                devices.append(devices_item)

        global_search_result_open_api_vo = cls(
            site_names=site_names,
            devices=devices,
        )

        global_search_result_open_api_vo.additional_properties = d
        return global_search_result_open_api_vo

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
