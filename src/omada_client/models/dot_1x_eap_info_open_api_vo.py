from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dot_1x_eap_port_info_open_api_vo import Dot1XEapPortInfoOpenApiVO


T = TypeVar("T", bound="Dot1XEapInfoOpenApiVO")


@_attrs_define
class Dot1XEapInfoOpenApiVO:
    """
    Attributes:
        name (str | Unset): EAP name
        mac (str | Unset): EAP MAC address
        model (str | Unset): EAP model
        version (str | Unset): EAP firmwareVersion
        status (str | Unset): Device status
        status_category (int | Unset): Device status category, 0: Disconnected, 1: Connected, 2: Pending,3: Heartbeat
            Missed, 4: Isolated
        ports (list[Dot1XEapPortInfoOpenApiVO] | Unset): EAP port information
    """

    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    version: str | Unset = UNSET
    status: str | Unset = UNSET
    status_category: int | Unset = UNSET
    ports: list[Dot1XEapPortInfoOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mac = self.mac

        model = self.model

        version = self.version

        status = self.status

        status_category = self.status_category

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
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if version is not UNSET:
            field_dict["version"] = version
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if ports is not UNSET:
            field_dict["ports"] = ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dot_1x_eap_port_info_open_api_vo import (
            Dot1XEapPortInfoOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        version = d.pop("version", UNSET)

        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        _ports = d.pop("ports", UNSET)
        ports: list[Dot1XEapPortInfoOpenApiVO] | Unset = UNSET
        if _ports is not UNSET:
            ports = []
            for ports_item_data in _ports:
                ports_item = Dot1XEapPortInfoOpenApiVO.from_dict(ports_item_data)

                ports.append(ports_item)

        dot_1x_eap_info_open_api_vo = cls(
            name=name,
            mac=mac,
            model=model,
            version=version,
            status=status,
            status_category=status_category,
            ports=ports,
        )

        dot_1x_eap_info_open_api_vo.additional_properties = d
        return dot_1x_eap_info_open_api_vo

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
