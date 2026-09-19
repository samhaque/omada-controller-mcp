from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidDhcpOptionOpenApiVO")


@_attrs_define
class SsidDhcpOptionOpenApiVO:
    """SSID DHCP Option 82 config.

    Attributes:
        dhcp_enable (bool | Unset): SSID DHCP Option 82 global config status. True: enable, false: disable.
        format_ (int | Unset): SSID DHCP Option 82 format config; It should be a value as follows: 0: ASCII; 1: Binary.
        delimiter (str | Unset): SSID DHCP Option 82 delimiter config (A single arbitrary ASCII character is
            acceptable).
        circuit_id (list[int] | Unset): SSID DHCP Option 82 Circuit-ID config. Circuit-ID is an array formed in the
            selected order, with each array element corresponding to the following enumeration values: 1: VLAN-ID; 2: AP
            Radio Mac-Address; 3: SSID-Type; 4: SSID-Name; 5: AP Ethernet MAC address; 6: Site-Name. As in the example
            [3,1,2,4], the following enumeration values are selected sequentially on the page: SSID-Type, VLAN-ID, AP Radio
            Mac-Address and SSID-Name.
        remote_id (list[int] | Unset): SSID DHCP Option 82 Remote-ID config. Remote-ID is an array formed in the
            selected order, with each array element corresponding to the following enumeration values: 1: VLAN-ID; 2: AP
            Radio Mac-Address; 3: SSID-Type; 4: SSID-Name; 5: AP Ethernet MAC address; 6: Site-Name. As in the example
            [3,1,2,4], the following enumeration values are selected sequentially on the page: SSID-Type, VLAN-ID, AP Radio
            Mac-Address and SSID-Name.
    """

    dhcp_enable: bool | Unset = UNSET
    format_: int | Unset = UNSET
    delimiter: str | Unset = UNSET
    circuit_id: list[int] | Unset = UNSET
    remote_id: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dhcp_enable = self.dhcp_enable

        format_ = self.format_

        delimiter = self.delimiter

        circuit_id: list[int] | Unset = UNSET
        if not isinstance(self.circuit_id, Unset):
            circuit_id = self.circuit_id

        remote_id: list[int] | Unset = UNSET
        if not isinstance(self.remote_id, Unset):
            remote_id = self.remote_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dhcp_enable is not UNSET:
            field_dict["dhcpEnable"] = dhcp_enable
        if format_ is not UNSET:
            field_dict["format"] = format_
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter
        if circuit_id is not UNSET:
            field_dict["circuitId"] = circuit_id
        if remote_id is not UNSET:
            field_dict["remoteId"] = remote_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dhcp_enable = d.pop("dhcpEnable", UNSET)

        format_ = d.pop("format", UNSET)

        delimiter = d.pop("delimiter", UNSET)

        circuit_id = cast(list[int], d.pop("circuitId", UNSET))

        remote_id = cast(list[int], d.pop("remoteId", UNSET))

        ssid_dhcp_option_open_api_vo = cls(
            dhcp_enable=dhcp_enable,
            format_=format_,
            delimiter=delimiter,
            circuit_id=circuit_id,
            remote_id=remote_id,
        )

        ssid_dhcp_option_open_api_vo.additional_properties = d
        return ssid_dhcp_option_open_api_vo

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
