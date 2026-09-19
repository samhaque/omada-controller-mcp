from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_traffic_with_applications import ClientTrafficWithApplications


T = TypeVar("T", bound="ApplicationStatTraffic")


@_attrs_define
class ApplicationStatTraffic:
    """
    Attributes:
        application_name (str | Unset): The name of the application.
        application_id (int | Unset): The id of the application.
        application_description (str | Unset): The description of the application.
        family_name (str | Unset): The name of the family.
        family_id (int | Unset): The id of the family.
        traffic (int | Unset): The total amount of traffic used by the app.
        traffic_percent (float | Unset): The percentage of traffic used by the app.
        block (int | Unset): The number of times this app has been blocked.
        active_user (int | Unset): The number of active users under this app.
        download (int | Unset): The download traffic used by the app.
        upload (int | Unset): The upload traffic used by the app.
        clients_count (int | Unset): The number of clients using the app.
        clients (list[ClientTrafficWithApplications] | Unset): The clients info.
    """

    application_name: str | Unset = UNSET
    application_id: int | Unset = UNSET
    application_description: str | Unset = UNSET
    family_name: str | Unset = UNSET
    family_id: int | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_percent: float | Unset = UNSET
    block: int | Unset = UNSET
    active_user: int | Unset = UNSET
    download: int | Unset = UNSET
    upload: int | Unset = UNSET
    clients_count: int | Unset = UNSET
    clients: list[ClientTrafficWithApplications] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        application_name = self.application_name

        application_id = self.application_id

        application_description = self.application_description

        family_name = self.family_name

        family_id = self.family_id

        traffic = self.traffic

        traffic_percent = self.traffic_percent

        block = self.block

        active_user = self.active_user

        download = self.download

        upload = self.upload

        clients_count = self.clients_count

        clients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.clients, Unset):
            clients = []
            for clients_item_data in self.clients:
                clients_item = clients_item_data.to_dict()
                clients.append(clients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if application_name is not UNSET:
            field_dict["applicationName"] = application_name
        if application_id is not UNSET:
            field_dict["applicationId"] = application_id
        if application_description is not UNSET:
            field_dict["applicationDescription"] = application_description
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if family_id is not UNSET:
            field_dict["familyId"] = family_id
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent
        if block is not UNSET:
            field_dict["block"] = block
        if active_user is not UNSET:
            field_dict["activeUser"] = active_user
        if download is not UNSET:
            field_dict["download"] = download
        if upload is not UNSET:
            field_dict["upload"] = upload
        if clients_count is not UNSET:
            field_dict["clientsCount"] = clients_count
        if clients is not UNSET:
            field_dict["clients"] = clients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_traffic_with_applications import (
            ClientTrafficWithApplications,
        )

        d = dict(src_dict)
        application_name = d.pop("applicationName", UNSET)

        application_id = d.pop("applicationId", UNSET)

        application_description = d.pop("applicationDescription", UNSET)

        family_name = d.pop("familyName", UNSET)

        family_id = d.pop("familyId", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        block = d.pop("block", UNSET)

        active_user = d.pop("activeUser", UNSET)

        download = d.pop("download", UNSET)

        upload = d.pop("upload", UNSET)

        clients_count = d.pop("clientsCount", UNSET)

        _clients = d.pop("clients", UNSET)
        clients: list[ClientTrafficWithApplications] | Unset = UNSET
        if _clients is not UNSET:
            clients = []
            for clients_item_data in _clients:
                clients_item = ClientTrafficWithApplications.from_dict(
                    clients_item_data
                )

                clients.append(clients_item)

        application_stat_traffic = cls(
            application_name=application_name,
            application_id=application_id,
            application_description=application_description,
            family_name=family_name,
            family_id=family_id,
            traffic=traffic,
            traffic_percent=traffic_percent,
            block=block,
            active_user=active_user,
            download=download,
            upload=upload,
            clients_count=clients_count,
            clients=clients,
        )

        application_stat_traffic.additional_properties = d
        return application_stat_traffic

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
