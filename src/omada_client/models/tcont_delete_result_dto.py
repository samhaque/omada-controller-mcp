from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TcontDeleteResultDTO")


@_attrs_define
class TcontDeleteResultDTO:
    """Device configuration information.If the type of data is 'Object',ignore this field

    Attributes:
        tconts_in_use (list[int] | Unset):  List of T-cont IDs that failed to delete because they are in use.
    """

    tconts_in_use: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tconts_in_use: list[int] | Unset = UNSET
        if not isinstance(self.tconts_in_use, Unset):
            tconts_in_use = self.tconts_in_use

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tconts_in_use is not UNSET:
            field_dict["tcontsInUse"] = tconts_in_use

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tconts_in_use = cast(list[int], d.pop("tcontsInUse", UNSET))

        tcont_delete_result_dto = cls(
            tconts_in_use=tconts_in_use,
        )

        tcont_delete_result_dto.additional_properties = d
        return tcont_delete_result_dto

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
