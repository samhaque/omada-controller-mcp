from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyLanNetworkBrief")


@_attrs_define
class ModifyLanNetworkBrief:
    """
    Attributes:
        id (str): The ID of the lan network
        site_id (str): The site ID of the lan network
        name (str): The name of the lan network
        gateway_subnet (str): The Gateway Subnet of the lan network
        ipaddr_start (str): The starting host IP address of gatewaySubnet
        ipaddr_end (str): The ending host IP address of gatewaySubnet
        vlan (int | Unset): The vlan number of the lan network
    """

    id: str
    site_id: str
    name: str
    gateway_subnet: str
    ipaddr_start: str
    ipaddr_end: str
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        site_id = self.site_id

        name = self.name

        gateway_subnet = self.gateway_subnet

        ipaddr_start = self.ipaddr_start

        ipaddr_end = self.ipaddr_end

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "siteId": site_id,
                "name": name,
                "gatewaySubnet": gateway_subnet,
                "ipaddrStart": ipaddr_start,
                "ipaddrEnd": ipaddr_end,
            }
        )
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        site_id = d.pop("siteId")

        name = d.pop("name")

        gateway_subnet = d.pop("gatewaySubnet")

        ipaddr_start = d.pop("ipaddrStart")

        ipaddr_end = d.pop("ipaddrEnd")

        vlan = d.pop("vlan", UNSET)

        modify_lan_network_brief = cls(
            id=id,
            site_id=site_id,
            name=name,
            gateway_subnet=gateway_subnet,
            ipaddr_start=ipaddr_start,
            ipaddr_end=ipaddr_end,
            vlan=vlan,
        )

        modify_lan_network_brief.additional_properties = d
        return modify_lan_network_brief

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
