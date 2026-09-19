from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PpskSettingV2")


@_attrs_define
class PpskSettingV2:
    """This field is required when Parameter [autoCreatePsks] is false; PPSK List In the PPSK Profile

    Attributes:
        name (str): PPSK Name, should contain 1 to 64 characters.
        psk (str): Password, should contain 8 to 63 visible ASCII characters.
        mac (str | Unset): Mac Bound With PSK.The MAC format requires the use of numbers and uppercase letters and
            connectors, such as AA-BB-CC-00-11-22.
        vlan (int | Unset): Vlan Bound With PSK, should be within the range of 1-4094.
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

        ppsk_setting_v2 = cls(
            name=name,
            psk=psk,
            mac=mac,
            vlan=vlan,
        )

        ppsk_setting_v2.additional_properties = d
        return ppsk_setting_v2

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
