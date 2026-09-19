from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClientAccessTimeInfoVO")


@_attrs_define
class ClientAccessTimeInfoVO:
    """
    Attributes:
        mac (str | Unset): Mac address
        ip (str | Unset): ip
        client_name (str | Unset): Client name
        device_type (str | Unset): Client-connected device type
        client_type (str | Unset): Client type for icon display (e.g. Mobile, Laptop, IPC)
        client_model (str | Unset): Client model for icon display
        total_time (int | Unset): Total access time, only including associationTime now
        association_time (int | Unset): Association time
        auth_time (int | Unset): Authorization time
        dhcp_time (int | Unset): DHCP time
        dns_time (int | Unset): DNS time
        incidents (int | Unset): Incident counts
    """

    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    client_name: str | Unset = UNSET
    device_type: str | Unset = UNSET
    client_type: str | Unset = UNSET
    client_model: str | Unset = UNSET
    total_time: int | Unset = UNSET
    association_time: int | Unset = UNSET
    auth_time: int | Unset = UNSET
    dhcp_time: int | Unset = UNSET
    dns_time: int | Unset = UNSET
    incidents: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        client_name = self.client_name

        device_type = self.device_type

        client_type = self.client_type

        client_model = self.client_model

        total_time = self.total_time

        association_time = self.association_time

        auth_time = self.auth_time

        dhcp_time = self.dhcp_time

        dns_time = self.dns_time

        incidents = self.incidents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if client_model is not UNSET:
            field_dict["clientModel"] = client_model
        if total_time is not UNSET:
            field_dict["totalTime"] = total_time
        if association_time is not UNSET:
            field_dict["associationTime"] = association_time
        if auth_time is not UNSET:
            field_dict["authTime"] = auth_time
        if dhcp_time is not UNSET:
            field_dict["dhcpTime"] = dhcp_time
        if dns_time is not UNSET:
            field_dict["dnsTime"] = dns_time
        if incidents is not UNSET:
            field_dict["incidents"] = incidents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        client_name = d.pop("clientName", UNSET)

        device_type = d.pop("deviceType", UNSET)

        client_type = d.pop("clientType", UNSET)

        client_model = d.pop("clientModel", UNSET)

        total_time = d.pop("totalTime", UNSET)

        association_time = d.pop("associationTime", UNSET)

        auth_time = d.pop("authTime", UNSET)

        dhcp_time = d.pop("dhcpTime", UNSET)

        dns_time = d.pop("dnsTime", UNSET)

        incidents = d.pop("incidents", UNSET)

        client_access_time_info_vo = cls(
            mac=mac,
            ip=ip,
            client_name=client_name,
            device_type=device_type,
            client_type=client_type,
            client_model=client_model,
            total_time=total_time,
            association_time=association_time,
            auth_time=auth_time,
            dhcp_time=dhcp_time,
            dns_time=dns_time,
            incidents=incidents,
        )

        client_access_time_info_vo.additional_properties = d
        return client_access_time_info_vo

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
