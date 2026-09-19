from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WidthRangeVO")


@_attrs_define
class WidthRangeVO:
    """Channel width range. Parameter [widthRange] should not be null when parameter [widthSelectEn] is true.

    Attributes:
        min_width_5_g (int | Unset): Minimum channel width in 5 GHz. Parameter [minWidth5g] should be 20,40,80,160,240.
        max_width_5_g (int | Unset): Maximum channel width in 5 GHz. Parameter [maxWidth5g] should be 20,40,80,160,240.
        min_width_6_g (int | Unset): Minimum channel width in 6 GHz. Parameter [minWidth6g] should be 20,40,80,160,320.
        max_width_6_g (int | Unset): Maximum channel width in 6 GHz. Parameter [maxWidth6g] should be 20,40,80,160,320.
    """

    min_width_5_g: int | Unset = UNSET
    max_width_5_g: int | Unset = UNSET
    min_width_6_g: int | Unset = UNSET
    max_width_6_g: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        min_width_5_g = self.min_width_5_g

        max_width_5_g = self.max_width_5_g

        min_width_6_g = self.min_width_6_g

        max_width_6_g = self.max_width_6_g

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if min_width_5_g is not UNSET:
            field_dict["minWidth5g"] = min_width_5_g
        if max_width_5_g is not UNSET:
            field_dict["maxWidth5g"] = max_width_5_g
        if min_width_6_g is not UNSET:
            field_dict["minWidth6g"] = min_width_6_g
        if max_width_6_g is not UNSET:
            field_dict["maxWidth6g"] = max_width_6_g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        min_width_5_g = d.pop("minWidth5g", UNSET)

        max_width_5_g = d.pop("maxWidth5g", UNSET)

        min_width_6_g = d.pop("minWidth6g", UNSET)

        max_width_6_g = d.pop("maxWidth6g", UNSET)

        width_range_vo = cls(
            min_width_5_g=min_width_5_g,
            max_width_5_g=max_width_5_g,
            min_width_6_g=min_width_6_g,
            max_width_6_g=max_width_6_g,
        )

        width_range_vo.additional_properties = d
        return width_range_vo

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
