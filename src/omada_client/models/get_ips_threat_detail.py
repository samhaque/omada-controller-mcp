from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetIpsThreatDetail")


@_attrs_define
class GetIpsThreatDetail:
    """
    Attributes:
        id (str | Unset): IPS threat ID
        time (int | Unset): Timestamp, in seconds, such as 1682000000
        src_ip (str | Unset): IPS threat source IP
        src_country (str | Unset): IPS threat destination Country
        dst_ip (str | Unset): IPS threat destination IP
        service (str | Unset): Ips threat description
        severity (int | Unset): Ips threat severity,  0：Critical, 1：Major, 2：Moderate 3：Minor 4:Low
        category (int | Unset): Ips threat category, Custom IDS/IPS categories list, if parameter[Dplevel] is 3,
            customCategories is needed.CustomCategories should be a list as follow: 1: Botcc, 2: Worm, 3: Malware, 4:
            Mobile_Malware, 6: P2P, 7: Tor, 8: Exploit, 9: Shellcode, 14: Activex, 15: DNS, 18: User Agents, 24: DShield
        classification (str | Unset): Ips threat classification
        activity (int | Unset): Ips threat dataUsage, in Byte
        protocol (str | Unset): Ips threat protocol
    """

    id: str | Unset = UNSET
    time: int | Unset = UNSET
    src_ip: str | Unset = UNSET
    src_country: str | Unset = UNSET
    dst_ip: str | Unset = UNSET
    service: str | Unset = UNSET
    severity: int | Unset = UNSET
    category: int | Unset = UNSET
    classification: str | Unset = UNSET
    activity: int | Unset = UNSET
    protocol: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        time = self.time

        src_ip = self.src_ip

        src_country = self.src_country

        dst_ip = self.dst_ip

        service = self.service

        severity = self.severity

        category = self.category

        classification = self.classification

        activity = self.activity

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if time is not UNSET:
            field_dict["time"] = time
        if src_ip is not UNSET:
            field_dict["srcIp"] = src_ip
        if src_country is not UNSET:
            field_dict["srcCountry"] = src_country
        if dst_ip is not UNSET:
            field_dict["dstIp"] = dst_ip
        if service is not UNSET:
            field_dict["service"] = service
        if severity is not UNSET:
            field_dict["severity"] = severity
        if category is not UNSET:
            field_dict["category"] = category
        if classification is not UNSET:
            field_dict["classification"] = classification
        if activity is not UNSET:
            field_dict["activity"] = activity
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        time = d.pop("time", UNSET)

        src_ip = d.pop("srcIp", UNSET)

        src_country = d.pop("srcCountry", UNSET)

        dst_ip = d.pop("dstIp", UNSET)

        service = d.pop("service", UNSET)

        severity = d.pop("severity", UNSET)

        category = d.pop("category", UNSET)

        classification = d.pop("classification", UNSET)

        activity = d.pop("activity", UNSET)

        protocol = d.pop("protocol", UNSET)

        get_ips_threat_detail = cls(
            id=id,
            time=time,
            src_ip=src_ip,
            src_country=src_country,
            dst_ip=dst_ip,
            service=service,
            severity=severity,
            category=category,
            classification=classification,
            activity=activity,
            protocol=protocol,
        )

        get_ips_threat_detail.additional_properties = d
        return get_ips_threat_detail

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
