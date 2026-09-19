from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_firmware_pool_grid_info_model_latest_fw_info_fw_num import (
        ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum,
    )
    from ..models.model_latest_fw_info import ModelLatestFwInfo


T = TypeVar("T", bound="ModelFirmwarePoolGridInfoModelLatestFwInfo")


@_attrs_define
class ModelFirmwarePoolGridInfoModelLatestFwInfo:
    """
    Attributes:
        total_rows (int | Unset): Total rows of all items.
        current_page (int | Unset): Current page number.
        current_size (int | Unset): Number of entries per page.
        data (list[ModelLatestFwInfo] | Unset):
        fw_num (ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum | Unset): The firmware quantity map for each channel:
            The key is channel: (0: stable; 1: Release Candidate(RC); 2: Beta), The Value is the quantity
    """

    total_rows: int | Unset = UNSET
    current_page: int | Unset = UNSET
    current_size: int | Unset = UNSET
    data: list[ModelLatestFwInfo] | Unset = UNSET
    fw_num: ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum | Unset = UNSET
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

        fw_num: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fw_num, Unset):
            fw_num = self.fw_num.to_dict()

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
        if fw_num is not UNSET:
            field_dict["fwNum"] = fw_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_firmware_pool_grid_info_model_latest_fw_info_fw_num import (
            ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum,
        )
        from ..models.model_latest_fw_info import ModelLatestFwInfo

        d = dict(src_dict)
        total_rows = d.pop("totalRows", UNSET)

        current_page = d.pop("currentPage", UNSET)

        current_size = d.pop("currentSize", UNSET)

        _data = d.pop("data", UNSET)
        data: list[ModelLatestFwInfo] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ModelLatestFwInfo.from_dict(data_item_data)

                data.append(data_item)

        _fw_num = d.pop("fwNum", UNSET)
        fw_num: ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum | Unset
        if isinstance(_fw_num, Unset):
            fw_num = UNSET
        else:
            fw_num = ModelFirmwarePoolGridInfoModelLatestFwInfoFwNum.from_dict(_fw_num)

        model_firmware_pool_grid_info_model_latest_fw_info = cls(
            total_rows=total_rows,
            current_page=current_page,
            current_size=current_size,
            data=data,
            fw_num=fw_num,
        )

        model_firmware_pool_grid_info_model_latest_fw_info.additional_properties = d
        return model_firmware_pool_grid_info_model_latest_fw_info

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
