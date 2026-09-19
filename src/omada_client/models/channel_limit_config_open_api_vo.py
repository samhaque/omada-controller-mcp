from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelLimitConfigOpenApiVO")


@_attrs_define
class ChannelLimitConfigOpenApiVO:
    """
    Attributes:
        support_channel_limit (bool | Unset): Indicates whether the device supports channel limit
        channel_limit_type (int | Unset): Channel limit enable status. It should be a value as follows: 0: default, 1:
            false, 2: true.
        default_inst_type_5_g (bool | Unset): default mode in 5g radio. true: outdoor; false: indoor
        default_inst_type_6_g (bool | Unset): default mode in 6g radio. true: outdoor; false: indoor
    """

    support_channel_limit: bool | Unset = UNSET
    channel_limit_type: int | Unset = UNSET
    default_inst_type_5_g: bool | Unset = UNSET
    default_inst_type_6_g: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        support_channel_limit = self.support_channel_limit

        channel_limit_type = self.channel_limit_type

        default_inst_type_5_g = self.default_inst_type_5_g

        default_inst_type_6_g = self.default_inst_type_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if support_channel_limit is not UNSET:
            field_dict["supportChannelLimit"] = support_channel_limit
        if channel_limit_type is not UNSET:
            field_dict["channelLimitType"] = channel_limit_type
        if default_inst_type_5_g is not UNSET:
            field_dict["defaultInstType5g"] = default_inst_type_5_g
        if default_inst_type_6_g is not UNSET:
            field_dict["defaultInstType6g"] = default_inst_type_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        support_channel_limit = d.pop("supportChannelLimit", UNSET)

        channel_limit_type = d.pop("channelLimitType", UNSET)

        default_inst_type_5_g = d.pop("defaultInstType5g", UNSET)

        default_inst_type_6_g = d.pop("defaultInstType6g", UNSET)

        channel_limit_config_open_api_vo = cls(
            support_channel_limit=support_channel_limit,
            channel_limit_type=channel_limit_type,
            default_inst_type_5_g=default_inst_type_5_g,
            default_inst_type_6_g=default_inst_type_6_g,
        )

        channel_limit_config_open_api_vo.additional_properties = d
        return channel_limit_config_open_api_vo

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
