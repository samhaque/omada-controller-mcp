from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_density_item_open_api_vo import ApDensityItemOpenApiVO


T = TypeVar("T", bound="ApDensityTrendDetailOpenApiVO")


@_attrs_define
class ApDensityTrendDetailOpenApiVO:
    """The trend of ap density displayed on the WIFI Dashboard page.

    Attributes:
        ap_density_item_list (list[ApDensityItemOpenApiVO] | Unset): The trend of ap density metrics displayed on the
            WIFI Dashboard page.
    """

    ap_density_item_list: list[ApDensityItemOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_density_item_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ap_density_item_list, Unset):
            ap_density_item_list = []
            for ap_density_item_list_item_data in self.ap_density_item_list:
                ap_density_item_list_item = ap_density_item_list_item_data.to_dict()
                ap_density_item_list.append(ap_density_item_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_density_item_list is not UNSET:
            field_dict["apDensityItemList"] = ap_density_item_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_density_item_open_api_vo import (
            ApDensityItemOpenApiVO,
        )

        d = dict(src_dict)
        _ap_density_item_list = d.pop("apDensityItemList", UNSET)
        ap_density_item_list: list[ApDensityItemOpenApiVO] | Unset = UNSET
        if _ap_density_item_list is not UNSET:
            ap_density_item_list = []
            for ap_density_item_list_item_data in _ap_density_item_list:
                ap_density_item_list_item = ApDensityItemOpenApiVO.from_dict(
                    ap_density_item_list_item_data
                )

                ap_density_item_list.append(ap_density_item_list_item)

        ap_density_trend_detail_open_api_vo = cls(
            ap_density_item_list=ap_density_item_list,
        )

        ap_density_trend_detail_open_api_vo.additional_properties = d
        return ap_density_trend_detail_open_api_vo

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
