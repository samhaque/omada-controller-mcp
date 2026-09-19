from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.batch_update_tab import BatchUpdateTab


T = TypeVar("T", bound="BatchEditTabs")


@_attrs_define
class BatchEditTabs:
    """
    Attributes:
        tabs (list[BatchUpdateTab] | Unset): Edit Tab Parameters
    """

    tabs: list[BatchUpdateTab] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tabs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tabs, Unset):
            tabs = []
            for tabs_item_data in self.tabs:
                tabs_item = tabs_item_data.to_dict()
                tabs.append(tabs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tabs is not UNSET:
            field_dict["tabs"] = tabs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.batch_update_tab import BatchUpdateTab

        d = dict(src_dict)
        _tabs = d.pop("tabs", UNSET)
        tabs: list[BatchUpdateTab] | Unset = UNSET
        if _tabs is not UNSET:
            tabs = []
            for tabs_item_data in _tabs:
                tabs_item = BatchUpdateTab.from_dict(tabs_item_data)

                tabs.append(tabs_item)

        batch_edit_tabs = cls(
            tabs=tabs,
        )

        batch_edit_tabs.additional_properties = d
        return batch_edit_tabs

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
