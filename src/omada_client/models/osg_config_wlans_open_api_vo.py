from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_ssid_override_open_api_vo import OsgSsidOverrideOpenApiVO


T = TypeVar("T", bound="OsgConfigWlansOpenApiVO")


@_attrs_define
class OsgConfigWlansOpenApiVO:
    """
    Attributes:
        ssid_overrides (list[OsgSsidOverrideOpenApiVO]): Overrided SSID List
        wlan_id (str | Unset): WLAN ID
        wlans_resource (int | Unset): Wlans Resource
    """

    ssid_overrides: list[OsgSsidOverrideOpenApiVO]
    wlan_id: str | Unset = UNSET
    wlans_resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_overrides = []
        for ssid_overrides_item_data in self.ssid_overrides:
            ssid_overrides_item = ssid_overrides_item_data.to_dict()
            ssid_overrides.append(ssid_overrides_item)

        wlan_id = self.wlan_id

        wlans_resource = self.wlans_resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ssidOverrides": ssid_overrides,
            }
        )
        if wlan_id is not UNSET:
            field_dict["wlanId"] = wlan_id
        if wlans_resource is not UNSET:
            field_dict["wlansResource"] = wlans_resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_ssid_override_open_api_vo import (
            OsgSsidOverrideOpenApiVO,
        )

        d = dict(src_dict)
        ssid_overrides = []
        _ssid_overrides = d.pop("ssidOverrides")
        for ssid_overrides_item_data in _ssid_overrides:
            ssid_overrides_item = OsgSsidOverrideOpenApiVO.from_dict(
                ssid_overrides_item_data
            )

            ssid_overrides.append(ssid_overrides_item)

        wlan_id = d.pop("wlanId", UNSET)

        wlans_resource = d.pop("wlansResource", UNSET)

        osg_config_wlans_open_api_vo = cls(
            ssid_overrides=ssid_overrides,
            wlan_id=wlan_id,
            wlans_resource=wlans_resource,
        )

        osg_config_wlans_open_api_vo.additional_properties = d
        return osg_config_wlans_open_api_vo

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
