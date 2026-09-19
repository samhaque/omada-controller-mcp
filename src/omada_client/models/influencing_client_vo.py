from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="InfluencingClientVO")


@_attrs_define
class InfluencingClientVO:
    """
    Attributes:
        mac (str | Unset): MAC address of the client
        client_name (str | Unset): Display name of the client
        client_type (str | Unset): Type of the client device
        ip (str | Unset): IP address of the client
        manager (bool | Unset): Whether the client is a managing host
        active (bool | Unset): Client status (true = connected, false = disconnected)
        auth_status (int | Unset): Authentication status.0: CONNECTED // Access without any authentication method.1:
            PENDING // Access to Portal, but authentication failed.2: AUTHORIZED // Pass through portal, pass other
            authentication without portal.3: AUTH-FREE // No portal authentication required.4: OFFLINE // Offline client.
        health (int | Unset): Client health score
        model (str | Unset): Client model
    """

    mac: str | Unset = UNSET
    client_name: str | Unset = UNSET
    client_type: str | Unset = UNSET
    ip: str | Unset = UNSET
    manager: bool | Unset = UNSET
    active: bool | Unset = UNSET
    auth_status: int | Unset = UNSET
    health: int | Unset = UNSET
    model: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        client_name = self.client_name

        client_type = self.client_type

        ip = self.ip

        manager = self.manager

        active = self.active

        auth_status = self.auth_status

        health = self.health

        model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if client_name is not UNSET:
            field_dict["clientName"] = client_name
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if ip is not UNSET:
            field_dict["ip"] = ip
        if manager is not UNSET:
            field_dict["manager"] = manager
        if active is not UNSET:
            field_dict["active"] = active
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status
        if health is not UNSET:
            field_dict["health"] = health
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        client_name = d.pop("clientName", UNSET)

        client_type = d.pop("clientType", UNSET)

        ip = d.pop("ip", UNSET)

        manager = d.pop("manager", UNSET)

        active = d.pop("active", UNSET)

        auth_status = d.pop("authStatus", UNSET)

        health = d.pop("health", UNSET)

        model = d.pop("model", UNSET)

        influencing_client_vo = cls(
            mac=mac,
            client_name=client_name,
            client_type=client_type,
            ip=ip,
            manager=manager,
            active=active,
            auth_status=auth_status,
            health=health,
            model=model,
        )

        influencing_client_vo.additional_properties = d
        return influencing_client_vo

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
