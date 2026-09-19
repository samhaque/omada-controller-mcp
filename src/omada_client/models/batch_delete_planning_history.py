from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchDeletePlanningHistory")


@_attrs_define
class BatchDeletePlanningHistory:
    """
    Attributes:
        type_ (str | Unset): Delete policy, all: delete all history, include: delete history in ids, exclude: exclude
            history in ids.
        ids (list[str] | Unset): HistoryId list
        start (int | Unset): Start time of the history to be deleted(millisecond timestamp)
        end (int | Unset): End time of the history to be deleted(millisecond timestamp)
        filter_mode (int | Unset): filtermode should be a value as follows: 1: rfPlanningHistory mode is manual;
            2:rfPlanningHistory mode is adaptive
    """

    type_: str | Unset = UNSET
    ids: list[str] | Unset = UNSET
    start: int | Unset = UNSET
    end: int | Unset = UNSET
    filter_mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        start = self.start

        end = self.end

        filter_mode = self.filter_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ids is not UNSET:
            field_dict["ids"] = ids
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if filter_mode is not UNSET:
            field_dict["filter_mode"] = filter_mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        ids = cast(list[str], d.pop("ids", UNSET))

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        filter_mode = d.pop("filter_mode", UNSET)

        batch_delete_planning_history = cls(
            type_=type_,
            ids=ids,
            start=start,
            end=end,
            filter_mode=filter_mode,
        )

        batch_delete_planning_history.additional_properties = d
        return batch_delete_planning_history

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
