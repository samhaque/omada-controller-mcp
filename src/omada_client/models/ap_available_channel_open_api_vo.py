from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_channel_detail_open_api_vo import ApChannelDetailOpenApiVO


T = TypeVar("T", bound="ApAvailableChannelOpenApiVO")


@_attrs_define
class ApAvailableChannelOpenApiVO:
    """
    Attributes:
        radio_id (int | Unset): (Wireless) Radio ID should be a value as follows: 0: 2.4GHz; 1: 5GHz-1; 2: 5GHz-2; 3:
            6GHz.
        ap_channel_detail_list (list[ApChannelDetailOpenApiVO] | Unset): channels detail supported by device
            configuration.
    """

    radio_id: int | Unset = UNSET
    ap_channel_detail_list: list[ApChannelDetailOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id = self.radio_id

        ap_channel_detail_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ap_channel_detail_list, Unset):
            ap_channel_detail_list = []
            for ap_channel_detail_list_item_data in self.ap_channel_detail_list:
                ap_channel_detail_list_item = ap_channel_detail_list_item_data.to_dict()
                ap_channel_detail_list.append(ap_channel_detail_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id is not UNSET:
            field_dict["radioId"] = radio_id
        if ap_channel_detail_list is not UNSET:
            field_dict["apChannelDetailList"] = ap_channel_detail_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_channel_detail_open_api_vo import (
            ApChannelDetailOpenApiVO,
        )

        d = dict(src_dict)
        radio_id = d.pop("radioId", UNSET)

        _ap_channel_detail_list = d.pop("apChannelDetailList", UNSET)
        ap_channel_detail_list: list[ApChannelDetailOpenApiVO] | Unset = UNSET
        if _ap_channel_detail_list is not UNSET:
            ap_channel_detail_list = []
            for ap_channel_detail_list_item_data in _ap_channel_detail_list:
                ap_channel_detail_list_item = ApChannelDetailOpenApiVO.from_dict(
                    ap_channel_detail_list_item_data
                )

                ap_channel_detail_list.append(ap_channel_detail_list_item)

        ap_available_channel_open_api_vo = cls(
            radio_id=radio_id,
            ap_channel_detail_list=ap_channel_detail_list,
        )

        ap_available_channel_open_api_vo.additional_properties = d
        return ap_available_channel_open_api_vo

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
