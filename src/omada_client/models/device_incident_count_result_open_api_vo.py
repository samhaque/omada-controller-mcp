from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident import Incident


T = TypeVar("T", bound="DeviceIncidentCountResultOpenApiVO")


@_attrs_define
class DeviceIncidentCountResultOpenApiVO:
    """
    Attributes:
        incidents (list[Incident] | Unset): Incident counts for the requested devices.
    """

    incidents: list[Incident] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incidents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.incidents, Unset):
            incidents = []
            for incidents_item_data in self.incidents:
                incidents_item = incidents_item_data.to_dict()
                incidents.append(incidents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incidents is not UNSET:
            field_dict["incidents"] = incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.incident import Incident

        d = dict(src_dict)
        _incidents = d.pop("incidents", UNSET)
        incidents: list[Incident] | Unset = UNSET
        if _incidents is not UNSET:
            incidents = []
            for incidents_item_data in _incidents:
                incidents_item = Incident.from_dict(incidents_item_data)

                incidents.append(incidents_item)

        device_incident_count_result_open_api_vo = cls(
            incidents=incidents,
        )

        device_incident_count_result_open_api_vo.additional_properties = d
        return device_incident_count_result_open_api_vo

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
