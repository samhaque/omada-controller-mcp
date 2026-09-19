from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_interference_vo import ApInterferenceVO


T = TypeVar("T", bound="TopApByInterferenceVO")


@_attrs_define
class TopApByInterferenceVO:
    """
    Attributes:
        top_ap_2_g_inter_list (list[ApInterferenceVO] | Unset):
        top_ap_5_g_inter_list (list[ApInterferenceVO] | Unset):
        top_ap_6_g_inter_list (list[ApInterferenceVO] | Unset):
    """

    top_ap_2_g_inter_list: list[ApInterferenceVO] | Unset = UNSET
    top_ap_5_g_inter_list: list[ApInterferenceVO] | Unset = UNSET
    top_ap_6_g_inter_list: list[ApInterferenceVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_ap_2_g_inter_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_2_g_inter_list, Unset):
            top_ap_2_g_inter_list = []
            for top_ap_2_g_inter_list_item_data in self.top_ap_2_g_inter_list:
                top_ap_2_g_inter_list_item = top_ap_2_g_inter_list_item_data.to_dict()
                top_ap_2_g_inter_list.append(top_ap_2_g_inter_list_item)

        top_ap_5_g_inter_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_5_g_inter_list, Unset):
            top_ap_5_g_inter_list = []
            for top_ap_5_g_inter_list_item_data in self.top_ap_5_g_inter_list:
                top_ap_5_g_inter_list_item = top_ap_5_g_inter_list_item_data.to_dict()
                top_ap_5_g_inter_list.append(top_ap_5_g_inter_list_item)

        top_ap_6_g_inter_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_6_g_inter_list, Unset):
            top_ap_6_g_inter_list = []
            for top_ap_6_g_inter_list_item_data in self.top_ap_6_g_inter_list:
                top_ap_6_g_inter_list_item = top_ap_6_g_inter_list_item_data.to_dict()
                top_ap_6_g_inter_list.append(top_ap_6_g_inter_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_ap_2_g_inter_list is not UNSET:
            field_dict["topAp2gInterList"] = top_ap_2_g_inter_list
        if top_ap_5_g_inter_list is not UNSET:
            field_dict["topAp5gInterList"] = top_ap_5_g_inter_list
        if top_ap_6_g_inter_list is not UNSET:
            field_dict["topAp6gInterList"] = top_ap_6_g_inter_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_interference_vo import ApInterferenceVO

        d = dict(src_dict)
        _top_ap_2_g_inter_list = d.pop("topAp2gInterList", UNSET)
        top_ap_2_g_inter_list: list[ApInterferenceVO] | Unset = UNSET
        if _top_ap_2_g_inter_list is not UNSET:
            top_ap_2_g_inter_list = []
            for top_ap_2_g_inter_list_item_data in _top_ap_2_g_inter_list:
                top_ap_2_g_inter_list_item = ApInterferenceVO.from_dict(
                    top_ap_2_g_inter_list_item_data
                )

                top_ap_2_g_inter_list.append(top_ap_2_g_inter_list_item)

        _top_ap_5_g_inter_list = d.pop("topAp5gInterList", UNSET)
        top_ap_5_g_inter_list: list[ApInterferenceVO] | Unset = UNSET
        if _top_ap_5_g_inter_list is not UNSET:
            top_ap_5_g_inter_list = []
            for top_ap_5_g_inter_list_item_data in _top_ap_5_g_inter_list:
                top_ap_5_g_inter_list_item = ApInterferenceVO.from_dict(
                    top_ap_5_g_inter_list_item_data
                )

                top_ap_5_g_inter_list.append(top_ap_5_g_inter_list_item)

        _top_ap_6_g_inter_list = d.pop("topAp6gInterList", UNSET)
        top_ap_6_g_inter_list: list[ApInterferenceVO] | Unset = UNSET
        if _top_ap_6_g_inter_list is not UNSET:
            top_ap_6_g_inter_list = []
            for top_ap_6_g_inter_list_item_data in _top_ap_6_g_inter_list:
                top_ap_6_g_inter_list_item = ApInterferenceVO.from_dict(
                    top_ap_6_g_inter_list_item_data
                )

                top_ap_6_g_inter_list.append(top_ap_6_g_inter_list_item)

        top_ap_by_interference_vo = cls(
            top_ap_2_g_inter_list=top_ap_2_g_inter_list,
            top_ap_5_g_inter_list=top_ap_5_g_inter_list,
            top_ap_6_g_inter_list=top_ap_6_g_inter_list,
        )

        top_ap_by_interference_vo.additional_properties = d
        return top_ap_by_interference_vo

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
