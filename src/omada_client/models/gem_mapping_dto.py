from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.gem_mapping_dto_port_mapping_type import GemMappingDTOPortMappingType
from ..models.gem_mapping_dto_vlan_type import GemMappingDTOVlanType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GemMappingDTO")


@_attrs_define
class GemMappingDTO:
    """
    Attributes:
        gem_mapping_id (int): GemMappingId should be within the range of 1 to 8,and should not be null
        gem_port_id (int): Gem port ID should be within the range of 1 to 1023
        line_profile_id (int | Unset): The ID of the associated Line Profile should be within the range of 1 to 512.
        vlan_type (GemMappingDTOVlanType | Unset): The mapping relationship between Gem Port and VLAN is valid when the
            Line Profile's mappingMode is set to: Vlan, Vlan-Priority, Port-Vlan, or Port-VLAN-Priority. VlanType should be
            a value as follows: TAGGED;UNTAGGED, with the default value being TAGGED.
        vlan_id (int | Unset): VLAN ID is valid when the vlanType is set to Tagged. VlanId should be within the range of
            1 to 4094.
        priority (int | Unset): The mapping relationship between Gem Port and 802.1p priority.It is valid when the Line
            Profile's mappingMode is set to: Priority, Vlan-Priority, Port-Priority, or Port-VLAN-Priority. Priority should
            be within the range of 0 to 7.
        port_mapping_type (GemMappingDTOPortMappingType | Unset): The mapping relationship between Gem Port and ONT Port
            ID is valid when the Line Profile's mappingMode is set to: Port, Port-Vlan, Port-Priority, or Port-Vlan-
            Priority. PortMappingType should be a value as follows:ETH;POTS, with the default value being ETH.
        port_id (int | Unset): The mapped ONT port ID is valid when the portMappingType has a value. When
            portMappingType is ETH, portId should be within the range of 1 to 24.
    """

    gem_mapping_id: int
    gem_port_id: int
    line_profile_id: int | Unset = UNSET
    vlan_type: GemMappingDTOVlanType | Unset = UNSET
    vlan_id: int | Unset = UNSET
    priority: int | Unset = UNSET
    port_mapping_type: GemMappingDTOPortMappingType | Unset = UNSET
    port_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gem_mapping_id = self.gem_mapping_id

        gem_port_id = self.gem_port_id

        line_profile_id = self.line_profile_id

        vlan_type: str | Unset = UNSET
        if not isinstance(self.vlan_type, Unset):
            vlan_type = self.vlan_type.value

        vlan_id = self.vlan_id

        priority = self.priority

        port_mapping_type: str | Unset = UNSET
        if not isinstance(self.port_mapping_type, Unset):
            port_mapping_type = self.port_mapping_type.value

        port_id = self.port_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "gemMappingId": gem_mapping_id,
                "gemPortId": gem_port_id,
            }
        )
        if line_profile_id is not UNSET:
            field_dict["lineProfileId"] = line_profile_id
        if vlan_type is not UNSET:
            field_dict["vlanType"] = vlan_type
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if port_mapping_type is not UNSET:
            field_dict["portMappingType"] = port_mapping_type
        if port_id is not UNSET:
            field_dict["portId"] = port_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gem_mapping_id = d.pop("gemMappingId")

        gem_port_id = d.pop("gemPortId")

        line_profile_id = d.pop("lineProfileId", UNSET)

        _vlan_type = d.pop("vlanType", UNSET)
        vlan_type: GemMappingDTOVlanType | Unset
        if isinstance(_vlan_type, Unset):
            vlan_type = UNSET
        else:
            vlan_type = GemMappingDTOVlanType(_vlan_type)

        vlan_id = d.pop("vlanId", UNSET)

        priority = d.pop("priority", UNSET)

        _port_mapping_type = d.pop("portMappingType", UNSET)
        port_mapping_type: GemMappingDTOPortMappingType | Unset
        if isinstance(_port_mapping_type, Unset):
            port_mapping_type = UNSET
        else:
            port_mapping_type = GemMappingDTOPortMappingType(_port_mapping_type)

        port_id = d.pop("portId", UNSET)

        gem_mapping_dto = cls(
            gem_mapping_id=gem_mapping_id,
            gem_port_id=gem_port_id,
            line_profile_id=line_profile_id,
            vlan_type=vlan_type,
            vlan_id=vlan_id,
            priority=priority,
            port_mapping_type=port_mapping_type,
            port_id=port_id,
        )

        gem_mapping_dto.additional_properties = d
        return gem_mapping_dto

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
