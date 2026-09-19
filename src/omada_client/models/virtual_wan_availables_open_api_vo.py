from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.virtual_wan_available_open_api_vo import VirtualWanAvailableOpenApiVO


T = TypeVar("T", bound="VirtualWanAvailablesOpenApiVO")


@_attrs_define
class VirtualWanAvailablesOpenApiVO:
    """VirtualWanAvailablesInfo

    Attributes:
        wan_ports (list[VirtualWanAvailableOpenApiVO] | Unset): Virtual WAN available list.
    """

    wan_ports: list[VirtualWanAvailableOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        wan_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_ports, Unset):
            wan_ports = []
            for wan_ports_item_data in self.wan_ports:
                wan_ports_item = wan_ports_item_data.to_dict()
                wan_ports.append(wan_ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wan_ports is not UNSET:
            field_dict["wanPorts"] = wan_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.virtual_wan_available_open_api_vo import (
            VirtualWanAvailableOpenApiVO,
        )

        d = dict(src_dict)
        _wan_ports = d.pop("wanPorts", UNSET)
        wan_ports: list[VirtualWanAvailableOpenApiVO] | Unset = UNSET
        if _wan_ports is not UNSET:
            wan_ports = []
            for wan_ports_item_data in _wan_ports:
                wan_ports_item = VirtualWanAvailableOpenApiVO.from_dict(
                    wan_ports_item_data
                )

                wan_ports.append(wan_ports_item)

        virtual_wan_availables_open_api_vo = cls(
            wan_ports=wan_ports,
        )

        virtual_wan_availables_open_api_vo.additional_properties = d
        return virtual_wan_availables_open_api_vo

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
