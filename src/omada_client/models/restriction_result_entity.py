from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestrictionResultEntity")


@_attrs_define
class RestrictionResultEntity:
    """
    Attributes:
        network_name (str | Unset): Network name. It should be the name of LAN network, can be obtained from 'Get LAN
            network list' interface.
        filter_id (int | Unset): Filter ID can be obtained from 'Get filter list' interface.
        restriction_id (int | Unset): Restriction ID
        filter_ (str | Unset): Filter name
        subnet (str | Unset): Subnet
        subnet_ipv_6 (str | Unset): Subnet Ipv6
        vlan (int | Unset): Vlan ID
        vlans (str | Unset): Vlan IDS
    """

    network_name: str | Unset = UNSET
    filter_id: int | Unset = UNSET
    restriction_id: int | Unset = UNSET
    filter_: str | Unset = UNSET
    subnet: str | Unset = UNSET
    subnet_ipv_6: str | Unset = UNSET
    vlan: int | Unset = UNSET
    vlans: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_name = self.network_name

        filter_id = self.filter_id

        restriction_id = self.restriction_id

        filter_ = self.filter_

        subnet = self.subnet

        subnet_ipv_6 = self.subnet_ipv_6

        vlan = self.vlan

        vlans = self.vlans

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if filter_id is not UNSET:
            field_dict["filterId"] = filter_id
        if restriction_id is not UNSET:
            field_dict["restrictionId"] = restriction_id
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if subnet is not UNSET:
            field_dict["subnet"] = subnet
        if subnet_ipv_6 is not UNSET:
            field_dict["subnetIpv6"] = subnet_ipv_6
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if vlans is not UNSET:
            field_dict["vlans"] = vlans

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_name = d.pop("networkName", UNSET)

        filter_id = d.pop("filterId", UNSET)

        restriction_id = d.pop("restrictionId", UNSET)

        filter_ = d.pop("filter", UNSET)

        subnet = d.pop("subnet", UNSET)

        subnet_ipv_6 = d.pop("subnetIpv6", UNSET)

        vlan = d.pop("vlan", UNSET)

        vlans = d.pop("vlans", UNSET)

        restriction_result_entity = cls(
            network_name=network_name,
            filter_id=filter_id,
            restriction_id=restriction_id,
            filter_=filter_,
            subnet=subnet,
            subnet_ipv_6=subnet_ipv_6,
            vlan=vlan,
            vlans=vlans,
        )

        restriction_result_entity.additional_properties = d
        return restriction_result_entity

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
