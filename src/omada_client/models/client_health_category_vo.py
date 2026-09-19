from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.health_distribution_vo import HealthDistributionVO
    from ..models.incident_vo import IncidentVO


T = TypeVar("T", bound="ClientHealthCategoryVO")


@_attrs_define
class ClientHealthCategoryVO:
    """Wired client health

    Attributes:
        health (HealthDistributionVO | Unset): Health distribution
        incident (IncidentVO | Unset): Incident statistics
    """

    health: HealthDistributionVO | Unset = UNSET
    incident: IncidentVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.health, Unset):
            health = self.health.to_dict()

        incident: dict[str, Any] | Unset = UNSET
        if not isinstance(self.incident, Unset):
            incident = self.incident.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if health is not UNSET:
            field_dict["health"] = health
        if incident is not UNSET:
            field_dict["incident"] = incident

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.health_distribution_vo import (
            HealthDistributionVO,
        )
        from ..models.incident_vo import IncidentVO

        d = dict(src_dict)
        _health = d.pop("health", UNSET)
        health: HealthDistributionVO | Unset
        if isinstance(_health, Unset):
            health = UNSET
        else:
            health = HealthDistributionVO.from_dict(_health)

        _incident = d.pop("incident", UNSET)
        incident: IncidentVO | Unset
        if isinstance(_incident, Unset):
            incident = UNSET
        else:
            incident = IncidentVO.from_dict(_incident)

        client_health_category_vo = cls(
            health=health,
            incident=incident,
        )

        client_health_category_vo.additional_properties = d
        return client_health_category_vo

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
