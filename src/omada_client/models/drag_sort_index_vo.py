from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.drag_sort_index_vo_indexes import DragSortIndexVOIndexes


T = TypeVar("T", bound="DragSortIndexVO")


@_attrs_define
class DragSortIndexVO:
    """
    Attributes:
        indexes (DragSortIndexVOIndexes): DragSort indexes. The key corresponds to the rule id and the value corresponds
            to the new index value.
        type_ (str | Unset):
        omadac_id (str | Unset):
        site_id (str | Unset):
    """

    indexes: DragSortIndexVOIndexes
    type_: str | Unset = UNSET
    omadac_id: str | Unset = UNSET
    site_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        indexes = self.indexes.to_dict()

        type_ = self.type_

        omadac_id = self.omadac_id

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "indexes": indexes,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if omadac_id is not UNSET:
            field_dict["omadacId"] = omadac_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.drag_sort_index_vo_indexes import (
            DragSortIndexVOIndexes,
        )

        d = dict(src_dict)
        indexes = DragSortIndexVOIndexes.from_dict(d.pop("indexes"))

        type_ = d.pop("type", UNSET)

        omadac_id = d.pop("omadacId", UNSET)

        site_id = d.pop("siteId", UNSET)

        drag_sort_index_vo = cls(
            indexes=indexes,
            type_=type_,
            omadac_id=omadac_id,
            site_id=site_id,
        )

        drag_sort_index_vo.additional_properties = d
        return drag_sort_index_vo

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
