from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrafficProfileAddResultDTO")


@_attrs_define
class TrafficProfileAddResultDTO:
    """Device configuration information.If the type of data is 'Object',ignore this field

    Attributes:
        name (str | Unset): Name of the traffic profile.
        traffic_id (int | Unset): Traffic profile ID
    """

    name: str | Unset = UNSET
    traffic_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        traffic_id = self.traffic_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if traffic_id is not UNSET:
            field_dict["trafficId"] = traffic_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        traffic_id = d.pop("trafficId", UNSET)

        traffic_profile_add_result_dto = cls(
            name=name,
            traffic_id=traffic_id,
        )

        traffic_profile_add_result_dto.additional_properties = d
        return traffic_profile_add_result_dto

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
