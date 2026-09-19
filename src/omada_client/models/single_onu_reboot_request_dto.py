from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SingleOnuRebootRequestDTO")


@_attrs_define
class SingleOnuRebootRequestDTO:
    """Reboot request list

    Attributes:
        equipment_id (str | Unset): ONT device ID should contain 1 to 20 characters in ASCII code from \\x21 to \\x7e.
        key (str | Unset): Identifier of ONU
        mac_address (str | Unset): Mac address of ONU
    """

    equipment_id: str | Unset = UNSET
    key: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        equipment_id = self.equipment_id

        key = self.key

        mac_address = self.mac_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if equipment_id is not UNSET:
            field_dict["equipmentId"] = equipment_id
        if key is not UNSET:
            field_dict["key"] = key
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        equipment_id = d.pop("equipmentId", UNSET)

        key = d.pop("key", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        single_onu_reboot_request_dto = cls(
            equipment_id=equipment_id,
            key=key,
            mac_address=mac_address,
        )

        single_onu_reboot_request_dto.additional_properties = d
        return single_onu_reboot_request_dto

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
