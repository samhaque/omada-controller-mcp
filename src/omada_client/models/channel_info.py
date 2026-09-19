from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelInfo")


@_attrs_define
class ChannelInfo:
    """Channel list that device supports in 6 GHz.

    Attributes:
        channel (int | Unset): Channel that device supports.
        dfs_flag (bool | Unset): Whether the channel is DFS channel.
    """

    channel: int | Unset = UNSET
    dfs_flag: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        dfs_flag = self.dfs_flag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if dfs_flag is not UNSET:
            field_dict["dfsFlag"] = dfs_flag

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        dfs_flag = d.pop("dfsFlag", UNSET)

        channel_info = cls(
            channel=channel,
            dfs_flag=dfs_flag,
        )

        channel_info.additional_properties = d
        return channel_info

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
