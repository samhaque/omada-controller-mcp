from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_port_poe_vo import OsgPortPoeVO


T = TypeVar("T", bound="OsgConfigCommonAdvancedOpenApiVO")


@_attrs_define
class OsgConfigCommonAdvancedOpenApiVO:
    """
    Attributes:
        hw_offload_enable (bool | Unset):
        lldp_enable (bool | Unset): Deprecated, filed lldpSetting is recommended
        lldp_setting (int | Unset):
        poe_settings (list[OsgPortPoeVO] | Unset):
        echo_server (str | Unset):
    """

    hw_offload_enable: bool | Unset = UNSET
    lldp_enable: bool | Unset = UNSET
    lldp_setting: int | Unset = UNSET
    poe_settings: list[OsgPortPoeVO] | Unset = UNSET
    echo_server: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        hw_offload_enable = self.hw_offload_enable

        lldp_enable = self.lldp_enable

        lldp_setting = self.lldp_setting

        poe_settings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.poe_settings, Unset):
            poe_settings = []
            for poe_settings_item_data in self.poe_settings:
                poe_settings_item = poe_settings_item_data.to_dict()
                poe_settings.append(poe_settings_item)

        echo_server = self.echo_server

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hw_offload_enable is not UNSET:
            field_dict["hwOffloadEnable"] = hw_offload_enable
        if lldp_enable is not UNSET:
            field_dict["lldpEnable"] = lldp_enable
        if lldp_setting is not UNSET:
            field_dict["lldpSetting"] = lldp_setting
        if poe_settings is not UNSET:
            field_dict["poeSettings"] = poe_settings
        if echo_server is not UNSET:
            field_dict["echoServer"] = echo_server

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_port_poe_vo import OsgPortPoeVO

        d = dict(src_dict)
        hw_offload_enable = d.pop("hwOffloadEnable", UNSET)

        lldp_enable = d.pop("lldpEnable", UNSET)

        lldp_setting = d.pop("lldpSetting", UNSET)

        _poe_settings = d.pop("poeSettings", UNSET)
        poe_settings: list[OsgPortPoeVO] | Unset = UNSET
        if _poe_settings is not UNSET:
            poe_settings = []
            for poe_settings_item_data in _poe_settings:
                poe_settings_item = OsgPortPoeVO.from_dict(poe_settings_item_data)

                poe_settings.append(poe_settings_item)

        echo_server = d.pop("echoServer", UNSET)

        osg_config_common_advanced_open_api_vo = cls(
            hw_offload_enable=hw_offload_enable,
            lldp_enable=lldp_enable,
            lldp_setting=lldp_setting,
            poe_settings=poe_settings,
            echo_server=echo_server,
        )

        osg_config_common_advanced_open_api_vo.additional_properties = d
        return osg_config_common_advanced_open_api_vo

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
