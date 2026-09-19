from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_lan_port_ipv_6_config_vo import OsgLanPortIpv6ConfigVO


T = TypeVar("T", bound="LanStatus")


@_attrs_define
class LanStatus:
    """
    Attributes:
        vlan (int | Unset): vlan
        lan_name (str | Unset): Lan name
        ip (str | Unset): Ip
        rx (int | Unset): Lan rx
        tx (int | Unset): Lan tx
        client_num (int | Unset): Lan client num
        lan_port_ipv_6_config (OsgLanPortIpv6ConfigVO | Unset):
    """

    vlan: int | Unset = UNSET
    lan_name: str | Unset = UNSET
    ip: str | Unset = UNSET
    rx: int | Unset = UNSET
    tx: int | Unset = UNSET
    client_num: int | Unset = UNSET
    lan_port_ipv_6_config: OsgLanPortIpv6ConfigVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vlan = self.vlan

        lan_name = self.lan_name

        ip = self.ip

        rx = self.rx

        tx = self.tx

        client_num = self.client_num

        lan_port_ipv_6_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.lan_port_ipv_6_config, Unset):
            lan_port_ipv_6_config = self.lan_port_ipv_6_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if lan_name is not UNSET:
            field_dict["lanName"] = lan_name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if client_num is not UNSET:
            field_dict["clientNum"] = client_num
        if lan_port_ipv_6_config is not UNSET:
            field_dict["lanPortIpv6Config"] = lan_port_ipv_6_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_lan_port_ipv_6_config_vo import (
            OsgLanPortIpv6ConfigVO,
        )

        d = dict(src_dict)
        vlan = d.pop("vlan", UNSET)

        lan_name = d.pop("lanName", UNSET)

        ip = d.pop("ip", UNSET)

        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        client_num = d.pop("clientNum", UNSET)

        _lan_port_ipv_6_config = d.pop("lanPortIpv6Config", UNSET)
        lan_port_ipv_6_config: OsgLanPortIpv6ConfigVO | Unset
        if isinstance(_lan_port_ipv_6_config, Unset):
            lan_port_ipv_6_config = UNSET
        else:
            lan_port_ipv_6_config = OsgLanPortIpv6ConfigVO.from_dict(
                _lan_port_ipv_6_config
            )

        lan_status = cls(
            vlan=vlan,
            lan_name=lan_name,
            ip=ip,
            rx=rx,
            tx=tx,
            client_num=client_num,
            lan_port_ipv_6_config=lan_port_ipv_6_config,
        )

        lan_status.additional_properties = d
        return lan_status

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
