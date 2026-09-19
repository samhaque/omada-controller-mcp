from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApChannelStat")


@_attrs_define
class ApChannelStat:
    """6g channel stat

    Attributes:
        channel (int | Unset): This entry indicates the channel index. For example, 36 means the 36 / 2160MHz channel.
        ap_num (int | Unset): AP number of the channel
        client_num (int | Unset): Client number of the channel
        channel_utilization (float | Unset): The average utilization of the channel by APs in percentage. Null means no
            data.
    """

    channel: int | Unset = UNSET
    ap_num: int | Unset = UNSET
    client_num: int | Unset = UNSET
    channel_utilization: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        ap_num = self.ap_num

        client_num = self.client_num

        channel_utilization = self.channel_utilization

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if ap_num is not UNSET:
            field_dict["apNum"] = ap_num
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num
        if channel_utilization is not UNSET:
            field_dict["channelUtilization"] = channel_utilization

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        ap_num = d.pop("apNum", UNSET)

        client_num = d.pop("clientNum", UNSET)

        channel_utilization = d.pop("channelUtilization", UNSET)

        ap_channel_stat = cls(
            channel=channel,
            ap_num=ap_num,
            client_num=client_num,
            channel_utilization=channel_utilization,
        )

        ap_channel_stat.additional_properties = d
        return ap_channel_stat

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
