from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteFilterInfo")


@_attrs_define
class DeleteFilterInfo:
    """
    Attributes:
        start (int): Start timestamp, in seconds, such as 1682000000.
        end (int): End timestamp, in seconds, such as 1682000000.
        search_key (str | Unset): Searching key for clients to delete, Searching by: client mac, client name, ssid name,
            network name.
    """

    start: int
    end: int
    search_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        search_key = self.search_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
            }
        )
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        search_key = d.pop("searchKey", UNSET)

        delete_filter_info = cls(
            start=start,
            end=end,
            search_key=search_key,
        )

        delete_filter_info.additional_properties = d
        return delete_filter_info

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
