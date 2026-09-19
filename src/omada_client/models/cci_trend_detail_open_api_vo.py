from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cci_trend_item_open_api_open_api_vo import (
        CciTrendItemOpenApiOpenApiVO,
    )


T = TypeVar("T", bound="CciTrendDetailOpenApiVO")


@_attrs_define
class CciTrendDetailOpenApiVO:
    """The trend of CCI metrics displayed on the WIFI Dashboard page.

    Attributes:
        cci_trend_item_list (list[CciTrendItemOpenApiOpenApiVO] | Unset): The trend of CCI metrics displayed on the WIFI
            Dashboard page.
    """

    cci_trend_item_list: list[CciTrendItemOpenApiOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cci_trend_item_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cci_trend_item_list, Unset):
            cci_trend_item_list = []
            for cci_trend_item_list_item_data in self.cci_trend_item_list:
                cci_trend_item_list_item = cci_trend_item_list_item_data.to_dict()
                cci_trend_item_list.append(cci_trend_item_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cci_trend_item_list is not UNSET:
            field_dict["cciTrendItemList"] = cci_trend_item_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.cci_trend_item_open_api_open_api_vo import (
            CciTrendItemOpenApiOpenApiVO,
        )

        d = dict(src_dict)
        _cci_trend_item_list = d.pop("cciTrendItemList", UNSET)
        cci_trend_item_list: list[CciTrendItemOpenApiOpenApiVO] | Unset = UNSET
        if _cci_trend_item_list is not UNSET:
            cci_trend_item_list = []
            for cci_trend_item_list_item_data in _cci_trend_item_list:
                cci_trend_item_list_item = CciTrendItemOpenApiOpenApiVO.from_dict(
                    cci_trend_item_list_item_data
                )

                cci_trend_item_list.append(cci_trend_item_list_item)

        cci_trend_detail_open_api_vo = cls(
            cci_trend_item_list=cci_trend_item_list,
        )

        cci_trend_detail_open_api_vo.additional_properties = d
        return cci_trend_detail_open_api_vo

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
