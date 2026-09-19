from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgPortStormCtrlVO")


@_attrs_define
class OsgPortStormCtrlVO:
    """
    Attributes:
        unknown_unicast_enable (bool):
        multicast_enable (bool):
        broadcast_enable (bool):
        unknown_unicast (int | Unset):
        multicast (int | Unset):
        broadcast (int | Unset):
        action (int | Unset):
        recover_time (int | Unset):
    """

    unknown_unicast_enable: bool
    multicast_enable: bool
    broadcast_enable: bool
    unknown_unicast: int | Unset = UNSET
    multicast: int | Unset = UNSET
    broadcast: int | Unset = UNSET
    action: int | Unset = UNSET
    recover_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_unicast_enable = self.unknown_unicast_enable

        multicast_enable = self.multicast_enable

        broadcast_enable = self.broadcast_enable

        unknown_unicast = self.unknown_unicast

        multicast = self.multicast

        broadcast = self.broadcast

        action = self.action

        recover_time = self.recover_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unknownUnicastEnable": unknown_unicast_enable,
                "multicastEnable": multicast_enable,
                "broadcastEnable": broadcast_enable,
            }
        )
        if unknown_unicast is not UNSET:
            field_dict["unknownUnicast"] = unknown_unicast
        if multicast is not UNSET:
            field_dict["multicast"] = multicast
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if action is not UNSET:
            field_dict["action"] = action
        if recover_time is not UNSET:
            field_dict["recoverTime"] = recover_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        unknown_unicast_enable = d.pop("unknownUnicastEnable")

        multicast_enable = d.pop("multicastEnable")

        broadcast_enable = d.pop("broadcastEnable")

        unknown_unicast = d.pop("unknownUnicast", UNSET)

        multicast = d.pop("multicast", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        action = d.pop("action", UNSET)

        recover_time = d.pop("recoverTime", UNSET)

        osg_port_storm_ctrl_vo = cls(
            unknown_unicast_enable=unknown_unicast_enable,
            multicast_enable=multicast_enable,
            broadcast_enable=broadcast_enable,
            unknown_unicast=unknown_unicast,
            multicast=multicast,
            broadcast=broadcast,
            action=action,
            recover_time=recover_time,
        )

        osg_port_storm_ctrl_vo.additional_properties = d
        return osg_port_storm_ctrl_vo

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
