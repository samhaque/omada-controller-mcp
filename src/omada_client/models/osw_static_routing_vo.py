from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStaticRoutingVO")


@_attrs_define
class OswStaticRoutingVO:
    """
    Attributes:
        status (bool): StaticRouting status
        destinations (list[str]): IP address/SubNet, up to 16 entries are allowed for the destinations list.
        distance (int): Distance should be within the range of 1–255.
        id (str | Unset): StaticRouting ID
        omadac_id (str | Unset): Omada ID
        site_id (str | Unset): Site ID
        entry_id (int | Unset): The entry ID of StaticRouting
        name (str | Unset): Switch name
        description (str | Unset): The description of static routing. It may contain 0 to 128 characters, including
            digits (0–9), uppercase and lowercase letters (A–Z, a–z), spaces, and -_@:/.+# .
        mac (str | Unset): Switch Mac
        vrf_id (str | Unset):
        ip_version (int | Unset): The IP Version of class rule should be a value as follows: 0: IPv4; 1: IPv6.
        next_hop_ip (str | Unset): NextHopIp
        next_hop_vrf_id (str | Unset):
        resource (int | Unset): Resource is a value as follows: 0: new created; 1: from template; 2: override
    """

    status: bool
    destinations: list[str]
    distance: int
    id: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    entry_id: int | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    mac: str | Unset = UNSET
    vrf_id: str | Unset = UNSET
    ip_version: int | Unset = UNSET
    next_hop_ip: str | Unset = UNSET
    next_hop_vrf_id: str | Unset = UNSET
    resource: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        destinations = self.destinations

        distance = self.distance

        id = self.id

        omadac_id = self.omadac_id

        site_id = self.site_id

        entry_id = self.entry_id

        name = self.name

        description = self.description

        mac = self.mac

        vrf_id = self.vrf_id

        ip_version = self.ip_version

        next_hop_ip = self.next_hop_ip

        next_hop_vrf_id = self.next_hop_vrf_id

        resource = self.resource

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "destinations": destinations,
                "distance": distance,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if entry_id is not UNSET:
            field_dict["entryId"] = entry_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if mac is not UNSET:
            field_dict["mac"] = mac
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if ip_version is not UNSET:
            field_dict["ipVersion"] = ip_version
        if next_hop_ip is not UNSET:
            field_dict["nextHopIp"] = next_hop_ip
        if next_hop_vrf_id is not UNSET:
            field_dict["nextHopVrfId"] = next_hop_vrf_id
        if resource is not UNSET:
            field_dict["resource"] = resource

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status")

        destinations = cast(list[str], d.pop("destinations"))

        distance = d.pop("distance")

        id = d.pop("id", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        entry_id = d.pop("entryId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        mac = d.pop("mac", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        ip_version = d.pop("ipVersion", UNSET)

        next_hop_ip = d.pop("nextHopIp", UNSET)

        next_hop_vrf_id = d.pop("nextHopVrfId", UNSET)

        resource = d.pop("resource", UNSET)

        osw_static_routing_vo = cls(
            status=status,
            destinations=destinations,
            distance=distance,
            id=id,
            omadac_id=omadac_id,
            site_id=site_id,
            entry_id=entry_id,
            name=name,
            description=description,
            mac=mac,
            vrf_id=vrf_id,
            ip_version=ip_version,
            next_hop_ip=next_hop_ip,
            next_hop_vrf_id=next_hop_vrf_id,
            resource=resource,
        )

        osw_static_routing_vo.additional_properties = d
        return osw_static_routing_vo

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
