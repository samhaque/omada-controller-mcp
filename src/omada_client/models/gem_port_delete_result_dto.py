from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GemPortDeleteResultDTO")


@_attrs_define
class GemPortDeleteResultDTO:
    """Device configuration information.If the type of data is 'Object',ignore this field

    Attributes:
        gem_ports_in_use (list[int] | Unset): The list of Gem Port ID that failed to delete due to being in use.
    """

    gem_ports_in_use: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gem_ports_in_use: list[int] | Unset = UNSET
        if not isinstance(self.gem_ports_in_use, Unset):
            gem_ports_in_use = self.gem_ports_in_use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gem_ports_in_use is not UNSET:
            field_dict["gemPortsInUse"] = gem_ports_in_use

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        gem_ports_in_use = cast(list[int], d.pop("gemPortsInUse", UNSET))

        gem_port_delete_result_dto = cls(
            gem_ports_in_use=gem_ports_in_use,
        )

        gem_port_delete_result_dto.additional_properties = d
        return gem_port_delete_result_dto

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
