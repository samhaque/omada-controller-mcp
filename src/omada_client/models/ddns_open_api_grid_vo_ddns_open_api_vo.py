from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ddns_open_api_vo import DdnsOpenApiVO


T = TypeVar("T", bound="DdnsOpenApiGridVODdnsOpenApiVO")


@_attrs_define
class DdnsOpenApiGridVODdnsOpenApiVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[DdnsOpenApiVO] | Unset):
        support_custom_ddns (bool | Unset): Whether Custom Service Provider is supported in Dynamic DNS.
        support_custom_interval (bool | Unset): Whether Custom Update Interval is supported in Dynamic DNS.
        support_tp_linkddns (int | Unset): Whether Dynamic DNS supports TP-Link as a service provider. 0: Not supported,
            1: Supported and not configured, 2: Supported and configured.
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[DdnsOpenApiVO] | Unset = UNSET
    support_custom_ddns: bool | Unset = UNSET
    support_custom_interval: bool | Unset = UNSET
    support_tp_linkddns: int | Unset = UNSET
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

        support_custom_ddns = self.support_custom_ddns

        support_custom_interval = self.support_custom_interval

        support_tp_linkddns = self.support_tp_linkddns

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
        if support_custom_ddns is not UNSET:
            field_dict["supportCustomDdns"] = support_custom_ddns
        if support_custom_interval is not UNSET:
            field_dict["supportCustomInterval"] = support_custom_interval
        if support_tp_linkddns is not UNSET:
            field_dict["supportTpLinkddns"] = support_tp_linkddns
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ddns_open_api_vo import DdnsOpenApiVO

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[DdnsOpenApiVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = DdnsOpenApiVO.from_dict(data_item_data)

                data.append(data_item)

        support_custom_ddns = d.pop("supportCustomDdns", UNSET)

        support_custom_interval = d.pop("supportCustomInterval", UNSET)

        support_tp_linkddns = d.pop("supportTpLinkddns", UNSET)

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        ddns_open_api_grid_vo_ddns_open_api_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_custom_ddns=support_custom_ddns,
            support_custom_interval=support_custom_interval,
            support_tp_linkddns=support_tp_linkddns,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
        )

        ddns_open_api_grid_vo_ddns_open_api_vo.additional_properties = d
        return ddns_open_api_grid_vo_ddns_open_api_vo

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
