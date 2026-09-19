from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PowerThresholdVO")


@_attrs_define
class PowerThresholdVO:
    """Power threshold.

    Attributes:
        mode (int | Unset): Parameter [mode] should be 0 or 1. 0: Auto. 1: Custom.
        threshold2g (int | Unset): Power threshold in 2.4 GHz. Parameter [threshold2g] should range from -75 and -60.
        threshold5g (int | Unset): Power threshold in 5 GHz. Parameter [threshold5g] should range from -75 and -60.
        threshold6g (int | Unset): Power threshold in 6 GHz. Parameter [threshold6g] should range from -75 and -60.
    """

    mode: int | Unset = UNSET
    threshold2g: int | Unset = UNSET
    threshold5g: int | Unset = UNSET
    threshold6g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        threshold2g = self.threshold2g

        threshold5g = self.threshold5g

        threshold6g = self.threshold6g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if threshold2g is not UNSET:
            field_dict["threshold2g"] = threshold2g
        if threshold5g is not UNSET:
            field_dict["threshold5g"] = threshold5g
        if threshold6g is not UNSET:
            field_dict["threshold6g"] = threshold6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode", UNSET)

        threshold2g = d.pop("threshold2g", UNSET)

        threshold5g = d.pop("threshold5g", UNSET)

        threshold6g = d.pop("threshold6g", UNSET)

        power_threshold_vo = cls(
            mode=mode,
            threshold2g=threshold2g,
            threshold5g=threshold5g,
            threshold6g=threshold6g,
        )

        power_threshold_vo.additional_properties = d
        return power_threshold_vo

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
