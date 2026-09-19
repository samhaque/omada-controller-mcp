from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usb_lte_setting_open_api_vo import UsbLteSettingOpenApiVO
    from ..models.wan_port_setting_open_api_vo import WanPortSettingOpenApiVO


T = TypeVar("T", bound="WanSettingOpenApiVO")


@_attrs_define
class WanSettingOpenApiVO:
    """
    Attributes:
        wan_ports_config (list[WanPortSettingOpenApiVO] | Unset): WAN ports config
        usb_ports_config (list[UsbLteSettingOpenApiVO] | Unset): USB lte ports config
    """

    wan_ports_config: list[WanPortSettingOpenApiVO] | Unset = UNSET
    usb_ports_config: list[UsbLteSettingOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_ports_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_ports_config, Unset):
            wan_ports_config = []
            for wan_ports_config_item_data in self.wan_ports_config:
                wan_ports_config_item = wan_ports_config_item_data.to_dict()
                wan_ports_config.append(wan_ports_config_item)

        usb_ports_config: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.usb_ports_config, Unset):
            usb_ports_config = []
            for usb_ports_config_item_data in self.usb_ports_config:
                usb_ports_config_item = usb_ports_config_item_data.to_dict()
                usb_ports_config.append(usb_ports_config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wan_ports_config is not UNSET:
            field_dict["wanPortsConfig"] = wan_ports_config
        if usb_ports_config is not UNSET:
            field_dict["UsbPortsConfig"] = usb_ports_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.usb_lte_setting_open_api_vo import (
            UsbLteSettingOpenApiVO,
        )
        from ..models.wan_port_setting_open_api_vo import (
            WanPortSettingOpenApiVO,
        )

        d = dict(src_dict)
        _wan_ports_config = d.pop("wanPortsConfig", UNSET)
        wan_ports_config: list[WanPortSettingOpenApiVO] | Unset = UNSET
        if _wan_ports_config is not UNSET:
            wan_ports_config = []
            for wan_ports_config_item_data in _wan_ports_config:
                wan_ports_config_item = WanPortSettingOpenApiVO.from_dict(
                    wan_ports_config_item_data
                )

                wan_ports_config.append(wan_ports_config_item)

        _usb_ports_config = d.pop("UsbPortsConfig", UNSET)
        usb_ports_config: list[UsbLteSettingOpenApiVO] | Unset = UNSET
        if _usb_ports_config is not UNSET:
            usb_ports_config = []
            for usb_ports_config_item_data in _usb_ports_config:
                usb_ports_config_item = UsbLteSettingOpenApiVO.from_dict(
                    usb_ports_config_item_data
                )

                usb_ports_config.append(usb_ports_config_item)

        wan_setting_open_api_vo = cls(
            wan_ports_config=wan_ports_config,
            usb_ports_config=usb_ports_config,
        )

        wan_setting_open_api_vo.additional_properties = d
        return wan_setting_open_api_vo

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
