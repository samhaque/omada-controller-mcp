from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SdWanLanNetworkNatReq")


@_attrs_define
class SdWanLanNetworkNatReq:
    """A list of original custom route

    Attributes:
        site_id (str): The site ID of the lan network
        gateway_subnet (str): The Gateway Subnet of the lan network
        id (str | Unset): The ID of the lan network
        need_map (bool | Unset): This value exists in customNetwork. If true, it indicates a conflicting route that
            requires mapping; routes with false should be avoided by NAT mapping.
    """

    site_id: str
    gateway_subnet: str
    id: str | Unset = UNSET
    need_map: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        gateway_subnet = self.gateway_subnet

        id = self.id

        need_map = self.need_map

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "siteId": site_id,
                "gatewaySubnet": gateway_subnet,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if need_map is not UNSET:
            field_dict["needMap"] = need_map

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_id = d.pop("siteId")

        gateway_subnet = d.pop("gatewaySubnet")

        id = d.pop("id", UNSET)

        need_map = d.pop("needMap", UNSET)

        sd_wan_lan_network_nat_req = cls(
            site_id=site_id,
            gateway_subnet=gateway_subnet,
            id=id,
            need_map=need_map,
        )

        sd_wan_lan_network_nat_req.additional_properties = d
        return sd_wan_lan_network_nat_req

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
