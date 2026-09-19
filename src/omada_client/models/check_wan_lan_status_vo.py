from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_wan_lan_status_vo_port_name import CheckWanLanStatusVOPortName
    from ..models.osg_wan_status_vo import OsgWanStatusVO


T = TypeVar("T", bound="CheckWanLanStatusVO")


@_attrs_define
class CheckWanLanStatusVO:
    """Internet Detail.

    Attributes:
        port_name (CheckWanLanStatusVOPortName | Unset):
        network_comptent (int | Unset):
        adopted_gateway (bool | Unset):
        support_ipv_6 (int | Unset):
        wan_list (list[OsgWanStatusVO] | Unset):
        iptv_ports (list[str] | Unset):
        pre_osg_model (int | Unset):
        osg_add_in_advance (bool | Unset):
        wireless_router (bool | Unset):
        model (str | Unset):
        model_version (str | Unset):
        has_gateway (bool | Unset):
    """

    port_name: CheckWanLanStatusVOPortName | Unset = UNSET
    network_comptent: int | Unset = UNSET
    adopted_gateway: bool | Unset = UNSET
    support_ipv_6: int | Unset = UNSET
    wan_list: list[OsgWanStatusVO] | Unset = UNSET
    iptv_ports: list[str] | Unset = UNSET
    pre_osg_model: int | Unset = UNSET
    osg_add_in_advance: bool | Unset = UNSET
    wireless_router: bool | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    has_gateway: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port_name: dict[str, Any] | Unset = UNSET
        if not isinstance(self.port_name, Unset):
            port_name = self.port_name.to_dict()

        network_comptent = self.network_comptent

        adopted_gateway = self.adopted_gateway

        support_ipv_6 = self.support_ipv_6

        wan_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_list, Unset):
            wan_list = []
            for wan_list_item_data in self.wan_list:
                wan_list_item = wan_list_item_data.to_dict()
                wan_list.append(wan_list_item)

        iptv_ports: list[str] | Unset = UNSET
        if not isinstance(self.iptv_ports, Unset):
            iptv_ports = self.iptv_ports

        pre_osg_model = self.pre_osg_model

        osg_add_in_advance = self.osg_add_in_advance

        wireless_router = self.wireless_router

        model = self.model

        model_version = self.model_version

        has_gateway = self.has_gateway

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port_name is not UNSET:
            field_dict["portName"] = port_name
        if network_comptent is not UNSET:
            field_dict["networkComptent"] = network_comptent
        if adopted_gateway is not UNSET:
            field_dict["adoptedGateway"] = adopted_gateway
        if support_ipv_6 is not UNSET:
            field_dict["supportIpv6"] = support_ipv_6
        if wan_list is not UNSET:
            field_dict["wanList"] = wan_list
        if iptv_ports is not UNSET:
            field_dict["iptvPorts"] = iptv_ports
        if pre_osg_model is not UNSET:
            field_dict["preOsgModel"] = pre_osg_model
        if osg_add_in_advance is not UNSET:
            field_dict["osgAddInAdvance"] = osg_add_in_advance
        if wireless_router is not UNSET:
            field_dict["wirelessRouter"] = wireless_router
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if has_gateway is not UNSET:
            field_dict["hasGateway"] = has_gateway

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.check_wan_lan_status_vo_port_name import (
            CheckWanLanStatusVOPortName,
        )
        from ..models.osg_wan_status_vo import OsgWanStatusVO

        d = dict(src_dict)
        _port_name = d.pop("portName", UNSET)
        port_name: CheckWanLanStatusVOPortName | Unset
        if isinstance(_port_name, Unset):
            port_name = UNSET
        else:
            port_name = CheckWanLanStatusVOPortName.from_dict(_port_name)

        network_comptent = d.pop("networkComptent", UNSET)

        adopted_gateway = d.pop("adoptedGateway", UNSET)

        support_ipv_6 = d.pop("supportIpv6", UNSET)

        _wan_list = d.pop("wanList", UNSET)
        wan_list: list[OsgWanStatusVO] | Unset = UNSET
        if _wan_list is not UNSET:
            wan_list = []
            for wan_list_item_data in _wan_list:
                wan_list_item = OsgWanStatusVO.from_dict(wan_list_item_data)

                wan_list.append(wan_list_item)

        iptv_ports = cast(list[str], d.pop("iptvPorts", UNSET))

        pre_osg_model = d.pop("preOsgModel", UNSET)

        osg_add_in_advance = d.pop("osgAddInAdvance", UNSET)

        wireless_router = d.pop("wirelessRouter", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        has_gateway = d.pop("hasGateway", UNSET)

        check_wan_lan_status_vo = cls(
            port_name=port_name,
            network_comptent=network_comptent,
            adopted_gateway=adopted_gateway,
            support_ipv_6=support_ipv_6,
            wan_list=wan_list,
            iptv_ports=iptv_ports,
            pre_osg_model=pre_osg_model,
            osg_add_in_advance=osg_add_in_advance,
            wireless_router=wireless_router,
            model=model,
            model_version=model_version,
            has_gateway=has_gateway,
        )

        check_wan_lan_status_vo.additional_properties = d
        return check_wan_lan_status_vo

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
