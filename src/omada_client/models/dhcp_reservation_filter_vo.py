from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_select_macs_vo import BatchSelectMacsVO
    from ..models.dhcp_reservation_filter_vo_sort_map import (
        DhcpReservationFilterVOSortMap,
    )


T = TypeVar("T", bound="DhcpReservationFilterVO")


@_attrs_define
class DhcpReservationFilterVO:
    """
    Attributes:
        select_macs (BatchSelectMacsVO): Selected Macs
        sort_map (DhcpReservationFilterVOSortMap | Unset): Sort Direction. The keys that can be sorted are:mac, ip,
            net_name, description, status, clientName, name, value is asc or desc
        net_id (str | Unset): Lan Network IDs
        type_ (str | Unset): Device types for which IP is reserved
        search_key (str | Unset): Search Key
    """

    select_macs: BatchSelectMacsVO
    sort_map: DhcpReservationFilterVOSortMap | Unset = UNSET
    net_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    search_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_macs = self.select_macs.to_dict()

        sort_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sort_map, Unset):
            sort_map = self.sort_map.to_dict()

        net_id = self.net_id

        type_ = self.type_

        search_key = self.search_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selectMacs": select_macs,
            }
        )
        if sort_map is not UNSET:
            field_dict["sortMap"] = sort_map
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_select_macs_vo import BatchSelectMacsVO
        from ..models.dhcp_reservation_filter_vo_sort_map import (
            DhcpReservationFilterVOSortMap,
        )

        d = dict(src_dict)
        select_macs = BatchSelectMacsVO.from_dict(d.pop("selectMacs"))

        _sort_map = d.pop("sortMap", UNSET)
        sort_map: DhcpReservationFilterVOSortMap | Unset
        if isinstance(_sort_map, Unset):
            sort_map = UNSET
        else:
            sort_map = DhcpReservationFilterVOSortMap.from_dict(_sort_map)

        net_id = d.pop("netId", UNSET)

        type_ = d.pop("type", UNSET)

        search_key = d.pop("searchKey", UNSET)

        dhcp_reservation_filter_vo = cls(
            select_macs=select_macs,
            sort_map=sort_map,
            net_id=net_id,
            type_=type_,
            search_key=search_key,
        )

        dhcp_reservation_filter_vo.additional_properties = d
        return dhcp_reservation_filter_vo

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
