from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStatQueryOpenApiDTO")


@_attrs_define
class OswStatQueryOpenApiDTO:
    """
    Attributes:
        start (int): Start time, number of seconds from UTC0 1970/01/01
        end (int): End time, number of seconds from UTC0 1970/01/01
        attrs (list[str]): Attributes to be queried. Attributes not included in attrs will return a value of 0. Item of
            attrs should be a value as follows: mem, cpu, tx, rx, txRate, rxRate, txPkts, rxPkts, txBroadPkts, rxBroadPkts,
            txMultiPkts, rxMultiPkts, dropPkts, txErrPkts, rxErrPkts
        ports (list[int] | Unset): Statistics of the selected ports of Switch would be queried.
    """

    start: int
    end: int
    attrs: list[str]
    ports: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        attrs = self.attrs

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "attrs": attrs,
            }
        )
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        attrs = cast(list[str], d.pop("attrs"))

        ports = cast(list[int], d.pop("ports", UNSET))

        osw_stat_query_open_api_dto = cls(
            start=start,
            end=end,
            attrs=attrs,
            ports=ports,
        )

        osw_stat_query_open_api_dto.additional_properties = d
        return osw_stat_query_open_api_dto

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
