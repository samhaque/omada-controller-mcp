from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueueScheduleConfigVO")


@_attrs_define
class QueueScheduleConfigVO:
    """
    Attributes:
        queue (int):
        type_ (int):
        weight (int | Unset):
    """

    queue: int
    type_: int
    weight: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        queue = self.queue

        type_ = self.type_

        weight = self.weight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "queue": queue,
                "type": type_,
            }
        )
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        queue = d.pop("queue")

        type_ = d.pop("type")

        weight = d.pop("weight", UNSET)

        queue_schedule_config_vo = cls(
            queue=queue,
            type_=type_,
            weight=weight,
        )

        queue_schedule_config_vo.additional_properties = d
        return queue_schedule_config_vo

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
