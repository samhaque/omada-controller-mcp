from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MadSettingVO")


@_attrs_define
class MadSettingVO:
    """Mad Setting

    Attributes:
        enable (bool | Unset): Enable
        mode (int | Unset): Mode should be 0
        select_ports (list[str] | Unset): Select Ports
    """

    enable: bool | Unset = UNSET
    mode: int | Unset = UNSET
    select_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        mode = self.mode

        select_ports: list[str] | Unset = UNSET
        if not isinstance(self.select_ports, Unset):
            select_ports = self.select_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if mode is not UNSET:
            field_dict["mode"] = mode
        if select_ports is not UNSET:
            field_dict["selectPorts"] = select_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        mode = d.pop("mode", UNSET)

        select_ports = cast(list[str], d.pop("selectPorts", UNSET))

        mad_setting_vo = cls(
            enable=enable,
            mode=mode,
            select_ports=select_ports,
        )

        mad_setting_vo.additional_properties = d
        return mad_setting_vo

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
