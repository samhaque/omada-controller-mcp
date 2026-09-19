from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_select_macs_vo import BatchSelectMacsVO
    from ..models.dhcp_user_filter_vo_sorts import DhcpUserFilterVOSorts


T = TypeVar("T", bound="DhcpUserFilterVO")


@_attrs_define
class DhcpUserFilterVO:
    """
    Attributes:
        select_macs (BatchSelectMacsVO): Selected Macs
        select_ips (list[str]): Selected Ips
        net_id (str | Unset): Lan Network IDs
        server_mac (str | Unset): Dhcp Server Macs
        server_stack_id (str | Unset): Dhcp Server StackIds
        type_ (str | Unset): Filter Type of Dhcp User: "device", "client" or "device, client"
        search_key (str | Unset): Search Key
        sorts (DhcpUserFilterVOSorts | Unset): Sort rule, key: sort field, value: sort direction, value parameter may be
            one of asc or desc.
    """

    select_macs: BatchSelectMacsVO
    select_ips: list[str]
    net_id: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    search_key: str | Unset = UNSET
    sorts: DhcpUserFilterVOSorts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_macs = self.select_macs.to_dict()

        select_ips = self.select_ips

        net_id = self.net_id

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        type_ = self.type_

        search_key = self.search_key

        sorts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = self.sorts.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selectMacs": select_macs,
                "selectIps": select_ips,
            }
        )
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if server_mac is not UNSET:
            field_dict["serverMac"] = server_mac
        if server_stack_id is not UNSET:
            field_dict["serverStackId"] = server_stack_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if sorts is not UNSET:
            field_dict["sorts"] = sorts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_select_macs_vo import BatchSelectMacsVO
        from ..models.dhcp_user_filter_vo_sorts import (
            DhcpUserFilterVOSorts,
        )

        d = dict(src_dict)
        select_macs = BatchSelectMacsVO.from_dict(d.pop("selectMacs"))

        select_ips = cast(list[str], d.pop("selectIps"))

        net_id = d.pop("netId", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        type_ = d.pop("type", UNSET)

        search_key = d.pop("searchKey", UNSET)

        _sorts = d.pop("sorts", UNSET)
        sorts: DhcpUserFilterVOSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = DhcpUserFilterVOSorts.from_dict(_sorts)

        dhcp_user_filter_vo = cls(
            select_macs=select_macs,
            select_ips=select_ips,
            net_id=net_id,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
            type_=type_,
            search_key=search_key,
            sorts=sorts,
        )

        dhcp_user_filter_vo.additional_properties = d
        return dhcp_user_filter_vo

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
