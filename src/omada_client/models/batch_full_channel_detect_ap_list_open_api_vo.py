from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_info_open_api_vo import ApInfoOpenApiVO


T = TypeVar("T", bound="BatchFullChannelDetectApListOpenApiVO")


@_attrs_define
class BatchFullChannelDetectApListOpenApiVO:
    """
    Attributes:
        scan_ap_num (int | Unset): The number of AP devices participating in batch full channel detection.
        device_info_list (list[ApInfoOpenApiVO] | Unset): A list of information for AP devices.
    """

    scan_ap_num: int | Unset = UNSET
    device_info_list: list[ApInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scan_ap_num = self.scan_ap_num

        device_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_info_list, Unset):
            device_info_list = []
            for device_info_list_item_data in self.device_info_list:
                device_info_list_item = device_info_list_item_data.to_dict()
                device_info_list.append(device_info_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scan_ap_num is not UNSET:
            field_dict["scanApNum"] = scan_ap_num
        if device_info_list is not UNSET:
            field_dict["deviceInfoList"] = device_info_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_info_open_api_vo import ApInfoOpenApiVO

        d = dict(src_dict)
        scan_ap_num = d.pop("scanApNum", UNSET)

        _device_info_list = d.pop("deviceInfoList", UNSET)
        device_info_list: list[ApInfoOpenApiVO] | Unset = UNSET
        if _device_info_list is not UNSET:
            device_info_list = []
            for device_info_list_item_data in _device_info_list:
                device_info_list_item = ApInfoOpenApiVO.from_dict(
                    device_info_list_item_data
                )

                device_info_list.append(device_info_list_item)

        batch_full_channel_detect_ap_list_open_api_vo = cls(
            scan_ap_num=scan_ap_num,
            device_info_list=device_info_list,
        )

        batch_full_channel_detect_ap_list_open_api_vo.additional_properties = d
        return batch_full_channel_detect_ap_list_open_api_vo

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
