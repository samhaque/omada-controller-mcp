from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_dsl_open_api_vo import VirtualWanDslOpenApiVO
    from ..models.virtual_wan_ipv_4_setting_info_open_api_vo import (
        VirtualWanIpv4SettingInfoOpenApiVO,
    )


T = TypeVar("T", bound="VirtualWanInfoOpenApiVO")


@_attrs_define
class VirtualWanInfoOpenApiVO:
    """VirtualWanInfo

    Attributes:
        status (bool | Unset): Virtual WAN status.
        name (str | Unset): Virtual WAN name.
        physical_wan_name (str | Unset): Physical WAN name.
        physical_wan_id (str | Unset): Physical WAN ID.
        physical_wan_port_id (int | Unset): Physical WAN port ID.
        id (str | Unset): Virtual WAN ID.
        wan_port_ipv_4_setting (VirtualWanIpv4SettingInfoOpenApiVO | Unset): VirtualWanIpv4SettingInfo
        dsl_setting (VirtualWanDslOpenApiVO | Unset): VirtualWanDslOpenApiVO
    """

    status: bool | Unset = UNSET
    name: str | Unset = UNSET
    physical_wan_name: str | Unset = UNSET
    physical_wan_id: str | Unset = UNSET
    physical_wan_port_id: int | Unset = UNSET
    id: str | Unset = UNSET
    wan_port_ipv_4_setting: VirtualWanIpv4SettingInfoOpenApiVO | Unset = UNSET
    dsl_setting: VirtualWanDslOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        name = self.name

        physical_wan_name = self.physical_wan_name

        physical_wan_id = self.physical_wan_id

        physical_wan_port_id = self.physical_wan_port_id

        id = self.id

        wan_port_ipv_4_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_port_ipv_4_setting, Unset):
            wan_port_ipv_4_setting = self.wan_port_ipv_4_setting.to_dict()

        dsl_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dsl_setting, Unset):
            dsl_setting = self.dsl_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if physical_wan_name is not UNSET:
            field_dict["physicalWanName"] = physical_wan_name
        if physical_wan_id is not UNSET:
            field_dict["physicalWanId"] = physical_wan_id
        if physical_wan_port_id is not UNSET:
            field_dict["physicalWanPortId"] = physical_wan_port_id
        if id is not UNSET:
            field_dict["id"] = id
        if wan_port_ipv_4_setting is not UNSET:
            field_dict["wanPortIpv4Setting"] = wan_port_ipv_4_setting
        if dsl_setting is not UNSET:
            field_dict["dslSetting"] = dsl_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_dsl_open_api_vo import (
            VirtualWanDslOpenApiVO,
        )
        from ..models.virtual_wan_ipv_4_setting_info_open_api_vo import (
            VirtualWanIpv4SettingInfoOpenApiVO,
        )

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        name = d.pop("name", UNSET)

        physical_wan_name = d.pop("physicalWanName", UNSET)

        physical_wan_id = d.pop("physicalWanId", UNSET)

        physical_wan_port_id = d.pop("physicalWanPortId", UNSET)

        id = d.pop("id", UNSET)

        _wan_port_ipv_4_setting = d.pop("wanPortIpv4Setting", UNSET)
        wan_port_ipv_4_setting: VirtualWanIpv4SettingInfoOpenApiVO | Unset
        if isinstance(_wan_port_ipv_4_setting, Unset):
            wan_port_ipv_4_setting = UNSET
        else:
            wan_port_ipv_4_setting = VirtualWanIpv4SettingInfoOpenApiVO.from_dict(
                _wan_port_ipv_4_setting
            )

        _dsl_setting = d.pop("dslSetting", UNSET)
        dsl_setting: VirtualWanDslOpenApiVO | Unset
        if isinstance(_dsl_setting, Unset):
            dsl_setting = UNSET
        else:
            dsl_setting = VirtualWanDslOpenApiVO.from_dict(_dsl_setting)

        virtual_wan_info_open_api_vo = cls(
            status=status,
            name=name,
            physical_wan_name=physical_wan_name,
            physical_wan_id=physical_wan_id,
            physical_wan_port_id=physical_wan_port_id,
            id=id,
            wan_port_ipv_4_setting=wan_port_ipv_4_setting,
            dsl_setting=dsl_setting,
        )

        virtual_wan_info_open_api_vo.additional_properties = d
        return virtual_wan_info_open_api_vo

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
