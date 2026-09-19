from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgPortStatBrief")


@_attrs_define
class OsgPortStatBrief:
    """A list of device port status info for SdWan Member.

    Attributes:
        mode (int): The mode whether the port works as a WAN or LAN.
        port (int | Unset): The port sequence number of the device.
        name (str | Unset): The port name of the osg.
        link_status (int | Unset): The status of link connection.
        public_ip (bool | Unset): Whether the device has a public IP.
        wan_ip (str | Unset): The wan IP of the device.
        port_uuid (str | Unset): The UUID of port.
    """

    mode: int
    port: int | Unset = UNSET
    name: str | Unset = UNSET
    link_status: int | Unset = UNSET
    public_ip: bool | Unset = UNSET
    wan_ip: str | Unset = UNSET
    port_uuid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        port = self.port

        name = self.name

        link_status = self.link_status

        public_ip = self.public_ip

        wan_ip = self.wan_ip

        port_uuid = self.port_uuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip
        if wan_ip is not UNSET:
            field_dict["wanIp"] = wan_ip
        if port_uuid is not UNSET:
            field_dict["portUuid"] = port_uuid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        public_ip = d.pop("publicIp", UNSET)

        wan_ip = d.pop("wanIp", UNSET)

        port_uuid = d.pop("portUuid", UNSET)

        osg_port_stat_brief = cls(
            mode=mode,
            port=port,
            name=name,
            link_status=link_status,
            public_ip=public_ip,
            wan_ip=wan_ip,
            port_uuid=port_uuid,
        )

        osg_port_stat_brief.additional_properties = d
        return osg_port_stat_brief

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
