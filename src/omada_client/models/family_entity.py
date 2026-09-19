from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="FamilyEntity")


@_attrs_define
class FamilyEntity:
    """
    Attributes:
        family_name (str | Unset): Family name
        family_id (int | Unset): Family ID
        description (str | Unset): Description of family
    """

    family_name: str | Unset = UNSET
    family_id: int | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        family_name = self.family_name

        family_id = self.family_id

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if family_id is not UNSET:
            field_dict["familyId"] = family_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        family_name = d.pop("familyName", UNSET)

        family_id = d.pop("familyId", UNSET)

        description = d.pop("description", UNSET)

        family_entity = cls(
            family_name=family_name,
            family_id=family_id,
            description=description,
        )

        family_entity.additional_properties = d
        return family_entity

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
