from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DhcpUserVO")


@_attrs_define
class DhcpUserVO:
    """
    Attributes:
        type_ (int | Unset): Type should be a value as follows: 0: Device; 1: Client
        ip_address (str | Unset): IP Address
        mac_address (str | Unset): Mac Address
        name (str | Unset): Dhcp User Name
        showing_type (str | Unset): Client Type or Device Type
        model (str | Unset): device Model
        model_version (str | Unset): device ModelVersion
        net_id (str | Unset): Network ID
        net_name (str | Unset): Network Name
        server_name (str | Unset): Dhcp Server Device Name
        server_mac (str | Unset): Dhcp Server Device Mac
        server_stack_id (str | Unset): Dhcp Server Stack ID
        left_lease_time (str | Unset): Left Lease Time
        status (int | Unset): Status should be a value as follows: 0: Dynamic Binding; 1: Static Binding
        ip_long (int | Unset):
    """

    type_: int | Unset = UNSET
    ip_address: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    name: str | Unset = UNSET
    showing_type: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    net_id: str | Unset = UNSET
    net_name: str | Unset = UNSET
    server_name: str | Unset = UNSET
    server_mac: str | Unset = UNSET
    server_stack_id: str | Unset = UNSET
    left_lease_time: str | Unset = UNSET
    status: int | Unset = UNSET
    ip_long: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        ip_address = self.ip_address

        mac_address = self.mac_address

        name = self.name

        showing_type = self.showing_type

        model = self.model

        model_version = self.model_version

        net_id = self.net_id

        net_name = self.net_name

        server_name = self.server_name

        server_mac = self.server_mac

        server_stack_id = self.server_stack_id

        left_lease_time = self.left_lease_time

        status = self.status

        ip_long = self.ip_long

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if name is not UNSET:
            field_dict["name"] = name
        if showing_type is not UNSET:
            field_dict["showingType"] = showing_type
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if net_id is not UNSET:
            field_dict["netId"] = net_id
        if net_name is not UNSET:
            field_dict["netName"] = net_name
        if server_name is not UNSET:
            field_dict["serverName"] = server_name
        if server_mac is not UNSET:
            field_dict["serverMac"] = server_mac
        if server_stack_id is not UNSET:
            field_dict["serverStackId"] = server_stack_id
        if left_lease_time is not UNSET:
            field_dict["leftLeaseTime"] = left_lease_time
        if status is not UNSET:
            field_dict["status"] = status
        if ip_long is not UNSET:
            field_dict["ipLong"] = ip_long

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        ip_address = d.pop("ipAddress", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        name = d.pop("name", UNSET)

        showing_type = d.pop("showingType", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        net_id = d.pop("netId", UNSET)

        net_name = d.pop("netName", UNSET)

        server_name = d.pop("serverName", UNSET)

        server_mac = d.pop("serverMac", UNSET)

        server_stack_id = d.pop("serverStackId", UNSET)

        left_lease_time = d.pop("leftLeaseTime", UNSET)

        status = d.pop("status", UNSET)

        ip_long = d.pop("ipLong", UNSET)

        dhcp_user_vo = cls(
            type_=type_,
            ip_address=ip_address,
            mac_address=mac_address,
            name=name,
            showing_type=showing_type,
            model=model,
            model_version=model_version,
            net_id=net_id,
            net_name=net_name,
            server_name=server_name,
            server_mac=server_mac,
            server_stack_id=server_stack_id,
            left_lease_time=left_lease_time,
            status=status,
            ip_long=ip_long,
        )

        dhcp_user_vo.additional_properties = d
        return dhcp_user_vo

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
