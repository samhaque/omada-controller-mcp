from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditFilterEntity")


@_attrs_define
class EditFilterEntity:
    """
    Attributes:
        filter_name (str): Filter name. It should be 1 - 128 characters
        rules (list[int]): Rule ID list can be obtained from 'Get rule list' interface.
        description (str | Unset): Description of filter. It should be 1 - 128 characters
    """

    filter_name: str
    rules: list[int]
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_name = self.filter_name

        rules = self.rules

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filterName": filter_name,
                "rules": rules,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        filter_name = d.pop("filterName")

        rules = cast(list[int], d.pop("rules"))

        description = d.pop("description", UNSET)

        edit_filter_entity = cls(
            filter_name=filter_name,
            rules=rules,
            description=description,
        )

        edit_filter_entity.additional_properties = d
        return edit_filter_entity

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
