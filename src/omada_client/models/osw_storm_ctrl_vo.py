from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_storm_ctrl_limit_range_vo import OswStormCtrlLimitRangeVO


T = TypeVar("T", bound="OswStormCtrlVO")


@_attrs_define
class OswStormCtrlVO:
    """Storm Control

    Attributes:
        unknown_unicast_enable (bool): Indicates whether unknown unicast is enabled
        multicast_enable (bool): Indicates whether multicast is enabled
        broadcast_enable (bool): Indicates whether broadcast is enabled
        action (int): Action should be a value as follows: 0: drop; 1: shutdown
        rate_mode (int | Unset): RateMode should be a value as follows: 0: ratio; 1: kbps
        unknown_unicast (int | Unset): Unknown Unicast
        multicast (int | Unset): Multicast
        broadcast (int | Unset): Broadcast
        recover_time (int | Unset): Recover Time
        limit_range (OswStormCtrlLimitRangeVO | Unset): The maximum rate limits for Broadcast/Multicast/Unknown Unicast.
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
    limit_range: OswStormCtrlLimitRangeVO | Unset = UNSET
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

        limit_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limit_range, Unset):
            limit_range = self.limit_range.to_dict()

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
        if limit_range is not UNSET:
            field_dict["limitRange"] = limit_range

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_storm_ctrl_limit_range_vo import (
            OswStormCtrlLimitRangeVO,
        )

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

        _limit_range = d.pop("limitRange", UNSET)
        limit_range: OswStormCtrlLimitRangeVO | Unset
        if isinstance(_limit_range, Unset):
            limit_range = UNSET
        else:
            limit_range = OswStormCtrlLimitRangeVO.from_dict(_limit_range)

        osw_storm_ctrl_vo = cls(
            unknown_unicast_enable=unknown_unicast_enable,
            multicast_enable=multicast_enable,
            broadcast_enable=broadcast_enable,
            action=action,
            rate_mode=rate_mode,
            unknown_unicast=unknown_unicast,
            multicast=multicast,
            broadcast=broadcast,
            recover_time=recover_time,
            limit_range=limit_range,
        )

        osw_storm_ctrl_vo.additional_properties = d
        return osw_storm_ctrl_vo

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
