from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_limit_setting_vo import ChannelLimitSettingVO


T = TypeVar("T", bound="SiteChannelLimitSetting")


@_attrs_define
class SiteChannelLimitSetting:
    """Site channel limit setting.

    Attributes:
        channel_limit (ChannelLimitSettingVO | Unset): Site channel limit.
    """

    channel_limit: ChannelLimitSettingVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_limit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_limit, Unset):
            channel_limit = self.channel_limit.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channel_limit is not UNSET:
            field_dict["channelLimit"] = channel_limit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.channel_limit_setting_vo import (
            ChannelLimitSettingVO,
        )

        d = dict(src_dict)
        _channel_limit = d.pop("channelLimit", UNSET)
        channel_limit: ChannelLimitSettingVO | Unset
        if isinstance(_channel_limit, Unset):
            channel_limit = UNSET
        else:
            channel_limit = ChannelLimitSettingVO.from_dict(_channel_limit)

        site_channel_limit_setting = cls(
            channel_limit=channel_limit,
        )

        site_channel_limit_setting.additional_properties = d
        return site_channel_limit_setting

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
