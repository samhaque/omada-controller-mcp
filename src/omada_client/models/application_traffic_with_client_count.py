from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationTrafficWithClientCount")


@_attrs_define
class ApplicationTrafficWithClientCount:
    """The applications info using by the client.

    Attributes:
        application_name (str | Unset): The name of the application.
        application_id (int | Unset): The id of the application.
        application_description (str | Unset): The description of the application.
        family_id (int | Unset): The id of the category.
        family_name (str | Unset): The name of the category.
        traffic (int | Unset): The total amount of traffic used by the app.
        traffic_percent (float | Unset): The percentage of traffic used by the app.
        clients_count (int | Unset): The number of clients using the app.
    """

    application_name: str | Unset = UNSET
    application_id: int | Unset = UNSET
    application_description: str | Unset = UNSET
    family_id: int | Unset = UNSET
    family_name: str | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_percent: float | Unset = UNSET
    clients_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        application_id = self.application_id

        application_description = self.application_description

        family_id = self.family_id

        family_name = self.family_name

        traffic = self.traffic

        traffic_percent = self.traffic_percent

        clients_count = self.clients_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_description is not UNSET:
            field_dict["applicationDescription"] = application_description
        if family_id is not UNSET:
            field_dict["familyId"] = family_id
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent
        if clients_count is not UNSET:
            field_dict["clientsCount"] = clients_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        application_name = d.pop("applicationName", UNSET)

        application_id = d.pop("applicationId", UNSET)

        application_description = d.pop("applicationDescription", UNSET)

        family_id = d.pop("familyId", UNSET)

        family_name = d.pop("familyName", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        clients_count = d.pop("clientsCount", UNSET)

        application_traffic_with_client_count = cls(
            application_name=application_name,
            application_id=application_id,
            application_description=application_description,
            family_id=family_id,
            family_name=family_name,
            traffic=traffic,
            traffic_percent=traffic_percent,
            clients_count=clients_count,
        )

        application_traffic_with_client_count.additional_properties = d
        return application_traffic_with_client_count

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
