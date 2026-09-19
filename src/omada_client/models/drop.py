from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Drop")


@_attrs_define
class Drop:
    """AP dropouts timing list

    Attributes:
        time (int | Unset): Sampling time second
        drop_times (int | Unset): Number of drop packets within one hour, such as 60 : 60%
        drop_rate (float | Unset): AP drop packet rate within one hour
    """

    time: int | Unset = UNSET
    drop_times: int | Unset = UNSET
    drop_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        drop_times = self.drop_times

        drop_rate = self.drop_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if drop_times is not UNSET:
            field_dict["dropTimes"] = drop_times
        if drop_rate is not UNSET:
            field_dict["dropRate"] = drop_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        drop_times = d.pop("dropTimes", UNSET)

        drop_rate = d.pop("dropRate", UNSET)

        drop = cls(
            time=time,
            drop_times=drop_times,
            drop_rate=drop_rate,
        )

        drop.additional_properties = d
        return drop

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
