from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vpn_used_function_open_api_vo import VpnUsedFunctionOpenApiVO


T = TypeVar("T", bound="VpnListUsedFunctionOpenApiVO")


@_attrs_define
class VpnListUsedFunctionOpenApiVO:
    """
    Attributes:
        vpn_list (list[VpnUsedFunctionOpenApiVO] | Unset): List of VPNs that have used the function.
    """

    vpn_list: list[VpnUsedFunctionOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vpn_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.vpn_list, Unset):
            vpn_list = []
            for vpn_list_item_data in self.vpn_list:
                vpn_list_item = vpn_list_item_data.to_dict()
                vpn_list.append(vpn_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vpn_list is not UNSET:
            field_dict["vpnList"] = vpn_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.vpn_used_function_open_api_vo import (
            VpnUsedFunctionOpenApiVO,
        )

        d = dict(src_dict)
        _vpn_list = d.pop("vpnList", UNSET)
        vpn_list: list[VpnUsedFunctionOpenApiVO] | Unset = UNSET
        if _vpn_list is not UNSET:
            vpn_list = []
            for vpn_list_item_data in _vpn_list:
                vpn_list_item = VpnUsedFunctionOpenApiVO.from_dict(vpn_list_item_data)

                vpn_list.append(vpn_list_item)

        vpn_list_used_function_open_api_vo = cls(
            vpn_list=vpn_list,
        )

        vpn_list_used_function_open_api_vo.additional_properties = d
        return vpn_list_used_function_open_api_vo

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
