from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswPortAndLagNetworkVO")


@_attrs_define
class OswPortAndLagNetworkVO:
    """OswPortAndLagNetworkVO

    Attributes:
        native_ports (list[int] | Unset): Native Vlan Port List, for example [1, 2]
        native_st_ports (list[str] | Unset): Native Vlan Standard Port List, for example ["1/0/1", "1/0/2"]
        native_lags (list[int] | Unset): Native Vlan Lag List, for example [1, 2]
        tag_ports (list[int] | Unset): Tag Vlan Port List, for example [1, 2]
        tag_st_ports (list[str] | Unset): Tag Vlan Standard Port List, for example ["1/0/1", "1/0/2"]
        tag_lags (list[int] | Unset): Tag Vlan Lag List, for example [1, 2]
        untag_ports (list[int] | Unset): Untag Vlan Port List, for example [1, 2]
        untag_st_ports (list[str] | Unset): Untag Vlan Standard Port List, for example ["1/0/1", "1/0/2"]
        untag_lags (list[int] | Unset): Untag Vlan Lag List, for example [1, 2]
        vlan (int | Unset): Vlan ID
        ipaddr (str | Unset): IP address.
        mode (int | Unset): Ip address mode, it should be a value as follows: 0:static 1:dynamic
    """

    native_ports: list[int] | Unset = UNSET
    native_st_ports: list[str] | Unset = UNSET
    native_lags: list[int] | Unset = UNSET
    tag_ports: list[int] | Unset = UNSET
    tag_st_ports: list[str] | Unset = UNSET
    tag_lags: list[int] | Unset = UNSET
    untag_ports: list[int] | Unset = UNSET
    untag_st_ports: list[str] | Unset = UNSET
    untag_lags: list[int] | Unset = UNSET
    vlan: int | Unset = UNSET
    ipaddr: str | Unset = UNSET
    mode: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        native_ports: list[int] | Unset = UNSET
        if not isinstance(self.native_ports, Unset):
            native_ports = self.native_ports

        native_st_ports: list[str] | Unset = UNSET
        if not isinstance(self.native_st_ports, Unset):
            native_st_ports = self.native_st_ports

        native_lags: list[int] | Unset = UNSET
        if not isinstance(self.native_lags, Unset):
            native_lags = self.native_lags

        tag_ports: list[int] | Unset = UNSET
        if not isinstance(self.tag_ports, Unset):
            tag_ports = self.tag_ports

        tag_st_ports: list[str] | Unset = UNSET
        if not isinstance(self.tag_st_ports, Unset):
            tag_st_ports = self.tag_st_ports

        tag_lags: list[int] | Unset = UNSET
        if not isinstance(self.tag_lags, Unset):
            tag_lags = self.tag_lags

        untag_ports: list[int] | Unset = UNSET
        if not isinstance(self.untag_ports, Unset):
            untag_ports = self.untag_ports

        untag_st_ports: list[str] | Unset = UNSET
        if not isinstance(self.untag_st_ports, Unset):
            untag_st_ports = self.untag_st_ports

        untag_lags: list[int] | Unset = UNSET
        if not isinstance(self.untag_lags, Unset):
            untag_lags = self.untag_lags

        vlan = self.vlan

        ipaddr = self.ipaddr

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if native_ports is not UNSET:
            field_dict["nativePorts"] = native_ports
        if native_st_ports is not UNSET:
            field_dict["nativeStPorts"] = native_st_ports
        if native_lags is not UNSET:
            field_dict["nativeLags"] = native_lags
        if tag_ports is not UNSET:
            field_dict["tagPorts"] = tag_ports
        if tag_st_ports is not UNSET:
            field_dict["tagStPorts"] = tag_st_ports
        if tag_lags is not UNSET:
            field_dict["tagLags"] = tag_lags
        if untag_ports is not UNSET:
            field_dict["untagPorts"] = untag_ports
        if untag_st_ports is not UNSET:
            field_dict["untagStPorts"] = untag_st_ports
        if untag_lags is not UNSET:
            field_dict["untagLags"] = untag_lags
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        native_ports = cast(list[int], d.pop("nativePorts", UNSET))

        native_st_ports = cast(list[str], d.pop("nativeStPorts", UNSET))

        native_lags = cast(list[int], d.pop("nativeLags", UNSET))

        tag_ports = cast(list[int], d.pop("tagPorts", UNSET))

        tag_st_ports = cast(list[str], d.pop("tagStPorts", UNSET))

        tag_lags = cast(list[int], d.pop("tagLags", UNSET))

        untag_ports = cast(list[int], d.pop("untagPorts", UNSET))

        untag_st_ports = cast(list[str], d.pop("untagStPorts", UNSET))

        untag_lags = cast(list[int], d.pop("untagLags", UNSET))

        vlan = d.pop("vlan", UNSET)

        ipaddr = d.pop("ipaddr", UNSET)

        mode = d.pop("mode", UNSET)

        osw_port_and_lag_network_vo = cls(
            native_ports=native_ports,
            native_st_ports=native_st_ports,
            native_lags=native_lags,
            tag_ports=tag_ports,
            tag_st_ports=tag_st_ports,
            tag_lags=tag_lags,
            untag_ports=untag_ports,
            untag_st_ports=untag_st_ports,
            untag_lags=untag_lags,
            vlan=vlan,
            ipaddr=ipaddr,
            mode=mode,
        )

        osw_port_and_lag_network_vo.additional_properties = d
        return osw_port_and_lag_network_vo

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
