from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SwitchPortsPoe")


@_attrs_define
class SwitchPortsPoe:
    """
    Attributes:
        port_list (list[int]): Port ID List.
        poe_mode (int): Poe mode should be a value as follows: 1: on(802.3at/af); 0: off.
    """

    port_list: list[int]
    poe_mode: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_list = self.port_list

        poe_mode = self.poe_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "portList": port_list,
                "poeMode": poe_mode,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_list = cast(list[int], d.pop("portList"))

        poe_mode = d.pop("poeMode")

        switch_ports_poe = cls(
            port_list=port_list,
            poe_mode=poe_mode,
        )

        switch_ports_poe.additional_properties = d
        return switch_ports_poe

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
