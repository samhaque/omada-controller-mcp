from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_detail_cci_info_open_api_open_api_vo import (
        ApDetailCciInfoOpenApiOpenApiVO,
    )
    from ..models.base_ap_info_open_api_vo import BaseApInfoOpenApiVO


T = TypeVar("T", bound="CciCurrentDetailOpenApiVO")


@_attrs_define
class CciCurrentDetailOpenApiVO:
    """The current detail of CCI metrics displayed on the WIFI Dashboard page.

    Attributes:
        current_high_cci_info_list (list[ApDetailCciInfoOpenApiOpenApiVO] | Unset): The current detail of high CCI
            metrics displayed on the WIFI Dashboard page.
        current_medium_cci_info_list (list[ApDetailCciInfoOpenApiOpenApiVO] | Unset): The current detail of medium CCI
            metrics displayed on the WIFI Dashboard page.
        current_low_cci_info_list (list[ApDetailCciInfoOpenApiOpenApiVO] | Unset): The current detail of low CCI metrics
            displayed on the WIFI Dashboard page.
        no_data_list (list[BaseApInfoOpenApiVO] | Unset): The current detail of no CCI metrics displayed on the WIFI
            Dashboard page.
    """

    current_high_cci_info_list: list[ApDetailCciInfoOpenApiOpenApiVO] | Unset = UNSET
    current_medium_cci_info_list: list[ApDetailCciInfoOpenApiOpenApiVO] | Unset = UNSET
    current_low_cci_info_list: list[ApDetailCciInfoOpenApiOpenApiVO] | Unset = UNSET
    no_data_list: list[BaseApInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_high_cci_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_high_cci_info_list, Unset):
            current_high_cci_info_list = []
            for current_high_cci_info_list_item_data in self.current_high_cci_info_list:
                current_high_cci_info_list_item = (
                    current_high_cci_info_list_item_data.to_dict()
                )
                current_high_cci_info_list.append(current_high_cci_info_list_item)

        current_medium_cci_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_medium_cci_info_list, Unset):
            current_medium_cci_info_list = []
            for (
                current_medium_cci_info_list_item_data
            ) in self.current_medium_cci_info_list:
                current_medium_cci_info_list_item = (
                    current_medium_cci_info_list_item_data.to_dict()
                )
                current_medium_cci_info_list.append(current_medium_cci_info_list_item)

        current_low_cci_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_low_cci_info_list, Unset):
            current_low_cci_info_list = []
            for current_low_cci_info_list_item_data in self.current_low_cci_info_list:
                current_low_cci_info_list_item = (
                    current_low_cci_info_list_item_data.to_dict()
                )
                current_low_cci_info_list.append(current_low_cci_info_list_item)

        no_data_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.no_data_list, Unset):
            no_data_list = []
            for no_data_list_item_data in self.no_data_list:
                no_data_list_item = no_data_list_item_data.to_dict()
                no_data_list.append(no_data_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_high_cci_info_list is not UNSET:
            field_dict["currentHighCciInfoList"] = current_high_cci_info_list
        if current_medium_cci_info_list is not UNSET:
            field_dict["currentMediumCciInfoList"] = current_medium_cci_info_list
        if current_low_cci_info_list is not UNSET:
            field_dict["currentLowCciInfoList"] = current_low_cci_info_list
        if no_data_list is not UNSET:
            field_dict["noDataList"] = no_data_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_detail_cci_info_open_api_open_api_vo import (
            ApDetailCciInfoOpenApiOpenApiVO,
        )
        from ..models.base_ap_info_open_api_vo import (
            BaseApInfoOpenApiVO,
        )

        d = dict(src_dict)
        _current_high_cci_info_list = d.pop("currentHighCciInfoList", UNSET)
        current_high_cci_info_list: list[ApDetailCciInfoOpenApiOpenApiVO] | Unset = (
            UNSET
        )
        if _current_high_cci_info_list is not UNSET:
            current_high_cci_info_list = []
            for current_high_cci_info_list_item_data in _current_high_cci_info_list:
                current_high_cci_info_list_item = (
                    ApDetailCciInfoOpenApiOpenApiVO.from_dict(
                        current_high_cci_info_list_item_data
                    )
                )

                current_high_cci_info_list.append(current_high_cci_info_list_item)

        _current_medium_cci_info_list = d.pop("currentMediumCciInfoList", UNSET)
        current_medium_cci_info_list: list[ApDetailCciInfoOpenApiOpenApiVO] | Unset = (
            UNSET
        )
        if _current_medium_cci_info_list is not UNSET:
            current_medium_cci_info_list = []
            for current_medium_cci_info_list_item_data in _current_medium_cci_info_list:
                current_medium_cci_info_list_item = (
                    ApDetailCciInfoOpenApiOpenApiVO.from_dict(
                        current_medium_cci_info_list_item_data
                    )
                )

                current_medium_cci_info_list.append(current_medium_cci_info_list_item)

        _current_low_cci_info_list = d.pop("currentLowCciInfoList", UNSET)
        current_low_cci_info_list: list[ApDetailCciInfoOpenApiOpenApiVO] | Unset = UNSET
        if _current_low_cci_info_list is not UNSET:
            current_low_cci_info_list = []
            for current_low_cci_info_list_item_data in _current_low_cci_info_list:
                current_low_cci_info_list_item = (
                    ApDetailCciInfoOpenApiOpenApiVO.from_dict(
                        current_low_cci_info_list_item_data
                    )
                )

                current_low_cci_info_list.append(current_low_cci_info_list_item)

        _no_data_list = d.pop("noDataList", UNSET)
        no_data_list: list[BaseApInfoOpenApiVO] | Unset = UNSET
        if _no_data_list is not UNSET:
            no_data_list = []
            for no_data_list_item_data in _no_data_list:
                no_data_list_item = BaseApInfoOpenApiVO.from_dict(
                    no_data_list_item_data
                )

                no_data_list.append(no_data_list_item)

        cci_current_detail_open_api_vo = cls(
            current_high_cci_info_list=current_high_cci_info_list,
            current_medium_cci_info_list=current_medium_cci_info_list,
            current_low_cci_info_list=current_low_cci_info_list,
            no_data_list=no_data_list,
        )

        cci_current_detail_open_api_vo.additional_properties = d
        return cci_current_detail_open_api_vo

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
