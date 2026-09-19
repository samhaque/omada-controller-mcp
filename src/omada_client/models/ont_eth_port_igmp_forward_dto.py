from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.ont_eth_port_igmp_forward_dto_igmp_forward_mode import (
    OntEthPortIGMPForwardDTOIgmpForwardMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OntEthPortIGMPForwardDTO")


@_attrs_define
class OntEthPortIGMPForwardDTO:
    """IgmpForward

    Attributes:
        igmp_forward_mode (OntEthPortIGMPForwardDTOIgmpForwardMode): IgmpForwardMode should not be null,igmpForwardMode
            should be a value as follows:UNCONCERN,TRANSLATION,DEFAULT,TRANSPARENT
        vlan (int | Unset): Vlan should be within the range of 1 to 4095
        priority (int | Unset): Priority should be within the range of -1 to 7
    """

    igmp_forward_mode: OntEthPortIGMPForwardDTOIgmpForwardMode
    vlan: int | Unset = UNSET
    priority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        igmp_forward_mode = self.igmp_forward_mode.value

        vlan = self.vlan

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "igmpForwardMode": igmp_forward_mode,
            }
        )
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        igmp_forward_mode = OntEthPortIGMPForwardDTOIgmpForwardMode(
            d.pop("igmpForwardMode")
        )

        vlan = d.pop("vlan", UNSET)

        priority = d.pop("priority", UNSET)

        ont_eth_port_igmp_forward_dto = cls(
            igmp_forward_mode=igmp_forward_mode,
            vlan=vlan,
            priority=priority,
        )

        ont_eth_port_igmp_forward_dto.additional_properties = d
        return ont_eth_port_igmp_forward_dto

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
