from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_user_grid_vo_dhcp_user_vo_net_name_to_id_map import (
        DhcpUserGridVODhcpUserVONetNameToIdMap,
    )
    from ..models.dhcp_user_grid_vo_dhcp_user_vo_server_name_to_mac_map import (
        DhcpUserGridVODhcpUserVOServerNameToMacMap,
    )
    from ..models.dhcp_user_grid_vo_dhcp_user_vo_server_name_to_stack_id_map import (
        DhcpUserGridVODhcpUserVOServerNameToStackIdMap,
    )
    from ..models.dhcp_user_vo import DhcpUserVO


T = TypeVar("T", bound="DhcpUserGridVODhcpUserVO")


@_attrs_define
class DhcpUserGridVODhcpUserVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[DhcpUserVO] | Unset):
        server_name_to_mac_map (DhcpUserGridVODhcpUserVOServerNameToMacMap | Unset): Mapping between server name and
            macs
        server_name_to_stack_id_map (DhcpUserGridVODhcpUserVOServerNameToStackIdMap | Unset): Mapping between server
            name and stack IDs
        net_name_to_id_map (DhcpUserGridVODhcpUserVONetNameToIdMap | Unset): Mapping between lan network name and lan
            network ID
        selected_num (int | Unset): The number of DHCP users that cannot be selected when adding from the user list in
            DHCP reservation.
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[DhcpUserVO] | Unset = UNSET
    server_name_to_mac_map: DhcpUserGridVODhcpUserVOServerNameToMacMap | Unset = UNSET
    server_name_to_stack_id_map: (
        DhcpUserGridVODhcpUserVOServerNameToStackIdMap | Unset
    ) = UNSET
    net_name_to_id_map: DhcpUserGridVODhcpUserVONetNameToIdMap | Unset = UNSET
    selected_num: int | Unset = UNSET
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

        server_name_to_mac_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_name_to_mac_map, Unset):
            server_name_to_mac_map = self.server_name_to_mac_map.to_dict()

        server_name_to_stack_id_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server_name_to_stack_id_map, Unset):
            server_name_to_stack_id_map = self.server_name_to_stack_id_map.to_dict()

        net_name_to_id_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.net_name_to_id_map, Unset):
            net_name_to_id_map = self.net_name_to_id_map.to_dict()

        selected_num = self.selected_num

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
        if server_name_to_mac_map is not UNSET:
            field_dict["serverNameToMacMap"] = server_name_to_mac_map
        if server_name_to_stack_id_map is not UNSET:
            field_dict["serverNameToStackIdMap"] = server_name_to_stack_id_map
        if net_name_to_id_map is not UNSET:
            field_dict["netNameToIdMap"] = net_name_to_id_map
        if selected_num is not UNSET:
            field_dict["selectedNum"] = selected_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_user_grid_vo_dhcp_user_vo_net_name_to_id_map import (
            DhcpUserGridVODhcpUserVONetNameToIdMap,
        )
        from ..models.dhcp_user_grid_vo_dhcp_user_vo_server_name_to_mac_map import (
            DhcpUserGridVODhcpUserVOServerNameToMacMap,
        )
        from ..models.dhcp_user_grid_vo_dhcp_user_vo_server_name_to_stack_id_map import (
            DhcpUserGridVODhcpUserVOServerNameToStackIdMap,
        )
        from ..models.dhcp_user_vo import DhcpUserVO

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[DhcpUserVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = DhcpUserVO.from_dict(data_item_data)

                data.append(data_item)

        _server_name_to_mac_map = d.pop("serverNameToMacMap", UNSET)
        server_name_to_mac_map: DhcpUserGridVODhcpUserVOServerNameToMacMap | Unset
        if isinstance(_server_name_to_mac_map, Unset):
            server_name_to_mac_map = UNSET
        else:
            server_name_to_mac_map = (
                DhcpUserGridVODhcpUserVOServerNameToMacMap.from_dict(
                    _server_name_to_mac_map
                )
            )

        _server_name_to_stack_id_map = d.pop("serverNameToStackIdMap", UNSET)
        server_name_to_stack_id_map: (
            DhcpUserGridVODhcpUserVOServerNameToStackIdMap | Unset
        )
        if isinstance(_server_name_to_stack_id_map, Unset):
            server_name_to_stack_id_map = UNSET
        else:
            server_name_to_stack_id_map = (
                DhcpUserGridVODhcpUserVOServerNameToStackIdMap.from_dict(
                    _server_name_to_stack_id_map
                )
            )

        _net_name_to_id_map = d.pop("netNameToIdMap", UNSET)
        net_name_to_id_map: DhcpUserGridVODhcpUserVONetNameToIdMap | Unset
        if isinstance(_net_name_to_id_map, Unset):
            net_name_to_id_map = UNSET
        else:
            net_name_to_id_map = DhcpUserGridVODhcpUserVONetNameToIdMap.from_dict(
                _net_name_to_id_map
            )

        selected_num = d.pop("selectedNum", UNSET)

        dhcp_user_grid_vo_dhcp_user_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            server_name_to_mac_map=server_name_to_mac_map,
            server_name_to_stack_id_map=server_name_to_stack_id_map,
            net_name_to_id_map=net_name_to_id_map,
            selected_num=selected_num,
        )

        dhcp_user_grid_vo_dhcp_user_vo.additional_properties = d
        return dhcp_user_grid_vo_dhcp_user_vo

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
