from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_forwarding_info_template import PortForwardingInfoTemplate


T = TypeVar("T", bound="PortForwardingOpenApiGridVOPortForwardingInfoTemplate")


@_attrs_define
class PortForwardingOpenApiGridVOPortForwardingInfoTemplate:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[PortForwardingInfoTemplate] | Unset):
        support_wan_ip (bool | Unset): Whether Wan Alias Ip configuration is supported of port forwarding.
        support_virtual_wan (bool | Unset): Whether Virtual Wan configuration is supported of port forwarding.
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[PortForwardingInfoTemplate] | Unset = UNSET
    support_wan_ip: bool | Unset = UNSET
    support_virtual_wan: bool | Unset = UNSET
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

        support_wan_ip = self.support_wan_ip

        support_virtual_wan = self.support_virtual_wan

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
        if support_wan_ip is not UNSET:
            field_dict["supportWanIp"] = support_wan_ip
        if support_virtual_wan is not UNSET:
            field_dict["supportVirtualWan"] = support_virtual_wan
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_forwarding_info_template import (
            PortForwardingInfoTemplate,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[PortForwardingInfoTemplate] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = PortForwardingInfoTemplate.from_dict(data_item_data)

                data.append(data_item)

        support_wan_ip = d.pop("supportWanIp", UNSET)

        support_virtual_wan = d.pop("supportVirtualWan", UNSET)

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        port_forwarding_open_api_grid_vo_port_forwarding_info_template = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_wan_ip=support_wan_ip,
            support_virtual_wan=support_virtual_wan,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
        )

        port_forwarding_open_api_grid_vo_port_forwarding_info_template.additional_properties = d
        return port_forwarding_open_api_grid_vo_port_forwarding_info_template

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
