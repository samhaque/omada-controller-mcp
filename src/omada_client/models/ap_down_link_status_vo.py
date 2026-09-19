from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApDownLinkStatusVO")


@_attrs_define
class ApDownLinkStatusVO:
    """Wired downlink device list

    Attributes:
        port (str | Unset):
        port_type (int | Unset):
        duplex (int | Unset):
        link (int | Unset):
        speed (int | Unset):
        poe_state (int | Unset):
        voip_state (int | Unset):
        mac (str | Unset):
        ip (str | Unset):
        type_ (str | Unset):
        device_name (str | Unset):
        model (str | Unset):
        model_version (str | Unset):
        tx_power (float | Unset):
        rx_power (float | Unset):
        temp (float | Unset):
        voltage (float | Unset):
        current (float | Unset):
        rx_pkts (int | Unset):
        tx_pkts (int | Unset):
        rx (int | Unset):
        tx (int | Unset):
        rx_drop_pkts (int | Unset):
        tx_drop_pkts (int | Unset):
        rx_err_pkts (int | Unset):
        tx_err_pkts (int | Unset):
        down_link_port (str | Unset):
        display (bool | Unset):
    """

    port: str | Unset = UNSET
    port_type: int | Unset = UNSET
    duplex: int | Unset = UNSET
    link: int | Unset = UNSET
    speed: int | Unset = UNSET
    poe_state: int | Unset = UNSET
    voip_state: int | Unset = UNSET
    mac: str | Unset = UNSET
    ip: str | Unset = UNSET
    type_: str | Unset = UNSET
    device_name: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    tx_power: float | Unset = UNSET
    rx_power: float | Unset = UNSET
    temp: float | Unset = UNSET
    voltage: float | Unset = UNSET
    current: float | Unset = UNSET
    rx_pkts: int | Unset = UNSET
    tx_pkts: int | Unset = UNSET
    rx: int | Unset = UNSET
    tx: int | Unset = UNSET
    rx_drop_pkts: int | Unset = UNSET
    tx_drop_pkts: int | Unset = UNSET
    rx_err_pkts: int | Unset = UNSET
    tx_err_pkts: int | Unset = UNSET
    down_link_port: str | Unset = UNSET
    display: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        port_type = self.port_type

        duplex = self.duplex

        link = self.link

        speed = self.speed

        poe_state = self.poe_state

        voip_state = self.voip_state

        mac = self.mac

        ip = self.ip

        type_ = self.type_

        device_name = self.device_name

        model = self.model

        model_version = self.model_version

        tx_power = self.tx_power

        rx_power = self.rx_power

        temp = self.temp

        voltage = self.voltage

        current = self.current

        rx_pkts = self.rx_pkts

        tx_pkts = self.tx_pkts

        rx = self.rx

        tx = self.tx

        rx_drop_pkts = self.rx_drop_pkts

        tx_drop_pkts = self.tx_drop_pkts

        rx_err_pkts = self.rx_err_pkts

        tx_err_pkts = self.tx_err_pkts

        down_link_port = self.down_link_port

        display = self.display

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if port_type is not UNSET:
            field_dict["portType"] = port_type
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if link is not UNSET:
            field_dict["link"] = link
        if speed is not UNSET:
            field_dict["speed"] = speed
        if poe_state is not UNSET:
            field_dict["poeState"] = poe_state
        if voip_state is not UNSET:
            field_dict["voipState"] = voip_state
        if mac is not UNSET:
            field_dict["mac"] = mac
        if ip is not UNSET:
            field_dict["ip"] = ip
        if type_ is not UNSET:
            field_dict["type"] = type_
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if tx_power is not UNSET:
            field_dict["txPower"] = tx_power
        if rx_power is not UNSET:
            field_dict["rxPower"] = rx_power
        if temp is not UNSET:
            field_dict["temp"] = temp
        if voltage is not UNSET:
            field_dict["voltage"] = voltage
        if current is not UNSET:
            field_dict["current"] = current
        if rx_pkts is not UNSET:
            field_dict["rxPkts"] = rx_pkts
        if tx_pkts is not UNSET:
            field_dict["txPkts"] = tx_pkts
        if rx is not UNSET:
            field_dict["rx"] = rx
        if tx is not UNSET:
            field_dict["tx"] = tx
        if rx_drop_pkts is not UNSET:
            field_dict["rxDropPkts"] = rx_drop_pkts
        if tx_drop_pkts is not UNSET:
            field_dict["txDropPkts"] = tx_drop_pkts
        if rx_err_pkts is not UNSET:
            field_dict["rxErrPkts"] = rx_err_pkts
        if tx_err_pkts is not UNSET:
            field_dict["txErrPkts"] = tx_err_pkts
        if down_link_port is not UNSET:
            field_dict["downLinkPort"] = down_link_port
        if display is not UNSET:
            field_dict["display"] = display

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        port = d.pop("port", UNSET)

        port_type = d.pop("portType", UNSET)

        duplex = d.pop("duplex", UNSET)

        link = d.pop("link", UNSET)

        speed = d.pop("speed", UNSET)

        poe_state = d.pop("poeState", UNSET)

        voip_state = d.pop("voipState", UNSET)

        mac = d.pop("mac", UNSET)

        ip = d.pop("ip", UNSET)

        type_ = d.pop("type", UNSET)

        device_name = d.pop("deviceName", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        tx_power = d.pop("txPower", UNSET)

        rx_power = d.pop("rxPower", UNSET)

        temp = d.pop("temp", UNSET)

        voltage = d.pop("voltage", UNSET)

        current = d.pop("current", UNSET)

        rx_pkts = d.pop("rxPkts", UNSET)

        tx_pkts = d.pop("txPkts", UNSET)

        rx = d.pop("rx", UNSET)

        tx = d.pop("tx", UNSET)

        rx_drop_pkts = d.pop("rxDropPkts", UNSET)

        tx_drop_pkts = d.pop("txDropPkts", UNSET)

        rx_err_pkts = d.pop("rxErrPkts", UNSET)

        tx_err_pkts = d.pop("txErrPkts", UNSET)

        down_link_port = d.pop("downLinkPort", UNSET)

        display = d.pop("display", UNSET)

        ap_down_link_status_vo = cls(
            port=port,
            port_type=port_type,
            duplex=duplex,
            link=link,
            speed=speed,
            poe_state=poe_state,
            voip_state=voip_state,
            mac=mac,
            ip=ip,
            type_=type_,
            device_name=device_name,
            model=model,
            model_version=model_version,
            tx_power=tx_power,
            rx_power=rx_power,
            temp=temp,
            voltage=voltage,
            current=current,
            rx_pkts=rx_pkts,
            tx_pkts=tx_pkts,
            rx=rx,
            tx=tx,
            rx_drop_pkts=rx_drop_pkts,
            tx_drop_pkts=tx_drop_pkts,
            rx_err_pkts=rx_err_pkts,
            tx_err_pkts=tx_err_pkts,
            down_link_port=down_link_port,
            display=display,
        )

        ap_down_link_status_vo.additional_properties = d
        return ap_down_link_status_vo

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
