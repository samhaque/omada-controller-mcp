from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_upgrade_info import ModelUpgradeInfo


T = TypeVar("T", bound="PlanUpgradeModelInfo")


@_attrs_define
class PlanUpgradeModelInfo:
    """
    Attributes:
        model_list (list[ModelUpgradeInfo] | Unset):
    """

    model_list: list[ModelUpgradeInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.model_list, Unset):
            model_list = []
            for model_list_item_data in self.model_list:
                model_list_item = model_list_item_data.to_dict()
                model_list.append(model_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if model_list is not UNSET:
            field_dict["modelList"] = model_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_upgrade_info import ModelUpgradeInfo

        d = dict(src_dict)
        _model_list = d.pop("modelList", UNSET)
        model_list: list[ModelUpgradeInfo] | Unset = UNSET
        if _model_list is not UNSET:
            model_list = []
            for model_list_item_data in _model_list:
                model_list_item = ModelUpgradeInfo.from_dict(model_list_item_data)

                model_list.append(model_list_item)

        plan_upgrade_model_info = cls(
            model_list=model_list,
        )

        plan_upgrade_model_info.additional_properties = d
        return plan_upgrade_model_info

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
