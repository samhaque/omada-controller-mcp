from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_vo import IncidentVO


T = TypeVar("T", bound="DeviceHealthVO")


@_attrs_define
class DeviceHealthVO:
    """
    Attributes:
        time (int | Unset): Timestamp
        total (int | Unset): Total number of devices
        good (int | Unset): Number of devices with good health status
        poor (int | Unset): Number of devices with poor health status
        no_data (int | Unset): Number of devices with no health data
        incident_detail (IncidentVO | Unset): Incident statistics
    """

    time: int | Unset = UNSET
    total: int | Unset = UNSET
    good: int | Unset = UNSET
    poor: int | Unset = UNSET
    no_data: int | Unset = UNSET
    incident_detail: IncidentVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        total = self.total

        good = self.good

        poor = self.poor

        no_data = self.no_data

        incident_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident_detail, Unset):
            incident_detail = self.incident_detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if total is not UNSET:
            field_dict["total"] = total
        if good is not UNSET:
            field_dict["good"] = good
        if poor is not UNSET:
            field_dict["poor"] = poor
        if no_data is not UNSET:
            field_dict["noData"] = no_data
        if incident_detail is not UNSET:
            field_dict["incidentDetail"] = incident_detail

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident_vo import IncidentVO

        d = dict(src_dict)
        time = d.pop("time", UNSET)

        total = d.pop("total", UNSET)

        good = d.pop("good", UNSET)

        poor = d.pop("poor", UNSET)

        no_data = d.pop("noData", UNSET)

        _incident_detail = d.pop("incidentDetail", UNSET)
        incident_detail: IncidentVO | Unset
        if isinstance(_incident_detail, Unset):
            incident_detail = UNSET
        else:
            incident_detail = IncidentVO.from_dict(_incident_detail)

        device_health_vo = cls(
            time=time,
            total=total,
            good=good,
            poor=poor,
            no_data=no_data,
            incident_detail=incident_detail,
        )

        device_health_vo.additional_properties = d
        return device_health_vo

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
