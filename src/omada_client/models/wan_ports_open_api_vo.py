from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WanPortsOpenApiVO")


@_attrs_define
class WanPortsOpenApiVO:
    """
    Attributes:
        enable (bool): whether to enable wan Settings Override
        pre_osg_model (int | Unset): select gateway model, you can query option from 'Get supported gateway model list
            for pre-configuration'. If already choose or adopted gateway,use current gateway model id.
        wan_port_num (int | Unset): custom number of wan ports, only for preOsgModel at 2
        port_uuids (list[str] | Unset): select wan ports to open, and other wan ports will be closed, you can get port
            uuid list from 'Get internet basic info'.
        force_change (bool | Unset): Force change wan ports. If set true, wan ports will be modified without check, and
            the gateway will reboot. If set false, consequence will be checked and return check result.
    """

    enable: bool
    pre_osg_model: int | Unset = UNSET
    wan_port_num: int | Unset = UNSET
    port_uuids: list[str] | Unset = UNSET
    force_change: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        pre_osg_model = self.pre_osg_model

        wan_port_num = self.wan_port_num

        port_uuids: list[str] | Unset = UNSET
        if not isinstance(self.port_uuids, Unset):
            port_uuids = self.port_uuids

        force_change = self.force_change

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if pre_osg_model is not UNSET:
            field_dict["preOsgModel"] = pre_osg_model
        if wan_port_num is not UNSET:
            field_dict["wanPortNum"] = wan_port_num
        if port_uuids is not UNSET:
            field_dict["portUuids"] = port_uuids
        if force_change is not UNSET:
            field_dict["forceChange"] = force_change

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        pre_osg_model = d.pop("preOsgModel", UNSET)

        wan_port_num = d.pop("wanPortNum", UNSET)

        port_uuids = cast(list[str], d.pop("portUuids", UNSET))

        force_change = d.pop("forceChange", UNSET)

        wan_ports_open_api_vo = cls(
            enable=enable,
            pre_osg_model=pre_osg_model,
            wan_port_num=wan_port_num,
            port_uuids=port_uuids,
            force_change=force_change,
        )

        wan_ports_open_api_vo.additional_properties = d
        return wan_ports_open_api_vo

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
