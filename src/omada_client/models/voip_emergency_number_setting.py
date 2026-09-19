from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VoipEmergencyNumberSetting")


@_attrs_define
class VoipEmergencyNumberSetting:
    """
    Attributes:
        emergency_number_enable (bool): Whether to enable the emergency number.
        no_operation_time (int | Unset): No operation time should be within the range of 2-8s.
        emergency_numbers (list[str] | Unset): Emergency number list.
    """

    emergency_number_enable: bool
    no_operation_time: int | Unset = UNSET
    emergency_numbers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emergency_number_enable = self.emergency_number_enable

        no_operation_time = self.no_operation_time

        emergency_numbers: list[str] | Unset = UNSET
        if not isinstance(self.emergency_numbers, Unset):
            emergency_numbers = self.emergency_numbers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emergencyNumberEnable": emergency_number_enable,
            }
        )
        if no_operation_time is not UNSET:
            field_dict["noOperationTime"] = no_operation_time
        if emergency_numbers is not UNSET:
            field_dict["emergencyNumbers"] = emergency_numbers

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        emergency_number_enable = d.pop("emergencyNumberEnable")

        no_operation_time = d.pop("noOperationTime", UNSET)

        emergency_numbers = cast(list[str], d.pop("emergencyNumbers", UNSET))

        voip_emergency_number_setting = cls(
            emergency_number_enable=emergency_number_enable,
            no_operation_time=no_operation_time,
            emergency_numbers=emergency_numbers,
        )

        voip_emergency_number_setting.additional_properties = d
        return voip_emergency_number_setting

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
