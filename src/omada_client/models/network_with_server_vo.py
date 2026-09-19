from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.brief_server_device_vo import BriefServerDeviceVO


T = TypeVar("T", bound="NetworkWithServerVO")


@_attrs_define
class NetworkWithServerVO:
    """Networks With Dhcp Servers

    Attributes:
        id (str | Unset): LAN Network ID
        name (str | Unset): LAN Network Name
        type_ (str | Unset): LAN Network Type
        server_devices (list[BriefServerDeviceVO] | Unset): List of devices acting as DHCP servers in this network
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    type_: str | Unset = UNSET
    server_devices: list[BriefServerDeviceVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        type_ = self.type_

        server_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.server_devices, Unset):
            server_devices = []
            for server_devices_item_data in self.server_devices:
                server_devices_item = server_devices_item_data.to_dict()
                server_devices.append(server_devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if server_devices is not UNSET:
            field_dict["serverDevices"] = server_devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.brief_server_device_vo import BriefServerDeviceVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        _server_devices = d.pop("serverDevices", UNSET)
        server_devices: list[BriefServerDeviceVO] | Unset = UNSET
        if _server_devices is not UNSET:
            server_devices = []
            for server_devices_item_data in _server_devices:
                server_devices_item = BriefServerDeviceVO.from_dict(
                    server_devices_item_data
                )

                server_devices.append(server_devices_item)

        network_with_server_vo = cls(
            id=id,
            name=name,
            type_=type_,
            server_devices=server_devices,
        )

        network_with_server_vo.additional_properties = d
        return network_with_server_vo

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
