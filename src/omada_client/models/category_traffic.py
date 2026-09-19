from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_traffic_with_client_count import (
        ApplicationTrafficWithClientCount,
    )
    from ..models.client_traffic_with_applications import ClientTrafficWithApplications


T = TypeVar("T", bound="CategoryTraffic")


@_attrs_define
class CategoryTraffic:
    """
    Attributes:
        family_id (int | Unset): The id of the category.
        family_name (str | Unset): The name of the category.
        traffic (int | Unset): The total amount of traffic used by the category.
        upload (int | Unset): The upload traffic used by the category.
        download (int | Unset): The download traffic used by the category.
        traffic_percent (float | Unset): The percentage of traffic used by the category.
        total_applications (int | Unset): The number of applications used in this category.
        applications (list[ApplicationTrafficWithClientCount] | Unset): The applications used in this category.
        total_clients (int | Unset): The number of clients using the app in this category.
        clients (list[ClientTrafficWithApplications] | Unset): The clients using the app in this category.
    """

    family_id: int | Unset = UNSET
    family_name: str | Unset = UNSET
    traffic: int | Unset = UNSET
    upload: int | Unset = UNSET
    download: int | Unset = UNSET
    traffic_percent: float | Unset = UNSET
    total_applications: int | Unset = UNSET
    applications: list[ApplicationTrafficWithClientCount] | Unset = UNSET
    total_clients: int | Unset = UNSET
    clients: list[ClientTrafficWithApplications] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family_id = self.family_id

        family_name = self.family_name

        traffic = self.traffic

        upload = self.upload

        download = self.download

        traffic_percent = self.traffic_percent

        total_applications = self.total_applications

        applications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.applications, Unset):
            applications = []
            for applications_item_data in self.applications:
                applications_item = applications_item_data.to_dict()
                applications.append(applications_item)

        total_clients = self.total_clients

        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if family_id is not UNSET:
            field_dict["familyId"] = family_id
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if upload is not UNSET:
            field_dict["upload"] = upload
        if download is not UNSET:
            field_dict["download"] = download
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent
        if total_applications is not UNSET:
            field_dict["totalApplications"] = total_applications
        if applications is not UNSET:
            field_dict["applications"] = applications
        if total_clients is not UNSET:
            field_dict["totalClients"] = total_clients
        if clients is not UNSET:
            field_dict["clients"] = clients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.application_traffic_with_client_count import (
            ApplicationTrafficWithClientCount,
        )
        from ..models.client_traffic_with_applications import (
            ClientTrafficWithApplications,
        )

        d = dict(src_dict)
        family_id = d.pop("familyId", UNSET)

        family_name = d.pop("familyName", UNSET)

        traffic = d.pop("traffic", UNSET)

        upload = d.pop("upload", UNSET)

        download = d.pop("download", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        total_applications = d.pop("totalApplications", UNSET)

        _applications = d.pop("applications", UNSET)
        applications: list[ApplicationTrafficWithClientCount] | Unset = UNSET
        if _applications is not UNSET:
            applications = []
            for applications_item_data in _applications:
                applications_item = ApplicationTrafficWithClientCount.from_dict(
                    applications_item_data
                )

                applications.append(applications_item)

        total_clients = d.pop("totalClients", UNSET)

        _clients = d.pop("clients", UNSET)
        clients: list[ClientTrafficWithApplications] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = ClientTrafficWithApplications.from_dict(
                    clients_item_data
                )

                clients.append(clients_item)

        category_traffic = cls(
            family_id=family_id,
            family_name=family_name,
            traffic=traffic,
            upload=upload,
            download=download,
            traffic_percent=traffic_percent,
            total_applications=total_applications,
            applications=applications,
            total_clients=total_clients,
            clients=clients,
        )

        category_traffic.additional_properties = d
        return category_traffic

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
