from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StormCtrlVO")


@_attrs_define
class StormCtrlVO:
    """StormCtrl

    Attributes:
        unknown_unicast_enable (bool): Unknown-Unicast enable status
        multicast_enable (bool): Multicast enable status
        broadcast_enable (bool): Broadcast enable status
        action (int): Action should be a value as follows: 0: drop(default), 1: shutdown
        rate_mode (int | Unset): RateMode should be a value as follows: 0: ratio; 1: kbps
        unknown_unicast (int | Unset): Unknown-Unicast
        multicast (int | Unset): Multicast
        broadcast (int | Unset): Broadcast
        recover_time (int | Unset): Recover Time should be within the range of 1-3600, default 3600
    """

    unknown_unicast_enable: bool
    multicast_enable: bool
    broadcast_enable: bool
    action: int
    rate_mode: int | Unset = UNSET
    unknown_unicast: int | Unset = UNSET
    multicast: int | Unset = UNSET
    broadcast: int | Unset = UNSET
    recover_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_unicast_enable = self.unknown_unicast_enable

        multicast_enable = self.multicast_enable

        broadcast_enable = self.broadcast_enable

        action = self.action

        rate_mode = self.rate_mode

        unknown_unicast = self.unknown_unicast

        multicast = self.multicast

        broadcast = self.broadcast

        recover_time = self.recover_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unknownUnicastEnable": unknown_unicast_enable,
                "multicastEnable": multicast_enable,
                "broadcastEnable": broadcast_enable,
                "action": action,
            }
        )
        if rate_mode is not UNSET:
            field_dict["rateMode"] = rate_mode
        if unknown_unicast is not UNSET:
            field_dict["unknownUnicast"] = unknown_unicast
        if multicast is not UNSET:
            field_dict["multicast"] = multicast
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if recover_time is not UNSET:
            field_dict["recoverTime"] = recover_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unknown_unicast_enable = d.pop("unknownUnicastEnable")

        multicast_enable = d.pop("multicastEnable")

        broadcast_enable = d.pop("broadcastEnable")

        action = d.pop("action")

        rate_mode = d.pop("rateMode", UNSET)

        unknown_unicast = d.pop("unknownUnicast", UNSET)

        multicast = d.pop("multicast", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        recover_time = d.pop("recoverTime", UNSET)

        storm_ctrl_vo = cls(
            unknown_unicast_enable=unknown_unicast_enable,
            multicast_enable=multicast_enable,
            broadcast_enable=broadcast_enable,
            action=action,
            rate_mode=rate_mode,
            unknown_unicast=unknown_unicast,
            multicast=multicast,
            broadcast=broadcast,
            recover_time=recover_time,
        )

        storm_ctrl_vo.additional_properties = d
        return storm_ctrl_vo

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
