from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.grid_vo_wlan_group_open_api_vo import GridVOWlanGroupOpenApiVO


T = TypeVar("T", bound="WlanGroupGridOpenApiVO")


@_attrs_define
class WlanGroupGridOpenApiVO:
    """
    Attributes:
        grid_wlan_group (GridVOWlanGroupOpenApiVO | Unset):
        max_ssids_2g (int | Unset): 2G radio max Ssid number in group
        max_ssids_5g (int | Unset): 5G radio max Ssid number in group
        max_ssids_6g (int | Unset): 6G radio max Ssid number in group
        max_ssids_mlo (int | Unset): max Mlo Ssid number in group
    """

    grid_wlan_group: GridVOWlanGroupOpenApiVO | Unset = UNSET
    max_ssids_2g: int | Unset = UNSET
    max_ssids_5g: int | Unset = UNSET
    max_ssids_6g: int | Unset = UNSET
    max_ssids_mlo: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        grid_wlan_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.grid_wlan_group, Unset):
            grid_wlan_group = self.grid_wlan_group.to_dict()

        max_ssids_2g = self.max_ssids_2g

        max_ssids_5g = self.max_ssids_5g

        max_ssids_6g = self.max_ssids_6g

        max_ssids_mlo = self.max_ssids_mlo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if grid_wlan_group is not UNSET:
            field_dict["gridWlanGroup"] = grid_wlan_group
        if max_ssids_2g is not UNSET:
            field_dict["maxSsids2G"] = max_ssids_2g
        if max_ssids_5g is not UNSET:
            field_dict["maxSsids5G"] = max_ssids_5g
        if max_ssids_6g is not UNSET:
            field_dict["maxSsids6G"] = max_ssids_6g
        if max_ssids_mlo is not UNSET:
            field_dict["maxSsidsMlo"] = max_ssids_mlo

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.grid_vo_wlan_group_open_api_vo import (
            GridVOWlanGroupOpenApiVO,
        )

        d = dict(src_dict)
        _grid_wlan_group = d.pop("gridWlanGroup", UNSET)
        grid_wlan_group: GridVOWlanGroupOpenApiVO | Unset
        if isinstance(_grid_wlan_group, Unset):
            grid_wlan_group = UNSET
        else:
            grid_wlan_group = GridVOWlanGroupOpenApiVO.from_dict(_grid_wlan_group)

        max_ssids_2g = d.pop("maxSsids2G", UNSET)

        max_ssids_5g = d.pop("maxSsids5G", UNSET)

        max_ssids_6g = d.pop("maxSsids6G", UNSET)

        max_ssids_mlo = d.pop("maxSsidsMlo", UNSET)

        wlan_group_grid_open_api_vo = cls(
            grid_wlan_group=grid_wlan_group,
            max_ssids_2g=max_ssids_2g,
            max_ssids_5g=max_ssids_5g,
            max_ssids_6g=max_ssids_6g,
            max_ssids_mlo=max_ssids_mlo,
        )

        wlan_group_grid_open_api_vo.additional_properties = d
        return wlan_group_grid_open_api_vo

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
