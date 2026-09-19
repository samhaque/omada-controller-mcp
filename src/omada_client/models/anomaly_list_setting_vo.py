from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnomalyListSettingVO")


@_attrs_define
class AnomalyListSettingVO:
    """
    Attributes:
        incidents (list[str] | Unset): List of anomaly event IDs to operate on. IDs are from 'Get grid incident List'
            API.
        select_all (bool | Unset): Whether to select all incidents. If true, 'incidents' list items are excluded;
            otherwise only listed items are processed.
        object_ (str | Unset): Device or client MAC, multiple MACs separated by comma. Required when selectAll is true.
        anomaly_code (str | Unset): Anomaly event code. Required when selectAll is true.
        start (int | Unset): Start time in seconds. If both start and end are omitted, the server defaults to the last
            30 days.
        end (int | Unset): End time in seconds. If both start and end are omitted, the server defaults to the last 30
            days.
        status (int | Unset): Current event status. 0: Unresolved, 1: Resolved, 2: Ignored. 3：Ongoing
        target_status (int | Unset): Target event status for modification. 0: Unresolved 1: Resolved, 2: Ignored. Not
            required for deletion.
    """

    incidents: list[str] | Unset = UNSET
    select_all: bool | Unset = UNSET
    object_: str | Unset = UNSET
    anomaly_code: str | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    status: int | Unset = UNSET
    target_status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incidents: list[str] | Unset = UNSET
        if not isinstance(self.incidents, Unset):
            incidents = self.incidents

        select_all = self.select_all

        object_ = self.object_

        anomaly_code = self.anomaly_code

        start = self.start

        end = self.end

        status = self.status

        target_status = self.target_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incidents is not UNSET:
            field_dict["incidents"] = incidents
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if object_ is not UNSET:
            field_dict["object"] = object_
        if anomaly_code is not UNSET:
            field_dict["anomalyCode"] = anomaly_code
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if status is not UNSET:
            field_dict["status"] = status
        if target_status is not UNSET:
            field_dict["targetStatus"] = target_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        incidents = cast(list[str], d.pop("incidents", UNSET))

        select_all = d.pop("selectAll", UNSET)

        object_ = d.pop("object", UNSET)

        anomaly_code = d.pop("anomalyCode", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        status = d.pop("status", UNSET)

        target_status = d.pop("targetStatus", UNSET)

        anomaly_list_setting_vo = cls(
            incidents=incidents,
            select_all=select_all,
            object_=object_,
            anomaly_code=anomaly_code,
            start=start,
            end=end,
            status=status,
            target_status=target_status,
        )

        anomaly_list_setting_vo.additional_properties = d
        return anomaly_list_setting_vo

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
