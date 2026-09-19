from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_group_open_api_vo import ApGroupOpenApiVO


T = TypeVar("T", bound="ApGroupGridVOApGroupOpenApiVO")


@_attrs_define
class ApGroupGridVOApGroupOpenApiVO:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[ApGroupOpenApiVO] | Unset):
        max_ssids_2g (int | Unset): 2G radio max Ssid number in group
        max_ssids_5g (int | Unset): 5G radio max Ssid number in group
        max_ssids_6g (int | Unset): 6G radio max Ssid number in group
        max_ssids_mlo (int | Unset): max Mlo Ssid number in group
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[ApGroupOpenApiVO] | Unset = UNSET
    max_ssids_2g: int | Unset = UNSET
    max_ssids_5g: int | Unset = UNSET
    max_ssids_6g: int | Unset = UNSET
    max_ssids_mlo: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_rows = self.total_rows

        current_page = self.current_page

        current_size = self.current_size

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        max_ssids_2g = self.max_ssids_2g

        max_ssids_5g = self.max_ssids_5g

        max_ssids_6g = self.max_ssids_6g

        max_ssids_mlo = self.max_ssids_mlo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_size is not UNSET:
            field_dict["currentSize"] = current_size
        if data is not UNSET:
            field_dict["data"] = data
        if max_ssids_2g is not UNSET:
            field_dict["maxSsids2G"] = max_ssids_2g
        if max_ssids_5g is not UNSET:
            field_dict["maxSsids5G"] = max_ssids_5g
        if max_ssids_6g is not UNSET:
            field_dict["maxSsids6G"] = max_ssids_6g
        if max_ssids_mlo is not UNSET:
            field_dict["maxSsidsMlo"] = max_ssids_mlo

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_group_open_api_vo import ApGroupOpenApiVO

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[ApGroupOpenApiVO] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ApGroupOpenApiVO.from_dict(data_item_data)

                data.append(data_item)

        max_ssids_2g = d.pop("maxSsids2G", UNSET)

        max_ssids_5g = d.pop("maxSsids5G", UNSET)

        max_ssids_6g = d.pop("maxSsids6G", UNSET)

        max_ssids_mlo = d.pop("maxSsidsMlo", UNSET)

        ap_group_grid_vo_ap_group_open_api_vo = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            max_ssids_2g=max_ssids_2g,
            max_ssids_5g=max_ssids_5g,
            max_ssids_6g=max_ssids_6g,
            max_ssids_mlo=max_ssids_mlo,
        )

        ap_group_grid_vo_ap_group_open_api_vo.additional_properties = d
        return ap_group_grid_vo_ap_group_open_api_vo

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
