from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApChannelDetailOpenApiVO")


@_attrs_define
class ApChannelDetailOpenApiVO:
    """channels detail supported by device configuration.

    Attributes:
        channel (int | Unset): channel value; For example, 1 in 1/2412MHz.
        freq (int | Unset): channel frequency; For example, 2412 in 1/2412MHz.
        available_channel_width_list (list[int] | Unset): Available bandwidth list for the channel configuration; For
            example: [20, 40, 80, 160, 240, 320].
        index (int | Unset): channel index; For example, if channel 36 is the first channel of the device's 5 GHz
            frequency band, its index is 1.
    """

    channel: int | Unset = UNSET
    freq: int | Unset = UNSET
    available_channel_width_list: list[int] | Unset = UNSET
    index: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel

        freq = self.freq

        available_channel_width_list: list[int] | Unset = UNSET
        if not isinstance(self.available_channel_width_list, Unset):
            available_channel_width_list = self.available_channel_width_list

        index = self.index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel is not UNSET:
            field_dict["channel"] = channel
        if freq is not UNSET:
            field_dict["freq"] = freq
        if available_channel_width_list is not UNSET:
            field_dict["availableChannelWidthList"] = available_channel_width_list
        if index is not UNSET:
            field_dict["index"] = index

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel = d.pop("channel", UNSET)

        freq = d.pop("freq", UNSET)

        available_channel_width_list = cast(
            list[int], d.pop("availableChannelWidthList", UNSET)
        )

        index = d.pop("index", UNSET)

        ap_channel_detail_open_api_vo = cls(
            channel=channel,
            freq=freq,
            available_channel_width_list=available_channel_width_list,
            index=index,
        )

        ap_channel_detail_open_api_vo.additional_properties = d
        return ap_channel_detail_open_api_vo

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
