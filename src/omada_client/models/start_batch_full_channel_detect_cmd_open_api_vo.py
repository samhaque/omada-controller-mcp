from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="StartBatchFullChannelDetectCmdOpenApiVO")


@_attrs_define
class StartBatchFullChannelDetectCmdOpenApiVO:
    """
    Attributes:
        select_type (str): Select type of macs. include: include selected aps, exclude: all but exclude selected aps,
            all: include all aps(Parameter [macList] need input '[]').
        mac_list (list[str] | Unset): Select the Aps to full channel detect;.
        enable_interference (bool | Unset): Whether to enable non-interference detect.
        enable_wifi_interference (bool | Unset): Whether to enable wifi interference detect.
        enable_channel_util (bool | Unset): Whether to enable channel load detect.
    """

    select_type: str
    mac_list: list[str] | Unset = UNSET
    enable_interference: bool | Unset = UNSET
    enable_wifi_interference: bool | Unset = UNSET
    enable_channel_util: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_type = self.select_type

        mac_list: list[str] | Unset = UNSET
        if not isinstance(self.mac_list, Unset):
            mac_list = self.mac_list

        enable_interference = self.enable_interference

        enable_wifi_interference = self.enable_wifi_interference

        enable_channel_util = self.enable_channel_util

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selectType": select_type,
            }
        )
        if mac_list is not UNSET:
            field_dict["macList"] = mac_list
        if enable_interference is not UNSET:
            field_dict["enableInterference"] = enable_interference
        if enable_wifi_interference is not UNSET:
            field_dict["enableWifiInterference"] = enable_wifi_interference
        if enable_channel_util is not UNSET:
            field_dict["enableChannelUtil"] = enable_channel_util

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        select_type = d.pop("selectType")

        mac_list = cast(list[str], d.pop("macList", UNSET))

        enable_interference = d.pop("enableInterference", UNSET)

        enable_wifi_interference = d.pop("enableWifiInterference", UNSET)

        enable_channel_util = d.pop("enableChannelUtil", UNSET)

        start_batch_full_channel_detect_cmd_open_api_vo = cls(
            select_type=select_type,
            mac_list=mac_list,
            enable_interference=enable_interference,
            enable_wifi_interference=enable_wifi_interference,
            enable_channel_util=enable_channel_util,
        )

        start_batch_full_channel_detect_cmd_open_api_vo.additional_properties = d
        return start_batch_full_channel_detect_cmd_open_api_vo

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
