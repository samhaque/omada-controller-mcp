from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_stand_port_vo import OswStandPortVO
    from ..models.osw_stat_down_link_vo import OswStatDownLinkVO
    from ..models.osw_stat_port_status_vo import OswStatPortStatusVO


T = TypeVar("T", bound="OswStatPortVO")


@_attrs_define
class OswStatPortVO:
    """Ports information

    Attributes:
        port (int | Unset): Port id
        name (str | Unset): Port name
        type_ (int | Unset): Type should be a value as follows: 1:Copper; 2:Combo; 3:SFP
        operation (str | Unset): Operation should be a value as follows: SWITCHING; MIRRORING; AGGREGATING
        port_status (OswStatPortStatusVO | Unset): Port Status
        downlink (OswStatDownLinkVO | Unset): Downlink devices of the port
        max_speed (int | Unset): Max speed supported by the port
        disable (bool | Unset): Whether the port is disabled
        config_stack (bool | Unset): Indicates whether the current port is configured as a stack port (joined a stack
            aggregation group)
        stack_ports_group_index (int | Unset): Number of the stacking port aggregation group to join
        config_mlag_peer_link (bool | Unset): Standard port information
        config_mlag_dad (bool | Unset):
        mad_used (bool | Unset):
        osw_stand_port (OswStandPortVO | Unset): Stack port aggregation group member port
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    type_: int | Unset = UNSET
    operation: str | Unset = UNSET
    port_status: OswStatPortStatusVO | Unset = UNSET
    downlink: OswStatDownLinkVO | Unset = UNSET
    max_speed: int | Unset = UNSET
    disable: bool | Unset = UNSET
    config_stack: bool | Unset = UNSET
    stack_ports_group_index: int | Unset = UNSET
    config_mlag_peer_link: bool | Unset = UNSET
    config_mlag_dad: bool | Unset = UNSET
    mad_used: bool | Unset = UNSET
    osw_stand_port: OswStandPortVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        type_ = self.type_

        operation = self.operation

        port_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_status, Unset):
            port_status = self.port_status.to_dict()

        downlink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.downlink, Unset):
            downlink = self.downlink.to_dict()

        max_speed = self.max_speed

        disable = self.disable

        config_stack = self.config_stack

        stack_ports_group_index = self.stack_ports_group_index

        config_mlag_peer_link = self.config_mlag_peer_link

        config_mlag_dad = self.config_mlag_dad

        mad_used = self.mad_used

        osw_stand_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.osw_stand_port, Unset):
            osw_stand_port = self.osw_stand_port.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if operation is not UNSET:
            field_dict["operation"] = operation
        if port_status is not UNSET:
            field_dict["portStatus"] = port_status
        if downlink is not UNSET:
            field_dict["downlink"] = downlink
        if max_speed is not UNSET:
            field_dict["maxSpeed"] = max_speed
        if disable is not UNSET:
            field_dict["disable"] = disable
        if config_stack is not UNSET:
            field_dict["configStack"] = config_stack
        if stack_ports_group_index is not UNSET:
            field_dict["stackPortsGroupIndex"] = stack_ports_group_index
        if config_mlag_peer_link is not UNSET:
            field_dict["configMlagPeerLink"] = config_mlag_peer_link
        if config_mlag_dad is not UNSET:
            field_dict["configMlagDad"] = config_mlag_dad
        if mad_used is not UNSET:
            field_dict["madUsed"] = mad_used
        if osw_stand_port is not UNSET:
            field_dict["oswStandPort"] = osw_stand_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_stand_port_vo import OswStandPortVO
        from ..models.osw_stat_down_link_vo import OswStatDownLinkVO
        from ..models.osw_stat_port_status_vo import (
            OswStatPortStatusVO,
        )

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        type_ = d.pop("type", UNSET)

        operation = d.pop("operation", UNSET)

        _port_status = d.pop("portStatus", UNSET)
        port_status: OswStatPortStatusVO | Unset
        if isinstance(_port_status, Unset):
            port_status = UNSET
        else:
            port_status = OswStatPortStatusVO.from_dict(_port_status)

        _downlink = d.pop("downlink", UNSET)
        downlink: OswStatDownLinkVO | Unset
        if isinstance(_downlink, Unset):
            downlink = UNSET
        else:
            downlink = OswStatDownLinkVO.from_dict(_downlink)

        max_speed = d.pop("maxSpeed", UNSET)

        disable = d.pop("disable", UNSET)

        config_stack = d.pop("configStack", UNSET)

        stack_ports_group_index = d.pop("stackPortsGroupIndex", UNSET)

        config_mlag_peer_link = d.pop("configMlagPeerLink", UNSET)

        config_mlag_dad = d.pop("configMlagDad", UNSET)

        mad_used = d.pop("madUsed", UNSET)

        _osw_stand_port = d.pop("oswStandPort", UNSET)
        osw_stand_port: OswStandPortVO | Unset
        if isinstance(_osw_stand_port, Unset):
            osw_stand_port = UNSET
        else:
            osw_stand_port = OswStandPortVO.from_dict(_osw_stand_port)

        osw_stat_port_vo = cls(
            port=port,
            name=name,
            type_=type_,
            operation=operation,
            port_status=port_status,
            downlink=downlink,
            max_speed=max_speed,
            disable=disable,
            config_stack=config_stack,
            stack_ports_group_index=stack_ports_group_index,
            config_mlag_peer_link=config_mlag_peer_link,
            config_mlag_dad=config_mlag_dad,
            mad_used=mad_used,
            osw_stand_port=osw_stand_port,
        )

        osw_stat_port_vo.additional_properties = d
        return osw_stat_port_vo

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
