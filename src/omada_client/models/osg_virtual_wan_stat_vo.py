from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_virtual_wan_ipv_4_config_vo import OsgVirtualWanIpv4ConfigVO


T = TypeVar("T", bound="OsgVirtualWanStatVO")


@_attrs_define
class OsgVirtualWanStatVO:
    """
    Attributes:
        virtual_wan_id (str | Unset): Virtual Wan Id
        name (str | Unset): Virtual wan name
        status (int | Unset): Virtual Wan status, 0-disconnected; 1-connected;
        internet_state (int | Unset): Virtual Wan internet state, 0-disconnected; 1-connected;
        online_detection (int | Unset):
        type_ (int | Unset):
        proto (str | Unset): Virtual WAN ipv4 proto type.
        dsl_modulation_type (int | Unset):
        annex_type (int | Unset):
        line_status (int | Unset):
        mac (str | Unset):
        wan_port_ipv_4_config (OsgVirtualWanIpv4ConfigVO | Unset):
    """

    virtual_wan_id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: int | Unset = UNSET
    internet_state: int | Unset = UNSET
    online_detection: int | Unset = UNSET
    type_: int | Unset = UNSET
    proto: str | Unset = UNSET
    dsl_modulation_type: int | Unset = UNSET
    annex_type: int | Unset = UNSET
    line_status: int | Unset = UNSET
    mac: str | Unset = UNSET
    wan_port_ipv_4_config: OsgVirtualWanIpv4ConfigVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        virtual_wan_id = self.virtual_wan_id

        name = self.name

        status = self.status

        internet_state = self.internet_state

        online_detection = self.online_detection

        type_ = self.type_

        proto = self.proto

        dsl_modulation_type = self.dsl_modulation_type

        annex_type = self.annex_type

        line_status = self.line_status

        mac = self.mac

        wan_port_ipv_4_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_port_ipv_4_config, Unset):
            wan_port_ipv_4_config = self.wan_port_ipv_4_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if virtual_wan_id is not UNSET:
            field_dict["virtualWanId"] = virtual_wan_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if internet_state is not UNSET:
            field_dict["internetState"] = internet_state
        if online_detection is not UNSET:
            field_dict["onlineDetection"] = online_detection
        if type_ is not UNSET:
            field_dict["type"] = type_
        if proto is not UNSET:
            field_dict["proto"] = proto
        if dsl_modulation_type is not UNSET:
            field_dict["dslModulationType"] = dsl_modulation_type
        if annex_type is not UNSET:
            field_dict["annexType"] = annex_type
        if line_status is not UNSET:
            field_dict["lineStatus"] = line_status
        if mac is not UNSET:
            field_dict["mac"] = mac
        if wan_port_ipv_4_config is not UNSET:
            field_dict["wanPortIpv4Config"] = wan_port_ipv_4_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_virtual_wan_ipv_4_config_vo import (
            OsgVirtualWanIpv4ConfigVO,
        )

        d = dict(src_dict)
        virtual_wan_id = d.pop("virtualWanId", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        internet_state = d.pop("internetState", UNSET)

        online_detection = d.pop("onlineDetection", UNSET)

        type_ = d.pop("type", UNSET)

        proto = d.pop("proto", UNSET)

        dsl_modulation_type = d.pop("dslModulationType", UNSET)

        annex_type = d.pop("annexType", UNSET)

        line_status = d.pop("lineStatus", UNSET)

        mac = d.pop("mac", UNSET)

        _wan_port_ipv_4_config = d.pop("wanPortIpv4Config", UNSET)
        wan_port_ipv_4_config: OsgVirtualWanIpv4ConfigVO | Unset
        if isinstance(_wan_port_ipv_4_config, Unset):
            wan_port_ipv_4_config = UNSET
        else:
            wan_port_ipv_4_config = OsgVirtualWanIpv4ConfigVO.from_dict(
                _wan_port_ipv_4_config
            )

        osg_virtual_wan_stat_vo = cls(
            virtual_wan_id=virtual_wan_id,
            name=name,
            status=status,
            internet_state=internet_state,
            online_detection=online_detection,
            type_=type_,
            proto=proto,
            dsl_modulation_type=dsl_modulation_type,
            annex_type=annex_type,
            line_status=line_status,
            mac=mac,
            wan_port_ipv_4_config=wan_port_ipv_4_config,
        )

        osg_virtual_wan_stat_vo.additional_properties = d
        return osg_virtual_wan_stat_vo

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
