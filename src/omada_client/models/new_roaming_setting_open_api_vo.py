from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewRoamingSettingOpenApiVO")


@_attrs_define
class NewRoamingSettingOpenApiVO:
    """Site roaming setting

    Attributes:
        fast_roaming_enable (bool): Whether to enable fast roaming
        ai_roaming_enable (bool): Whether to enable AI roaming, this configuration will take effect only when fast
            roaming is enabled
        non_stick_roaming_enable (bool | Unset): Whether to enable non-stick roaming
        non_ping_pong_roaming_enable (bool | Unset): Whether to enable non-ping-pong roaming
        ping_pong_assoc_threshold (int | Unset): Association frequency threshold of ping-pong roaming
    """

    fast_roaming_enable: bool
    ai_roaming_enable: bool
    non_stick_roaming_enable: bool | Unset = UNSET
    non_ping_pong_roaming_enable: bool | Unset = UNSET
    ping_pong_assoc_threshold: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fast_roaming_enable = self.fast_roaming_enable

        ai_roaming_enable = self.ai_roaming_enable

        non_stick_roaming_enable = self.non_stick_roaming_enable

        non_ping_pong_roaming_enable = self.non_ping_pong_roaming_enable

        ping_pong_assoc_threshold = self.ping_pong_assoc_threshold

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fastRoamingEnable": fast_roaming_enable,
                "aiRoamingEnable": ai_roaming_enable,
            }
        )
        if non_stick_roaming_enable is not UNSET:
            field_dict["nonStickRoamingEnable"] = non_stick_roaming_enable
        if non_ping_pong_roaming_enable is not UNSET:
            field_dict["nonPingPongRoamingEnable"] = non_ping_pong_roaming_enable
        if ping_pong_assoc_threshold is not UNSET:
            field_dict["pingPongAssocThreshold"] = ping_pong_assoc_threshold

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        fast_roaming_enable = d.pop("fastRoamingEnable")

        ai_roaming_enable = d.pop("aiRoamingEnable")

        non_stick_roaming_enable = d.pop("nonStickRoamingEnable", UNSET)

        non_ping_pong_roaming_enable = d.pop("nonPingPongRoamingEnable", UNSET)

        ping_pong_assoc_threshold = d.pop("pingPongAssocThreshold", UNSET)

        new_roaming_setting_open_api_vo = cls(
            fast_roaming_enable=fast_roaming_enable,
            ai_roaming_enable=ai_roaming_enable,
            non_stick_roaming_enable=non_stick_roaming_enable,
            non_ping_pong_roaming_enable=non_ping_pong_roaming_enable,
            ping_pong_assoc_threshold=ping_pong_assoc_threshold,
        )

        new_roaming_setting_open_api_vo.additional_properties = d
        return new_roaming_setting_open_api_vo

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
