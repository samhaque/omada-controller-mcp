from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Retry")


@_attrs_define
class Retry:
    """AP retries timing list

    Attributes:
        time (int | Unset): Sampling time second
        retry_times (int | Unset): Number of new contracts within one hour, such as 60 : 60%
        retry_rate (float | Unset): AP re-contracting rate within one hour
    """

    time: int | Unset = UNSET
    retry_times: int | Unset = UNSET
    retry_rate: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        retry_times = self.retry_times

        retry_rate = self.retry_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if retry_times is not UNSET:
            field_dict["retryTimes"] = retry_times
        if retry_rate is not UNSET:
            field_dict["retryRate"] = retry_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        retry_times = d.pop("retryTimes", UNSET)

        retry_rate = d.pop("retryRate", UNSET)

        retry = cls(
            time=time,
            retry_times=retry_times,
            retry_rate=retry_rate,
        )

        retry.additional_properties = d
        return retry

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
