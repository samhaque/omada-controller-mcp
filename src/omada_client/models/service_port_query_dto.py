from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.c import C


T = TypeVar("T", bound="ServicePortQueryDTO")


@_attrs_define
class ServicePortQueryDTO:
    """
    Attributes:
        search_key (str | Unset): Query conditions.
        sorts (list[C] | Unset): Sorting fields.
        size (int | Unset): Page size must be greater or equal to 1,with the default value of 10.
        number (int | Unset): Current page number must be greater or equal to 0, with a default value of 0.
        search_field (str | Unset): Search Field
    """

    search_key: str | Unset = UNSET
    sorts: list[C] | Unset = UNSET
    size: int | Unset = UNSET
    number: int | Unset = UNSET
    search_field: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_key = self.search_key

        sorts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = []
            for sorts_item_data in self.sorts:
                sorts_item = sorts_item_data.to_dict()
                sorts.append(sorts_item)

        size = self.size

        number = self.number

        search_field = self.search_field

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if size is not UNSET:
            field_dict["size"] = size
        if number is not UNSET:
            field_dict["number"] = number
        if search_field is not UNSET:
            field_dict["searchField"] = search_field

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.c import C

        d = dict(src_dict)
        search_key = d.pop("searchKey", UNSET)

        _sorts = d.pop("sorts", UNSET)
        sorts: list[C] | Unset = UNSET
        if _sorts is not UNSET:
            sorts = []
            for sorts_item_data in _sorts:
                sorts_item = C.from_dict(sorts_item_data)

                sorts.append(sorts_item)

        size = d.pop("size", UNSET)

        number = d.pop("number", UNSET)

        search_field = d.pop("searchField", UNSET)

        service_port_query_dto = cls(
            search_key=search_key,
            sorts=sorts,
            size=size,
            number=number,
            search_field=search_field,
        )

        service_port_query_dto.additional_properties = d
        return service_port_query_dto

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
