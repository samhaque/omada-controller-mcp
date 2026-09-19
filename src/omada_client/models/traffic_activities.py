from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_traffic_activity import DeviceTrafficActivity


T = TypeVar("T", bound="TrafficActivities")


@_attrs_define
class TrafficActivities:
    """
    Attributes:
        ap_traffic_activities (list[DeviceTrafficActivity] | Unset): Wireless network total traffic timing list
        switch_traffic_activities (list[DeviceTrafficActivity] | Unset): Wired network total traffic timing list
    """

    ap_traffic_activities: list[DeviceTrafficActivity] | Unset = UNSET
    switch_traffic_activities: list[DeviceTrafficActivity] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_traffic_activities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ap_traffic_activities, Unset):
            ap_traffic_activities = []
            for ap_traffic_activities_item_data in self.ap_traffic_activities:
                ap_traffic_activities_item = ap_traffic_activities_item_data.to_dict()
                ap_traffic_activities.append(ap_traffic_activities_item)

        switch_traffic_activities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.switch_traffic_activities, Unset):
            switch_traffic_activities = []
            for switch_traffic_activities_item_data in self.switch_traffic_activities:
                switch_traffic_activities_item = (
                    switch_traffic_activities_item_data.to_dict()
                )
                switch_traffic_activities.append(switch_traffic_activities_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_traffic_activities is not UNSET:
            field_dict["apTrafficActivities"] = ap_traffic_activities
        if switch_traffic_activities is not UNSET:
            field_dict["switchTrafficActivities"] = switch_traffic_activities

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_traffic_activity import (
            DeviceTrafficActivity,
        )

        d = dict(src_dict)
        _ap_traffic_activities = d.pop("apTrafficActivities", UNSET)
        ap_traffic_activities: list[DeviceTrafficActivity] | Unset = UNSET
        if _ap_traffic_activities is not UNSET:
            ap_traffic_activities = []
            for ap_traffic_activities_item_data in _ap_traffic_activities:
                ap_traffic_activities_item = DeviceTrafficActivity.from_dict(
                    ap_traffic_activities_item_data
                )

                ap_traffic_activities.append(ap_traffic_activities_item)

        _switch_traffic_activities = d.pop("switchTrafficActivities", UNSET)
        switch_traffic_activities: list[DeviceTrafficActivity] | Unset = UNSET
        if _switch_traffic_activities is not UNSET:
            switch_traffic_activities = []
            for switch_traffic_activities_item_data in _switch_traffic_activities:
                switch_traffic_activities_item = DeviceTrafficActivity.from_dict(
                    switch_traffic_activities_item_data
                )

                switch_traffic_activities.append(switch_traffic_activities_item)

        traffic_activities = cls(
            ap_traffic_activities=ap_traffic_activities,
            switch_traffic_activities=switch_traffic_activities,
        )

        traffic_activities.additional_properties = d
        return traffic_activities

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
