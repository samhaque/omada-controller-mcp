from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DslSettings")


@_attrs_define
class DslSettings:
    """DSL port configurations.

    Attributes:
        modulation_type (int | Unset): Enter a value as follows: 0-Auto Sync-up, 2-ADSL2, 3-ADSL2+, 4-G.dmt, 5-T1.423,
            6-VDSL2, 7-G.Lte.
        annex_type (int | Unset): Enter a value as follows: 0-Annex Auto, 1-Annex A, 2-Annex B, 3-Annex I, 4-Annex J,
            5-Annex M, 6-Annex A/L, 7-Annex B/J, 8-Annex A/I/J/L/M
        bit_swap (int | Unset): Enter a value as follows: 0-off, 1-on.
        sra (int | Unset): Enter a value as follows: 0-off, 1-on.
    """

    modulation_type: int | Unset = UNSET
    annex_type: int | Unset = UNSET
    bit_swap: int | Unset = UNSET
    sra: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modulation_type = self.modulation_type

        annex_type = self.annex_type

        bit_swap = self.bit_swap

        sra = self.sra

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if modulation_type is not UNSET:
            field_dict["modulationType"] = modulation_type
        if annex_type is not UNSET:
            field_dict["annexType"] = annex_type
        if bit_swap is not UNSET:
            field_dict["bitSwap"] = bit_swap
        if sra is not UNSET:
            field_dict["sra"] = sra

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        modulation_type = d.pop("modulationType", UNSET)

        annex_type = d.pop("annexType", UNSET)

        bit_swap = d.pop("bitSwap", UNSET)

        sra = d.pop("sra", UNSET)

        dsl_settings = cls(
            modulation_type=modulation_type,
            annex_type=annex_type,
            bit_swap=bit_swap,
            sra=sra,
        )

        dsl_settings.additional_properties = d
        return dsl_settings

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
