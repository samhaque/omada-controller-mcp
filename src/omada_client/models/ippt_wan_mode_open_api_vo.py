from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpptWanModeOpenApiVO")


@_attrs_define
class IpptWanModeOpenApiVO:
    """
    Attributes:
        enable (bool): whether to enable wan Settings Override
        interval (int | Unset): Time taken to check the connection of wan port.
        unit (int | Unset): Unit. 0: minute, 1: second.
    """

    enable: bool
    interval: int | Unset = UNSET
    unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        interval = self.interval

        unit = self.unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if interval is not UNSET:
            field_dict["interval"] = interval
        if unit is not UNSET:
            field_dict["unit"] = unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        interval = d.pop("interval", UNSET)

        unit = d.pop("unit", UNSET)

        ippt_wan_mode_open_api_vo = cls(
            enable=enable,
            interval=interval,
            unit=unit,
        )

        ippt_wan_mode_open_api_vo.additional_properties = d
        return ippt_wan_mode_open_api_vo

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
