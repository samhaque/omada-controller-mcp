from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SdmResourceUsage")


@_attrs_define
class SdmResourceUsage:
    """The list contains usage details of SDM resources on the device, including used and available resources.

    Attributes:
        category (int | Unset): It should be a value as follows: 0:Packet Control,  1:Packet Control V6 , 2:MAC ACL
            Ingress,  3:IP ACL Ingress,  4:IPV6 ACL Ingress,  5:Combined ACL Ingress,  6:MAC Diffserv Ingress, 7:IP Diffserv
            Ingress,  8:IPV6 Diffserv Ingress,  9:MAC Diffserv Egress,  10:IP Diffserv Egress,  11:IPV6 Diffserv Egress,
            12:Voice VLAN,  13:QoS VLAN,  14:VLAN VPN Ingress,  15:VLAN VPN Egress,  16:IPV4 Source Guard,  17:IPV6 Source
            Guard,  18:CPP Egress,  19:VRF,  20:Tunnel V4,  21:Tunnel V6 Stage0,  22:Tunnel V6 Stage1,  23:MPLS UNI,
            24:MPLS NNI0,  25:MPLS NNI1,  26:VXLAN V4 UNI,  27:VXLAN V6 UNI,  28:VXLAN V4 NNI Stage0,  29:VXLAN V4 NNI
            Stage1,  30:VXLAN V6 NNI Stage0,  31:VXLAN V6 NNI Stage1,  32:BFD V4,  33:BFD V6,  34:VXLAN Passenger,  35:QoS
            Rule V4,  36:QoS Rule V6 .
        used_num (int | Unset): The number of entries currently used by the feature.
        free_num (int | Unset): The number of entries currently available for use by the feature.
    """

    category: int | Unset = UNSET
    used_num: int | Unset = UNSET
    free_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        used_num = self.used_num

        free_num = self.free_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if used_num is not UNSET:
            field_dict["usedNum"] = used_num
        if free_num is not UNSET:
            field_dict["freeNum"] = free_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        category = d.pop("category", UNSET)

        used_num = d.pop("usedNum", UNSET)

        free_num = d.pop("freeNum", UNSET)

        sdm_resource_usage = cls(
            category=category,
            used_num=used_num,
            free_num=free_num,
        )

        sdm_resource_usage.additional_properties = d
        return sdm_resource_usage

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
