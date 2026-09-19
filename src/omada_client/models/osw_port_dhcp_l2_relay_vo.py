from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswPortDhcpL2RelayVO")


@_attrs_define
class OswPortDhcpL2RelayVO:
    """Dhcp L2 Relay Setting

    Attributes:
        enable (bool | Unset): Enable
        format_ (int | Unset): Format should be a value as follows: 0: Normal; 1: Private
        circuit_id (str | Unset): Circuit ID
        remote_id (str | Unset): Remote ID
    """

    enable: bool | Unset = UNSET
    format_: int | Unset = UNSET
    circuit_id: str | Unset = UNSET
    remote_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        format_ = self.format_

        circuit_id = self.circuit_id

        remote_id = self.remote_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if format_ is not UNSET:
            field_dict["format"] = format_
        if circuit_id is not UNSET:
            field_dict["circuitId"] = circuit_id
        if remote_id is not UNSET:
            field_dict["remoteId"] = remote_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        format_ = d.pop("format", UNSET)

        circuit_id = d.pop("circuitId", UNSET)

        remote_id = d.pop("remoteId", UNSET)

        osw_port_dhcp_l2_relay_vo = cls(
            enable=enable,
            format_=format_,
            circuit_id=circuit_id,
            remote_id=remote_id,
        )

        osw_port_dhcp_l2_relay_vo.additional_properties = d
        return osw_port_dhcp_l2_relay_vo

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
