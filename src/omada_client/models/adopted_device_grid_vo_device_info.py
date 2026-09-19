from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_info import DeviceInfo
    from ..models.osw_mlag_data_vo_device_info import OswMlagDataVODeviceInfo
    from ..models.osw_stack_data_vo_device_info import OswStackDataVODeviceInfo


T = TypeVar("T", bound="AdoptedDeviceGridVODeviceInfo")


@_attrs_define
class AdoptedDeviceGridVODeviceInfo:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[DeviceInfo] | Unset):
        stack_data (list[OswStackDataVODeviceInfo] | Unset):
        mlag_data (list[OswMlagDataVODeviceInfo] | Unset):
        p_2_p_group_total_rows (int | Unset):
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[DeviceInfo] | Unset = UNSET
    stack_data: list[OswStackDataVODeviceInfo] | Unset = UNSET
    mlag_data: list[OswMlagDataVODeviceInfo] | Unset = UNSET
    p_2_p_group_total_rows: int | Unset = UNSET
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

        stack_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_data, Unset):
            stack_data = []
            for stack_data_item_data in self.stack_data:
                stack_data_item = stack_data_item_data.to_dict()
                stack_data.append(stack_data_item)

        mlag_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mlag_data, Unset):
            mlag_data = []
            for mlag_data_item_data in self.mlag_data:
                mlag_data_item = mlag_data_item_data.to_dict()
                mlag_data.append(mlag_data_item)

        p_2_p_group_total_rows = self.p_2_p_group_total_rows

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
        if stack_data is not UNSET:
            field_dict["stackData"] = stack_data
        if mlag_data is not UNSET:
            field_dict["mlagData"] = mlag_data
        if p_2_p_group_total_rows is not UNSET:
            field_dict["p2pGroupTotalRows"] = p_2_p_group_total_rows

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_info import DeviceInfo
        from ..models.osw_mlag_data_vo_device_info import (
            OswMlagDataVODeviceInfo,
        )
        from ..models.osw_stack_data_vo_device_info import (
            OswStackDataVODeviceInfo,
        )

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[DeviceInfo] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = DeviceInfo.from_dict(data_item_data)

                data.append(data_item)

        _stack_data = d.pop("stackData", UNSET)
        stack_data: list[OswStackDataVODeviceInfo] | Unset = UNSET
        if _stack_data is not UNSET:
            stack_data = []
            for stack_data_item_data in _stack_data:
                stack_data_item = OswStackDataVODeviceInfo.from_dict(
                    stack_data_item_data
                )

                stack_data.append(stack_data_item)

        _mlag_data = d.pop("mlagData", UNSET)
        mlag_data: list[OswMlagDataVODeviceInfo] | Unset = UNSET
        if _mlag_data is not UNSET:
            mlag_data = []
            for mlag_data_item_data in _mlag_data:
                mlag_data_item = OswMlagDataVODeviceInfo.from_dict(mlag_data_item_data)

                mlag_data.append(mlag_data_item)

        p_2_p_group_total_rows = d.pop("p2pGroupTotalRows", UNSET)

        adopted_device_grid_vo_device_info = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            stack_data=stack_data,
            mlag_data=mlag_data,
            p_2_p_group_total_rows=p_2_p_group_total_rows,
        )

        adopted_device_grid_vo_device_info.additional_properties = d
        return adopted_device_grid_vo_device_info

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
