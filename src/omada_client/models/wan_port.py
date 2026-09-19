from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanPort")


@_attrs_define
class WanPort:
    """Wan Port List

    Attributes:
        port (str | Unset): Port Id
        name (str | Unset): Port Name
        status (int | Unset): Port Status
        internet_state (int | Unset): Port Internet State
        online_detection (int | Unset): Port Online Detection
        link_speed (int | Unset): Link Speed
        duplex (int | Unset): Duplex
        health_level (int | Unset): Health Level
        wireless (bool | Unset): Whether the port is wireless.
        tx_rate (int | Unset): Rx Rate
    """

    port: str | Unset = UNSET
    name: str | Unset = UNSET
    status: int | Unset = UNSET
    internet_state: int | Unset = UNSET
    online_detection: int | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    health_level: int | Unset = UNSET
    wireless: bool | Unset = UNSET
    tx_rate: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        status = self.status

        internet_state = self.internet_state

        online_detection = self.online_detection

        link_speed = self.link_speed

        duplex = self.duplex

        health_level = self.health_level

        wireless = self.wireless

        tx_rate = self.tx_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if internet_state is not UNSET:
            field_dict["internetState"] = internet_state
        if online_detection is not UNSET:
            field_dict["onlineDetection"] = online_detection
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if health_level is not UNSET:
            field_dict["healthLevel"] = health_level
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        internet_state = d.pop("internetState", UNSET)

        online_detection = d.pop("onlineDetection", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        health_level = d.pop("healthLevel", UNSET)

        wireless = d.pop("wireless", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        wan_port = cls(
            port=port,
            name=name,
            status=status,
            internet_state=internet_state,
            online_detection=online_detection,
            link_speed=link_speed,
            duplex=duplex,
            health_level=health_level,
            wireless=wireless,
            tx_rate=tx_rate,
        )

        wan_port.additional_properties = d
        return wan_port

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
