from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topology_client_connected_network import (
        TopologyClientConnectedNetwork,
    )
    from ..models.topology_client_connected_ssid import TopologyClientConnectedSsid
    from ..models.topology_client_wired_up_info import TopologyClientWiredUpInfo
    from ..models.topology_client_wireless_up_info import TopologyClientWirelessUpInfo


T = TypeVar("T", bound="TopologyClientNode")


@_attrs_define
class TopologyClientNode:
    """Client In Topology.

    Attributes:
        mac (str | Unset): Client MAC address, like AA-BB-CC-DD-EE-FF.
        name (str | Unset): Client Name.
        ip (str | Unset): Client Ip.
        wireless (bool | Unset): Whether the client is wireless.
        guest (bool | Unset): Whether the client is a guest.
        type_ (str | Unset): Client Type.
        vendor (str | Unset): Client Vendor.
        model (str | Unset): Client Model.
        dev_tx_rate (int | Unset): Realtime txRate
        dev_rx_rate (int | Unset): Realtime rxRate
        health_score (int | Unset): Client health score.
        wired_up_info (TopologyClientWiredUpInfo | Unset): Client uplink information while connection is wired.
        wireless_up_info (TopologyClientWirelessUpInfo | Unset): Client uplink information while connection is wireless.
        connected_network (TopologyClientConnectedNetwork | Unset): Network that client connected.
        connected_ssid (TopologyClientConnectedSsid | Unset): SSID that client connected.
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    guest: bool | Unset = UNSET
    type_: str | Unset = UNSET
    vendor: str | Unset = UNSET
    model: str | Unset = UNSET
    dev_tx_rate: int | Unset = UNSET
    dev_rx_rate: int | Unset = UNSET
    health_score: int | Unset = UNSET
    wired_up_info: TopologyClientWiredUpInfo | Unset = UNSET
    wireless_up_info: TopologyClientWirelessUpInfo | Unset = UNSET
    connected_network: TopologyClientConnectedNetwork | Unset = UNSET
    connected_ssid: TopologyClientConnectedSsid | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        ip = self.ip

        wireless = self.wireless

        guest = self.guest

        type_ = self.type_

        vendor = self.vendor

        model = self.model

        dev_tx_rate = self.dev_tx_rate

        dev_rx_rate = self.dev_rx_rate

        health_score = self.health_score

        wired_up_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wired_up_info, Unset):
            wired_up_info = self.wired_up_info.to_dict()

        wireless_up_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_up_info, Unset):
            wireless_up_info = self.wireless_up_info.to_dict()

        connected_network: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_network, Unset):
            connected_network = self.connected_network.to_dict()

        connected_ssid: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connected_ssid, Unset):
            connected_ssid = self.connected_ssid.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if wireless is not UNSET:
            field_dict["wireless"] = wireless
        if guest is not UNSET:
            field_dict["guest"] = guest
        if type_ is not UNSET:
            field_dict["type"] = type_
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if dev_tx_rate is not UNSET:
            field_dict["devTxRate"] = dev_tx_rate
        if dev_rx_rate is not UNSET:
            field_dict["devRxRate"] = dev_rx_rate
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if wired_up_info is not UNSET:
            field_dict["wiredUpInfo"] = wired_up_info
        if wireless_up_info is not UNSET:
            field_dict["wirelessUpInfo"] = wireless_up_info
        if connected_network is not UNSET:
            field_dict["connectedNetwork"] = connected_network
        if connected_ssid is not UNSET:
            field_dict["connectedSsid"] = connected_ssid

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.topology_client_connected_network import (
            TopologyClientConnectedNetwork,
        )
        from ..models.topology_client_connected_ssid import (
            TopologyClientConnectedSsid,
        )
        from ..models.topology_client_wired_up_info import (
            TopologyClientWiredUpInfo,
        )
        from ..models.topology_client_wireless_up_info import (
            TopologyClientWirelessUpInfo,
        )

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        wireless = d.pop("wireless", UNSET)

        guest = d.pop("guest", UNSET)

        type_ = d.pop("type", UNSET)

        vendor = d.pop("vendor", UNSET)

        model = d.pop("model", UNSET)

        dev_tx_rate = d.pop("devTxRate", UNSET)

        dev_rx_rate = d.pop("devRxRate", UNSET)

        health_score = d.pop("healthScore", UNSET)

        _wired_up_info = d.pop("wiredUpInfo", UNSET)
        wired_up_info: TopologyClientWiredUpInfo | Unset
        if isinstance(_wired_up_info, Unset):
            wired_up_info = UNSET
        else:
            wired_up_info = TopologyClientWiredUpInfo.from_dict(_wired_up_info)

        _wireless_up_info = d.pop("wirelessUpInfo", UNSET)
        wireless_up_info: TopologyClientWirelessUpInfo | Unset
        if isinstance(_wireless_up_info, Unset):
            wireless_up_info = UNSET
        else:
            wireless_up_info = TopologyClientWirelessUpInfo.from_dict(_wireless_up_info)

        _connected_network = d.pop("connectedNetwork", UNSET)
        connected_network: TopologyClientConnectedNetwork | Unset
        if isinstance(_connected_network, Unset):
            connected_network = UNSET
        else:
            connected_network = TopologyClientConnectedNetwork.from_dict(
                _connected_network
            )

        _connected_ssid = d.pop("connectedSsid", UNSET)
        connected_ssid: TopologyClientConnectedSsid | Unset
        if isinstance(_connected_ssid, Unset):
            connected_ssid = UNSET
        else:
            connected_ssid = TopologyClientConnectedSsid.from_dict(_connected_ssid)

        topology_client_node = cls(
            mac=mac,
            name=name,
            ip=ip,
            wireless=wireless,
            guest=guest,
            type_=type_,
            vendor=vendor,
            model=model,
            dev_tx_rate=dev_tx_rate,
            dev_rx_rate=dev_rx_rate,
            health_score=health_score,
            wired_up_info=wired_up_info,
            wireless_up_info=wireless_up_info,
            connected_network=connected_network,
            connected_ssid=connected_ssid,
        )

        topology_client_node.additional_properties = d
        return topology_client_node

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
