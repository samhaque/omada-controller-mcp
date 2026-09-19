from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AnomalyCategoryEventCountVO")


@_attrs_define
class AnomalyCategoryEventCountVO:
    """Anomaly category event count information

    Attributes:
        anomaly_code (str | Unset): For the values of Anomaly event code, refer to section 5.7.2.1 of the Open API
            Access Example: 01001001.
        counts (int | Unset): Total count of unresolved and ongoing events
        total_counts (int | Unset): Total count of events in all status
        current_status_counts (int | Unset): Count of events in the current status
        influencing_devices (int | Unset): Number of influenced devices
        influencing_clients (int | Unset): Number of influenced clients
        level (int | Unset): Level of this incident
    """

    anomaly_code: str | Unset = UNSET
    counts: int | Unset = UNSET
    total_counts: int | Unset = UNSET
    current_status_counts: int | Unset = UNSET
    influencing_devices: int | Unset = UNSET
    influencing_clients: int | Unset = UNSET
    level: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        anomaly_code = self.anomaly_code

        counts = self.counts

        total_counts = self.total_counts

        current_status_counts = self.current_status_counts

        influencing_devices = self.influencing_devices

        influencing_clients = self.influencing_clients

        level = self.level

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if anomaly_code is not UNSET:
            field_dict["anomalyCode"] = anomaly_code
        if counts is not UNSET:
            field_dict["counts"] = counts
        if total_counts is not UNSET:
            field_dict["totalCounts"] = total_counts
        if current_status_counts is not UNSET:
            field_dict["currentStatusCounts"] = current_status_counts
        if influencing_devices is not UNSET:
            field_dict["influencingDevices"] = influencing_devices
        if influencing_clients is not UNSET:
            field_dict["influencingClients"] = influencing_clients
        if level is not UNSET:
            field_dict["level"] = level

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        anomaly_code = d.pop("anomalyCode", UNSET)

        counts = d.pop("counts", UNSET)

        total_counts = d.pop("totalCounts", UNSET)

        current_status_counts = d.pop("currentStatusCounts", UNSET)

        influencing_devices = d.pop("influencingDevices", UNSET)

        influencing_clients = d.pop("influencingClients", UNSET)

        level = d.pop("level", UNSET)

        anomaly_category_event_count_vo = cls(
            anomaly_code=anomaly_code,
            counts=counts,
            total_counts=total_counts,
            current_status_counts=current_status_counts,
            influencing_devices=influencing_devices,
            influencing_clients=influencing_clients,
            level=level,
        )

        anomaly_category_event_count_vo.additional_properties = d
        return anomaly_category_event_count_vo

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
