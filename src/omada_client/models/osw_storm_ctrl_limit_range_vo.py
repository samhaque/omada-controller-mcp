from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStormCtrlLimitRangeVO")


@_attrs_define
class OswStormCtrlLimitRangeVO:
    """The maximum rate limits for Broadcast/Multicast/Unknown Unicast.

    Attributes:
        broadcast_limit_kbps (int | Unset): The maximum rate limits for Broadcast(kbps).
        multicast_limit_kbps (int | Unset): The maximum rate limits for Multicast(kbps).
        unknown_unicast_limit_kbps (int | Unset): The maximum rate limits for Unknown Unicast(kbps).
    """

    broadcast_limit_kbps: int | Unset = UNSET
    multicast_limit_kbps: int | Unset = UNSET
    unknown_unicast_limit_kbps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        broadcast_limit_kbps = self.broadcast_limit_kbps

        multicast_limit_kbps = self.multicast_limit_kbps

        unknown_unicast_limit_kbps = self.unknown_unicast_limit_kbps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if broadcast_limit_kbps is not UNSET:
            field_dict["broadcastLimitKbps"] = broadcast_limit_kbps
        if multicast_limit_kbps is not UNSET:
            field_dict["multicastLimitKbps"] = multicast_limit_kbps
        if unknown_unicast_limit_kbps is not UNSET:
            field_dict["unknownUnicastLimitKbps"] = unknown_unicast_limit_kbps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        broadcast_limit_kbps = d.pop("broadcastLimitKbps", UNSET)

        multicast_limit_kbps = d.pop("multicastLimitKbps", UNSET)

        unknown_unicast_limit_kbps = d.pop("unknownUnicastLimitKbps", UNSET)

        osw_storm_ctrl_limit_range_vo = cls(
            broadcast_limit_kbps=broadcast_limit_kbps,
            multicast_limit_kbps=multicast_limit_kbps,
            unknown_unicast_limit_kbps=unknown_unicast_limit_kbps,
        )

        osw_storm_ctrl_limit_range_vo.additional_properties = d
        return osw_storm_ctrl_limit_range_vo

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
