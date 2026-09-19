from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlagCccResultVO")


@_attrs_define
class MlagCccResultVO:
    """M-LAG group members configuration check result

    Attributes:
        cfg_name (str | Unset): M-LAG group member configuration name
        path_type (int | Unset): M-LAG group member configuration path. It should be a value as follows:-1 : Settings ->
            CLI Configuration0 : Device configuration page -> config -> General -> Hash Algorithm1 : Device configuration
            page -> ports -> Profile Overrides -> Operation(Aggregating)2 : Device configuration page -> config -> Services
            -> Loopback Control -> Loopback Detection3 : Device configuration page -> ports -> Profile Overrides -> Loopback
            Control4 : Device configuration page -> config -> Services -> Loopback Control -> Spanning Tree5 : Device
            configuration page -> config -> Services -> Loopback Control -> CIST Priority6 : Device configuration page ->
            config -> Services -> Loopback Control -> MSTP Instance config7 : Device configuration page -> ports -> Profile
            Overrides -> Spanning Tree Config8 : Device configuration page -> ports -> Profile Overrides -> Loopback
            Control9 : Device configuration page -> config -> VLAN Interface10 : Settings -> Transmission -> VRRP ->
            Optional Settings11 : Settings -> Transmission -> VRRP12 : Settings -> Wired&Wireless Networks -> LAN ->
            Networks -> DHCP L2 Relay13 : Device configuration page -> ports -> LAG -> Profile14 : Settings ->
            Wired&Wireless Networks -> LAN -> Networks -> IGMP Snooping15 : Settings -> Wired&Wireless Networks -> LAN ->
            Networks -> MLD Snooping
        type_ (int | Unset): M-LAG group member configuration type. It should be a value as follows:1 : Critical2 :
            Significant
        ccc_rslt (str | Unset): The result of the M-LAG consistency check.
        local_val (str | Unset): The local configuration values for M-LAG consistency check.
        peer_val (str | Unset): The opposite-end configuration values for M-LAG consistency check.
    """

    cfg_name: str | Unset = UNSET
    path_type: int | Unset = UNSET
    type_: int | Unset = UNSET
    ccc_rslt: str | Unset = UNSET
    local_val: str | Unset = UNSET
    peer_val: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cfg_name = self.cfg_name

        path_type = self.path_type

        type_ = self.type_

        ccc_rslt = self.ccc_rslt

        local_val = self.local_val

        peer_val = self.peer_val

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cfg_name is not UNSET:
            field_dict["cfgName"] = cfg_name
        if path_type is not UNSET:
            field_dict["pathType"] = path_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if ccc_rslt is not UNSET:
            field_dict["cccRslt"] = ccc_rslt
        if local_val is not UNSET:
            field_dict["localVal"] = local_val
        if peer_val is not UNSET:
            field_dict["peerVal"] = peer_val

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        cfg_name = d.pop("cfgName", UNSET)

        path_type = d.pop("pathType", UNSET)

        type_ = d.pop("type", UNSET)

        ccc_rslt = d.pop("cccRslt", UNSET)

        local_val = d.pop("localVal", UNSET)

        peer_val = d.pop("peerVal", UNSET)

        mlag_ccc_result_vo = cls(
            cfg_name=cfg_name,
            path_type=path_type,
            type_=type_,
            ccc_rslt=ccc_rslt,
            local_val=local_val,
            peer_val=peer_val,
        )

        mlag_ccc_result_vo.additional_properties = d
        return mlag_ccc_result_vo

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
