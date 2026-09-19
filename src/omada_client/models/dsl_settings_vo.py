from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DslSettingsVO")


@_attrs_define
class DslSettingsVO:
    """
    Attributes:
        modulation (int | Unset):
        annex (int | Unset):
        bit_swap (int | Unset):
        sra (int | Unset):
    """

    modulation: int | Unset = UNSET
    annex: int | Unset = UNSET
    bit_swap: int | Unset = UNSET
    sra: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modulation = self.modulation

        annex = self.annex

        bit_swap = self.bit_swap

        sra = self.sra

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modulation is not UNSET:
            field_dict["modulation"] = modulation
        if annex is not UNSET:
            field_dict["annex"] = annex
        if bit_swap is not UNSET:
            field_dict["bitSwap"] = bit_swap
        if sra is not UNSET:
            field_dict["sra"] = sra

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        modulation = d.pop("modulation", UNSET)

        annex = d.pop("annex", UNSET)

        bit_swap = d.pop("bitSwap", UNSET)

        sra = d.pop("sra", UNSET)

        dsl_settings_vo = cls(
            modulation=modulation,
            annex=annex,
            bit_swap=bit_swap,
            sra=sra,
        )

        dsl_settings_vo.additional_properties = d
        return dsl_settings_vo

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
