from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswLldpNeighborVO")


@_attrs_define
class OswLldpNeighborVO:
    """
    Attributes:
        port_id (int | Unset): Port ID
        standard_port (str | Unset): Standard Port
        device_id (str | Unset): Device ID
        system_name (str | Unset): System Name
        neighbor_port_id (str | Unset): The port on which the neighboring device is connected to the current switch
        ttl (int | Unset): Time that neighbor LLDP packets can survive
        capabilities (str | Unset): Capabilities
    """

    port_id: int | Unset = UNSET
    standard_port: str | Unset = UNSET
    device_id: str | Unset = UNSET
    system_name: str | Unset = UNSET
    neighbor_port_id: str | Unset = UNSET
    ttl: int | Unset = UNSET
    capabilities: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        standard_port = self.standard_port

        device_id = self.device_id

        system_name = self.system_name

        neighbor_port_id = self.neighbor_port_id

        ttl = self.ttl

        capabilities = self.capabilities

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if standard_port is not UNSET:
            field_dict["standardPort"] = standard_port
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if system_name is not UNSET:
            field_dict["systemName"] = system_name
        if neighbor_port_id is not UNSET:
            field_dict["neighborPortId"] = neighbor_port_id
        if ttl is not UNSET:
            field_dict["ttl"] = ttl
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        standard_port = d.pop("standardPort", UNSET)

        device_id = d.pop("deviceId", UNSET)

        system_name = d.pop("systemName", UNSET)

        neighbor_port_id = d.pop("neighborPortId", UNSET)

        ttl = d.pop("ttl", UNSET)

        capabilities = d.pop("capabilities", UNSET)

        osw_lldp_neighbor_vo = cls(
            port_id=port_id,
            standard_port=standard_port,
            device_id=device_id,
            system_name=system_name,
            neighbor_port_id=neighbor_port_id,
            ttl=ttl,
            capabilities=capabilities,
        )

        osw_lldp_neighbor_vo.additional_properties = d
        return osw_lldp_neighbor_vo

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
