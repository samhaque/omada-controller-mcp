from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TrafficOpenApiVO")


@_attrs_define
class TrafficOpenApiVO:
    """
    Attributes:
        id (int | Unset): Application id
        name (str | Unset): Application name
        family_id (int | Unset): Family id
        family_name (str | Unset): Family name
        up (int | Unset): Upload bytes used of the application
        down (int | Unset): Download bytes used of the application
        traffic (int | Unset): Total bytes used of the application
    """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    family_id: int | Unset = UNSET
    family_name: str | Unset = UNSET
    up: int | Unset = UNSET
    down: int | Unset = UNSET
    traffic: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        family_id = self.family_id

        family_name = self.family_name

        up = self.up

        down = self.down

        traffic = self.traffic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if family_id is not UNSET:
            field_dict["familyId"] = family_id
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if up is not UNSET:
            field_dict["up"] = up
        if down is not UNSET:
            field_dict["down"] = down
        if traffic is not UNSET:
            field_dict["traffic"] = traffic

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        family_id = d.pop("familyId", UNSET)

        family_name = d.pop("familyName", UNSET)

        up = d.pop("up", UNSET)

        down = d.pop("down", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_open_api_vo = cls(
            id=id,
            name=name,
            family_id=family_id,
            family_name=family_name,
            up=up,
            down=down,
            traffic=traffic,
        )

        traffic_open_api_vo.additional_properties = d
        return traffic_open_api_vo

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
