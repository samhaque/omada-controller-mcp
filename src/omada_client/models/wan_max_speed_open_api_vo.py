from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanMaxSpeedOpenApiVO")


@_attrs_define
class WanMaxSpeedOpenApiVO:
    """
    Attributes:
        upstream (int | Unset): upstream speed
        downstream (int | Unset): downstream speed
    """

    upstream: int | Unset = UNSET
    downstream: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upstream = self.upstream

        downstream = self.downstream

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if upstream is not UNSET:
            field_dict["upstream"] = upstream
        if downstream is not UNSET:
            field_dict["downstream"] = downstream

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        upstream = d.pop("upstream", UNSET)

        downstream = d.pop("downstream", UNSET)

        wan_max_speed_open_api_vo = cls(
            upstream=upstream,
            downstream=downstream,
        )

        wan_max_speed_open_api_vo.additional_properties = d
        return wan_max_speed_open_api_vo

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
