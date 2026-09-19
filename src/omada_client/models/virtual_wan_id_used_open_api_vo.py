from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanIdUsedOpenApiVO")


@_attrs_define
class VirtualWanIdUsedOpenApiVO:
    """
    Attributes:
        virtual_wan_id (str | Unset): The ID of the Virtual WAN.
        functions (list[str] | Unset): The functions that have adopted the current Virtual WAN
        not_allow_delete_functions (list[str] | Unset): The Virtual WAN related settings that are not allowed to be
            deleted.
        allow_delete_functions (list[str] | Unset): The Virtual WAN related settings that are allowed to be deleted.
        allow_delete (bool | Unset): Whether all Virtual WAN related functions are allowed to be deleted.
    """

    virtual_wan_id: str | Unset = UNSET
    functions: list[str] | Unset = UNSET
    not_allow_delete_functions: list[str] | Unset = UNSET
    allow_delete_functions: list[str] | Unset = UNSET
    allow_delete: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_wan_id = self.virtual_wan_id

        functions: list[str] | Unset = UNSET
        if not isinstance(self.functions, Unset):
            functions = self.functions

        not_allow_delete_functions: list[str] | Unset = UNSET
        if not isinstance(self.not_allow_delete_functions, Unset):
            not_allow_delete_functions = self.not_allow_delete_functions

        allow_delete_functions: list[str] | Unset = UNSET
        if not isinstance(self.allow_delete_functions, Unset):
            allow_delete_functions = self.allow_delete_functions

        allow_delete = self.allow_delete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id
        if functions is not UNSET:
            field_dict["functions"] = functions
        if not_allow_delete_functions is not UNSET:
            field_dict["notAllowDeleteFunctions"] = not_allow_delete_functions
        if allow_delete_functions is not UNSET:
            field_dict["allowDeleteFunctions"] = allow_delete_functions
        if allow_delete is not UNSET:
            field_dict["allowDelete"] = allow_delete

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        virtual_wan_id = d.pop("virtualWanId", UNSET)

        functions = cast(list[str], d.pop("functions", UNSET))

        not_allow_delete_functions = cast(
            list[str], d.pop("notAllowDeleteFunctions", UNSET)
        )

        allow_delete_functions = cast(list[str], d.pop("allowDeleteFunctions", UNSET))

        allow_delete = d.pop("allowDelete", UNSET)

        virtual_wan_id_used_open_api_vo = cls(
            virtual_wan_id=virtual_wan_id,
            functions=functions,
            not_allow_delete_functions=not_allow_delete_functions,
            allow_delete_functions=allow_delete_functions,
            allow_delete=allow_delete,
        )

        virtual_wan_id_used_open_api_vo.additional_properties = d
        return virtual_wan_id_used_open_api_vo

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
