from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_basic_info import ApplicationBasicInfo


T = TypeVar("T", bound="ClientTrafficWithApplications")


@_attrs_define
class ClientTrafficWithApplications:
    """The clients info.

    Attributes:
        type_ (str | Unset): The type of the client.
        manager (bool | Unset): Whether the client is managed by the controller..
        client_name (str | Unset): The name of the client.
        mac (str | Unset): The mac of the client.
        traffic (int | Unset): The total amount of traffic used by the client.
        traffic_percent (float | Unset): The percentage of download traffic used by the client.
        upload (int | Unset): The upload traffic used by the client.
        download (int | Unset): The download traffic used by the client.
        total_applications (int | Unset): The number of applications using by the client.
        application_list (list[ApplicationBasicInfo] | Unset): The applications info using by the client.
    """

    type_: str | Unset = UNSET
    manager: bool | Unset = UNSET
    client_name: str | Unset = UNSET
    mac: str | Unset = UNSET
    traffic: int | Unset = UNSET
    traffic_percent: float | Unset = UNSET
    upload: int | Unset = UNSET
    download: int | Unset = UNSET
    total_applications: int | Unset = UNSET
    application_list: list[ApplicationBasicInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        manager = self.manager

        client_name = self.client_name

        mac = self.mac

        traffic = self.traffic

        traffic_percent = self.traffic_percent

        upload = self.upload

        download = self.download

        total_applications = self.total_applications

        application_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.application_list, Unset):
            application_list = []
            for application_list_item_data in self.application_list:
                application_list_item = application_list_item_data.to_dict()
                application_list.append(application_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if manager is not UNSET:
            field_dict["manager"] = manager
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if traffic is not UNSET:
            field_dict["traffic"] = traffic
        if traffic_percent is not UNSET:
            field_dict["trafficPercent"] = traffic_percent
        if upload is not UNSET:
            field_dict["upload"] = upload
        if download is not UNSET:
            field_dict["download"] = download
        if total_applications is not UNSET:
            field_dict["totalApplications"] = total_applications
        if application_list is not UNSET:
            field_dict["applicationList"] = application_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.application_basic_info import (
            ApplicationBasicInfo,
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        manager = d.pop("manager", UNSET)

        client_name = d.pop("clientName", UNSET)

        mac = d.pop("mac", UNSET)

        traffic = d.pop("traffic", UNSET)

        traffic_percent = d.pop("trafficPercent", UNSET)

        upload = d.pop("upload", UNSET)

        download = d.pop("download", UNSET)

        total_applications = d.pop("totalApplications", UNSET)

        _application_list = d.pop("applicationList", UNSET)
        application_list: list[ApplicationBasicInfo] | Unset = UNSET
        if _application_list is not UNSET:
            application_list = []
            for application_list_item_data in _application_list:
                application_list_item = ApplicationBasicInfo.from_dict(
                    application_list_item_data
                )

                application_list.append(application_list_item)

        client_traffic_with_applications = cls(
            type_=type_,
            manager=manager,
            client_name=client_name,
            mac=mac,
            traffic=traffic,
            traffic_percent=traffic_percent,
            upload=upload,
            download=download,
            total_applications=total_applications,
            application_list=application_list,
        )

        client_traffic_with_applications.additional_properties = d
        return client_traffic_with_applications

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
