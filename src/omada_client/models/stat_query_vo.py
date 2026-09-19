from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatQueryVO")


@_attrs_define
class StatQueryVO:
    """
    Attributes:
        start (int): Start time, number of seconds from UTC0 1970/01/01
        end (int): end time, number of seconds from UTC0 1970/01/01
        attrs (list[str]): Attributes to be queried. Attributes not included in attrs will return a value of 0 or be
            omitted. The supported attrs and response fields depend on the device type and statistic granularity. For
            details, refer to section 5.9.1 Device Statistics of the Open API Access Guide.
        ports (list[int] | Unset): The ports in the lag. Each item is Integer, for example: [1, 2].
        standard_ports (list[str] | Unset): Statistics of the selected ports would be queried , the param is valid when
            stacking
        olt_ports (list[str] | Unset): Statistics of the selected ports of olt would be queried.
    """

    start: int
    end: int
    attrs: list[str]
    ports: list[int] | Unset = UNSET
    standard_ports: list[str] | Unset = UNSET
    olt_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        attrs = self.attrs

        ports: list[int] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports

        standard_ports: list[str] | Unset = UNSET
        if not isinstance(self.standard_ports, Unset):
            standard_ports = self.standard_ports

        olt_ports: list[str] | Unset = UNSET
        if not isinstance(self.olt_ports, Unset):
            olt_ports = self.olt_ports

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
        if standard_ports is not UNSET:
            field_dict["standardPorts"] = standard_ports
        if olt_ports is not UNSET:
            field_dict["oltPorts"] = olt_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        attrs = cast(list[str], d.pop("attrs"))

        ports = cast(list[int], d.pop("ports", UNSET))

        standard_ports = cast(list[str], d.pop("standardPorts", UNSET))

        olt_ports = cast(list[str], d.pop("oltPorts", UNSET))

        stat_query_vo = cls(
            start=start,
            end=end,
            attrs=attrs,
            ports=ports,
            standard_ports=standard_ports,
            olt_ports=olt_ports,
        )

        stat_query_vo.additional_properties = d
        return stat_query_vo

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
