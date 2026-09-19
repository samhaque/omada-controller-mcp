from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyDeviceClient")


@_attrs_define
class TopologyDeviceClient:
    """Device or Client In Topology.

    Attributes:
        mac (str | Unset): Device or Client MAC address, like AA-BB-CC-DD-EE-FF.
        name (str | Unset): Device or Client Name.
        ip (str | Unset): Device or Client Ip.
        model (str | Unset): Device model.
        show_model (str | Unset): Device model.
        model_version (str | Unset): Device model version.
        special_model (str | Unset): Special device model,for example:EAP225-Outdoor-1a20a950b8d950e8
        type_ (str | Unset): Type of Device
        stack_group (bool | Unset): Whether this node is stack or not
        omada_device_type (str | Unset): Type of omada device when it's type is other in topology
        uplink_mac (str | Unset): Uplink Device MAC address of client.
        group_type (int | Unset): Topology group type of client, 0：clientGroup  1：cameraGroup
        is_client (bool | Unset): Whether this entry is a client
        device_type (str | Unset): Type of Client
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    model: str | Unset = UNSET
    show_model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    special_model: str | Unset = UNSET
    type_: str | Unset = UNSET
    stack_group: bool | Unset = UNSET
    omada_device_type: str | Unset = UNSET
    uplink_mac: str | Unset = UNSET
    group_type: int | Unset = UNSET
    is_client: bool | Unset = UNSET
    device_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        ip = self.ip

        model = self.model

        show_model = self.show_model

        model_version = self.model_version

        special_model = self.special_model

        type_ = self.type_

        stack_group = self.stack_group

        omada_device_type = self.omada_device_type

        uplink_mac = self.uplink_mac

        group_type = self.group_type

        is_client = self.is_client

        device_type = self.device_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if model is not UNSET:
            field_dict["model"] = model
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if special_model is not UNSET:
            field_dict["specialModel"] = special_model
        if type_ is not UNSET:
            field_dict["type"] = type_
        if stack_group is not UNSET:
            field_dict["stackGroup"] = stack_group
        if omada_device_type is not UNSET:
            field_dict["omadaDeviceType"] = omada_device_type
        if uplink_mac is not UNSET:
            field_dict["uplinkMac"] = uplink_mac
        if group_type is not UNSET:
            field_dict["groupType"] = group_type
        if is_client is not UNSET:
            field_dict["isClient"] = is_client
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        model = d.pop("model", UNSET)

        show_model = d.pop("showModel", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        special_model = d.pop("specialModel", UNSET)

        type_ = d.pop("type", UNSET)

        stack_group = d.pop("stackGroup", UNSET)

        omada_device_type = d.pop("omadaDeviceType", UNSET)

        uplink_mac = d.pop("uplinkMac", UNSET)

        group_type = d.pop("groupType", UNSET)

        is_client = d.pop("isClient", UNSET)

        device_type = d.pop("deviceType", UNSET)

        topology_device_client = cls(
            mac=mac,
            name=name,
            ip=ip,
            model=model,
            show_model=show_model,
            model_version=model_version,
            special_model=special_model,
            type_=type_,
            stack_group=stack_group,
            omada_device_type=omada_device_type,
            uplink_mac=uplink_mac,
            group_type=group_type,
            is_client=is_client,
            device_type=device_type,
        )

        topology_device_client.additional_properties = d
        return topology_device_client

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
