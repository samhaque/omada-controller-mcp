from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PSKVO")


@_attrs_define
class PSKVO:
    """PSK List In the PPSK Profile

    Attributes:
        name (str): PSK Name
        psk (str): Password
        mac (str | Unset): Mac Bound With PSK
        vlan (int | Unset): Vlan Bound With PSK
    """

    name: str
    psk: str
    mac: str | Unset = UNSET
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        psk = self.psk

        mac = self.mac

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "psk": psk,
            }
        )
        if mac is not UNSET:
            field_dict["mac"] = mac
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        psk = d.pop("psk")

        mac = d.pop("mac", UNSET)

        vlan = d.pop("vlan", UNSET)

        pskvo = cls(
            name=name,
            psk=psk,
            mac=mac,
            vlan=vlan,
        )

        pskvo.additional_properties = d
        return pskvo

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
