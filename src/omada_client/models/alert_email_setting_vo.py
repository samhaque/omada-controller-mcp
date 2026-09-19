from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertEmailSettingVO")


@_attrs_define
class AlertEmailSettingVO:
    """Abnormal Alert Email(This config applies to the Abnormal > Notification view).

    Attributes:
        delay_enable (bool): Enable alert emails delay
        delay (int | Unset): Send similar alerts within x seconds in one email, Note that when the number of incidents
            reaches 100, the log will be sent immediately
    """

    delay_enable: bool
    delay: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        delay_enable = self.delay_enable

        delay = self.delay

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delayEnable": delay_enable,
            }
        )
        if delay is not UNSET:
            field_dict["delay"] = delay

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        delay_enable = d.pop("delayEnable")

        delay = d.pop("delay", UNSET)

        alert_email_setting_vo = cls(
            delay_enable=delay_enable,
            delay=delay,
        )

        alert_email_setting_vo.additional_properties = d
        return alert_email_setting_vo

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
