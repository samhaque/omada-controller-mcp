from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NatTraversalTunnelOpenApiVO")


@_attrs_define
class NatTraversalTunnelOpenApiVO:
    """
    Attributes:
        name (str): Name of the remote access tunnel.
        local_address (str): IP address of the local target device.
        local_port (int): Port of the local target device's service.
        app_type (str): App type of the remote access tunnel for the local target device. HTTP, HTTPS, SSH, TELNET.
        duration (int | Unset): Valid duration time of the remote access tunnel, 1-24 hours.
        open_status (bool | Unset): If open the remote access tunnel after create.
        local_mac (str | Unset): Mac of the local target device.
        client_manager (bool | Unset): Client's manager of the remote access tunnel for the client.
        client_name (str | Unset): Client's name of the remote access tunnel for the client.
        client_device_type (str | Unset): Client's type of the remote access tunnel for the client.
        client_model (str | Unset): Client's model of the remote access tunnel for the client.
        tunnel_entry_type (int | Unset): Entry of the remote access tunnel.1: custom tunnel 2: device tunnel 3:device
            detail 4:client detail
    """

    name: str
    local_address: str
    local_port: int
    app_type: str
    duration: int | Unset = UNSET
    open_status: bool | Unset = UNSET
    local_mac: str | Unset = UNSET
    client_manager: bool | Unset = UNSET
    client_name: str | Unset = UNSET
    client_device_type: str | Unset = UNSET
    client_model: str | Unset = UNSET
    tunnel_entry_type: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        local_address = self.local_address

        local_port = self.local_port

        app_type = self.app_type

        duration = self.duration

        open_status = self.open_status

        local_mac = self.local_mac

        client_manager = self.client_manager

        client_name = self.client_name

        client_device_type = self.client_device_type

        client_model = self.client_model

        tunnel_entry_type = self.tunnel_entry_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "localAddress": local_address,
                "localPort": local_port,
                "appType": app_type,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration
        if open_status is not UNSET:
            field_dict["openStatus"] = open_status
        if local_mac is not UNSET:
            field_dict["localMac"] = local_mac
        if client_manager is not UNSET:
            field_dict["clientManager"] = client_manager
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if client_device_type is not UNSET:
            field_dict["clientDeviceType"] = client_device_type
        if client_model is not UNSET:
            field_dict["clientModel"] = client_model
        if tunnel_entry_type is not UNSET:
            field_dict["tunnelEntryType"] = tunnel_entry_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        local_address = d.pop("localAddress")

        local_port = d.pop("localPort")

        app_type = d.pop("appType")

        duration = d.pop("duration", UNSET)

        open_status = d.pop("openStatus", UNSET)

        local_mac = d.pop("localMac", UNSET)

        client_manager = d.pop("clientManager", UNSET)

        client_name = d.pop("clientName", UNSET)

        client_device_type = d.pop("clientDeviceType", UNSET)

        client_model = d.pop("clientModel", UNSET)

        tunnel_entry_type = d.pop("tunnelEntryType", UNSET)

        nat_traversal_tunnel_open_api_vo = cls(
            name=name,
            local_address=local_address,
            local_port=local_port,
            app_type=app_type,
            duration=duration,
            open_status=open_status,
            local_mac=local_mac,
            client_manager=client_manager,
            client_name=client_name,
            client_device_type=client_device_type,
            client_model=client_model,
            tunnel_entry_type=tunnel_entry_type,
        )

        nat_traversal_tunnel_open_api_vo.additional_properties = d
        return nat_traversal_tunnel_open_api_vo

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
