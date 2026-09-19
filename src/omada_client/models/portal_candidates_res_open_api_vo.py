from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portal_network_open_api_vo import PortalNetworkOpenApiVO
    from ..models.portal_wlan_open_api_vo import PortalWlanOpenApiVO


T = TypeVar("T", bound="PortalCandidatesResOpenApiVO")


@_attrs_define
class PortalCandidatesResOpenApiVO:
    """
    Attributes:
        wlan_list (list[PortalWlanOpenApiVO] | Unset): WLAN list of the portals.
        network_list (list[PortalNetworkOpenApiVO] | Unset): Network list of the portals.
    """

    wlan_list: list[PortalWlanOpenApiVO] | Unset = UNSET
    network_list: list[PortalNetworkOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wlan_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wlan_list, Unset):
            wlan_list = []
            for wlan_list_item_data in self.wlan_list:
                wlan_list_item = wlan_list_item_data.to_dict()
                wlan_list.append(wlan_list_item)

        network_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_list, Unset):
            network_list = []
            for network_list_item_data in self.network_list:
                network_list_item = network_list_item_data.to_dict()
                network_list.append(network_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wlan_list is not UNSET:
            field_dict["wlanList"] = wlan_list
        if network_list is not UNSET:
            field_dict["networkList"] = network_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.portal_network_open_api_vo import (
            PortalNetworkOpenApiVO,
        )
        from ..models.portal_wlan_open_api_vo import (
            PortalWlanOpenApiVO,
        )

        d = dict(src_dict)
        _wlan_list = d.pop("wlanList", UNSET)
        wlan_list: list[PortalWlanOpenApiVO] | Unset = UNSET
        if _wlan_list is not UNSET:
            wlan_list = []
            for wlan_list_item_data in _wlan_list:
                wlan_list_item = PortalWlanOpenApiVO.from_dict(wlan_list_item_data)

                wlan_list.append(wlan_list_item)

        _network_list = d.pop("networkList", UNSET)
        network_list: list[PortalNetworkOpenApiVO] | Unset = UNSET
        if _network_list is not UNSET:
            network_list = []
            for network_list_item_data in _network_list:
                network_list_item = PortalNetworkOpenApiVO.from_dict(
                    network_list_item_data
                )

                network_list.append(network_list_item)

        portal_candidates_res_open_api_vo = cls(
            wlan_list=wlan_list,
            network_list=network_list,
        )

        portal_candidates_res_open_api_vo.additional_properties = d
        return portal_candidates_res_open_api_vo

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
