from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.vlan_oui_mode_open_api_vo import VlanOuiModeOpenApiVO


T = TypeVar("T", bound="OuiBasedVlanTemplateOpenApiVO")


@_attrs_define
class OuiBasedVlanTemplateOpenApiVO:
    """
    Attributes:
        enable (bool): Switch Rule state.
        name (str): Switch Rule name should contain 1 to 128 characters.
        mode (int): Switch Rule type should be a value as follows: 0: All device port
        rule_combine (list[VlanOuiModeOpenApiVO]): Basic vlan-oui-priority configuration of oui based rule. Cannot be
            empty.
    """

    enable: bool
    name: str
    mode: int
    rule_combine: list[VlanOuiModeOpenApiVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        name = self.name

        mode = self.mode

        rule_combine = []
        for rule_combine_item_data in self.rule_combine:
            rule_combine_item = rule_combine_item_data.to_dict()
            rule_combine.append(rule_combine_item)

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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
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

        oui_based_vlan_template_open_api_vo = cls(
            enable=enable,
            name=name,
            mode=mode,
            rule_combine=rule_combine,
        )

        oui_based_vlan_template_open_api_vo.additional_properties = d
        return oui_based_vlan_template_open_api_vo

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
