from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentCountOpenApiVO")


@_attrs_define
class IncidentCountOpenApiVO:
    """List of incident count items grouped by severity level (critical/error/warning/info) and by function type (category)

    Attributes:
        critical (int | Unset): Number of critical incidents in this time bucket
        error (int | Unset): Number of error incidents in this time bucket
        warning (int | Unset): Number of warning incidents in this time bucket
        info (int | Unset): Number of info incidents in this time bucket
        access (int | Unset): Number of access incidents in this time bucket
        authentication (int | Unset): Number of authentication incidents in this time bucket
        roaming (int | Unset): Number of roaming incidents in this time bucket
        wireless_network (int | Unset): Number of wireless network incidents in this time bucket
        wired_network (int | Unset): Number of wired network incidents in this time bucket
        link (int | Unset): Number of link incidents in this time bucket
        wan_and_services (int | Unset): Number of WAN and services incidents in this time bucket
        device_status (int | Unset): Number of device status incidents in this time bucket
        security (int | Unset): Number of security incidents in this time bucket
        all_ (int | Unset): Total incident count across all levels in this time bucket
        time (int | Unset): Timestamp in seconds representing this time bucket
    """

    critical: int | Unset = UNSET
    error: int | Unset = UNSET
    warning: int | Unset = UNSET
    info: int | Unset = UNSET
    access: int | Unset = UNSET
    authentication: int | Unset = UNSET
    roaming: int | Unset = UNSET
    wireless_network: int | Unset = UNSET
    wired_network: int | Unset = UNSET
    link: int | Unset = UNSET
    wan_and_services: int | Unset = UNSET
    device_status: int | Unset = UNSET
    security: int | Unset = UNSET
    all_: int | Unset = UNSET
    time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        critical = self.critical

        error = self.error

        warning = self.warning

        info = self.info

        access = self.access

        authentication = self.authentication

        roaming = self.roaming

        wireless_network = self.wireless_network

        wired_network = self.wired_network

        link = self.link

        wan_and_services = self.wan_and_services

        device_status = self.device_status

        security = self.security

        all_ = self.all_

        time = self.time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if critical is not UNSET:
            field_dict["critical"] = critical
        if error is not UNSET:
            field_dict["error"] = error
        if warning is not UNSET:
            field_dict["warning"] = warning
        if info is not UNSET:
            field_dict["info"] = info
        if access is not UNSET:
            field_dict["access"] = access
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if roaming is not UNSET:
            field_dict["roaming"] = roaming
        if wireless_network is not UNSET:
            field_dict["wirelessNetwork"] = wireless_network
        if wired_network is not UNSET:
            field_dict["wiredNetwork"] = wired_network
        if link is not UNSET:
            field_dict["link"] = link
        if wan_and_services is not UNSET:
            field_dict["wanAndServices"] = wan_and_services
        if device_status is not UNSET:
            field_dict["deviceStatus"] = device_status
        if security is not UNSET:
            field_dict["security"] = security
        if all_ is not UNSET:
            field_dict["all"] = all_
        if time is not UNSET:
            field_dict["time"] = time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        critical = d.pop("critical", UNSET)

        error = d.pop("error", UNSET)

        warning = d.pop("warning", UNSET)

        info = d.pop("info", UNSET)

        access = d.pop("access", UNSET)

        authentication = d.pop("authentication", UNSET)

        roaming = d.pop("roaming", UNSET)

        wireless_network = d.pop("wirelessNetwork", UNSET)

        wired_network = d.pop("wiredNetwork", UNSET)

        link = d.pop("link", UNSET)

        wan_and_services = d.pop("wanAndServices", UNSET)

        device_status = d.pop("deviceStatus", UNSET)

        security = d.pop("security", UNSET)

        all_ = d.pop("all", UNSET)

        time = d.pop("time", UNSET)

        incident_count_open_api_vo = cls(
            critical=critical,
            error=error,
            warning=warning,
            info=info,
            access=access,
            authentication=authentication,
            roaming=roaming,
            wireless_network=wireless_network,
            wired_network=wired_network,
            link=link,
            wan_and_services=wan_and_services,
            device_status=device_status,
            security=security,
            all_=all_,
            time=time,
        )

        incident_count_open_api_vo.additional_properties = d
        return incident_count_open_api_vo

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
