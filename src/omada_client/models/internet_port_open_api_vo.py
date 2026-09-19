from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lte_wan_setting_open_api_vo import LteWanSettingOpenApiVO
    from ..models.usb_lte_setting_open_api_vo import UsbLteSettingOpenApiVO
    from ..models.wan_port_setting_open_api_vo import WanPortSettingOpenApiVO


T = TypeVar("T", bound="InternetPortOpenApiVO")


@_attrs_define
class InternetPortOpenApiVO:
    """
    Attributes:
        type_ (int): The Type of the Internet port as follows: 0: WAN; 1: USB; 2: LTE; 3: DSL.
        wan_port_setting (WanPortSettingOpenApiVO | Unset): WAN ports config
        usb_lte_setting (UsbLteSettingOpenApiVO | Unset): A list of USB LTE setting.
        lte_wan_setting (LteWanSettingOpenApiVO | Unset): The setting of the WAN lte.
    """

    type_: int
    wan_port_setting: WanPortSettingOpenApiVO | Unset = UNSET
    usb_lte_setting: UsbLteSettingOpenApiVO | Unset = UNSET
    lte_wan_setting: LteWanSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        wan_port_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_port_setting, Unset):
            wan_port_setting = self.wan_port_setting.to_dict()

        usb_lte_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.usb_lte_setting, Unset):
            usb_lte_setting = self.usb_lte_setting.to_dict()

        lte_wan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lte_wan_setting, Unset):
            lte_wan_setting = self.lte_wan_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if wan_port_setting is not UNSET:
            field_dict["wanPortSetting"] = wan_port_setting
        if usb_lte_setting is not UNSET:
            field_dict["usbLteSetting"] = usb_lte_setting
        if lte_wan_setting is not UNSET:
            field_dict["lteWanSetting"] = lte_wan_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lte_wan_setting_open_api_vo import (
            LteWanSettingOpenApiVO,
        )
        from ..models.usb_lte_setting_open_api_vo import (
            UsbLteSettingOpenApiVO,
        )
        from ..models.wan_port_setting_open_api_vo import (
            WanPortSettingOpenApiVO,
        )

        d = dict(src_dict)
        type_ = d.pop("type")

        _wan_port_setting = d.pop("wanPortSetting", UNSET)
        wan_port_setting: WanPortSettingOpenApiVO | Unset
        if isinstance(_wan_port_setting, Unset):
            wan_port_setting = UNSET
        else:
            wan_port_setting = WanPortSettingOpenApiVO.from_dict(_wan_port_setting)

        _usb_lte_setting = d.pop("usbLteSetting", UNSET)
        usb_lte_setting: UsbLteSettingOpenApiVO | Unset
        if isinstance(_usb_lte_setting, Unset):
            usb_lte_setting = UNSET
        else:
            usb_lte_setting = UsbLteSettingOpenApiVO.from_dict(_usb_lte_setting)

        _lte_wan_setting = d.pop("lteWanSetting", UNSET)
        lte_wan_setting: LteWanSettingOpenApiVO | Unset
        if isinstance(_lte_wan_setting, Unset):
            lte_wan_setting = UNSET
        else:
            lte_wan_setting = LteWanSettingOpenApiVO.from_dict(_lte_wan_setting)

        internet_port_open_api_vo = cls(
            type_=type_,
            wan_port_setting=wan_port_setting,
            usb_lte_setting=usb_lte_setting,
            lte_wan_setting=lte_wan_setting,
        )

        internet_port_open_api_vo.additional_properties = d
        return internet_port_open_api_vo

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
