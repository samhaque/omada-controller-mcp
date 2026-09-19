from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_port_info import ContentPortInfo


T = TypeVar("T", bound="StatusContent")


@_attrs_define
class StatusContent:
    """
    Attributes:
        name (bool | Unset): Whether to query device model name.
        uptime (bool | Unset): Whether to query device boot time.
        version (bool | Unset): Whether to query device firmware version.
        mac (bool | Unset): Whether to query device MAC address.
        ports (list[ContentPortInfo] | Unset):
    """

    name: bool | Unset = UNSET
    uptime: bool | Unset = UNSET
    version: bool | Unset = UNSET
    mac: bool | Unset = UNSET
    ports: list[ContentPortInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        uptime = self.uptime

        version = self.version

        mac = self.mac

        ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = []
            for ports_item_data in self.ports:
                ports_item = ports_item_data.to_dict()
                ports.append(ports_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if version is not UNSET:
            field_dict["version"] = version
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.content_port_info import ContentPortInfo

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        uptime = d.pop("uptime", UNSET)

        version = d.pop("version", UNSET)

        mac = d.pop("mac", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[ContentPortInfo] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = ContentPortInfo.from_dict(ports_item_data)

                ports.append(ports_item)

        status_content = cls(
            name=name,
            uptime=uptime,
            version=version,
            mac=mac,
            ports=ports,
        )

        status_content.additional_properties = d
        return status_content

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
