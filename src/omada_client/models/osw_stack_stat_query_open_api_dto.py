from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStackStatQueryOpenApiDTO")


@_attrs_define
class OswStackStatQueryOpenApiDTO:
    """
    Attributes:
        start (int): Start time, number of seconds from UTC0 1970/01/01
        end (int): End time, number of seconds from UTC0 1970/01/01
        attrs (list[str]): Attributes to be queried. Attributes not included in attrs will return a value of 0. Item of
            attrs should be a value as follows: mem, cpu, tx, rx, txRate, rxRate, txPkts, rxPkts, txBroadPkts, rxBroadPkts,
            txMultiPkts, rxMultiPkts, dropPkts, txErrPkts, rxErrPkts
        standard_ports (list[str] | Unset): Statistics of the selected ports of Stack would be queried.
    """

    start: int
    end: int
    attrs: list[str]
    standard_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        attrs = self.attrs

        standard_ports: list[str] | Unset = UNSET
        if not isinstance(self.standard_ports, Unset):
            standard_ports = self.standard_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "attrs": attrs,
            }
        )
        if standard_ports is not UNSET:
            field_dict["standardPorts"] = standard_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        attrs = cast(list[str], d.pop("attrs"))

        standard_ports = cast(list[str], d.pop("standardPorts", UNSET))

        osw_stack_stat_query_open_api_dto = cls(
            start=start,
            end=end,
            attrs=attrs,
            standard_ports=standard_ports,
        )

        osw_stack_stat_query_open_api_dto.additional_properties = d
        return osw_stack_stat_query_open_api_dto

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
