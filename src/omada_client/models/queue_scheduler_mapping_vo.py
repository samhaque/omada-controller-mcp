from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.queue_schedule_config_vo import QueueScheduleConfigVO


T = TypeVar("T", bound="QueueSchedulerMappingVO")


@_attrs_define
class QueueSchedulerMappingVO:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        types (int | Unset):
        mapping (list[QueueScheduleConfigVO] | Unset):
        build_in (bool | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    types: int | Unset = UNSET
    mapping: list[QueueScheduleConfigVO] | Unset = UNSET
    build_in: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        types = self.types

        mapping: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mapping, Unset):
            mapping = []
            for mapping_item_data in self.mapping:
                mapping_item = mapping_item_data.to_dict()
                mapping.append(mapping_item)

        build_in = self.build_in

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if types is not UNSET:
            field_dict["types"] = types
        if mapping is not UNSET:
            field_dict["mapping"] = mapping
        if build_in is not UNSET:
            field_dict["buildIn"] = build_in

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.queue_schedule_config_vo import (
            QueueScheduleConfigVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        types = d.pop("types", UNSET)

        _mapping = d.pop("mapping", UNSET)
        mapping: list[QueueScheduleConfigVO] | Unset = UNSET
        if _mapping is not UNSET:
            mapping = []
            for mapping_item_data in _mapping:
                mapping_item = QueueScheduleConfigVO.from_dict(mapping_item_data)

                mapping.append(mapping_item)

        build_in = d.pop("buildIn", UNSET)

        queue_scheduler_mapping_vo = cls(
            id=id,
            name=name,
            types=types,
            mapping=mapping,
            build_in=build_in,
        )

        queue_scheduler_mapping_vo.additional_properties = d
        return queue_scheduler_mapping_vo

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
