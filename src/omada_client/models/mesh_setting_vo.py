from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MeshSettingVO")


@_attrs_define
class MeshSettingVO:
    """Site mesh.

    Attributes:
        mesh_enable (bool): Whether to enable mesh
        auto_failover_enable (bool | Unset): Whether to enable auto failover
        def_gateway_enable (bool | Unset): Connectivity detection, parameter defGatewayEnable should be a value as
            follows: true: Auto(Recommended) ; false: Customer IP
        gateway (str | Unset): Customer IP
        full_sector (bool | Unset): Whether to enable full-sector DFS
    """

    mesh_enable: bool
    auto_failover_enable: bool | Unset = UNSET
    def_gateway_enable: bool | Unset = UNSET
    gateway: str | Unset = UNSET
    full_sector: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mesh_enable = self.mesh_enable

        auto_failover_enable = self.auto_failover_enable

        def_gateway_enable = self.def_gateway_enable

        gateway = self.gateway

        full_sector = self.full_sector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meshEnable": mesh_enable,
            }
        )
        if auto_failover_enable is not UNSET:
            field_dict["autoFailoverEnable"] = auto_failover_enable
        if def_gateway_enable is not UNSET:
            field_dict["defGatewayEnable"] = def_gateway_enable
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if full_sector is not UNSET:
            field_dict["fullSector"] = full_sector

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mesh_enable = d.pop("meshEnable")

        auto_failover_enable = d.pop("autoFailoverEnable", UNSET)

        def_gateway_enable = d.pop("defGatewayEnable", UNSET)

        gateway = d.pop("gateway", UNSET)

        full_sector = d.pop("fullSector", UNSET)

        mesh_setting_vo = cls(
            mesh_enable=mesh_enable,
            auto_failover_enable=auto_failover_enable,
            def_gateway_enable=def_gateway_enable,
            gateway=gateway,
            full_sector=full_sector,
        )

        mesh_setting_vo.additional_properties = d
        return mesh_setting_vo

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
