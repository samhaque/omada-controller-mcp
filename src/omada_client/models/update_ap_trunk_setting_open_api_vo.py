from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApTrunkSettingOpenApiVO")


@_attrs_define
class UpdateApTrunkSettingOpenApiVO:
    """
    Attributes:
        enable (bool | Unset): Whether the device enables LAG. The following situations cause port aggregation to be
            ineffective: 1. When a specific Uplink Port is selected. 2. When PoE Out is enabled on target ports. 3. When
            Custom VLAN configurations is configured on target ports. 4. When Status is disabled on target ports.
        mode (int | Unset): LAG mode. Mode should be a value as follows: 0：SRC MAC + DST MAC; 1：DST MAC; 2：SRC MAC.
    """

    enable: bool | Unset = UNSET
    mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        mode = d.pop("mode", UNSET)

        update_ap_trunk_setting_open_api_vo = cls(
            enable=enable,
            mode=mode,
        )

        update_ap_trunk_setting_open_api_vo.additional_properties = d
        return update_ap_trunk_setting_open_api_vo

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
