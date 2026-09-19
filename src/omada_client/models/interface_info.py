from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_brief_vo import DeviceBriefVO


T = TypeVar("T", bound="InterfaceInfo")


@_attrs_define
class InterfaceInfo:
    """
    Attributes:
        interface_type (int | Unset): Parameter [interfaceType] should be a value as follows: 0: Wired, 1: Wireless.
        interface_name (str | Unset): Interface name.
        channel (int | Unset): Parameter [channel] should be a value as follows: 0: 2.4GHz  1: 5GHz-1  2:5GHz-2 3: 6GHz
        interface_id (str | Unset): Interface ID, for example: if interfaceType is network, interfaceId should be LAN
            network ID. LAN Network can be created using 'Create LAN network' interface, and LAN Network ID can be obtained
            from 'Get LAN network list' interface.
        link_status (int | Unset): Link status should be a value as follows: 0:LINK_DOWN;1:LINK_UP
        is_copper (bool | Unset): Whether the port is copper when the port is combo.
        downlink_devices (list[DeviceBriefVO] | Unset): Downlink Devices
    """

    interface_type: int | Unset = UNSET
    interface_name: str | Unset = UNSET
    channel: int | Unset = UNSET
    interface_id: str | Unset = UNSET
    link_status: int | Unset = UNSET
    is_copper: bool | Unset = UNSET
    downlink_devices: list[DeviceBriefVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interface_type = self.interface_type

        interface_name = self.interface_name

        channel = self.channel

        interface_id = self.interface_id

        link_status = self.link_status

        is_copper = self.is_copper

        downlink_devices: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_devices, Unset):
            downlink_devices = []
            for downlink_devices_item_data in self.downlink_devices:
                downlink_devices_item = downlink_devices_item_data.to_dict()
                downlink_devices.append(downlink_devices_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interface_type is not UNSET:
            field_dict["interfaceType"] = interface_type
        if interface_name is not UNSET:
            field_dict["interfaceName"] = interface_name
        if channel is not UNSET:
            field_dict["channel"] = channel
        if interface_id is not UNSET:
            field_dict["interfaceId"] = interface_id
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if is_copper is not UNSET:
            field_dict["isCopper"] = is_copper
        if downlink_devices is not UNSET:
            field_dict["downlinkDevices"] = downlink_devices

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_brief_vo import DeviceBriefVO

        d = dict(src_dict)
        interface_type = d.pop("interfaceType", UNSET)

        interface_name = d.pop("interfaceName", UNSET)

        channel = d.pop("channel", UNSET)

        interface_id = d.pop("interfaceId", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        is_copper = d.pop("isCopper", UNSET)

        _downlink_devices = d.pop("downlinkDevices", UNSET)
        downlink_devices: list[DeviceBriefVO] | Unset = UNSET
        if _downlink_devices is not UNSET:
            downlink_devices = []
            for downlink_devices_item_data in _downlink_devices:
                downlink_devices_item = DeviceBriefVO.from_dict(
                    downlink_devices_item_data
                )

                downlink_devices.append(downlink_devices_item)

        interface_info = cls(
            interface_type=interface_type,
            interface_name=interface_name,
            channel=channel,
            interface_id=interface_id,
            link_status=link_status,
            is_copper=is_copper,
            downlink_devices=downlink_devices,
        )

        interface_info.additional_properties = d
        return interface_info

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
