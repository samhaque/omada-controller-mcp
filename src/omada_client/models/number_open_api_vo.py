from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NumberOpenApiVO")


@_attrs_define
class NumberOpenApiVO:
    """Telephone numbers.

    Attributes:
        telephone_number_id (str | Unset): telephone number id
        telephone_number (str | Unset): telephone number
    """

    telephone_number_id: str | Unset = UNSET
    telephone_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        telephone_number_id = self.telephone_number_id

        telephone_number = self.telephone_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if telephone_number_id is not UNSET:
            field_dict["telephone number id"] = telephone_number_id
        if telephone_number is not UNSET:
            field_dict["telephone number"] = telephone_number

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        telephone_number_id = d.pop("telephone number id", UNSET)

        telephone_number = d.pop("telephone number", UNSET)

        number_open_api_vo = cls(
            telephone_number_id=telephone_number_id,
            telephone_number=telephone_number,
        )

        number_open_api_vo.additional_properties = d
        return number_open_api_vo

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
