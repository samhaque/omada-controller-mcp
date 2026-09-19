from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.port_info import PortInfo


T = TypeVar("T", bound="EasyManageOverviewInfo")


@_attrs_define
class EasyManageOverviewInfo:
    """
    Attributes:
        mac (str | Unset): Switch MAC address
        ip (str | Unset): Switch IP address
        model (str | Unset): Model
        firmware_version (str | Unset): Firmware Version e.g:2.5.0 Build 20190118 Rel. 64821
        version (str | Unset): Firmware Version e.g:2.5.0
        hw_version (str | Unset): Hardware Version
        uptime (str | Unset): Uptime
        port_list (list[PortInfo] | Unset): Port List
    """

    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    model: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    version: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    uptime: str | Unset = UNSET
    port_list: list[PortInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        ip = self.ip

        model = self.model

        firmware_version = self.firmware_version

        version = self.version

        hw_version = self.hw_version

        uptime = self.uptime

        port_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.port_list, Unset):
            port_list = []
            for port_list_item_data in self.port_list:
                port_list_item = port_list_item_data.to_dict()
                port_list.append(port_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if model is not UNSET:
            field_dict["model"] = model
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if version is not UNSET:
            field_dict["version"] = version
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if uptime is not UNSET:
            field_dict["uptime"] = uptime
        if port_list is not UNSET:
            field_dict["portList"] = port_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.port_info import PortInfo

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        model = d.pop("model", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        version = d.pop("version", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        uptime = d.pop("uptime", UNSET)

        _port_list = d.pop("portList", UNSET)
        port_list: list[PortInfo] | Unset = UNSET
        if _port_list is not UNSET:
            port_list = []
            for port_list_item_data in _port_list:
                port_list_item = PortInfo.from_dict(port_list_item_data)

                port_list.append(port_list_item)

        easy_manage_overview_info = cls(
            mac=mac,
            ip=ip,
            model=model,
            firmware_version=firmware_version,
            version=version,
            hw_version=hw_version,
            uptime=uptime,
            port_list=port_list,
        )

        easy_manage_overview_info.additional_properties = d
        return easy_manage_overview_info

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
