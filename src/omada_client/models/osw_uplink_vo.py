from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_peer_port_vo import OswPeerPortVO


T = TypeVar("T", bound="OswUplinkVO")


@_attrs_define
class OswUplinkVO:
    """Uplink Omada device

    Attributes:
        port (int | Unset): Port
        st_port (str | Unset): Standard Port, unit/slot/port
        lag_id (int | Unset): LagId. If it is not null, it indicates that the port is a LAG port
        mac (str | Unset): The mac of uplink device
        stack_id (str | Unset): The ID of uplink stack device
        stack_name (str | Unset): The name of uplink stack device
        name (str | Unset): The name of uplink device
        model (str | Unset): The model of uplink device
        hw_version (str | Unset): HwVersion
        model_version (str | Unset): Model Version
        link_speed (int | Unset): Link Speed
        duplex (int | Unset): Duplex
        rx (int | Unset): Port total rx bytes
        rx_rate (int | Unset): Rx Rate
        tx (int | Unset): Port total tx bytes
        tx_rate (int | Unset): Tx Rate
        stp_discarding (bool | Unset): STP Discarding
        blocked_vlans (str | Unset): Blocked Vlans
        blocked_type (int | Unset): Blocked Type
        type_ (str | Unset): The type of uplink device, it should be a value as follows: ap, gateway, switch(stack)
        link_peer_port_info (OswPeerPortVO | Unset): Downlink Port Info
        ip (str | Unset):
    """

    port: int | Unset = UNSET
    st_port: str | Unset = UNSET
    lag_id: int | Unset = UNSET
    mac: str | Unset = UNSET
    stack_id: str | Unset = UNSET
    stack_name: str | Unset = UNSET
    name: str | Unset = UNSET
    model: str | Unset = UNSET
    hw_version: str | Unset = UNSET
    model_version: str | Unset = UNSET
    link_speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    rx: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    stp_discarding: bool | Unset = UNSET
    blocked_vlans: str | Unset = UNSET
    blocked_type: int | Unset = UNSET
    type_: str | Unset = UNSET
    link_peer_port_info: OswPeerPortVO | Unset = UNSET
    ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        st_port = self.st_port

        lag_id = self.lag_id

        mac = self.mac

        stack_id = self.stack_id

        stack_name = self.stack_name

        name = self.name

        model = self.model

        hw_version = self.hw_version

        model_version = self.model_version

        link_speed = self.link_speed

        duplex = self.duplex

        rx = self.rx

        rx_rate = self.rx_rate

        tx = self.tx

        tx_rate = self.tx_rate

        stp_discarding = self.stp_discarding

        blocked_vlans = self.blocked_vlans

        blocked_type = self.blocked_type

        type_ = self.type_

        link_peer_port_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.link_peer_port_info, Unset):
            link_peer_port_info = self.link_peer_port_info.to_dict()

        ip = self.ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if st_port is not UNSET:
            field_dict["stPort"] = st_port
        if lag_id is not UNSET:
            field_dict["lagId"] = lag_id
        if mac is not UNSET:
            field_dict["mac"] = mac
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if stack_name is not UNSET:
            field_dict["stackName"] = stack_name
        if name is not UNSET:
            field_dict["name"] = name
        if model is not UNSET:
            field_dict["model"] = model
        if hw_version is not UNSET:
            field_dict["hwVersion"] = hw_version
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if link_speed is not UNSET:
            field_dict["linkSpeed"] = link_speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if rx is not UNSET:
            field_dict["rx"] = rx
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx is not UNSET:
            field_dict["tx"] = tx
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if stp_discarding is not UNSET:
            field_dict["stpDiscarding"] = stp_discarding
        if blocked_vlans is not UNSET:
            field_dict["blockedVlans"] = blocked_vlans
        if blocked_type is not UNSET:
            field_dict["blockedType"] = blocked_type
        if type_ is not UNSET:
            field_dict["type"] = type_
        if link_peer_port_info is not UNSET:
            field_dict["linkPeerPortInfo"] = link_peer_port_info
        if ip is not UNSET:
            field_dict["ip"] = ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_peer_port_vo import OswPeerPortVO

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        st_port = d.pop("stPort", UNSET)

        lag_id = d.pop("lagId", UNSET)

        mac = d.pop("mac", UNSET)

        stack_id = d.pop("stackId", UNSET)

        stack_name = d.pop("stackName", UNSET)

        name = d.pop("name", UNSET)

        model = d.pop("model", UNSET)

        hw_version = d.pop("hwVersion", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        link_speed = d.pop("linkSpeed", UNSET)

        duplex = d.pop("duplex", UNSET)

        rx = d.pop("rx", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx = d.pop("tx", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        stp_discarding = d.pop("stpDiscarding", UNSET)

        blocked_vlans = d.pop("blockedVlans", UNSET)

        blocked_type = d.pop("blockedType", UNSET)

        type_ = d.pop("type", UNSET)

        _link_peer_port_info = d.pop("linkPeerPortInfo", UNSET)
        link_peer_port_info: OswPeerPortVO | Unset
        if isinstance(_link_peer_port_info, Unset):
            link_peer_port_info = UNSET
        else:
            link_peer_port_info = OswPeerPortVO.from_dict(_link_peer_port_info)

        ip = d.pop("ip", UNSET)

        osw_uplink_vo = cls(
            port=port,
            st_port=st_port,
            lag_id=lag_id,
            mac=mac,
            stack_id=stack_id,
            stack_name=stack_name,
            name=name,
            model=model,
            hw_version=hw_version,
            model_version=model_version,
            link_speed=link_speed,
            duplex=duplex,
            rx=rx,
            rx_rate=rx_rate,
            tx=tx,
            tx_rate=tx_rate,
            stp_discarding=stp_discarding,
            blocked_vlans=blocked_vlans,
            blocked_type=blocked_type,
            type_=type_,
            link_peer_port_info=link_peer_port_info,
            ip=ip,
        )

        osw_uplink_vo.additional_properties = d
        return osw_uplink_vo

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
