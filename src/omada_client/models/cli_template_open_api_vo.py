from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CliTemplateOpenApiVO")


@_attrs_define
class CliTemplateOpenApiVO:
    """CLI template configuration entry

    Attributes:
        id (str | Unset): CLI configuration ID
        name (str | Unset): CLI configuration name
        description (str | Unset): CLI configuration description, it should be within the range of 0 - 256 characters.
        status (int | Unset): CLI configuration status, it should be a value as follows: 0: active, 1: inactive
        apply (bool | Unset): Whether the CLI configuration can be applied. Only the CLI configuration in inactive state
            can be applied.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    status: int | Unset = UNSET
    apply: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        status = self.status

        apply = self.apply

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if status is not UNSET:
            field_dict["status"] = status
        if apply is not UNSET:
            field_dict["apply"] = apply

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        status = d.pop("status", UNSET)

        apply = d.pop("apply", UNSET)

        cli_template_open_api_vo = cls(
            id=id,
            name=name,
            description=description,
            status=status,
            apply=apply,
        )

        cli_template_open_api_vo.additional_properties = d
        return cli_template_open_api_vo

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
