from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PpskAutoCreateSetting")


@_attrs_define
class PpskAutoCreateSetting:
    """Auto Create PPSK Setting.

    Attributes:
        number (int): Generate Number, should be within the range of 1-1024.
        prefix (str): PSK Name Prefix, should contain 1 to 60 visible ASCII characters.
        length (int): PSK Password Length, should be within the range of 8-63.
        vlan (int | Unset): PSK Bound Vlan, should be within the range of 1-4094.
    """

    number: int
    prefix: str
    length: int
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        prefix = self.prefix

        length = self.length

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "prefix": prefix,
                "length": length,
            }
        )
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        number = d.pop("number")

        prefix = d.pop("prefix")

        length = d.pop("length")

        vlan = d.pop("vlan", UNSET)

        ppsk_auto_create_setting = cls(
            number=number,
            prefix=prefix,
            length=length,
            vlan=vlan,
        )

        ppsk_auto_create_setting.additional_properties = d
        return ppsk_auto_create_setting

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
