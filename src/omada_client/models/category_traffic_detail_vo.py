from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryTrafficDetailVO")


@_attrs_define
class CategoryTrafficDetailVO:
    """
    Attributes:
        family_id (int | Unset): category id
        family_name (str | Unset): category name
        traffic (int | Unset): traffic
        percent (int | Unset): percent
    """

    family_id: int | Unset = UNSET
    family_name: str | Unset = UNSET
    traffic: int | Unset = UNSET
    percent: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family_id = self.family_id

        family_name = self.family_name

        traffic = self.traffic

        percent = self.percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if family_id is not UNSET:
            field_dict["familyId"] = family_id
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if percent is not UNSET:
            field_dict["percent"] = percent

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        family_id = d.pop("familyId", UNSET)

        family_name = d.pop("familyName", UNSET)

        traffic = d.pop("traffic", UNSET)

        percent = d.pop("percent", UNSET)

        category_traffic_detail_vo = cls(
            family_id=family_id,
            family_name=family_name,
            traffic=traffic,
            percent=percent,
        )

        category_traffic_detail_vo.additional_properties = d
        return category_traffic_detail_vo

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
