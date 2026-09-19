from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_density_info_open_api_vo import ApDensityInfoOpenApiVO
    from ..models.base_ap_info_open_api_vo import BaseApInfoOpenApiVO


T = TypeVar("T", bound="ApDensityCurrentDetailOpenApiVO")


@_attrs_define
class ApDensityCurrentDetailOpenApiVO:
    """The current detail of ap density displayed on the WIFI Dashboard page.

    Attributes:
        current_ap_density_high_info (list[ApDensityInfoOpenApiVO] | Unset): The current detail of high ap density
            metrics displayed on the WIFI Dashboard page.
        current_ap_density_medium_info (list[ApDensityInfoOpenApiVO] | Unset): The current detail of medium ap density
            metrics displayed on the WIFI Dashboard page.
        current_ap_density_low_info (list[ApDensityInfoOpenApiVO] | Unset): The current detail of low ap density metrics
            displayed on the WIFI Dashboard page.
        no_data_list (list[BaseApInfoOpenApiVO] | Unset): The current detail of no ap density metrics displayed on the
            WIFI Dashboard page.
    """

    current_ap_density_high_info: list[ApDensityInfoOpenApiVO] | Unset = UNSET
    current_ap_density_medium_info: list[ApDensityInfoOpenApiVO] | Unset = UNSET
    current_ap_density_low_info: list[ApDensityInfoOpenApiVO] | Unset = UNSET
    no_data_list: list[BaseApInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_ap_density_high_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_ap_density_high_info, Unset):
            current_ap_density_high_info = []
            for (
                current_ap_density_high_info_item_data
            ) in self.current_ap_density_high_info:
                current_ap_density_high_info_item = (
                    current_ap_density_high_info_item_data.to_dict()
                )
                current_ap_density_high_info.append(current_ap_density_high_info_item)

        current_ap_density_medium_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_ap_density_medium_info, Unset):
            current_ap_density_medium_info = []
            for (
                current_ap_density_medium_info_item_data
            ) in self.current_ap_density_medium_info:
                current_ap_density_medium_info_item = (
                    current_ap_density_medium_info_item_data.to_dict()
                )
                current_ap_density_medium_info.append(
                    current_ap_density_medium_info_item
                )

        current_ap_density_low_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.current_ap_density_low_info, Unset):
            current_ap_density_low_info = []
            for (
                current_ap_density_low_info_item_data
            ) in self.current_ap_density_low_info:
                current_ap_density_low_info_item = (
                    current_ap_density_low_info_item_data.to_dict()
                )
                current_ap_density_low_info.append(current_ap_density_low_info_item)

        no_data_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.no_data_list, Unset):
            no_data_list = []
            for no_data_list_item_data in self.no_data_list:
                no_data_list_item = no_data_list_item_data.to_dict()
                no_data_list.append(no_data_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_ap_density_high_info is not UNSET:
            field_dict["currentApDensityHighInfo"] = current_ap_density_high_info
        if current_ap_density_medium_info is not UNSET:
            field_dict["currentApDensityMediumInfo"] = current_ap_density_medium_info
        if current_ap_density_low_info is not UNSET:
            field_dict["currentApDensityLowInfo"] = current_ap_density_low_info
        if no_data_list is not UNSET:
            field_dict["noDataList"] = no_data_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_density_info_open_api_vo import (
            ApDensityInfoOpenApiVO,
        )
        from ..models.base_ap_info_open_api_vo import (
            BaseApInfoOpenApiVO,
        )

        d = dict(src_dict)
        _current_ap_density_high_info = d.pop("currentApDensityHighInfo", UNSET)
        current_ap_density_high_info: list[ApDensityInfoOpenApiVO] | Unset = UNSET
        if _current_ap_density_high_info is not UNSET:
            current_ap_density_high_info = []
            for current_ap_density_high_info_item_data in _current_ap_density_high_info:
                current_ap_density_high_info_item = ApDensityInfoOpenApiVO.from_dict(
                    current_ap_density_high_info_item_data
                )

                current_ap_density_high_info.append(current_ap_density_high_info_item)

        _current_ap_density_medium_info = d.pop("currentApDensityMediumInfo", UNSET)
        current_ap_density_medium_info: list[ApDensityInfoOpenApiVO] | Unset = UNSET
        if _current_ap_density_medium_info is not UNSET:
            current_ap_density_medium_info = []
            for (
                current_ap_density_medium_info_item_data
            ) in _current_ap_density_medium_info:
                current_ap_density_medium_info_item = ApDensityInfoOpenApiVO.from_dict(
                    current_ap_density_medium_info_item_data
                )

                current_ap_density_medium_info.append(
                    current_ap_density_medium_info_item
                )

        _current_ap_density_low_info = d.pop("currentApDensityLowInfo", UNSET)
        current_ap_density_low_info: list[ApDensityInfoOpenApiVO] | Unset = UNSET
        if _current_ap_density_low_info is not UNSET:
            current_ap_density_low_info = []
            for current_ap_density_low_info_item_data in _current_ap_density_low_info:
                current_ap_density_low_info_item = ApDensityInfoOpenApiVO.from_dict(
                    current_ap_density_low_info_item_data
                )

                current_ap_density_low_info.append(current_ap_density_low_info_item)

        _no_data_list = d.pop("noDataList", UNSET)
        no_data_list: list[BaseApInfoOpenApiVO] | Unset = UNSET
        if _no_data_list is not UNSET:
            no_data_list = []
            for no_data_list_item_data in _no_data_list:
                no_data_list_item = BaseApInfoOpenApiVO.from_dict(
                    no_data_list_item_data
                )

                no_data_list.append(no_data_list_item)

        ap_density_current_detail_open_api_vo = cls(
            current_ap_density_high_info=current_ap_density_high_info,
            current_ap_density_medium_info=current_ap_density_medium_info,
            current_ap_density_low_info=current_ap_density_low_info,
            no_data_list=no_data_list,
        )

        ap_density_current_detail_open_api_vo.additional_properties = d
        return ap_density_current_detail_open_api_vo

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
