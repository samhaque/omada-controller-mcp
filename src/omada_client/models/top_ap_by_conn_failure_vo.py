from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conn_failure_ap_vo import ConnFailureApVO


T = TypeVar("T", bound="TopApByConnFailureVO")


@_attrs_define
class TopApByConnFailureVO:
    """Top AP by connection failure

    Attributes:
        top_ap_2_g_fail_list (list[ConnFailureApVO] | Unset): Top AP by connection failure on 2G band
        top_ap_5_g_fail_list (list[ConnFailureApVO] | Unset): Top AP by connection failure on 5G band
        top_ap_6_g_fail_list (list[ConnFailureApVO] | Unset): Top AP by connection failure on 6G band
        need_tip (bool | Unset): Not supported by the firmware on some devices
    """

    top_ap_2_g_fail_list: list[ConnFailureApVO] | Unset = UNSET
    top_ap_5_g_fail_list: list[ConnFailureApVO] | Unset = UNSET
    top_ap_6_g_fail_list: list[ConnFailureApVO] | Unset = UNSET
    need_tip: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_ap_2_g_fail_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_2_g_fail_list, Unset):
            top_ap_2_g_fail_list = []
            for top_ap_2_g_fail_list_item_data in self.top_ap_2_g_fail_list:
                top_ap_2_g_fail_list_item = top_ap_2_g_fail_list_item_data.to_dict()
                top_ap_2_g_fail_list.append(top_ap_2_g_fail_list_item)

        top_ap_5_g_fail_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_5_g_fail_list, Unset):
            top_ap_5_g_fail_list = []
            for top_ap_5_g_fail_list_item_data in self.top_ap_5_g_fail_list:
                top_ap_5_g_fail_list_item = top_ap_5_g_fail_list_item_data.to_dict()
                top_ap_5_g_fail_list.append(top_ap_5_g_fail_list_item)

        top_ap_6_g_fail_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.top_ap_6_g_fail_list, Unset):
            top_ap_6_g_fail_list = []
            for top_ap_6_g_fail_list_item_data in self.top_ap_6_g_fail_list:
                top_ap_6_g_fail_list_item = top_ap_6_g_fail_list_item_data.to_dict()
                top_ap_6_g_fail_list.append(top_ap_6_g_fail_list_item)

        need_tip = self.need_tip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if top_ap_2_g_fail_list is not UNSET:
            field_dict["topAp2gFailList"] = top_ap_2_g_fail_list
        if top_ap_5_g_fail_list is not UNSET:
            field_dict["topAp5gFailList"] = top_ap_5_g_fail_list
        if top_ap_6_g_fail_list is not UNSET:
            field_dict["topAp6gFailList"] = top_ap_6_g_fail_list
        if need_tip is not UNSET:
            field_dict["needTip"] = need_tip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.conn_failure_ap_vo import ConnFailureApVO

        d = dict(src_dict)
        _top_ap_2_g_fail_list = d.pop("topAp2gFailList", UNSET)
        top_ap_2_g_fail_list: list[ConnFailureApVO] | Unset = UNSET
        if _top_ap_2_g_fail_list is not UNSET:
            top_ap_2_g_fail_list = []
            for top_ap_2_g_fail_list_item_data in _top_ap_2_g_fail_list:
                top_ap_2_g_fail_list_item = ConnFailureApVO.from_dict(
                    top_ap_2_g_fail_list_item_data
                )

                top_ap_2_g_fail_list.append(top_ap_2_g_fail_list_item)

        _top_ap_5_g_fail_list = d.pop("topAp5gFailList", UNSET)
        top_ap_5_g_fail_list: list[ConnFailureApVO] | Unset = UNSET
        if _top_ap_5_g_fail_list is not UNSET:
            top_ap_5_g_fail_list = []
            for top_ap_5_g_fail_list_item_data in _top_ap_5_g_fail_list:
                top_ap_5_g_fail_list_item = ConnFailureApVO.from_dict(
                    top_ap_5_g_fail_list_item_data
                )

                top_ap_5_g_fail_list.append(top_ap_5_g_fail_list_item)

        _top_ap_6_g_fail_list = d.pop("topAp6gFailList", UNSET)
        top_ap_6_g_fail_list: list[ConnFailureApVO] | Unset = UNSET
        if _top_ap_6_g_fail_list is not UNSET:
            top_ap_6_g_fail_list = []
            for top_ap_6_g_fail_list_item_data in _top_ap_6_g_fail_list:
                top_ap_6_g_fail_list_item = ConnFailureApVO.from_dict(
                    top_ap_6_g_fail_list_item_data
                )

                top_ap_6_g_fail_list.append(top_ap_6_g_fail_list_item)

        need_tip = d.pop("needTip", UNSET)

        top_ap_by_conn_failure_vo = cls(
            top_ap_2_g_fail_list=top_ap_2_g_fail_list,
            top_ap_5_g_fail_list=top_ap_5_g_fail_list,
            top_ap_6_g_fail_list=top_ap_6_g_fail_list,
            need_tip=need_tip,
        )

        top_ap_by_conn_failure_vo.additional_properties = d
        return top_ap_by_conn_failure_vo

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
