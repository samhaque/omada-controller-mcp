from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="OswStackStatQueryVO")


@_attrs_define
class OswStackStatQueryVO:
    """
    Attributes:
        start (int): Start time, number of seconds from UTC0 1970/01/01
        end (int): End time, number of seconds from UTC0 1970/01/01
        attrs (list[str]): Attributes to be queried. Attributes not included in attrs will return a value of 0.Item of
            attrs should be a value as follows: mem, cpu, tx, rx, txRate, rxRate, txPkts, rxPkts, txBroadPkts, rxBroadPkts,
            txMultiPkts, rxMultiPkts, dropPkts, txErrPkts, rxErrPkts
        interval (int): Interval should be a value as follows: 0:5min, 1:hourly, 2:daily
    """

    start: int
    end: int
    attrs: list[str]
    interval: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start = self.start

        end = self.end

        attrs = self.attrs

        interval = self.interval

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "end": end,
                "attrs": attrs,
                "interval": interval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        start = d.pop("start")

        end = d.pop("end")

        attrs = cast(list[str], d.pop("attrs"))

        interval = d.pop("interval")

        osw_stack_stat_query_vo = cls(
            start=start,
            end=end,
            attrs=attrs,
            interval=interval,
        )

        osw_stack_stat_query_vo.additional_properties = d
        return osw_stack_stat_query_vo

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
