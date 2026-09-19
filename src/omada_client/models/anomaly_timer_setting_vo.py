from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.anomaly_brief_query_vo import AnomalyBriefQueryVO


T = TypeVar("T", bound="AnomalyTimerSettingVO")


@_attrs_define
class AnomalyTimerSettingVO:
    """
    Attributes:
        status (int): Current event status. 0: Unresolved, 1: Resolved, 2: Ignored. 3: Ongoing
        start_time (int): Start time in milliseconds (Unix timestamp).
        end_time (int): End time in milliseconds (Unix timestamp).
        incidents (list[AnomalyBriefQueryVO] | Unset): List of anomaly event objects to operate on, identified by
            anomaly code and MAC.
        select_all (bool | Unset): Whether to select all incidents. If true, 'incidents' list items are excluded;
            otherwise only listed items are processed.
        search_key (str | Unset): Search keyword for event content, device name/MAC/IP. Required when selectAll is true.
        level (int | Unset): Event severity level filter. 0: Critical, 1: Error, 2: Warning, 3: Info.
        category (str | Unset): Event category filter, comma-separated. Required when selectAll is true.
        object_type (str | Unset): Object type filter, comma-separated (e.g. 'ap,wirelessClient'). Required when
            selectAll is true.
        target_status (int | Unset): Target event status for modification. 0: Unresolved 1: Resolved, 2: Ignored. Not
            required for deletion.
        start (int | Unset): Start time in seconds (Unix timestamp).
        end (int | Unset): End time in seconds (Unix timestamp).
    """

    status: int
    start_time: int
    end_time: int
    incidents: list[AnomalyBriefQueryVO] | Unset = UNSET
    select_all: bool | Unset = UNSET
    search_key: str | Unset = UNSET
    level: int | Unset = UNSET
    category: str | Unset = UNSET
    object_type: str | Unset = UNSET
    target_status: int | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        start_time = self.start_time

        end_time = self.end_time

        incidents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incidents, Unset):
            incidents = []
            for incidents_item_data in self.incidents:
                incidents_item = incidents_item_data.to_dict()
                incidents.append(incidents_item)

        select_all = self.select_all

        search_key = self.search_key

        level = self.level

        category = self.category

        object_type = self.object_type

        target_status = self.target_status

        start = self.start

        end = self.end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "startTime": start_time,
                "endTime": end_time,
            }
        )
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if level is not UNSET:
            field_dict["level"] = level
        if category is not UNSET:
            field_dict["category"] = category
        if object_type is not UNSET:
            field_dict["objectType"] = object_type
        if target_status is not UNSET:
            field_dict["targetStatus"] = target_status
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.anomaly_brief_query_vo import AnomalyBriefQueryVO

        d = dict(src_dict)
        status = d.pop("status")

        start_time = d.pop("startTime")

        end_time = d.pop("endTime")

        _incidents = d.pop("incidents", UNSET)
        incidents: list[AnomalyBriefQueryVO] | Unset = UNSET
        if _incidents is not UNSET:
            incidents = []
            for incidents_item_data in _incidents:
                incidents_item = AnomalyBriefQueryVO.from_dict(incidents_item_data)

                incidents.append(incidents_item)

        select_all = d.pop("selectAll", UNSET)

        search_key = d.pop("searchKey", UNSET)

        level = d.pop("level", UNSET)

        category = d.pop("category", UNSET)

        object_type = d.pop("objectType", UNSET)

        target_status = d.pop("targetStatus", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        anomaly_timer_setting_vo = cls(
            status=status,
            start_time=start_time,
            end_time=end_time,
            incidents=incidents,
            select_all=select_all,
            search_key=search_key,
            level=level,
            category=category,
            object_type=object_type,
            target_status=target_status,
            start=start,
            end=end,
        )

        anomaly_timer_setting_vo.additional_properties = d
        return anomaly_timer_setting_vo

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
