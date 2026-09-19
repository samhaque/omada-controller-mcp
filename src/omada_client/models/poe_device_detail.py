from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_poe_ports import DevicePoePorts


T = TypeVar("T", bound="PoeDeviceDetail")


@_attrs_define
class PoeDeviceDetail:
    """
    Attributes:
        type_ (str | Unset): Device type. "gateway", "switch"
        mac (str | Unset): Device MAC.
        name (str | Unset): Device name.
        site (str | Unset): Site ID
        model (str | Unset): Device model.
        model_version (str | Unset): Device model version.
        hw_version (str | Unset): Device hardware version.
        firmware_version (str | Unset): Device firmware version.
        status (int | Unset): Device status.
        sn (str | Unset): Device SN code.
        combined_gateway (bool | Unset): Indicates whether it is a combined-gateway.
        poe_port (DevicePoePorts | Unset): Device poe ports info.
    """

    type_: str | Unset = UNSET
    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    site: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    firmware_version: str | Unset = UNSET
    status: int | Unset = UNSET
    sn: str | Unset = UNSET
    combined_gateway: bool | Unset = UNSET
    poe_port: DevicePoePorts | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        mac = self.mac

        name = self.name

        site = self.site

        model = self.model

        model_version = self.model_version

        hw_version = self.hw_version

        firmware_version = self.firmware_version

        status = self.status

        sn = self.sn

        combined_gateway = self.combined_gateway

        poe_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.poe_port, Unset):
            poe_port = self.poe_port.to_dict()

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
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if status is not UNSET:
            field_dict["status"] = status
        if sn is not UNSET:
            field_dict["sn"] = sn
        if combined_gateway is not UNSET:
            field_dict["combinedGateway"] = combined_gateway
        if poe_port is not UNSET:
            field_dict["poePort"] = poe_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_poe_ports import DevicePoePorts

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        site = d.pop("site", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        status = d.pop("status", UNSET)

        sn = d.pop("sn", UNSET)

        combined_gateway = d.pop("combinedGateway", UNSET)

        _poe_port = d.pop("poePort", UNSET)
        poe_port: DevicePoePorts | Unset
        if isinstance(_poe_port, Unset):
            poe_port = UNSET
        else:
            poe_port = DevicePoePorts.from_dict(_poe_port)

        poe_device_detail = cls(
            type_=type_,
            mac=mac,
            name=name,
            site=site,
            model=model,
            model_version=model_version,
            hw_version=hw_version,
            firmware_version=firmware_version,
            status=status,
            sn=sn,
            combined_gateway=combined_gateway,
            poe_port=poe_port,
        )

        poe_device_detail.additional_properties = d
        return poe_device_detail

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
