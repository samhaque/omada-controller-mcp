from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_info_open_api_vo import VirtualWanInfoOpenApiVO


T = TypeVar("T", bound="VirtualWanGridOpenApiVOVirtualWanInfoOpenApiVO")


@_attrs_define
class VirtualWanGridOpenApiVOVirtualWanInfoOpenApiVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[VirtualWanInfoOpenApiVO] | Unset):
        support_mss_clamping (bool | Unset): Whether the pppoe supports mss clamping.
        support_pppoe_mru (bool | Unset): Whether the virtual WAN supports configuring pppoe mru.
        num_reach_limit (bool | Unset): Whether the virtual WAN reaches number limit.
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[VirtualWanInfoOpenApiVO] | Unset = UNSET
    support_mss_clamping: bool | Unset = UNSET
    support_pppoe_mru: bool | Unset = UNSET
    num_reach_limit: bool | Unset = UNSET
    support_by_ds_lite_and_map_e: bool | Unset = UNSET
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

        support_mss_clamping = self.support_mss_clamping

        support_pppoe_mru = self.support_pppoe_mru

        num_reach_limit = self.num_reach_limit

        support_by_ds_lite_and_map_e = self.support_by_ds_lite_and_map_e

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
        if support_mss_clamping is not UNSET:
            field_dict["supportMssClamping"] = support_mss_clamping
        if support_pppoe_mru is not UNSET:
            field_dict["supportPppoeMru"] = support_pppoe_mru
        if num_reach_limit is not UNSET:
            field_dict["numReachLimit"] = num_reach_limit
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_info_open_api_vo import (
            VirtualWanInfoOpenApiVO,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[VirtualWanInfoOpenApiVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = VirtualWanInfoOpenApiVO.from_dict(data_item_data)

                data.append(data_item)

        support_mss_clamping = d.pop("supportMssClamping", UNSET)

        support_pppoe_mru = d.pop("supportPppoeMru", UNSET)

        num_reach_limit = d.pop("numReachLimit", UNSET)

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        virtual_wan_grid_open_api_vo_virtual_wan_info_open_api_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_mss_clamping=support_mss_clamping,
            support_pppoe_mru=support_pppoe_mru,
            num_reach_limit=num_reach_limit,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
        )

        virtual_wan_grid_open_api_vo_virtual_wan_info_open_api_vo.additional_properties = d
        return virtual_wan_grid_open_api_vo_virtual_wan_info_open_api_vo

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
