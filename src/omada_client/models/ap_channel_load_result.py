from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_channel import ApChannel


T = TypeVar("T", bound="ApChannelLoadResult")


@_attrs_define
class ApChannelLoadResult:
    """
    Attributes:
        channel_loads_2_g (list[ApChannel] | Unset): List of 2G channel loads.
        channel_loads_5_g (list[ApChannel] | Unset): List of 5G channel loads.
        channel_loads_6_g (list[ApChannel] | Unset): List of 6G channel loads.
    """

    channel_loads_2_g: list[ApChannel] | Unset = UNSET
    channel_loads_5_g: list[ApChannel] | Unset = UNSET
    channel_loads_6_g: list[ApChannel] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_loads_2_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_loads_2_g, Unset):
            channel_loads_2_g = []
            for channel_loads_2_g_item_data in self.channel_loads_2_g:
                channel_loads_2_g_item = channel_loads_2_g_item_data.to_dict()
                channel_loads_2_g.append(channel_loads_2_g_item)

        channel_loads_5_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_loads_5_g, Unset):
            channel_loads_5_g = []
            for channel_loads_5_g_item_data in self.channel_loads_5_g:
                channel_loads_5_g_item = channel_loads_5_g_item_data.to_dict()
                channel_loads_5_g.append(channel_loads_5_g_item)

        channel_loads_6_g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channel_loads_6_g, Unset):
            channel_loads_6_g = []
            for channel_loads_6_g_item_data in self.channel_loads_6_g:
                channel_loads_6_g_item = channel_loads_6_g_item_data.to_dict()
                channel_loads_6_g.append(channel_loads_6_g_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_loads_2_g is not UNSET:
            field_dict["channelLoads2g"] = channel_loads_2_g
        if channel_loads_5_g is not UNSET:
            field_dict["channelLoads5g"] = channel_loads_5_g
        if channel_loads_6_g is not UNSET:
            field_dict["channelLoads6g"] = channel_loads_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_channel import ApChannel

        d = dict(src_dict)
        _channel_loads_2_g = d.pop("channelLoads2g", UNSET)
        channel_loads_2_g: list[ApChannel] | Unset = UNSET
        if _channel_loads_2_g is not UNSET:
            channel_loads_2_g = []
            for channel_loads_2_g_item_data in _channel_loads_2_g:
                channel_loads_2_g_item = ApChannel.from_dict(
                    channel_loads_2_g_item_data
                )

                channel_loads_2_g.append(channel_loads_2_g_item)

        _channel_loads_5_g = d.pop("channelLoads5g", UNSET)
        channel_loads_5_g: list[ApChannel] | Unset = UNSET
        if _channel_loads_5_g is not UNSET:
            channel_loads_5_g = []
            for channel_loads_5_g_item_data in _channel_loads_5_g:
                channel_loads_5_g_item = ApChannel.from_dict(
                    channel_loads_5_g_item_data
                )

                channel_loads_5_g.append(channel_loads_5_g_item)

        _channel_loads_6_g = d.pop("channelLoads6g", UNSET)
        channel_loads_6_g: list[ApChannel] | Unset = UNSET
        if _channel_loads_6_g is not UNSET:
            channel_loads_6_g = []
            for channel_loads_6_g_item_data in _channel_loads_6_g:
                channel_loads_6_g_item = ApChannel.from_dict(
                    channel_loads_6_g_item_data
                )

                channel_loads_6_g.append(channel_loads_6_g_item)

        ap_channel_load_result = cls(
            channel_loads_2_g=channel_loads_2_g,
            channel_loads_5_g=channel_loads_5_g,
            channel_loads_6_g=channel_loads_6_g,
        )

        ap_channel_load_result.additional_properties = d
        return ap_channel_load_result

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
