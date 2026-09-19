from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_ports import DevicePorts


T = TypeVar("T", bound="PortDeviceDetail")


@_attrs_define
class PortDeviceDetail:
    """
    Attributes:
        type_ (str | Unset): Device type. "gateway", "switch"
        mac (str | Unset): Device mac.
        name (str | Unset): Device name.
        site (str | Unset): Site ID
        model (str | Unset): Device model.
        model_version (str | Unset): Device model version.
        hw_version (str | Unset): Device hardware version.
        status (int | Unset): Device status.
        sn (str | Unset): Device SN code.
        ports (DevicePorts | Unset): Device ports info.
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    site: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    status: int | Unset = UNSET
    sn: str | Unset = UNSET
    ports: DevicePorts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        site = self.site

        model = self.model

        model_version = self.model_version

        hw_version = self.hw_version

        status = self.status

        sn = self.sn

        ports: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ports, Unset):
            ports = self.ports.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if site is not UNSET:
            field_dict["site"] = site
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if status is not UNSET:
            field_dict["status"] = status
        if sn is not UNSET:
            field_dict["sn"] = sn
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_ports import DevicePorts

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        site = d.pop("site", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        status = d.pop("status", UNSET)

        sn = d.pop("sn", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: DevicePorts | Unset
        if isinstance(_ports, Unset):
            ports = UNSET
        else:
            ports = DevicePorts.from_dict(_ports)

        port_device_detail = cls(
            type_=type_,
            mac=mac,
            name=name,
            site=site,
            model=model,
            model_version=model_version,
            hw_version=hw_version,
            status=status,
            sn=sn,
            ports=ports,
        )

        port_device_detail.additional_properties = d
        return port_device_detail

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
