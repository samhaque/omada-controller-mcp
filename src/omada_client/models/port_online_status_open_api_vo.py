from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_online_status_open_api_vo import (
        VirtualWanOnlineStatusOpenApiVO,
    )
    from ..models.wan_online_status_open_api_vo import WanOnlineStatusOpenApiVO


T = TypeVar("T", bound="PortOnlineStatusOpenApiVO")


@_attrs_define
class PortOnlineStatusOpenApiVO:
    """Port online status.

    Attributes:
        virtual_wan_online_status (list[VirtualWanOnlineStatusOpenApiVO] | Unset): Virtual WAN online status list
        wan_online_status (list[WanOnlineStatusOpenApiVO] | Unset): WAN online status list
    """

    virtual_wan_online_status: list[VirtualWanOnlineStatusOpenApiVO] | Unset = UNSET
    wan_online_status: list[WanOnlineStatusOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_wan_online_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.virtual_wan_online_status, Unset):
            virtual_wan_online_status = []
            for virtual_wan_online_status_item_data in self.virtual_wan_online_status:
                virtual_wan_online_status_item = (
                    virtual_wan_online_status_item_data.to_dict()
                )
                virtual_wan_online_status.append(virtual_wan_online_status_item)

        wan_online_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_online_status, Unset):
            wan_online_status = []
            for wan_online_status_item_data in self.wan_online_status:
                wan_online_status_item = wan_online_status_item_data.to_dict()
                wan_online_status.append(wan_online_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_wan_online_status is not UNSET:
            field_dict["virtualWanOnlineStatus"] = virtual_wan_online_status
        if wan_online_status is not UNSET:
            field_dict["wanOnlineStatus"] = wan_online_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_online_status_open_api_vo import (
            VirtualWanOnlineStatusOpenApiVO,
        )
        from ..models.wan_online_status_open_api_vo import (
            WanOnlineStatusOpenApiVO,
        )

        d = dict(src_dict)
        _virtual_wan_online_status = d.pop("virtualWanOnlineStatus", UNSET)
        virtual_wan_online_status: list[VirtualWanOnlineStatusOpenApiVO] | Unset = UNSET
        if _virtual_wan_online_status is not UNSET:
            virtual_wan_online_status = []
            for virtual_wan_online_status_item_data in _virtual_wan_online_status:
                virtual_wan_online_status_item = (
                    VirtualWanOnlineStatusOpenApiVO.from_dict(
                        virtual_wan_online_status_item_data
                    )
                )

                virtual_wan_online_status.append(virtual_wan_online_status_item)

        _wan_online_status = d.pop("wanOnlineStatus", UNSET)
        wan_online_status: list[WanOnlineStatusOpenApiVO] | Unset = UNSET
        if _wan_online_status is not UNSET:
            wan_online_status = []
            for wan_online_status_item_data in _wan_online_status:
                wan_online_status_item = WanOnlineStatusOpenApiVO.from_dict(
                    wan_online_status_item_data
                )

                wan_online_status.append(wan_online_status_item)

        port_online_status_open_api_vo = cls(
            virtual_wan_online_status=virtual_wan_online_status,
            wan_online_status=wan_online_status,
        )

        port_online_status_open_api_vo.additional_properties = d
        return port_online_status_open_api_vo

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
