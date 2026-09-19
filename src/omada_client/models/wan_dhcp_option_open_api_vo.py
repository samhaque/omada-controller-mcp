from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanDhcpOptionOpenApiVO")


@_attrs_define
class WanDhcpOptionOpenApiVO:
    """
    Attributes:
        code (int | Unset): Dhcp option code
        type_ (int | Unset): Type should be a value as follows: 0: "String"; 1: "IP Address"; 2: "Hex Array"
        value (str | Unset): Dhcp option value
    """

    code: int | Unset = UNSET
    type_: int | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        type_ = self.type_

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
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
        code = d.pop("code", UNSET)

        type_ = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        wan_dhcp_option_open_api_vo = cls(
            code=code,
            type_=type_,
            value=value,
        )

        wan_dhcp_option_open_api_vo.additional_properties = d
        return wan_dhcp_option_open_api_vo

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
