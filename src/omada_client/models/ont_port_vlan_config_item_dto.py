from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.ont_port_vlan_config_item_dto_vlan_mode import (
    OntPortVlanConfigItemDTOVlanMode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OntPortVlanConfigItemDTO")


@_attrs_define
class OntPortVlanConfigItemDTO:
    """Config item edit list

    Attributes:
        id (int): Vlan ID should not be null
        vlan_mode (OntPortVlanConfigItemDTOVlanMode): Vlan mode should not be null,vlanMode should be a value as
            follows:TRANSLATION,QINQ,TRUNK
        svlan (int): SVlan ID should be within the range of 1 to 4095 and should not be null
        spriority (int | Unset): SVlan priority should be within the range of -2 to 7
        cvlan (int | Unset): CVlan ID should be within the range of 1 to 4095
        cpriority (int | Unset): CVlan priority should be within the range of -1 to 7
    """

    id: int
    vlan_mode: OntPortVlanConfigItemDTOVlanMode
    svlan: int
    spriority: int | Unset = UNSET
    cvlan: int | Unset = UNSET
    cpriority: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        vlan_mode = self.vlan_mode.value

        svlan = self.svlan

        spriority = self.spriority

        cvlan = self.cvlan

        cpriority = self.cpriority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "vlanMode": vlan_mode,
                "svlan": svlan,
            }
        )
        if spriority is not UNSET:
            field_dict["spriority"] = spriority
        if cvlan is not UNSET:
            field_dict["cvlan"] = cvlan
        if cpriority is not UNSET:
            field_dict["cpriority"] = cpriority

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id")

        vlan_mode = OntPortVlanConfigItemDTOVlanMode(d.pop("vlanMode"))

        svlan = d.pop("svlan")

        spriority = d.pop("spriority", UNSET)

        cvlan = d.pop("cvlan", UNSET)

        cpriority = d.pop("cpriority", UNSET)

        ont_port_vlan_config_item_dto = cls(
            id=id,
            vlan_mode=vlan_mode,
            svlan=svlan,
            spriority=spriority,
            cvlan=cvlan,
            cpriority=cpriority,
        )

        ont_port_vlan_config_item_dto.additional_properties = d
        return ont_port_vlan_config_item_dto

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
