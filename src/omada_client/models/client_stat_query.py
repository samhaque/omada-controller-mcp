from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ClientStatQuery")


@_attrs_define
class ClientStatQuery:
    """
    Attributes:
        start_sec (int): Start timestamp, unit: second.
        end_sec (int): End timestamp, unit: second.
    """

    start_sec: int
    end_sec: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_sec = self.start_sec

        end_sec = self.end_sec

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "startSec": start_sec,
                "endSec": end_sec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start_sec = d.pop("startSec")

        end_sec = d.pop("endSec")

        client_stat_query = cls(
            start_sec=start_sec,
            end_sec=end_sec,
        )

        client_stat_query.additional_properties = d
        return client_stat_query

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
