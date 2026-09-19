from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateApChannelConfigOpenApiVO")


@_attrs_define
class UpdateApChannelConfigOpenApiVO:
    """
    Attributes:
        radio_id (int): (Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz(5GHz-1); 2: 5GHz-2; 3:
            6GHz.
        radio_enable (bool): Enable/Disable radio setting(if false, other params is not required)
        channel (int | Unset): Radios-Channel config; The channel list supported by device can be obtained from
            interface : Get available channel list of ap; If select auto configuration need to enter 0.
        channel_width (int | Unset): Radios-Channel width config; The channelWidth list supported by device can be
            obtained from interface : Get available channel list of ap; If select auto configuration need to enter 0.
    """

    radio_id: int
    radio_enable: bool
    channel: int | Unset = UNSET
    channel_width: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        radio_enable = self.radio_enable

        channel = self.channel

        channel_width = self.channel_width

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radioId": radio_id,
                "radioEnable": radio_enable,
            }
        )
        if channel is not UNSET:
            field_dict["channel"] = channel
        if channel_width is not UNSET:
            field_dict["channelWidth"] = channel_width

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id = d.pop("radioId")

        radio_enable = d.pop("radioEnable")

        channel = d.pop("channel", UNSET)

        channel_width = d.pop("channelWidth", UNSET)

        update_ap_channel_config_open_api_vo = cls(
            radio_id=radio_id,
            radio_enable=radio_enable,
            channel=channel,
            channel_width=channel_width,
        )

        update_ap_channel_config_open_api_vo.additional_properties = d
        return update_ap_channel_config_open_api_vo

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
