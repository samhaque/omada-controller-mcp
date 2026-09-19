from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_agg_health_dto import ClientAggHealthDTO
    from ..models.lan_port import LanPort
    from ..models.osw_up_info import OswUpInfo
    from ..models.wan_port import WanPort
    from ..models.wire_up_link import WireUpLink
    from ..models.wireless_up_link import WirelessUpLink


T = TypeVar("T", bound="TopologyOpenApiNodeVO")


@_attrs_define
class TopologyOpenApiNodeVO:
    """Topology Nodes

    Attributes:
        type_ (str | Unset): Device Type
        name (str | Unset): Device Name
        mac (str | Unset): Device Mac
        model (str | Unset): Device Model
        model_version (str | Unset): Device ModelVersion
        device_series_type (int | Unset): Device Series Type
        client_count (int | Unset): Client Count
        health_score (int | Unset): Health Score
        client_health (ClientAggHealthDTO | Unset): Client Health
        wired_up_link (WireUpLink | Unset): Wired UpLink Info
        wireless_up_link (WirelessUpLink | Unset): Wireless UpLink Info
        rd_mode_2_g (str | Unset): rdMode2g
        channel2g (int | Unset): channel2g
        rd_mode_5_g (str | Unset): rdMode5g
        channel5g (int | Unset): channel5g
        rd_mode_5_g_2 (str | Unset): rdMode5g2
        channel5g2 (int | Unset): channel5g2
        rd_mode_6_g (str | Unset): rdMode6g
        channel6g (int | Unset): channel6g
        support5g2 (bool | Unset): support5g2
        wan_ports (list[WanPort] | Unset): Wan Port List
        lan_ports (list[LanPort] | Unset): Lan Port List
        stack_group (bool | Unset): Stack Group
        stack_id (str | Unset): Stack Id
        upper_port (OswUpInfo | Unset): Upper Info of Switch
    """

    type_: str | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    device_series_type: int | Unset = UNSET
    client_count: int | Unset = UNSET
    health_score: int | Unset = UNSET
    client_health: ClientAggHealthDTO | Unset = UNSET
    wired_up_link: WireUpLink | Unset = UNSET
    wireless_up_link: WirelessUpLink | Unset = UNSET
    rd_mode_2_g: str | Unset = UNSET
    channel2g: int | Unset = UNSET
    rd_mode_5_g: str | Unset = UNSET
    channel5g: int | Unset = UNSET
    rd_mode_5_g_2: str | Unset = UNSET
    channel5g2: int | Unset = UNSET
    rd_mode_6_g: str | Unset = UNSET
    channel6g: int | Unset = UNSET
    support5g2: bool | Unset = UNSET
    wan_ports: list[WanPort] | Unset = UNSET
    lan_ports: list[LanPort] | Unset = UNSET
    stack_group: bool | Unset = UNSET
    stack_id: str | Unset = UNSET
    upper_port: OswUpInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        name = self.name

        mac = self.mac

        model = self.model

        model_version = self.model_version

        device_series_type = self.device_series_type

        client_count = self.client_count

        health_score = self.health_score

        client_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.client_health, Unset):
            client_health = self.client_health.to_dict()

        wired_up_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wired_up_link, Unset):
            wired_up_link = self.wired_up_link.to_dict()

        wireless_up_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_up_link, Unset):
            wireless_up_link = self.wireless_up_link.to_dict()

        rd_mode_2_g = self.rd_mode_2_g

        channel2g = self.channel2g

        rd_mode_5_g = self.rd_mode_5_g

        channel5g = self.channel5g

        rd_mode_5_g_2 = self.rd_mode_5_g_2

        channel5g2 = self.channel5g2

        rd_mode_6_g = self.rd_mode_6_g

        channel6g = self.channel6g

        support5g2 = self.support5g2

        wan_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_ports, Unset):
            wan_ports = []
            for wan_ports_item_data in self.wan_ports:
                wan_ports_item = wan_ports_item_data.to_dict()
                wan_ports.append(wan_ports_item)

        lan_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_ports, Unset):
            lan_ports = []
            for lan_ports_item_data in self.lan_ports:
                lan_ports_item = lan_ports_item_data.to_dict()
                lan_ports.append(lan_ports_item)

        stack_group = self.stack_group

        stack_id = self.stack_id

        upper_port: dict[str, Any] | Unset = UNSET
        if not isinstance(self.upper_port, Unset):
            upper_port = self.upper_port.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if device_series_type is not UNSET:
            field_dict["deviceSeriesType"] = device_series_type
        if client_count is not UNSET:
            field_dict["clientCount"] = client_count
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if client_health is not UNSET:
            field_dict["clientHealth"] = client_health
        if wired_up_link is not UNSET:
            field_dict["wiredUpLink"] = wired_up_link
        if wireless_up_link is not UNSET:
            field_dict["wirelessUpLink"] = wireless_up_link
        if rd_mode_2_g is not UNSET:
            field_dict["rdMode2g"] = rd_mode_2_g
        if channel2g is not UNSET:
            field_dict["channel2g"] = channel2g
        if rd_mode_5_g is not UNSET:
            field_dict["rdMode5g"] = rd_mode_5_g
        if channel5g is not UNSET:
            field_dict["channel5g"] = channel5g
        if rd_mode_5_g_2 is not UNSET:
            field_dict["rdMode5g2"] = rd_mode_5_g_2
        if channel5g2 is not UNSET:
            field_dict["channel5g2"] = channel5g2
        if rd_mode_6_g is not UNSET:
            field_dict["rdMode6g"] = rd_mode_6_g
        if channel6g is not UNSET:
            field_dict["channel6g"] = channel6g
        if support5g2 is not UNSET:
            field_dict["support5g2"] = support5g2
        if wan_ports is not UNSET:
            field_dict["wanPorts"] = wan_ports
        if lan_ports is not UNSET:
            field_dict["lanPorts"] = lan_ports
        if stack_group is not UNSET:
            field_dict["stackGroup"] = stack_group
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if upper_port is not UNSET:
            field_dict["upperPort"] = upper_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.client_agg_health_dto import ClientAggHealthDTO
        from ..models.lan_port import LanPort
        from ..models.osw_up_info import OswUpInfo
        from ..models.wan_port import WanPort
        from ..models.wire_up_link import WireUpLink
        from ..models.wireless_up_link import WirelessUpLink

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        device_series_type = d.pop("deviceSeriesType", UNSET)

        client_count = d.pop("clientCount", UNSET)

        health_score = d.pop("healthScore", UNSET)

        _client_health = d.pop("clientHealth", UNSET)
        client_health: ClientAggHealthDTO | Unset
        if isinstance(_client_health, Unset):
            client_health = UNSET
        else:
            client_health = ClientAggHealthDTO.from_dict(_client_health)

        _wired_up_link = d.pop("wiredUpLink", UNSET)
        wired_up_link: WireUpLink | Unset
        if isinstance(_wired_up_link, Unset):
            wired_up_link = UNSET
        else:
            wired_up_link = WireUpLink.from_dict(_wired_up_link)

        _wireless_up_link = d.pop("wirelessUpLink", UNSET)
        wireless_up_link: WirelessUpLink | Unset
        if isinstance(_wireless_up_link, Unset):
            wireless_up_link = UNSET
        else:
            wireless_up_link = WirelessUpLink.from_dict(_wireless_up_link)

        rd_mode_2_g = d.pop("rdMode2g", UNSET)

        channel2g = d.pop("channel2g", UNSET)

        rd_mode_5_g = d.pop("rdMode5g", UNSET)

        channel5g = d.pop("channel5g", UNSET)

        rd_mode_5_g_2 = d.pop("rdMode5g2", UNSET)

        channel5g2 = d.pop("channel5g2", UNSET)

        rd_mode_6_g = d.pop("rdMode6g", UNSET)

        channel6g = d.pop("channel6g", UNSET)

        support5g2 = d.pop("support5g2", UNSET)

        _wan_ports = d.pop("wanPorts", UNSET)
        wan_ports: list[WanPort] | Unset = UNSET
        if _wan_ports is not UNSET:
            wan_ports = []
            for wan_ports_item_data in _wan_ports:
                wan_ports_item = WanPort.from_dict(wan_ports_item_data)

                wan_ports.append(wan_ports_item)

        _lan_ports = d.pop("lanPorts", UNSET)
        lan_ports: list[LanPort] | Unset = UNSET
        if _lan_ports is not UNSET:
            lan_ports = []
            for lan_ports_item_data in _lan_ports:
                lan_ports_item = LanPort.from_dict(lan_ports_item_data)

                lan_ports.append(lan_ports_item)

        stack_group = d.pop("stackGroup", UNSET)

        stack_id = d.pop("stackId", UNSET)

        _upper_port = d.pop("upperPort", UNSET)
        upper_port: OswUpInfo | Unset
        if isinstance(_upper_port, Unset):
            upper_port = UNSET
        else:
            upper_port = OswUpInfo.from_dict(_upper_port)

        topology_open_api_node_vo = cls(
            type_=type_,
            name=name,
            mac=mac,
            model=model,
            model_version=model_version,
            device_series_type=device_series_type,
            client_count=client_count,
            health_score=health_score,
            client_health=client_health,
            wired_up_link=wired_up_link,
            wireless_up_link=wireless_up_link,
            rd_mode_2_g=rd_mode_2_g,
            channel2g=channel2g,
            rd_mode_5_g=rd_mode_5_g,
            channel5g=channel5g,
            rd_mode_5_g_2=rd_mode_5_g_2,
            channel5g2=channel5g2,
            rd_mode_6_g=rd_mode_6_g,
            channel6g=channel6g,
            support5g2=support5g2,
            wan_ports=wan_ports,
            lan_ports=lan_ports,
            stack_group=stack_group,
            stack_id=stack_id,
            upper_port=upper_port,
        )

        topology_open_api_node_vo.additional_properties = d
        return topology_open_api_node_vo

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
