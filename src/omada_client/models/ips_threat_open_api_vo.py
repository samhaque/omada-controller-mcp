from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsThreatOpenApiVO")


@_attrs_define
class IpsThreatOpenApiVO:
    """
    Attributes:
        id (str | Unset): ID.
        omadac_id (str | Unset): Omada ID
        site_id (str | Unset): Site ID
        site_name (str | Unset): Site Name.
        time (int | Unset): Time.
        severity (int | Unset): 0：critical, 1：major, 2：concerning 3：minor.
        service (str | Unset): Service.
        signature (str | Unset): Signature.
        category (int | Unset): Category.
        activity (str | Unset): Activity.
        data_usage (int | Unset): Data Usage.
        src_ip (str | Unset): Source Ip.
        dst_ip (str | Unset): Destination Ip.
        src_country (str | Unset): Source Country.
        dst_country (str | Unset): Destination Country.
        protocol (str | Unset): Protocol.
        sid (int | Unset): Sid.
        src_latitude (float | Unset): Source Latitude(The precision is four decimal places).
        src_longitude (float | Unset): Source Longitude(The precision is four decimal places).
        dst_latitude (float | Unset): Destination Latitude(The precision is four decimal places).
        dst_longitude (float | Unset): Destination Longitude(The precision is four decimal places).
        archived (bool | Unset): Whether archived.
        classification (str | Unset): Classification.
        creat_time (int | Unset): Creat Time.
    """

    id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    site_name: str | Unset = UNSET
    time: int | Unset = UNSET
    severity: int | Unset = UNSET
    service: str | Unset = UNSET
    signature: str | Unset = UNSET
    category: int | Unset = UNSET
    activity: str | Unset = UNSET
    data_usage: int | Unset = UNSET
    src_ip: str | Unset = UNSET
    dst_ip: str | Unset = UNSET
    src_country: str | Unset = UNSET
    dst_country: str | Unset = UNSET
    protocol: str | Unset = UNSET
    sid: int | Unset = UNSET
    src_latitude: float | Unset = UNSET
    src_longitude: float | Unset = UNSET
    dst_latitude: float | Unset = UNSET
    dst_longitude: float | Unset = UNSET
    archived: bool | Unset = UNSET
    classification: str | Unset = UNSET
    creat_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        omadac_id = self.omadac_id

        site_id = self.site_id

        site_name = self.site_name

        time = self.time

        severity = self.severity

        service = self.service

        signature = self.signature

        category = self.category

        activity = self.activity

        data_usage = self.data_usage

        src_ip = self.src_ip

        dst_ip = self.dst_ip

        src_country = self.src_country

        dst_country = self.dst_country

        protocol = self.protocol

        sid = self.sid

        src_latitude = self.src_latitude

        src_longitude = self.src_longitude

        dst_latitude = self.dst_latitude

        dst_longitude = self.dst_longitude

        archived = self.archived

        classification = self.classification

        creat_time = self.creat_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if time is not UNSET:
            field_dict["time"] = time
        if severity is not UNSET:
            field_dict["severity"] = severity
        if service is not UNSET:
            field_dict["service"] = service
        if signature is not UNSET:
            field_dict["signature"] = signature
        if category is not UNSET:
            field_dict["category"] = category
        if activity is not UNSET:
            field_dict["activity"] = activity
        if data_usage is not UNSET:
            field_dict["dataUsage"] = data_usage
        if src_ip is not UNSET:
            field_dict["srcIp"] = src_ip
        if dst_ip is not UNSET:
            field_dict["dstIp"] = dst_ip
        if src_country is not UNSET:
            field_dict["srcCountry"] = src_country
        if dst_country is not UNSET:
            field_dict["dstCountry"] = dst_country
        if protocol is not UNSET:
            field_dict["protocol"] = protocol
        if sid is not UNSET:
            field_dict["sid"] = sid
        if src_latitude is not UNSET:
            field_dict["srcLatitude"] = src_latitude
        if src_longitude is not UNSET:
            field_dict["srcLongitude"] = src_longitude
        if dst_latitude is not UNSET:
            field_dict["dstLatitude"] = dst_latitude
        if dst_longitude is not UNSET:
            field_dict["dstLongitude"] = dst_longitude
        if archived is not UNSET:
            field_dict["archived"] = archived
        if classification is not UNSET:
            field_dict["classification"] = classification
        if creat_time is not UNSET:
            field_dict["creatTime"] = creat_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        time = d.pop("time", UNSET)

        severity = d.pop("severity", UNSET)

        service = d.pop("service", UNSET)

        signature = d.pop("signature", UNSET)

        category = d.pop("category", UNSET)

        activity = d.pop("activity", UNSET)

        data_usage = d.pop("dataUsage", UNSET)

        src_ip = d.pop("srcIp", UNSET)

        dst_ip = d.pop("dstIp", UNSET)

        src_country = d.pop("srcCountry", UNSET)

        dst_country = d.pop("dstCountry", UNSET)

        protocol = d.pop("protocol", UNSET)

        sid = d.pop("sid", UNSET)

        src_latitude = d.pop("srcLatitude", UNSET)

        src_longitude = d.pop("srcLongitude", UNSET)

        dst_latitude = d.pop("dstLatitude", UNSET)

        dst_longitude = d.pop("dstLongitude", UNSET)

        archived = d.pop("archived", UNSET)

        classification = d.pop("classification", UNSET)

        creat_time = d.pop("creatTime", UNSET)

        ips_threat_open_api_vo = cls(
            id=id,
            omadac_id=omadac_id,
            site_id=site_id,
            site_name=site_name,
            time=time,
            severity=severity,
            service=service,
            signature=signature,
            category=category,
            activity=activity,
            data_usage=data_usage,
            src_ip=src_ip,
            dst_ip=dst_ip,
            src_country=src_country,
            dst_country=dst_country,
            protocol=protocol,
            sid=sid,
            src_latitude=src_latitude,
            src_longitude=src_longitude,
            dst_latitude=dst_latitude,
            dst_longitude=dst_longitude,
            archived=archived,
            classification=classification,
            creat_time=creat_time,
        )

        ips_threat_open_api_vo.additional_properties = d
        return ips_threat_open_api_vo

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
