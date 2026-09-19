from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.static_routing_interface_info import StaticRoutingInterfaceInfo


T = TypeVar("T", bound="StaticRoutingInterfaceResult")


@_attrs_define
class StaticRoutingInterfaceResult:
    """
    Attributes:
        interface_info_list (list[StaticRoutingInterfaceInfo] | Unset): Interface information list.
        has_wan_enable (bool | Unset): Internet has enable WAN port(s).
    """

    interface_info_list: list[StaticRoutingInterfaceInfo] | Unset = UNSET
    has_wan_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_info_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interface_info_list, Unset):
            interface_info_list = []
            for interface_info_list_item_data in self.interface_info_list:
                interface_info_list_item = interface_info_list_item_data.to_dict()
                interface_info_list.append(interface_info_list_item)

        has_wan_enable = self.has_wan_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface_info_list is not UNSET:
            field_dict["interfaceInfoList"] = interface_info_list
        if has_wan_enable is not UNSET:
            field_dict["hasWanEnable"] = has_wan_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.static_routing_interface_info import (
            StaticRoutingInterfaceInfo,
        )

        d = dict(src_dict)
        _interface_info_list = d.pop("interfaceInfoList", UNSET)
        interface_info_list: list[StaticRoutingInterfaceInfo] | Unset = UNSET
        if _interface_info_list is not UNSET:
            interface_info_list = []
            for interface_info_list_item_data in _interface_info_list:
                interface_info_list_item = StaticRoutingInterfaceInfo.from_dict(
                    interface_info_list_item_data
                )

                interface_info_list.append(interface_info_list_item)

        has_wan_enable = d.pop("hasWanEnable", UNSET)

        static_routing_interface_result = cls(
            interface_info_list=interface_info_list,
            has_wan_enable=has_wan_enable,
        )

        static_routing_interface_result.additional_properties = d
        return static_routing_interface_result

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
