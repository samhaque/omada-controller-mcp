from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_port_vo import DevicePortVO


T = TypeVar("T", bound="RouterPortVO")


@_attrs_define
class RouterPortVO:
    """The specific list of router ports info,including network, devices and the ports on them.

    Attributes:
        network_id (str | Unset): The unique identification of one network.
        network_name (str | Unset): The name of network.
        vlan (int | Unset): The vlan of the network.
        devices (list[DevicePortVO] | Unset): The collection of related devices.
        static_router_ports_num (int | Unset): The total num of static router ports related to this network.
        forbidden_router_ports_num (int | Unset): The total num of forbidden router ports related to this network.
    """

    network_id: str | Unset = UNSET
    network_name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    devices: list[DevicePortVO] | Unset = UNSET
    static_router_ports_num: int | Unset = UNSET
    forbidden_router_ports_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_id = self.network_id

        network_name = self.network_name

        vlan = self.vlan

        devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.devices, Unset):
            devices = []
            for devices_item_data in self.devices:
                devices_item = devices_item_data.to_dict()
                devices.append(devices_item)

        static_router_ports_num = self.static_router_ports_num

        forbidden_router_ports_num = self.forbidden_router_ports_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if devices is not UNSET:
            field_dict["devices"] = devices
        if static_router_ports_num is not UNSET:
            field_dict["staticRouterPortsNum"] = static_router_ports_num
        if forbidden_router_ports_num is not UNSET:
            field_dict["forbiddenRouterPortsNum"] = forbidden_router_ports_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_port_vo import DevicePortVO

        d = dict(src_dict)
        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        vlan = d.pop("vlan", UNSET)

        _devices = d.pop("devices", UNSET)
        devices: list[DevicePortVO] | Unset = UNSET
        if _devices is not UNSET:
            devices = []
            for devices_item_data in _devices:
                devices_item = DevicePortVO.from_dict(devices_item_data)

                devices.append(devices_item)

        static_router_ports_num = d.pop("staticRouterPortsNum", UNSET)

        forbidden_router_ports_num = d.pop("forbiddenRouterPortsNum", UNSET)

        router_port_vo = cls(
            network_id=network_id,
            network_name=network_name,
            vlan=vlan,
            devices=devices,
            static_router_ports_num=static_router_ports_num,
            forbidden_router_ports_num=forbidden_router_ports_num,
        )

        router_port_vo.additional_properties = d
        return router_port_vo

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
