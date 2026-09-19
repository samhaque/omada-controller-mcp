from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..models.system_interface_dto_interface_type import SystemInterfaceDTOInterfaceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemInterfaceDTO")


@_attrs_define
class SystemInterfaceDTO:
    """Management System Interfaces.

    Attributes:
        interface_type (SystemInterfaceDTOInterfaceType): Interface Type should be a value as follows: MANAGEMENT, NONE,
            VLAN, ROUTED_PORT, PORT_CHANNEL.
        interface_id (int | Unset): Management System Interface ID, its value should be within the range of 0-3.
        interface_value (str | Unset): Interface Value
    """

    interface_type: SystemInterfaceDTOInterfaceType
    interface_id: int | Unset = UNSET
    interface_value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_type = self.interface_type.value

        interface_id = self.interface_id

        interface_value = self.interface_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interfaceType": interface_type,
            }
        )
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if interface_value is not UNSET:
            field_dict["interfaceValue"] = interface_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        interface_type = SystemInterfaceDTOInterfaceType(d.pop("interfaceType"))

        interface_id = d.pop("interfaceId", UNSET)

        interface_value = d.pop("interfaceValue", UNSET)

        system_interface_dto = cls(
            interface_type=interface_type,
            interface_id=interface_id,
            interface_value=interface_value,
        )

        system_interface_dto.additional_properties = d
        return system_interface_dto

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
