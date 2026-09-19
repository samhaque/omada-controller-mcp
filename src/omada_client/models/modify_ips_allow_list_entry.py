from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyIPSAllowListEntry")


@_attrs_define
class ModifyIPSAllowListEntry:
    """
    Attributes:
        id (str): Allow list entry ID.
        direction (int | Unset): The location of the target that can trigger the threat, direction should be a value as
            follows:0: both 1: source, 2: destination.
        traffic_type (int | Unset): Exempt the category of objects (targets) that can trigger the threat, trafficType
            should be a value as follows: 0: IP Address, 1: Network, 2: Subnet.
        ip_address (str | Unset): The value of the trafficType is 0, indicating IP address.
        network (str | Unset): The value of the trafficType is 1, indicating LAN network ID.
        subnet (str | Unset): The value of the trafficType is 2, indicating subnet.
    """

    id: str
    direction: int | Unset = UNSET
    traffic_type: int | Unset = UNSET
    ip_address: str | Unset = UNSET
    network: str | Unset = UNSET
    subnet: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        direction = self.direction

        traffic_type = self.traffic_type

        ip_address = self.ip_address

        network = self.network

        subnet = self.subnet

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if direction is not UNSET:
            field_dict["direction"] = direction
        if traffic_type is not UNSET:
            field_dict["trafficType"] = traffic_type
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if network is not UNSET:
            field_dict["network"] = network
        if subnet is not UNSET:
            field_dict["subnet"] = subnet

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        direction = d.pop("direction", UNSET)

        traffic_type = d.pop("trafficType", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        network = d.pop("network", UNSET)

        subnet = d.pop("subnet", UNSET)

        modify_ips_allow_list_entry = cls(
            id=id,
            direction=direction,
            traffic_type=traffic_type,
            ip_address=ip_address,
            network=network,
            subnet=subnet,
        )

        modify_ips_allow_list_entry.additional_properties = d
        return modify_ips_allow_list_entry

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
