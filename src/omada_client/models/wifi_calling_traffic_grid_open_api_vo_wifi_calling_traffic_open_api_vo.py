from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wifi_calling_traffic_open_api_vo import WifiCallingTrafficOpenApiVO


T = TypeVar("T", bound="WifiCallingTrafficGridOpenApiVOWifiCallingTrafficOpenApiVO")


@_attrs_define
class WifiCallingTrafficGridOpenApiVOWifiCallingTrafficOpenApiVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[WifiCallingTrafficOpenApiVO] | Unset):
        top_k_ssids (list[WifiCallingTrafficOpenApiVO] | Unset): Top k SSIDs based on voice call traffic statistics.
        top_kepd_gs (list[WifiCallingTrafficOpenApiVO] | Unset): Top k ePDGs based on voice call traffic statistics.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[WifiCallingTrafficOpenApiVO] | Unset = UNSET
    top_k_ssids: list[WifiCallingTrafficOpenApiVO] | Unset = UNSET
    top_kepd_gs: list[WifiCallingTrafficOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        top_k_ssids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_k_ssids, Unset):
            top_k_ssids = []
            for top_k_ssids_item_data in self.top_k_ssids:
                top_k_ssids_item = top_k_ssids_item_data.to_dict()
                top_k_ssids.append(top_k_ssids_item)

        top_kepd_gs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_kepd_gs, Unset):
            top_kepd_gs = []
            for top_kepd_gs_item_data in self.top_kepd_gs:
                top_kepd_gs_item = top_kepd_gs_item_data.to_dict()
                top_kepd_gs.append(top_kepd_gs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data
        if top_k_ssids is not UNSET:
            field_dict["topKSsids"] = top_k_ssids
        if top_kepd_gs is not UNSET:
            field_dict["topKEPDGs"] = top_kepd_gs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wifi_calling_traffic_open_api_vo import (
            WifiCallingTrafficOpenApiVO,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[WifiCallingTrafficOpenApiVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = WifiCallingTrafficOpenApiVO.from_dict(data_item_data)

                data.append(data_item)

        _top_k_ssids = d.pop("topKSsids", UNSET)
        top_k_ssids: list[WifiCallingTrafficOpenApiVO] | Unset = UNSET
        if _top_k_ssids is not UNSET:
            top_k_ssids = []
            for top_k_ssids_item_data in _top_k_ssids:
                top_k_ssids_item = WifiCallingTrafficOpenApiVO.from_dict(
                    top_k_ssids_item_data
                )

                top_k_ssids.append(top_k_ssids_item)

        _top_kepd_gs = d.pop("topKEPDGs", UNSET)
        top_kepd_gs: list[WifiCallingTrafficOpenApiVO] | Unset = UNSET
        if _top_kepd_gs is not UNSET:
            top_kepd_gs = []
            for top_kepd_gs_item_data in _top_kepd_gs:
                top_kepd_gs_item = WifiCallingTrafficOpenApiVO.from_dict(
                    top_kepd_gs_item_data
                )

                top_kepd_gs.append(top_kepd_gs_item)

        wifi_calling_traffic_grid_open_api_vo_wifi_calling_traffic_open_api_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            top_k_ssids=top_k_ssids,
            top_kepd_gs=top_kepd_gs,
        )

        wifi_calling_traffic_grid_open_api_vo_wifi_calling_traffic_open_api_vo.additional_properties = d
        return wifi_calling_traffic_grid_open_api_vo_wifi_calling_traffic_open_api_vo

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
