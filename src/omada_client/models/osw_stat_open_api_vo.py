from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stat_detail_open_api_vo import OswStatDetailOpenApiVO
    from ..models.osw_stat_open_api_vo_port_map import OswStatOpenApiVOPortMap


T = TypeVar("T", bound="OswStatOpenApiVO")


@_attrs_define
class OswStatOpenApiVO:
    """
    Attributes:
        port_map (OswStatOpenApiVOPortMap | Unset): Port total traffic map
        stat_list (list[OswStatDetailOpenApiVO] | Unset): Detailed traffic information of ports
        switch_type (int | Unset): Type of Switch should be a value as follows: 0:Non-Agile Series Switch, 1:Agile
            Series Switch
    """

    port_map: OswStatOpenApiVOPortMap | Unset = UNSET
    stat_list: list[OswStatDetailOpenApiVO] | Unset = UNSET
    switch_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_map, Unset):
            port_map = self.port_map.to_dict()

        stat_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stat_list, Unset):
            stat_list = []
            for stat_list_item_data in self.stat_list:
                stat_list_item = stat_list_item_data.to_dict()
                stat_list.append(stat_list_item)

        switch_type = self.switch_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_map is not UNSET:
            field_dict["portMap"] = port_map
        if stat_list is not UNSET:
            field_dict["statList"] = stat_list
        if switch_type is not UNSET:
            field_dict["switchType"] = switch_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stat_detail_open_api_vo import (
            OswStatDetailOpenApiVO,
        )
        from ..models.osw_stat_open_api_vo_port_map import (
            OswStatOpenApiVOPortMap,
        )

        d = dict(src_dict)
        _port_map = d.pop("portMap", UNSET)
        port_map: OswStatOpenApiVOPortMap | Unset
        if isinstance(_port_map, Unset):
            port_map = UNSET
        else:
            port_map = OswStatOpenApiVOPortMap.from_dict(_port_map)

        _stat_list = d.pop("statList", UNSET)
        stat_list: list[OswStatDetailOpenApiVO] | Unset = UNSET
        if _stat_list is not UNSET:
            stat_list = []
            for stat_list_item_data in _stat_list:
                stat_list_item = OswStatDetailOpenApiVO.from_dict(stat_list_item_data)

                stat_list.append(stat_list_item)

        switch_type = d.pop("switchType", UNSET)

        osw_stat_open_api_vo = cls(
            port_map=port_map,
            stat_list=stat_list,
            switch_type=switch_type,
        )

        osw_stat_open_api_vo.additional_properties = d
        return osw_stat_open_api_vo

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
