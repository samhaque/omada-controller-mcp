from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_query_open_api_vo import LanNetworkQueryOpenApiVO


T = TypeVar("T", bound="LanNetworkOpenApiGridVOLanNetworkQueryOpenApiVO")


@_attrs_define
class LanNetworkOpenApiGridVOLanNetworkQueryOpenApiVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[LanNetworkQueryOpenApiVO] | Unset):
        support_multi_vlan (bool | Unset): Whether multi vlan configuration is supported of the lan netowrk.
        support_ra (bool | Unset): Whether Router Advertisement configuration is supported of the lan netowrk.
        support_custom_dhcp_option (bool | Unset): Whether custom DHCP option configuration is supported of the lan
            netowrk.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[LanNetworkQueryOpenApiVO] | Unset = UNSET
    support_multi_vlan: bool | Unset = UNSET
    support_ra: bool | Unset = UNSET
    support_custom_dhcp_option: bool | Unset = UNSET
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

        support_multi_vlan = self.support_multi_vlan

        support_ra = self.support_ra

        support_custom_dhcp_option = self.support_custom_dhcp_option

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
        if support_multi_vlan is not UNSET:
            field_dict["supportMultiVlan"] = support_multi_vlan
        if support_ra is not UNSET:
            field_dict["supportRA"] = support_ra
        if support_custom_dhcp_option is not UNSET:
            field_dict["supportCustomDhcpOption"] = support_custom_dhcp_option

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_query_open_api_vo import (
            LanNetworkQueryOpenApiVO,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[LanNetworkQueryOpenApiVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = LanNetworkQueryOpenApiVO.from_dict(data_item_data)

                data.append(data_item)

        support_multi_vlan = d.pop("supportMultiVlan", UNSET)

        support_ra = d.pop("supportRA", UNSET)

        support_custom_dhcp_option = d.pop("supportCustomDhcpOption", UNSET)

        lan_network_open_api_grid_vo_lan_network_query_open_api_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            support_multi_vlan=support_multi_vlan,
            support_ra=support_ra,
            support_custom_dhcp_option=support_custom_dhcp_option,
        )

        lan_network_open_api_grid_vo_lan_network_query_open_api_vo.additional_properties = d
        return lan_network_open_api_grid_vo_lan_network_query_open_api_vo

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
