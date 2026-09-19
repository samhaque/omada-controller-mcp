from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopApplicationByTrafficVO")


@_attrs_define
class TopApplicationByTrafficVO:
    """
    Attributes:
        application_id (int | Unset): application id
        application_name (str | Unset): application name
        family_id (int | Unset): category id
        family_name (str | Unset): category name
        traffic (int | Unset): traffic
        traffic_percent (int | Unset): percent of traffic
        down (int | Unset): rx traffic
        up (int | Unset): tx traffic
    """

    application_id: int | Unset = UNSET
    application_name: str | Unset = UNSET
    family_id: int | Unset = UNSET
    family_name: str | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_percent: int | Unset = UNSET
    down: int | Unset = UNSET
    up: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_id = self.application_id

        application_name = self.application_name

        family_id = self.family_id

        family_name = self.family_name

        traffic = self.traffic

        traffic_percent = self.traffic_percent

        down = self.down

        up = self.up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if family_id is not UNSET:
            field_dict["familyId"] = family_id
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent
        if down is not UNSET:
            field_dict["down"] = down
        if up is not UNSET:
            field_dict["up"] = up

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        application_id = d.pop("applicationId", UNSET)

        application_name = d.pop("applicationName", UNSET)

        family_id = d.pop("familyId", UNSET)

        family_name = d.pop("familyName", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        down = d.pop("down", UNSET)

        up = d.pop("up", UNSET)

        top_application_by_traffic_vo = cls(
            application_id=application_id,
            application_name=application_name,
            family_id=family_id,
            family_name=family_name,
            traffic=traffic,
            traffic_percent=traffic_percent,
            down=down,
            up=up,
        )

        top_application_by_traffic_vo.additional_properties = d
        return top_application_by_traffic_vo

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
