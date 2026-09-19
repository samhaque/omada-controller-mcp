from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PSK")


@_attrs_define
class PSK:
    """Auto Created PSKs.

    Attributes:
        name (str): PSK Name
        psk (str): Password
        vlan (int | Unset): Vlan Bound With PSK
    """

    name: str
    psk: str
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        psk = self.psk

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "psk": psk,
            }
        )
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        psk = d.pop("psk")

        vlan = d.pop("vlan", UNSET)

        psk = cls(
            name=name,
            psk=psk,
            vlan=vlan,
        )

        psk.additional_properties = d
        return psk

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
