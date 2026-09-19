from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_oui_mode_open_api_vo import DeviceOuiModeOpenApiVO
    from ..models.vlan_oui_mode_open_api_vo import VlanOuiModeOpenApiVO


T = TypeVar("T", bound="OuiBasedVlanSwitchOpenApiVO")


@_attrs_define
class OuiBasedVlanSwitchOpenApiVO:
    """
    Attributes:
        enable (bool): Switch Rule state.
        name (str): Switch Rule name should contain 1 to 128 characters.
        mode (int): Switch Rule type. 0:"All device port", 1:"Custom device port"
        rule_combine (list[VlanOuiModeOpenApiVO]): Basic vlan-oui-priority configuration of oui based rule. Cannot be
            empty.
        device_list (list[DeviceOuiModeOpenApiVO] | Unset): When mode is 1, should configure device info.
    """

    enable: bool
    name: str
    mode: int
    rule_combine: list[VlanOuiModeOpenApiVO]
    device_list: list[DeviceOuiModeOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        name = self.name

        mode = self.mode

        rule_combine = []
        for rule_combine_item_data in self.rule_combine:
            rule_combine_item = rule_combine_item_data.to_dict()
            rule_combine.append(rule_combine_item)

        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "name": name,
                "mode": mode,
                "ruleCombine": rule_combine,
            }
        )
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_oui_mode_open_api_vo import (
            DeviceOuiModeOpenApiVO,
        )
        from ..models.vlan_oui_mode_open_api_vo import (
            VlanOuiModeOpenApiVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        name = d.pop("name")

        mode = d.pop("mode")

        rule_combine = []
        _rule_combine = d.pop("ruleCombine")
        for rule_combine_item_data in _rule_combine:
            rule_combine_item = VlanOuiModeOpenApiVO.from_dict(rule_combine_item_data)

            rule_combine.append(rule_combine_item)

        _device_list = d.pop("deviceList", UNSET)
        device_list: list[DeviceOuiModeOpenApiVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = DeviceOuiModeOpenApiVO.from_dict(
                    device_list_item_data
                )

                device_list.append(device_list_item)

        oui_based_vlan_switch_open_api_vo = cls(
            enable=enable,
            name=name,
            mode=mode,
            rule_combine=rule_combine,
            device_list=device_list,
        )

        oui_based_vlan_switch_open_api_vo.additional_properties = d
        return oui_based_vlan_switch_open_api_vo

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
