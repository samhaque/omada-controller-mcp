from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_port_and_lag_network_vo import OswPortAndLagNetworkVO


T = TypeVar("T", bound="OswNetworkDetailInfoOpenApiVO")


@_attrs_define
class OswNetworkDetailInfoOpenApiVO:
    """OswNetworkDetailInfoOpenApiVO

    Attributes:
        id (str | Unset): Network's ID
        name (str | Unset): Network's name
        vlan (int | Unset): VLAN ID
        isolation (bool | Unset): Whether network isolated.
        port_lag_network_info (OswPortAndLagNetworkVO | Unset): OswPortAndLagNetworkVO
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    isolation: bool | Unset = UNSET
    port_lag_network_info: OswPortAndLagNetworkVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        vlan = self.vlan

        isolation = self.isolation

        port_lag_network_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_lag_network_info, Unset):
            port_lag_network_info = self.port_lag_network_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if isolation is not UNSET:
            field_dict["isolation"] = isolation
        if port_lag_network_info is not UNSET:
            field_dict["portLagNetworkInfo"] = port_lag_network_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_port_and_lag_network_vo import (
            OswPortAndLagNetworkVO,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        vlan = d.pop("vlan", UNSET)

        isolation = d.pop("isolation", UNSET)

        _port_lag_network_info = d.pop("portLagNetworkInfo", UNSET)
        port_lag_network_info: OswPortAndLagNetworkVO | Unset
        if isinstance(_port_lag_network_info, Unset):
            port_lag_network_info = UNSET
        else:
            port_lag_network_info = OswPortAndLagNetworkVO.from_dict(
                _port_lag_network_info
            )

        osw_network_detail_info_open_api_vo = cls(
            id=id,
            name=name,
            vlan=vlan,
            isolation=isolation,
            port_lag_network_info=port_lag_network_info,
        )

        osw_network_detail_info_open_api_vo.additional_properties = d
        return osw_network_detail_info_open_api_vo

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
