from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswStpRpvstInstanceVO")


@_attrs_define
class OswStpRpvstInstanceVO:
    """Instances

    Attributes:
        priority (int | Unset): Priority
        vlan (str | Unset): Vlan
        enable (int | Unset): Enable
    """

    priority: int | Unset = UNSET
    vlan: str | Unset = UNSET
    enable: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        priority = self.priority

        vlan = self.vlan

        enable = self.enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if priority is not UNSET:
            field_dict["priority"] = priority
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if enable is not UNSET:
            field_dict["enable"] = enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        priority = d.pop("priority", UNSET)

        vlan = d.pop("vlan", UNSET)

        enable = d.pop("enable", UNSET)

        osw_stp_rpvst_instance_vo = cls(
            priority=priority,
            vlan=vlan,
            enable=enable,
        )

        osw_stp_rpvst_instance_vo.additional_properties = d
        return osw_stp_rpvst_instance_vo

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
