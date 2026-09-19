from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeviceClientStatQueryOpenApiVO")


@_attrs_define
class DeviceClientStatQueryOpenApiVO:
    """
    Attributes:
        start (int): Start timestamp, in seconds, such as 1682000000
        end (int): End timestamp, in seconds, such as 1682000000
        attrs (list[str]): Attribute list to get.
    """

    start: int
    end: int
    attrs: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        attrs = self.attrs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "attrs": attrs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        attrs = cast(list[str], d.pop("attrs"))

        device_client_stat_query_open_api_vo = cls(
            start=start,
            end=end,
            attrs=attrs,
        )

        device_client_stat_query_open_api_vo.additional_properties = d
        return device_client_stat_query_open_api_vo

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
