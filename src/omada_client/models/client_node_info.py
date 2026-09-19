from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_node_info import DeviceNodeInfo
    from ..models.uplink_ap_info import UplinkAPInfo
    from ..models.uplink_switch_info import UplinkSwitchInfo


T = TypeVar("T", bound="ClientNodeInfo")


@_attrs_define
class ClientNodeInfo:
    """Client node info.

    Attributes:
        mac (str | Unset): Client MAC Address.
        name (str | Unset): Client name.
        ip (str | Unset): Client IP.
        wireless (bool | Unset): true: Wireless client;  false: Not wireless client
        guest (bool | Unset): (Wireless) Whether it is Guest (used to display the wireless Guest client icon).
        client_type (str | Unset): Client Type: iphone, ipod, android, pc, printer, tv...
        up_device_type (int | Unset): Uplink device type, 0: AP; 1: Switch; 2: Gateway.
        auth_status (int | Unset): Authentication status should be a value as follows: <br/>0: CONNECTED // Access
            without any authentication method; <br/>1: PENDING // Access to Portal, but authentication failed; <br/>2:
            AUTHORIZED // Pass through portal, pass other authentication without portal; <br/>3: AUTH-FREE // No portal
            authentication required.
        model (str | Unset): Model of client device.
        manager (bool | Unset): Whether it is the device currently accessing the Controller itself.
        dev_tx_rate (int | Unset): Client real-time uploadRate
        dev_rx_rate (int | Unset): Client real-time downloadRate
        health_score (int | Unset): Health Score, 1~3: poor; 4~7: fair; 0: no data; 8~10 good.
        up_osw_info (UplinkSwitchInfo | Unset): Uplink switch info, exists when parameter [upDeviceType] is 1.
        up_ap_info (UplinkAPInfo | Unset): Uplink AP info, exists when parameter [upDeviceType] is 0.
        downlink_nodes (list[DeviceNodeInfo] | Unset): Downlink nodes, exists when client is other gateway
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    ip: str | Unset = UNSET
    wireless: bool | Unset = UNSET
    guest: bool | Unset = UNSET
    client_type: str | Unset = UNSET
    up_device_type: int | Unset = UNSET
    auth_status: int | Unset = UNSET
    model: str | Unset = UNSET
    manager: bool | Unset = UNSET
    dev_tx_rate: int | Unset = UNSET
    dev_rx_rate: int | Unset = UNSET
    health_score: int | Unset = UNSET
    up_osw_info: UplinkSwitchInfo | Unset = UNSET
    up_ap_info: UplinkAPInfo | Unset = UNSET
    downlink_nodes: list[DeviceNodeInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        ip = self.ip

        wireless = self.wireless

        guest = self.guest

        client_type = self.client_type

        up_device_type = self.up_device_type

        auth_status = self.auth_status

        model = self.model

        manager = self.manager

        dev_tx_rate = self.dev_tx_rate

        dev_rx_rate = self.dev_rx_rate

        health_score = self.health_score

        up_osw_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.up_osw_info, Unset):
            up_osw_info = self.up_osw_info.to_dict()

        up_ap_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.up_ap_info, Unset):
            up_ap_info = self.up_ap_info.to_dict()

        downlink_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.downlink_nodes, Unset):
            downlink_nodes = []
            for downlink_nodes_item_data in self.downlink_nodes:
                downlink_nodes_item = downlink_nodes_item_data.to_dict()
                downlink_nodes.append(downlink_nodes_item)

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
        if client_type is not UNSET:
            field_dict["clientType"] = client_type
        if up_device_type is not UNSET:
            field_dict["upDeviceType"] = up_device_type
        if auth_status is not UNSET:
            field_dict["authStatus"] = auth_status
        if model is not UNSET:
            field_dict["model"] = model
        if manager is not UNSET:
            field_dict["manager"] = manager
        if dev_tx_rate is not UNSET:
            field_dict["devTxRate"] = dev_tx_rate
        if dev_rx_rate is not UNSET:
            field_dict["devRxRate"] = dev_rx_rate
        if health_score is not UNSET:
            field_dict["healthScore"] = health_score
        if up_osw_info is not UNSET:
            field_dict["upOswInfo"] = up_osw_info
        if up_ap_info is not UNSET:
            field_dict["upApInfo"] = up_ap_info
        if downlink_nodes is not UNSET:
            field_dict["downlinkNodes"] = downlink_nodes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_node_info import DeviceNodeInfo
        from ..models.uplink_ap_info import UplinkAPInfo
        from ..models.uplink_switch_info import UplinkSwitchInfo

        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        ip = d.pop("ip", UNSET)

        wireless = d.pop("wireless", UNSET)

        guest = d.pop("guest", UNSET)

        client_type = d.pop("clientType", UNSET)

        up_device_type = d.pop("upDeviceType", UNSET)

        auth_status = d.pop("authStatus", UNSET)

        model = d.pop("model", UNSET)

        manager = d.pop("manager", UNSET)

        dev_tx_rate = d.pop("devTxRate", UNSET)

        dev_rx_rate = d.pop("devRxRate", UNSET)

        health_score = d.pop("healthScore", UNSET)

        _up_osw_info = d.pop("upOswInfo", UNSET)
        up_osw_info: UplinkSwitchInfo | Unset
        if isinstance(_up_osw_info, Unset):
            up_osw_info = UNSET
        else:
            up_osw_info = UplinkSwitchInfo.from_dict(_up_osw_info)

        _up_ap_info = d.pop("upApInfo", UNSET)
        up_ap_info: UplinkAPInfo | Unset
        if isinstance(_up_ap_info, Unset):
            up_ap_info = UNSET
        else:
            up_ap_info = UplinkAPInfo.from_dict(_up_ap_info)

        _downlink_nodes = d.pop("downlinkNodes", UNSET)
        downlink_nodes: list[DeviceNodeInfo] | Unset = UNSET
        if _downlink_nodes is not UNSET:
            downlink_nodes = []
            for downlink_nodes_item_data in _downlink_nodes:
                downlink_nodes_item = DeviceNodeInfo.from_dict(downlink_nodes_item_data)

                downlink_nodes.append(downlink_nodes_item)

        client_node_info = cls(
            mac=mac,
            name=name,
            ip=ip,
            wireless=wireless,
            guest=guest,
            client_type=client_type,
            up_device_type=up_device_type,
            auth_status=auth_status,
            model=model,
            manager=manager,
            dev_tx_rate=dev_tx_rate,
            dev_rx_rate=dev_rx_rate,
            health_score=health_score,
            up_osw_info=up_osw_info,
            up_ap_info=up_ap_info,
            downlink_nodes=downlink_nodes,
        )

        client_node_info.additional_properties = d
        return client_node_info

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
