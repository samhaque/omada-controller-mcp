from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VpnUsedFunctionOpenApiVO")


@_attrs_define
class VpnUsedFunctionOpenApiVO:
    """List of VPNs that have used the function.

    Attributes:
        id (str | Unset): ID of the VPN.
        name (str | Unset): VPN name.
        functions (list[str] | Unset): List of functions used by VPN.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    functions: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        functions: list[str] | Unset = UNSET
        if not isinstance(self.functions, Unset):
            functions = self.functions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if functions is not UNSET:
            field_dict["functions"] = functions

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        functions = cast(list[str], d.pop("functions", UNSET))

        vpn_used_function_open_api_vo = cls(
            id=id,
            name=name,
            functions=functions,
        )

        vpn_used_function_open_api_vo.additional_properties = d
        return vpn_used_function_open_api_vo

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
