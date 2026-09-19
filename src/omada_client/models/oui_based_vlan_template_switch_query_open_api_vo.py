from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vlan_oui_mode_query_open_api_vo import VlanOuiModeQueryOpenApiVO


T = TypeVar("T", bound="OuiBasedVlanTemplateSwitchQueryOpenApiVO")


@_attrs_define
class OuiBasedVlanTemplateSwitchQueryOpenApiVO:
    """
    Attributes:
        id (str | Unset): Rule ID
        enable (bool | Unset): Switch Rule state.
        name (str | Unset): Switch Rule name should contain 1 to 128 characters.
        mode (int | Unset): Switch Rule type should be a value as follows: 0: All device port; 1: Custom device port
        rule_combine (list[VlanOuiModeQueryOpenApiVO] | Unset): Basic vlan-oui-priority configuration of oui based vlan
            rule.
    """

    id: str | Unset = UNSET
    enable: bool | Unset = UNSET
    name: str | Unset = UNSET
    mode: int | Unset = UNSET
    rule_combine: list[VlanOuiModeQueryOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        enable = self.enable

        name = self.name

        mode = self.mode

        rule_combine: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rule_combine, Unset):
            rule_combine = []
            for rule_combine_item_data in self.rule_combine:
                rule_combine_item = rule_combine_item_data.to_dict()
                rule_combine.append(rule_combine_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if enable is not UNSET:
            field_dict["enable"] = enable
        if name is not UNSET:
            field_dict["name"] = name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if rule_combine is not UNSET:
            field_dict["ruleCombine"] = rule_combine

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vlan_oui_mode_query_open_api_vo import (
            VlanOuiModeQueryOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        enable = d.pop("enable", UNSET)

        name = d.pop("name", UNSET)

        mode = d.pop("mode", UNSET)

        _rule_combine = d.pop("ruleCombine", UNSET)
        rule_combine: list[VlanOuiModeQueryOpenApiVO] | Unset = UNSET
        if _rule_combine is not UNSET:
            rule_combine = []
            for rule_combine_item_data in _rule_combine:
                rule_combine_item = VlanOuiModeQueryOpenApiVO.from_dict(
                    rule_combine_item_data
                )

                rule_combine.append(rule_combine_item)

        oui_based_vlan_template_switch_query_open_api_vo = cls(
            id=id,
            enable=enable,
            name=name,
            mode=mode,
            rule_combine=rule_combine,
        )

        oui_based_vlan_template_switch_query_open_api_vo.additional_properties = d
        return oui_based_vlan_template_switch_query_open_api_vo

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
