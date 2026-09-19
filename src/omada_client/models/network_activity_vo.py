from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_base_vo import ActivityBaseVO


T = TypeVar("T", bound="NetworkActivityVO")


@_attrs_define
class NetworkActivityVO:
    """
    Attributes:
        total_traffic (int | Unset): total traffic
        total_upload (int | Unset): total tx traffic
        total_download (int | Unset): total rx traffic
        activity_list (list[ActivityBaseVO] | Unset):
        exist_data (bool | Unset): mark whether the data exists
        total_wired_count (int | Unset): total number of wired client
        total_wireless_count (int | Unset): total number of wireless client
        total_client_count (int | Unset): total number of client
    """

    total_traffic: int | Unset = UNSET
    total_upload: int | Unset = UNSET
    total_download: int | Unset = UNSET
    activity_list: list[ActivityBaseVO] | Unset = UNSET
    exist_data: bool | Unset = UNSET
    total_wired_count: int | Unset = UNSET
    total_wireless_count: int | Unset = UNSET
    total_client_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_traffic = self.total_traffic

        total_upload = self.total_upload

        total_download = self.total_download

        activity_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.activity_list, Unset):
            activity_list = []
            for activity_list_item_data in self.activity_list:
                activity_list_item = activity_list_item_data.to_dict()
                activity_list.append(activity_list_item)

        exist_data = self.exist_data

        total_wired_count = self.total_wired_count

        total_wireless_count = self.total_wireless_count

        total_client_count = self.total_client_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if total_upload is not UNSET:
            field_dict["totalUpload"] = total_upload
        if total_download is not UNSET:
            field_dict["totalDownload"] = total_download
        if activity_list is not UNSET:
            field_dict["activityList"] = activity_list
        if exist_data is not UNSET:
            field_dict["existData"] = exist_data
        if total_wired_count is not UNSET:
            field_dict["totalWiredCount"] = total_wired_count
        if total_wireless_count is not UNSET:
            field_dict["totalWirelessCount"] = total_wireless_count
        if total_client_count is not UNSET:
            field_dict["totalClientCount"] = total_client_count

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.activity_base_vo import ActivityBaseVO

        d = dict(src_dict)
        total_traffic = d.pop("totalTraffic", UNSET)

        total_upload = d.pop("totalUpload", UNSET)

        total_download = d.pop("totalDownload", UNSET)

        _activity_list = d.pop("activityList", UNSET)
        activity_list: list[ActivityBaseVO] | Unset = UNSET
        if _activity_list is not UNSET:
            activity_list = []
            for activity_list_item_data in _activity_list:
                activity_list_item = ActivityBaseVO.from_dict(activity_list_item_data)

                activity_list.append(activity_list_item)

        exist_data = d.pop("existData", UNSET)

        total_wired_count = d.pop("totalWiredCount", UNSET)

        total_wireless_count = d.pop("totalWirelessCount", UNSET)

        total_client_count = d.pop("totalClientCount", UNSET)

        network_activity_vo = cls(
            total_traffic=total_traffic,
            total_upload=total_upload,
            total_download=total_download,
            activity_list=activity_list,
            exist_data=exist_data,
            total_wired_count=total_wired_count,
            total_wireless_count=total_wireless_count,
            total_client_count=total_client_count,
        )

        network_activity_vo.additional_properties = d
        return network_activity_vo

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
