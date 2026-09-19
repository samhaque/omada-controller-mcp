from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDHCPOptions")


@_attrs_define
class CustomDHCPOptions:
    """User custom DHCP options

    Attributes:
        custom (bool | Unset): Whether is custom by user.
        name (str | Unset): Custom DHCP option name.
        code (int | Unset): Custom DHCP option code
        type_ (int | Unset): Type should be a value as follows: 0: "String"; 1: "IP Address"; 2: "Hex Array"
        value (str | Unset): Value
    """

    custom: bool | Unset = UNSET
    name: str | Unset = UNSET
    code: int | Unset = UNSET
    type_: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom = self.custom

        name = self.name

        code = self.code

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom is not UNSET:
            field_dict["custom"] = custom
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        custom = d.pop("custom", UNSET)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        custom_dhcp_options = cls(
            custom=custom,
            name=name,
            code=code,
            type_=type_,
            value=value,
        )

        custom_dhcp_options.additional_properties = d
        return custom_dhcp_options

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
