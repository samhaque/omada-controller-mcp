from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_info_open_api_vo import ApInfoOpenApiVO


T = TypeVar("T", bound="BatchFullChannelDetectHistoryOpenApiVO")


@_attrs_define
class BatchFullChannelDetectHistoryOpenApiVO:
    """
    Attributes:
        history_id (str | Unset): Id of batch full channel detect history.
        last_seen (int | Unset): Last full channel detect time.
        scan_ap_num (int | Unset): The total number of APs participating in the full channel detect.
        status (int | Unset): full channel detect status. 0: finish, 1: scanning.
        enable_interference (bool | Unset): Whether to enable interference detect
        device_info_list (list[ApInfoOpenApiVO] | Unset): Device information list
    """

    history_id: str | Unset = UNSET
    last_seen: int | Unset = UNSET
    scan_ap_num: int | Unset = UNSET
    status: int | Unset = UNSET
    enable_interference: bool | Unset = UNSET
    device_info_list: list[ApInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        history_id = self.history_id

        last_seen = self.last_seen

        scan_ap_num = self.scan_ap_num

        status = self.status

        enable_interference = self.enable_interference

        device_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_info_list, Unset):
            device_info_list = []
            for device_info_list_item_data in self.device_info_list:
                device_info_list_item = device_info_list_item_data.to_dict()
                device_info_list.append(device_info_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if last_seen is not UNSET:
            field_dict["lastSeen"] = last_seen
        if scan_ap_num is not UNSET:
            field_dict["scanApNum"] = scan_ap_num
        if status is not UNSET:
            field_dict["status"] = status
        if enable_interference is not UNSET:
            field_dict["enableInterference"] = enable_interference
        if device_info_list is not UNSET:
            field_dict["deviceInfoList"] = device_info_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_info_open_api_vo import ApInfoOpenApiVO

        d = dict(src_dict)
        history_id = d.pop("historyId", UNSET)

        last_seen = d.pop("lastSeen", UNSET)

        scan_ap_num = d.pop("scanApNum", UNSET)

        status = d.pop("status", UNSET)

        enable_interference = d.pop("enableInterference", UNSET)

        _device_info_list = d.pop("deviceInfoList", UNSET)
        device_info_list: list[ApInfoOpenApiVO] | Unset = UNSET
        if _device_info_list is not UNSET:
            device_info_list = []
            for device_info_list_item_data in _device_info_list:
                device_info_list_item = ApInfoOpenApiVO.from_dict(
                    device_info_list_item_data
                )

                device_info_list.append(device_info_list_item)

        batch_full_channel_detect_history_open_api_vo = cls(
            history_id=history_id,
            last_seen=last_seen,
            scan_ap_num=scan_ap_num,
            status=status,
            enable_interference=enable_interference,
            device_info_list=device_info_list,
        )

        batch_full_channel_detect_history_open_api_vo.additional_properties = d
        return batch_full_channel_detect_history_open_api_vo

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
