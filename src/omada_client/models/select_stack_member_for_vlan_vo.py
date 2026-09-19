from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.select_stack_member_port_for_vlan_vo import (
        SelectStackMemberPortForVlanVO,
    )


T = TypeVar("T", bound="SelectStackMemberForVlanVO")


@_attrs_define
class SelectStackMemberForVlanVO:
    """Stack Members

    Attributes:
        name (str | Unset): Device Name
        mac (str | Unset): Device Mac
        model (str | Unset): Device Model
        mode_version (str | Unset): Device Model Version
        unit (int | Unset): Stack member's unit
        status_category (int | Unset): Device status category, 0: Disconnected, 1: Connected, 2: Pending,3: Heartbeat
            Missed, 4: Isolated
        compatible (int | Unset): Device firmware and controller compatibility type.Compatible should be a value as
            follows: 0:COMPATIBLE;1:HIGH_MAJOR_VER;2:LOW_MAJOR_VER;3:HIGH_MINOR_VER;4:LOW_MINOR_VER;7:HIGH_COMPONENT_VER;10:
            DEVICE_NOT_COMPATIBLE;11:HIGH_ADOPT_COMMPONENT;12:DEVICE_CATEGORY_NOT_COMPATIBLE;14:DEVICE_NOT_COMPATIBLE_IN_CLU
            STER
        added_in_advanced (bool | Unset): Whether the device is added in advanced.
        ports (list[SelectStackMemberPortForVlanVO] | Unset): Ports
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    mode_version: str | Unset = UNSET
    unit: int | Unset = UNSET
    status_category: int | Unset = UNSET
    compatible: int | Unset = UNSET
    added_in_advanced: bool | Unset = UNSET
    ports: list[SelectStackMemberPortForVlanVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        mode_version = self.mode_version

        unit = self.unit

        status_category = self.status_category

        compatible = self.compatible

        added_in_advanced = self.added_in_advanced

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if mode_version is not UNSET:
            field_dict["modeVersion"] = mode_version
        if unit is not UNSET:
            field_dict["unit"] = unit
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if compatible is not UNSET:
            field_dict["compatible"] = compatible
        if added_in_advanced is not UNSET:
            field_dict["addedInAdvanced"] = added_in_advanced
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.select_stack_member_port_for_vlan_vo import (
            SelectStackMemberPortForVlanVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        mode_version = d.pop("modeVersion", UNSET)

        unit = d.pop("unit", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        compatible = d.pop("compatible", UNSET)

        added_in_advanced = d.pop("addedInAdvanced", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[SelectStackMemberPortForVlanVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = SelectStackMemberPortForVlanVO.from_dict(ports_item_data)

                ports.append(ports_item)

        select_stack_member_for_vlan_vo = cls(
            name=name,
            mac=mac,
            model=model,
            mode_version=mode_version,
            unit=unit,
            status_category=status_category,
            compatible=compatible,
            added_in_advanced=added_in_advanced,
            ports=ports,
        )

        select_stack_member_for_vlan_vo.additional_properties = d
        return select_stack_member_for_vlan_vo

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
