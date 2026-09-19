from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.system_interface_dto import SystemInterfaceDTO


T = TypeVar("T", bound="ManagementSystemInterfaceDTO")


@_attrs_define
class ManagementSystemInterfaceDTO:
    """
    Attributes:
        system_interfaces (list[SystemInterfaceDTO] | Unset): Management System Interfaces.
    """

    system_interfaces: list[SystemInterfaceDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        system_interfaces: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.system_interfaces, Unset):
            system_interfaces = []
            for system_interfaces_item_data in self.system_interfaces:
                system_interfaces_item = system_interfaces_item_data.to_dict()
                system_interfaces.append(system_interfaces_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if system_interfaces is not UNSET:
            field_dict["systemInterfaces"] = system_interfaces

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.system_interface_dto import SystemInterfaceDTO

        d = dict(src_dict)
        _system_interfaces = d.pop("systemInterfaces", UNSET)
        system_interfaces: list[SystemInterfaceDTO] | Unset = UNSET
        if _system_interfaces is not UNSET:
            system_interfaces = []
            for system_interfaces_item_data in _system_interfaces:
                system_interfaces_item = SystemInterfaceDTO.from_dict(
                    system_interfaces_item_data
                )

                system_interfaces.append(system_interfaces_item)

        management_system_interface_dto = cls(
            system_interfaces=system_interfaces,
        )

        management_system_interface_dto.additional_properties = d
        return management_system_interface_dto

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
