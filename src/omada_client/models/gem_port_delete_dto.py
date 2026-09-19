from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GemPortDeleteDTO")


@_attrs_define
class GemPortDeleteDTO:
    """
    Attributes:
        ids (list[int]): ID list
        line_profile_id (int | Unset): The ID of the associated Line Profile,lineProfile should be within the range of 1
            to 512.
    """

    ids: list[int]
    line_profile_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        line_profile_id = self.line_profile_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
            }
        )
        if line_profile_id is not UNSET:
            field_dict["lineProfileId"] = line_profile_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ids = cast(list[int], d.pop("ids"))

        line_profile_id = d.pop("lineProfileId", UNSET)

        gem_port_delete_dto = cls(
            ids=ids,
            line_profile_id=line_profile_id,
        )

        gem_port_delete_dto.additional_properties = d
        return gem_port_delete_dto

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
