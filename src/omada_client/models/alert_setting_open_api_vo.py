from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertSettingOpenApiVO")


@_attrs_define
class AlertSettingOpenApiVO:
    """Site alert setting.

    Attributes:
        enable (bool): Alert enable.
        delay_enable (bool | Unset): Alert delay enable.
        delay (int | Unset): Time of Log delay email (unit:s). The value should be within the range of 0–99999.
    """

    enable: bool
    delay_enable: bool | Unset = UNSET
    delay: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        delay_enable = self.delay_enable

        delay = self.delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if delay_enable is not UNSET:
            field_dict["delayEnable"] = delay_enable
        if delay is not UNSET:
            field_dict["delay"] = delay

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        delay_enable = d.pop("delayEnable", UNSET)

        delay = d.pop("delay", UNSET)

        alert_setting_open_api_vo = cls(
            enable=enable,
            delay_enable=delay_enable,
            delay=delay,
        )

        alert_setting_open_api_vo.additional_properties = d
        return alert_setting_open_api_vo

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
