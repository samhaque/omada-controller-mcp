from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArpDetectStatusVO")


@_attrs_define
class ArpDetectStatusVO:
    """
    Attributes:
        arp_detect_enable (bool | Unset): Whether open the arp detect switch.
        snoop_for_entry_enable (bool | Unset): Whether open the snoop for entry.
    """

    arp_detect_enable: bool | Unset = UNSET
    snoop_for_entry_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arp_detect_enable = self.arp_detect_enable

        snoop_for_entry_enable = self.snoop_for_entry_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if arp_detect_enable is not UNSET:
            field_dict["arpDetectEnable"] = arp_detect_enable
        if snoop_for_entry_enable is not UNSET:
            field_dict["snoopForEntryEnable"] = snoop_for_entry_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        arp_detect_enable = d.pop("arpDetectEnable", UNSET)

        snoop_for_entry_enable = d.pop("snoopForEntryEnable", UNSET)

        arp_detect_status_vo = cls(
            arp_detect_enable=arp_detect_enable,
            snoop_for_entry_enable=snoop_for_entry_enable,
        )

        arp_detect_status_vo.additional_properties = d
        return arp_detect_status_vo

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
