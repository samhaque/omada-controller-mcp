from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityBaseVO")


@_attrs_define
class ActivityBaseVO:
    """
    Attributes:
        time (int | Unset): time
        upload (int | Unset): tx traffic of internet
        download (int | Unset): rx traffic of internet
        wired_count (int | Unset): number of wireless device
        wireless_count (int | Unset): number of wireless device
        total_data (int | Unset): total traffic
    """

    time: int | Unset = UNSET
    upload: int | Unset = UNSET
    download: int | Unset = UNSET
    wired_count: int | Unset = UNSET
    wireless_count: int | Unset = UNSET
    total_data: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        upload = self.upload

        download = self.download

        wired_count = self.wired_count

        wireless_count = self.wireless_count

        total_data = self.total_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if time is not UNSET:
            field_dict["time"] = time
        if upload is not UNSET:
            field_dict["upload"] = upload
        if download is not UNSET:
            field_dict["download"] = download
        if wired_count is not UNSET:
            field_dict["wiredCount"] = wired_count
        if wireless_count is not UNSET:
            field_dict["wirelessCount"] = wireless_count
        if total_data is not UNSET:
            field_dict["totalData"] = total_data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        time = d.pop("time", UNSET)

        upload = d.pop("upload", UNSET)

        download = d.pop("download", UNSET)

        wired_count = d.pop("wiredCount", UNSET)

        wireless_count = d.pop("wirelessCount", UNSET)

        total_data = d.pop("totalData", UNSET)

        activity_base_vo = cls(
            time=time,
            upload=upload,
            download=download,
            wired_count=wired_count,
            wireless_count=wireless_count,
            total_data=total_data,
        )

        activity_base_vo.additional_properties = d
        return activity_base_vo

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
