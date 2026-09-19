from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.planning_history_list_vo_history_list_item import (
        PlanningHistoryListVOHistoryListItem,
    )


T = TypeVar("T", bound="PlanningHistoryListVO")


@_attrs_define
class PlanningHistoryListVO:
    """
    Attributes:
        history_list (list[PlanningHistoryListVOHistoryListItem] | Unset):
    """

    history_list: list[PlanningHistoryListVOHistoryListItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.history_list, Unset):
            history_list = []
            for history_list_item_data in self.history_list:
                history_list_item = history_list_item_data.to_dict()
                history_list.append(history_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if history_list is not UNSET:
            field_dict["historyList"] = history_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.planning_history_list_vo_history_list_item import (
            PlanningHistoryListVOHistoryListItem,
        )

        d = dict(src_dict)
        _history_list = d.pop("historyList", UNSET)
        history_list: list[PlanningHistoryListVOHistoryListItem] | Unset = UNSET
        if _history_list is not UNSET:
            history_list = []
            for history_list_item_data in _history_list:
                history_list_item = PlanningHistoryListVOHistoryListItem.from_dict(
                    history_list_item_data
                )

                history_list.append(history_list_item)

        planning_history_list_vo = cls(
            history_list=history_list,
        )

        planning_history_list_vo.additional_properties = d
        return planning_history_list_vo

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
