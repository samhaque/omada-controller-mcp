from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lag_info_open_api_vo import LagInfoOpenApiVO


T = TypeVar("T", bound="DeviceOuiModeQueryOpenApiVO")


@_attrs_define
class DeviceOuiModeQueryOpenApiVO:
    """When mode is 0, Show configured device info.

    Attributes:
        device_mac (str): Device MAC. E.g. AA-BB-CC-DD-11-22 .
        device_name (str | Unset): Device Name
        port_list (list[int] | Unset): Configured Switch port.
        lag_list (list[int] | Unset): Configured Switch lag.
        lag_info (list[LagInfoOpenApiVO] | Unset): Switch lag info.
    """

    device_mac: str
    device_name: str | Unset = UNSET
    port_list: list[int] | Unset = UNSET
    lag_list: list[int] | Unset = UNSET
    lag_info: list[LagInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        device_name = self.device_name

        port_list: list[int] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = self.port_list

        lag_list: list[int] | Unset = UNSET
        if not isinstance(self.lag_list, Unset):
            lag_list = self.lag_list

        lag_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lag_info, Unset):
            lag_info = []
            for lag_info_item_data in self.lag_info:
                lag_info_item = lag_info_item_data.to_dict()
                lag_info.append(lag_info_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceMac": device_mac,
            }
        )
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if port_list is not UNSET:
            field_dict["portList"] = port_list
        if lag_list is not UNSET:
            field_dict["lagList"] = lag_list
        if lag_info is not UNSET:
            field_dict["lagInfo"] = lag_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lag_info_open_api_vo import LagInfoOpenApiVO

        d = dict(src_dict)
        device_mac = d.pop("deviceMac")

        device_name = d.pop("deviceName", UNSET)

        port_list = cast(list[int], d.pop("portList", UNSET))

        lag_list = cast(list[int], d.pop("lagList", UNSET))

        _lag_info = d.pop("lagInfo", UNSET)
        lag_info: list[LagInfoOpenApiVO] | Unset = UNSET
        if _lag_info is not UNSET:
            lag_info = []
            for lag_info_item_data in _lag_info:
                lag_info_item = LagInfoOpenApiVO.from_dict(lag_info_item_data)

                lag_info.append(lag_info_item)

        device_oui_mode_query_open_api_vo = cls(
            device_mac=device_mac,
            device_name=device_name,
            port_list=port_list,
            lag_list=lag_list,
            lag_info=lag_info,
        )

        device_oui_mode_query_open_api_vo.additional_properties = d
        return device_oui_mode_query_open_api_vo

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
