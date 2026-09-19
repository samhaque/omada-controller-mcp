from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="UpdateChannelLimitConfigOpenApiVO")


@_attrs_define
class UpdateChannelLimitConfigOpenApiVO:
    """
    Attributes:
        channel_limit_type (int): Channel limit enable status. It should be a value as follows: 0: default, 1: false, 2:
            true.
    """

    channel_limit_type: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_limit_type = self.channel_limit_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channelLimitType": channel_limit_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        channel_limit_type = d.pop("channelLimitType")

        update_channel_limit_config_open_api_vo = cls(
            channel_limit_type=channel_limit_type,
        )

        update_channel_limit_config_open_api_vo.additional_properties = d
        return update_channel_limit_config_open_api_vo

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
