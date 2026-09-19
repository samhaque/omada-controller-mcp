from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DdnsIntervalOpenApiVO")


@_attrs_define
class DdnsIntervalOpenApiVO:
    """Dynamic DNS interval configuration. You can configure one of two intervals, when parameter [service] is 2 or 3, you
    can only choose [updateInterval] to configure, when parameter [service] is 5, you don’t need to configure interval.

        Attributes:
            update_interval (int | Unset): Dynamic DNS update interval, unit: hour. UpdateInterval should be a value as
                follows: 0, 1, 6, 12, 24, 48 or 72
            custom_interval (int | Unset): Dynamic DNS custom interval, valid when parameter [server] is 0, 1 or 4, unit:
                minute. CustomInterval should be within the range of 1-60
    """

    update_interval: int | Unset = UNSET
    custom_interval: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        update_interval = self.update_interval

        custom_interval = self.custom_interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if update_interval is not UNSET:
            field_dict["updateInterval"] = update_interval
        if custom_interval is not UNSET:
            field_dict["customInterval"] = custom_interval

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        update_interval = d.pop("updateInterval", UNSET)

        custom_interval = d.pop("customInterval", UNSET)

        ddns_interval_open_api_vo = cls(
            update_interval=update_interval,
            custom_interval=custom_interval,
        )

        ddns_interval_open_api_vo.additional_properties = d
        return ddns_interval_open_api_vo

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
