from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LanPortMappingVO")


@_attrs_define
class LanPortMappingVO:
    """
    Attributes:
        dst_port (str | Unset):
        src_ports (list[str] | Unset):
    """

    dst_port: str | Unset = UNSET
    src_ports: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dst_port = self.dst_port

        src_ports: list[str] | Unset = UNSET
        if not isinstance(self.src_ports, Unset):
            src_ports = self.src_ports

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dst_port is not UNSET:
            field_dict["dstPort"] = dst_port
        if src_ports is not UNSET:
            field_dict["srcPorts"] = src_ports

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dst_port = d.pop("dstPort", UNSET)

        src_ports = cast(list[str], d.pop("srcPorts", UNSET))

        lan_port_mapping_vo = cls(
            dst_port=dst_port,
            src_ports=src_ports,
        )

        lan_port_mapping_vo.additional_properties = d
        return lan_port_mapping_vo

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
