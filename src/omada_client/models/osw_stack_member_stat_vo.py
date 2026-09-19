from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stack_member_stat_vo_port_map import OswStackMemberStatVOPortMap
    from ..models.osw_stat_dto import OswStatDTO


T = TypeVar("T", bound="OswStackMemberStatVO")


@_attrs_define
class OswStackMemberStatVO:
    """
    Attributes:
        unit (int | Unset): Unit ID
        mac (str | Unset): Device mac
        port_map (OswStackMemberStatVOPortMap | Unset): Port total traffic map
        stat_list (list[OswStatDTO] | Unset): Detailed traffic information of ports
    """

    unit: int | Unset = UNSET
    mac: str | Unset = UNSET
    port_map: OswStackMemberStatVOPortMap | Unset = UNSET
    stat_list: list[OswStatDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unit = self.unit

        mac = self.mac

        port_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_map, Unset):
            port_map = self.port_map.to_dict()

        stat_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stat_list, Unset):
            stat_list = []
            for stat_list_item_data in self.stat_list:
                stat_list_item = stat_list_item_data.to_dict()
                stat_list.append(stat_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unit is not UNSET:
            field_dict["unit"] = unit
        if mac is not UNSET:
            field_dict["mac"] = mac
        if port_map is not UNSET:
            field_dict["portMap"] = port_map
        if stat_list is not UNSET:
            field_dict["statList"] = stat_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stack_member_stat_vo_port_map import (
            OswStackMemberStatVOPortMap,
        )
        from ..models.osw_stat_dto import OswStatDTO

        d = dict(src_dict)
        unit = d.pop("unit", UNSET)

        mac = d.pop("mac", UNSET)

        _port_map = d.pop("portMap", UNSET)
        port_map: OswStackMemberStatVOPortMap | Unset
        if isinstance(_port_map, Unset):
            port_map = UNSET
        else:
            port_map = OswStackMemberStatVOPortMap.from_dict(_port_map)

        _stat_list = d.pop("statList", UNSET)
        stat_list: list[OswStatDTO] | Unset = UNSET
        if _stat_list is not UNSET:
            stat_list = []
            for stat_list_item_data in _stat_list:
                stat_list_item = OswStatDTO.from_dict(stat_list_item_data)

                stat_list.append(stat_list_item)

        osw_stack_member_stat_vo = cls(
            unit=unit,
            mac=mac,
            port_map=port_map,
            stat_list=stat_list,
        )

        osw_stack_member_stat_vo.additional_properties = d
        return osw_stack_member_stat_vo

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
