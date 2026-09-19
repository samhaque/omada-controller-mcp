from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStaticRoutingConfigOpenApiVO")


@_attrs_define
class OswStaticRoutingConfigOpenApiVO:
    """
    Attributes:
        ip_version (int): The IP Version of class rule should be a value as follows: 0: IPv4; 1: IPv6.
        status (bool): StaticRouting status
        destinations (list[str]): IP address/SubNet, up to 16 entries are allowed for the destinations list.
        next_hop_ip (str): NextHopIp
        distance (int): Distance should be within the range of 1–255.
        description (str | Unset): The description of static routing. It may contain 0 to 128 characters, including
            digits (0–9), uppercase and lowercase letters (A–Z, a–z), spaces, and -_@:/.+# .
        vrf_id (str | Unset): VrfId
        next_hop_vrf_id (str | Unset): NextHopVrfId
    """

    ip_version: int
    status: bool
    destinations: list[str]
    next_hop_ip: str
    distance: int
    description: str | Unset = UNSET
    vrf_id: str | Unset = UNSET
    next_hop_vrf_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_version = self.ip_version

        status = self.status

        destinations = self.destinations

        next_hop_ip = self.next_hop_ip

        distance = self.distance

        description = self.description

        vrf_id = self.vrf_id

        next_hop_vrf_id = self.next_hop_vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipVersion": ip_version,
                "status": status,
                "destinations": destinations,
                "nextHopIp": next_hop_ip,
                "distance": distance,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if next_hop_vrf_id is not UNSET:
            field_dict["nextHopVrfId"] = next_hop_vrf_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ip_version = d.pop("ipVersion")

        status = d.pop("status")

        destinations = cast(list[str], d.pop("destinations"))

        next_hop_ip = d.pop("nextHopIp")

        distance = d.pop("distance")

        description = d.pop("description", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        next_hop_vrf_id = d.pop("nextHopVrfId", UNSET)

        osw_static_routing_config_open_api_vo = cls(
            ip_version=ip_version,
            status=status,
            destinations=destinations,
            next_hop_ip=next_hop_ip,
            distance=distance,
            description=description,
            vrf_id=vrf_id,
            next_hop_vrf_id=next_hop_vrf_id,
        )

        osw_static_routing_config_open_api_vo.additional_properties = d
        return osw_static_routing_config_open_api_vo

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
