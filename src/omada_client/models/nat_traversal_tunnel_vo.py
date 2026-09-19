from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NatTraversalTunnelVO")


@_attrs_define
class NatTraversalTunnelVO:
    """
    Attributes:
        local_port (int): Port of the local target device's service.
        id (str | Unset): ID of the remote access tunnel.
        tunnel_id (int | Unset): Tunnel ID of the remote access tunnel.
        name (str | Unset): Name of the remote access tunnel.
        local_address (str | Unset): IP address of the local target device.
        local_mac (str | Unset): Mac of the local target device.
        jump_mac (str | Unset): Mac of the jumper device.
        duration (int | Unset): Valid duration time of the remote access tunnel, 1-24 hours.
        type_ (str | Unset): Type of the remote access tunnel.
        closure_time (int | Unset): Closure time of the remote access tunnel.
        custom_tunnel (bool | Unset): If the remote access tunnel is a custom tunnel.
        auto_login (bool | Unset): If the remote access tunnel enabled auto login.
        app_type (int | Unset): App type of the remote access tunnel for the local target device. 21:HTTP, 22:HTTPS,
            31:SSH, 32:TELNET.
        status (int | Unset): Status of the remote access tunnel. 0: Disconnected, 1: Connected, 2: Opening, -1:
            Heartbeat Missed, -2: Expired.
        open_status (bool | Unset): Open Status of the remote access tunnel.
        tunnel_entry_type (int | Unset): Entry of the remote access tunnel.1: custom tunnel 2: device tunnel 3:device
            detail 4:client detail
        client_manager (bool | Unset): Client's manager of the remote access tunnel for the client.
        client_name (str | Unset): Client's name of the remote access tunnel for the client.
        client_device_type (str | Unset): Client's type of the remote access tunnel for the client.
        client_model (str | Unset): Client's model of the remote access tunnel for the client.
        support_web_auto_login (bool | Unset): If the remote access tunnel supports web auto login.
        support_ssh_telnet_tunnel (bool | Unset): If the remote access tunnel supports SSH and telnet connections.
        support_http_https_tunnel (bool | Unset): If the remote access tunnel supports HTTP and HTTPS connections.
        enable_ssh (bool | Unset): If the SSH Login is enabled in site settings.
        enable_http (bool | Unset): If the HTTP Login is enabled in global settings.
        enable_https (bool | Unset): If the HTTPs Login is enabled in global settings.
        eweb_host (str | Unset): Nat traversal tunnel eweb host
    """

    local_port: int
    id: str | Unset = UNSET
    tunnel_id: int | Unset = UNSET
    name: str | Unset = UNSET
    local_address: str | Unset = UNSET
    local_mac: str | Unset = UNSET
    jump_mac: str | Unset = UNSET
    duration: int | Unset = UNSET
    type_: str | Unset = UNSET
    closure_time: int | Unset = UNSET
    custom_tunnel: bool | Unset = UNSET
    auto_login: bool | Unset = UNSET
    app_type: int | Unset = UNSET
    status: int | Unset = UNSET
    open_status: bool | Unset = UNSET
    tunnel_entry_type: int | Unset = UNSET
    client_manager: bool | Unset = UNSET
    client_name: str | Unset = UNSET
    client_device_type: str | Unset = UNSET
    client_model: str | Unset = UNSET
    support_web_auto_login: bool | Unset = UNSET
    support_ssh_telnet_tunnel: bool | Unset = UNSET
    support_http_https_tunnel: bool | Unset = UNSET
    enable_ssh: bool | Unset = UNSET
    enable_http: bool | Unset = UNSET
    enable_https: bool | Unset = UNSET
    eweb_host: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        local_port = self.local_port

        id = self.id

        tunnel_id = self.tunnel_id

        name = self.name

        local_address = self.local_address

        local_mac = self.local_mac

        jump_mac = self.jump_mac

        duration = self.duration

        type_ = self.type_

        closure_time = self.closure_time

        custom_tunnel = self.custom_tunnel

        auto_login = self.auto_login

        app_type = self.app_type

        status = self.status

        open_status = self.open_status

        tunnel_entry_type = self.tunnel_entry_type

        client_manager = self.client_manager

        client_name = self.client_name

        client_device_type = self.client_device_type

        client_model = self.client_model

        support_web_auto_login = self.support_web_auto_login

        support_ssh_telnet_tunnel = self.support_ssh_telnet_tunnel

        support_http_https_tunnel = self.support_http_https_tunnel

        enable_ssh = self.enable_ssh

        enable_http = self.enable_http

        enable_https = self.enable_https

        eweb_host = self.eweb_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "localPort": local_port,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if tunnel_id is not UNSET:
            field_dict["tunnelId"] = tunnel_id
        if name is not UNSET:
            field_dict["name"] = name
        if local_address is not UNSET:
            field_dict["localAddress"] = local_address
        if local_mac is not UNSET:
            field_dict["localMac"] = local_mac
        if jump_mac is not UNSET:
            field_dict["jumpMac"] = jump_mac
        if duration is not UNSET:
            field_dict["duration"] = duration
        if type_ is not UNSET:
            field_dict["type"] = type_
        if closure_time is not UNSET:
            field_dict["closureTime"] = closure_time
        if custom_tunnel is not UNSET:
            field_dict["customTunnel"] = custom_tunnel
        if auto_login is not UNSET:
            field_dict["autoLogin"] = auto_login
        if app_type is not UNSET:
            field_dict["appType"] = app_type
        if status is not UNSET:
            field_dict["status"] = status
        if open_status is not UNSET:
            field_dict["openStatus"] = open_status
        if tunnel_entry_type is not UNSET:
            field_dict["tunnelEntryType"] = tunnel_entry_type
        if client_manager is not UNSET:
            field_dict["clientManager"] = client_manager
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if client_device_type is not UNSET:
            field_dict["clientDeviceType"] = client_device_type
        if client_model is not UNSET:
            field_dict["clientModel"] = client_model
        if support_web_auto_login is not UNSET:
            field_dict["supportWebAutoLogin"] = support_web_auto_login
        if support_ssh_telnet_tunnel is not UNSET:
            field_dict["supportSshTelnetTunnel"] = support_ssh_telnet_tunnel
        if support_http_https_tunnel is not UNSET:
            field_dict["supportHttpHttpsTunnel"] = support_http_https_tunnel
        if enable_ssh is not UNSET:
            field_dict["enableSsh"] = enable_ssh
        if enable_http is not UNSET:
            field_dict["enableHttp"] = enable_http
        if enable_https is not UNSET:
            field_dict["enableHttps"] = enable_https
        if eweb_host is not UNSET:
            field_dict["ewebHost"] = eweb_host

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        local_port = d.pop("localPort")

        id = d.pop("id", UNSET)

        tunnel_id = d.pop("tunnelId", UNSET)

        name = d.pop("name", UNSET)

        local_address = d.pop("localAddress", UNSET)

        local_mac = d.pop("localMac", UNSET)

        jump_mac = d.pop("jumpMac", UNSET)

        duration = d.pop("duration", UNSET)

        type_ = d.pop("type", UNSET)

        closure_time = d.pop("closureTime", UNSET)

        custom_tunnel = d.pop("customTunnel", UNSET)

        auto_login = d.pop("autoLogin", UNSET)

        app_type = d.pop("appType", UNSET)

        status = d.pop("status", UNSET)

        open_status = d.pop("openStatus", UNSET)

        tunnel_entry_type = d.pop("tunnelEntryType", UNSET)

        client_manager = d.pop("clientManager", UNSET)

        client_name = d.pop("clientName", UNSET)

        client_device_type = d.pop("clientDeviceType", UNSET)

        client_model = d.pop("clientModel", UNSET)

        support_web_auto_login = d.pop("supportWebAutoLogin", UNSET)

        support_ssh_telnet_tunnel = d.pop("supportSshTelnetTunnel", UNSET)

        support_http_https_tunnel = d.pop("supportHttpHttpsTunnel", UNSET)

        enable_ssh = d.pop("enableSsh", UNSET)

        enable_http = d.pop("enableHttp", UNSET)

        enable_https = d.pop("enableHttps", UNSET)

        eweb_host = d.pop("ewebHost", UNSET)

        nat_traversal_tunnel_vo = cls(
            local_port=local_port,
            id=id,
            tunnel_id=tunnel_id,
            name=name,
            local_address=local_address,
            local_mac=local_mac,
            jump_mac=jump_mac,
            duration=duration,
            type_=type_,
            closure_time=closure_time,
            custom_tunnel=custom_tunnel,
            auto_login=auto_login,
            app_type=app_type,
            status=status,
            open_status=open_status,
            tunnel_entry_type=tunnel_entry_type,
            client_manager=client_manager,
            client_name=client_name,
            client_device_type=client_device_type,
            client_model=client_model,
            support_web_auto_login=support_web_auto_login,
            support_ssh_telnet_tunnel=support_ssh_telnet_tunnel,
            support_http_https_tunnel=support_http_https_tunnel,
            enable_ssh=enable_ssh,
            enable_http=enable_http,
            enable_https=enable_https,
            eweb_host=eweb_host,
        )

        nat_traversal_tunnel_vo.additional_properties = d
        return nat_traversal_tunnel_vo

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
