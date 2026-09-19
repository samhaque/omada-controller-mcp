from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApTrunkSettingOpenApiVO")


@_attrs_define
class ApTrunkSettingOpenApiVO:
    """
    Attributes:
        support_trunk_setting (bool | Unset): Whether the device supports trunk setting (LAG).
        enable (bool | Unset): Whether the device enables trunk setting (LAG).
        mode (int | Unset): Trunk setting (LAG) mode. Mode should be a value as follows: 0：SRC MAC + DST MAC; 1：DST MAC;
            2：SRC MAC.
    """

    support_trunk_setting: bool | Unset = UNSET
    enable: bool | Unset = UNSET
    mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_trunk_setting = self.support_trunk_setting

        enable = self.enable

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support_trunk_setting is not UNSET:
            field_dict["supportTrunkSetting"] = support_trunk_setting
        if enable is not UNSET:
            field_dict["enable"] = enable
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support_trunk_setting = d.pop("supportTrunkSetting", UNSET)

        enable = d.pop("enable", UNSET)

        mode = d.pop("mode", UNSET)

        ap_trunk_setting_open_api_vo = cls(
            support_trunk_setting=support_trunk_setting,
            enable=enable,
            mode=mode,
        )

        ap_trunk_setting_open_api_vo.additional_properties = d
        return ap_trunk_setting_open_api_vo

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
