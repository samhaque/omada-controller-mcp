from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_ssid_open_api_vo import PortalSsidOpenApiVO


T = TypeVar("T", bound="PortalWlanOpenApiVO")


@_attrs_define
class PortalWlanOpenApiVO:
    """WLAN list of the portals.

    Attributes:
        wlan_id (str | Unset): WLAN ID
        wlan_name (str | Unset): WLAN name
        ssid_list (list[PortalSsidOpenApiVO] | Unset): SSID list of WLAN
    """

    wlan_id: str | Unset = UNSET
    wlan_name: str | Unset = UNSET
    ssid_list: list[PortalSsidOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wlan_id = self.wlan_id

        wlan_name = self.wlan_name

        ssid_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ssid_list, Unset):
            ssid_list = []
            for ssid_list_item_data in self.ssid_list:
                ssid_list_item = ssid_list_item_data.to_dict()
                ssid_list.append(ssid_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wlan_id is not UNSET:
            field_dict["wlanId"] = wlan_id
        if wlan_name is not UNSET:
            field_dict["wlanName"] = wlan_name
        if ssid_list is not UNSET:
            field_dict["ssidList"] = ssid_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.portal_ssid_open_api_vo import (
            PortalSsidOpenApiVO,
        )

        d = dict(src_dict)
        wlan_id = d.pop("wlanId", UNSET)

        wlan_name = d.pop("wlanName", UNSET)

        _ssid_list = d.pop("ssidList", UNSET)
        ssid_list: list[PortalSsidOpenApiVO] | Unset = UNSET
        if _ssid_list is not UNSET:
            ssid_list = []
            for ssid_list_item_data in _ssid_list:
                ssid_list_item = PortalSsidOpenApiVO.from_dict(ssid_list_item_data)

                ssid_list.append(ssid_list_item)

        portal_wlan_open_api_vo = cls(
            wlan_id=wlan_id,
            wlan_name=wlan_name,
            ssid_list=ssid_list,
        )

        portal_wlan_open_api_vo.additional_properties = d
        return portal_wlan_open_api_vo

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
