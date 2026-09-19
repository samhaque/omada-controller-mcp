from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.multicast_except_device_vo import MulticastExceptDeviceVO


T = TypeVar("T", bound="ReportSuppressionConfigVO")


@_attrs_define
class ReportSuppressionConfigVO:
    """reportSuppressionExceptDevice

    Attributes:
        enable (bool | Unset): enable
        device_list (list[MulticastExceptDeviceVO] | Unset): report suppression except device list
    """

    enable: bool | Unset = UNSET
    device_list: list[MulticastExceptDeviceVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        device_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.device_list, Unset):
            device_list = []
            for device_list_item_data in self.device_list:
                device_list_item = device_list_item_data.to_dict()
                device_list.append(device_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if device_list is not UNSET:
            field_dict["deviceList"] = device_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.multicast_except_device_vo import (
            MulticastExceptDeviceVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        _device_list = d.pop("deviceList", UNSET)
        device_list: list[MulticastExceptDeviceVO] | Unset = UNSET
        if _device_list is not UNSET:
            device_list = []
            for device_list_item_data in _device_list:
                device_list_item = MulticastExceptDeviceVO.from_dict(
                    device_list_item_data
                )

                device_list.append(device_list_item)

        report_suppression_config_vo = cls(
            enable=enable,
            device_list=device_list,
        )

        report_suppression_config_vo.additional_properties = d
        return report_suppression_config_vo

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
