from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanList")


@_attrs_define
class WanList:
    """The WAN list of gateway

    Attributes:
        port_id (str | Unset): Wan port ID.
        port_name (str | Unset): Wan port name.
        enable (int | Unset): IPv6 enable. 0:"Disable", 1:"Enable"
        network_id (str | Unset): If networkId is not null, indicates this wan is used by specific "Lan Network".
        proto (int | Unset): IPv6 connection type of wan port. Includes: 0:"static", 1:"dynamic", 2:"pppoe",
            3:"6to4Tunnel", 4:"bridge", 7:"pppoa", 8:"ipoa". Only type is "bridge", can be selected by passthrough(Lan
            Network mode)
        pd_enable (int | Unset): Prefix Delegation. 0:"Disable", 1:"Enable"(Default)
        prefix (str | Unset): True prefix of wan port.
        pd_size (int | Unset): Prefix size
    """

    port_id: str | Unset = UNSET
    port_name: str | Unset = UNSET
    enable: int | Unset = UNSET
    network_id: str | Unset = UNSET
    proto: int | Unset = UNSET
    pd_enable: int | Unset = UNSET
    prefix: str | Unset = UNSET
    pd_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_id = self.port_id

        port_name = self.port_name

        enable = self.enable

        network_id = self.network_id

        proto = self.proto

        pd_enable = self.pd_enable

        prefix = self.prefix

        pd_size = self.pd_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_id is not UNSET:
            field_dict["portId"] = port_id
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if enable is not UNSET:
            field_dict["enable"] = enable
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if proto is not UNSET:
            field_dict["proto"] = proto
        if pd_enable is not UNSET:
            field_dict["pdEnable"] = pd_enable
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if pd_size is not UNSET:
            field_dict["pdSize"] = pd_size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port_id = d.pop("portId", UNSET)

        port_name = d.pop("portName", UNSET)

        enable = d.pop("enable", UNSET)

        network_id = d.pop("networkId", UNSET)

        proto = d.pop("proto", UNSET)

        pd_enable = d.pop("pdEnable", UNSET)

        prefix = d.pop("prefix", UNSET)

        pd_size = d.pop("pdSize", UNSET)

        wan_list = cls(
            port_id=port_id,
            port_name=port_name,
            enable=enable,
            network_id=network_id,
            proto=proto,
            pd_enable=pd_enable,
            prefix=prefix,
            pd_size=pd_size,
        )

        wan_list.additional_properties = d
        return wan_list

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
