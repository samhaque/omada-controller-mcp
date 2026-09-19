from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwitchACLEtherTypeEntity")


@_attrs_define
class SwitchACLEtherTypeEntity:
    """Ethertype(4-hex number; 0-9，A-F) is only editable when the Source Type and Destination Type are both selected as MAC
    Group in the Rule.

        Attributes:
            enable (bool): Default:false
            value (str | Unset): Value, if enable is true, value must not be null
    """

    enable: bool
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        value = d.pop("value", UNSET)

        switch_acl_ether_type_entity = cls(
            enable=enable,
            value=value,
        )

        switch_acl_ether_type_entity.additional_properties = d
        return switch_acl_ether_type_entity

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
