from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mirrored_port import MirroredPort
    from ..models.osg_wan_port_ipv_4_config_vo import OsgWanPortIpv4ConfigVO
    from ..models.osg_wan_port_ipv_6_config_vo import OsgWanPortIpv6ConfigVO


T = TypeVar("T", bound="GatewayWanStatusEntity")


@_attrs_define
class GatewayWanStatusEntity:
    """
    Attributes:
        port (int | Unset): Port serial number
        name (str | Unset): Port name
        mac (str | Unset): Port mac
        port_desc (str | Unset): Port description
        type_ (int | Unset): Port type, 0:WAN,1:WAN/LAN,2:LAN;
        physical_type (int | Unset):
        mode (int | Unset): Port mode, 0:WAN,1:LAN;
        poe (bool | Unset): Port poe power supply, 1 for active, 0 or null for not
        poe_power (float | Unset): Port poe power
        status (int | Unset): Port status should be a value as follows: 0: disconnected; 1: connected
        internet_state (int | Unset): Wan internet state should be a value as follows: 0: disconnected; 1: connected
        ip (str | Unset): Ip
        online_detection (int | Unset):
        ip2 (str | Unset): Ip2
        speed (int | Unset): Port speed, 1-10M，2-100M，3-1000M
        duplex (int | Unset): Port duplex, 1-Half，2-Full
        rx (int | Unset): Port total rx bytes
        rx_pkt (int | Unset): Port total rx packets
        rx_pkt_rate (int | Unset): Port rx Packet rate, Unit: Pkt/s;
        rx_rate (int | Unset): Port rx rate, Unit: KB/s;
        tx (int | Unset): Port total tx bytes
        tx_pkt (int | Unset): Port total tx packets
        tx_pkt_rate (int | Unset): Port tx packet rate, Unit: Pkt/s;
        tx_rate (int | Unset): Port tx rate, Unit: KB/s;
        proto (str | Unset): WAN IPv4 connection type, it supports Static IP, DHCP, PPPoE, L2TP, PPTP, DS-Lite, and
            MAP-E.
        wan_ipv_6_comptent (int | Unset): Gateway wan ipv6 component version
        wan_port_ipv_6_config (OsgWanPortIpv6ConfigVO | Unset): Wan ipv6 config
        wan_port_ipv_4_config (OsgWanPortIpv4ConfigVO | Unset): Wan ipv4 config
        mirrored_ports (list[MirroredPort] | Unset): Mirrored ports
        health_level (int | Unset): Wan health level
        latency (int | Unset): Wan latency, when mode is wan and device is connected, Unit: ms
        loss (float | Unset): Wan packet loss rate, Unit : %
        tx_training_rate (int | Unset): Upload current training rate.
        rx_training_rate (int | Unset): Download current training rate.
        isp (str | Unset):
        card_status (int | Unset):
        internet_status (int | Unset):
        net_type (int | Unset):
        band (str | Unset):
        signal (int | Unset):
        rsrp (int | Unset):
        rsrq (int | Unset):
        snr (int | Unset):
        data_usage (float | Unset):
        total_data (float | Unset):
        isp_version (str | Unset):
        roaming_status (int | Unset):
        traffic_status (int | Unset):
        support_sms (bool | Unset):
        sms_operator (str | Unset):
        sim_card_used (int | Unset):
        dsl_modulation_type (int | Unset):
        annex_type (int | Unset):
        line_status (int | Unset):
        max_rx_rate (int | Unset):
        max_tx_rate (int | Unset):
        rx_snr_margin (int | Unset):
        tx_snr_margin (int | Unset):
        rx_line_attenuation (int | Unset):
        tx_line_attenuation (int | Unset):
        rx_error_pkts (int | Unset):
        tx_error_pkts (int | Unset):
    """

    port: int | Unset = UNSET
    name: str | Unset = UNSET
    mac: str | Unset = UNSET
    port_desc: str | Unset = UNSET
    type_: int | Unset = UNSET
    physical_type: int | Unset = UNSET
    mode: int | Unset = UNSET
    poe: bool | Unset = UNSET
    poe_power: float | Unset = UNSET
    status: int | Unset = UNSET
    internet_state: int | Unset = UNSET
    ip: str | Unset = UNSET
    online_detection: int | Unset = UNSET
    ip2: str | Unset = UNSET
    speed: int | Unset = UNSET
    duplex: int | Unset = UNSET
    rx: int | Unset = UNSET
    rx_pkt: int | Unset = UNSET
    rx_pkt_rate: int | Unset = UNSET
    rx_rate: int | Unset = UNSET
    tx: int | Unset = UNSET
    tx_pkt: int | Unset = UNSET
    tx_pkt_rate: int | Unset = UNSET
    tx_rate: int | Unset = UNSET
    proto: str | Unset = UNSET
    wan_ipv_6_comptent: int | Unset = UNSET
    wan_port_ipv_6_config: OsgWanPortIpv6ConfigVO | Unset = UNSET
    wan_port_ipv_4_config: OsgWanPortIpv4ConfigVO | Unset = UNSET
    mirrored_ports: list[MirroredPort] | Unset = UNSET
    health_level: int | Unset = UNSET
    latency: int | Unset = UNSET
    loss: float | Unset = UNSET
    tx_training_rate: int | Unset = UNSET
    rx_training_rate: int | Unset = UNSET
    isp: str | Unset = UNSET
    card_status: int | Unset = UNSET
    internet_status: int | Unset = UNSET
    net_type: int | Unset = UNSET
    band: str | Unset = UNSET
    signal: int | Unset = UNSET
    rsrp: int | Unset = UNSET
    rsrq: int | Unset = UNSET
    snr: int | Unset = UNSET
    data_usage: float | Unset = UNSET
    total_data: float | Unset = UNSET
    isp_version: str | Unset = UNSET
    roaming_status: int | Unset = UNSET
    traffic_status: int | Unset = UNSET
    support_sms: bool | Unset = UNSET
    sms_operator: str | Unset = UNSET
    sim_card_used: int | Unset = UNSET
    dsl_modulation_type: int | Unset = UNSET
    annex_type: int | Unset = UNSET
    line_status: int | Unset = UNSET
    max_rx_rate: int | Unset = UNSET
    max_tx_rate: int | Unset = UNSET
    rx_snr_margin: int | Unset = UNSET
    tx_snr_margin: int | Unset = UNSET
    rx_line_attenuation: int | Unset = UNSET
    tx_line_attenuation: int | Unset = UNSET
    rx_error_pkts: int | Unset = UNSET
    tx_error_pkts: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        port = self.port

        name = self.name

        mac = self.mac

        port_desc = self.port_desc

        type_ = self.type_

        physical_type = self.physical_type

        mode = self.mode

        poe = self.poe

        poe_power = self.poe_power

        status = self.status

        internet_state = self.internet_state

        ip = self.ip

        online_detection = self.online_detection

        ip2 = self.ip2

        speed = self.speed

        duplex = self.duplex

        rx = self.rx

        rx_pkt = self.rx_pkt

        rx_pkt_rate = self.rx_pkt_rate

        rx_rate = self.rx_rate

        tx = self.tx

        tx_pkt = self.tx_pkt

        tx_pkt_rate = self.tx_pkt_rate

        tx_rate = self.tx_rate

        proto = self.proto

        wan_ipv_6_comptent = self.wan_ipv_6_comptent

        wan_port_ipv_6_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_port_ipv_6_config, Unset):
            wan_port_ipv_6_config = self.wan_port_ipv_6_config.to_dict()

        wan_port_ipv_4_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_port_ipv_4_config, Unset):
            wan_port_ipv_4_config = self.wan_port_ipv_4_config.to_dict()

        mirrored_ports: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mirrored_ports, Unset):
            mirrored_ports = []
            for mirrored_ports_item_data in self.mirrored_ports:
                mirrored_ports_item = mirrored_ports_item_data.to_dict()
                mirrored_ports.append(mirrored_ports_item)

        health_level = self.health_level

        latency = self.latency

        loss = self.loss

        tx_training_rate = self.tx_training_rate

        rx_training_rate = self.rx_training_rate

        isp = self.isp

        card_status = self.card_status

        internet_status = self.internet_status

        net_type = self.net_type

        band = self.band

        signal = self.signal

        rsrp = self.rsrp

        rsrq = self.rsrq

        snr = self.snr

        data_usage = self.data_usage

        total_data = self.total_data

        isp_version = self.isp_version

        roaming_status = self.roaming_status

        traffic_status = self.traffic_status

        support_sms = self.support_sms

        sms_operator = self.sms_operator

        sim_card_used = self.sim_card_used

        dsl_modulation_type = self.dsl_modulation_type

        annex_type = self.annex_type

        line_status = self.line_status

        max_rx_rate = self.max_rx_rate

        max_tx_rate = self.max_tx_rate

        rx_snr_margin = self.rx_snr_margin

        tx_snr_margin = self.tx_snr_margin

        rx_line_attenuation = self.rx_line_attenuation

        tx_line_attenuation = self.tx_line_attenuation

        rx_error_pkts = self.rx_error_pkts

        tx_error_pkts = self.tx_error_pkts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if port is not UNSET:
            field_dict["port"] = port
        if name is not UNSET:
            field_dict["name"] = name
        if mac is not UNSET:
            field_dict["mac"] = mac
        if port_desc is not UNSET:
            field_dict["portDesc"] = port_desc
        if type_ is not UNSET:
            field_dict["type"] = type_
        if physical_type is not UNSET:
            field_dict["physicalType"] = physical_type
        if mode is not UNSET:
            field_dict["mode"] = mode
        if poe is not UNSET:
            field_dict["poe"] = poe
        if poe_power is not UNSET:
            field_dict["poePower"] = poe_power
        if status is not UNSET:
            field_dict["status"] = status
        if internet_state is not UNSET:
            field_dict["internetState"] = internet_state
        if ip is not UNSET:
            field_dict["ip"] = ip
        if online_detection is not UNSET:
            field_dict["onlineDetection"] = online_detection
        if ip2 is not UNSET:
            field_dict["ip2"] = ip2
        if speed is not UNSET:
            field_dict["speed"] = speed
        if duplex is not UNSET:
            field_dict["duplex"] = duplex
        if rx is not UNSET:
            field_dict["rx"] = rx
        if rx_pkt is not UNSET:
            field_dict["rxPkt"] = rx_pkt
        if rx_pkt_rate is not UNSET:
            field_dict["rxPktRate"] = rx_pkt_rate
        if rx_rate is not UNSET:
            field_dict["rxRate"] = rx_rate
        if tx is not UNSET:
            field_dict["tx"] = tx
        if tx_pkt is not UNSET:
            field_dict["txPkt"] = tx_pkt
        if tx_pkt_rate is not UNSET:
            field_dict["txPktRate"] = tx_pkt_rate
        if tx_rate is not UNSET:
            field_dict["txRate"] = tx_rate
        if proto is not UNSET:
            field_dict["proto"] = proto
        if wan_ipv_6_comptent is not UNSET:
            field_dict["wanIpv6Comptent"] = wan_ipv_6_comptent
        if wan_port_ipv_6_config is not UNSET:
            field_dict["wanPortIpv6Config"] = wan_port_ipv_6_config
        if wan_port_ipv_4_config is not UNSET:
            field_dict["wanPortIpv4Config"] = wan_port_ipv_4_config
        if mirrored_ports is not UNSET:
            field_dict["mirroredPorts"] = mirrored_ports
        if health_level is not UNSET:
            field_dict["healthLevel"] = health_level
        if latency is not UNSET:
            field_dict["latency"] = latency
        if loss is not UNSET:
            field_dict["loss"] = loss
        if tx_training_rate is not UNSET:
            field_dict["txTrainingRate"] = tx_training_rate
        if rx_training_rate is not UNSET:
            field_dict["rxTrainingRate"] = rx_training_rate
        if isp is not UNSET:
            field_dict["isp"] = isp
        if card_status is not UNSET:
            field_dict["cardStatus"] = card_status
        if internet_status is not UNSET:
            field_dict["internetStatus"] = internet_status
        if net_type is not UNSET:
            field_dict["netType"] = net_type
        if band is not UNSET:
            field_dict["band"] = band
        if signal is not UNSET:
            field_dict["signal"] = signal
        if rsrp is not UNSET:
            field_dict["rsrp"] = rsrp
        if rsrq is not UNSET:
            field_dict["rsrq"] = rsrq
        if snr is not UNSET:
            field_dict["snr"] = snr
        if data_usage is not UNSET:
            field_dict["dataUsage"] = data_usage
        if total_data is not UNSET:
            field_dict["totalData"] = total_data
        if isp_version is not UNSET:
            field_dict["ispVersion"] = isp_version
        if roaming_status is not UNSET:
            field_dict["roamingStatus"] = roaming_status
        if traffic_status is not UNSET:
            field_dict["trafficStatus"] = traffic_status
        if support_sms is not UNSET:
            field_dict["supportSms"] = support_sms
        if sms_operator is not UNSET:
            field_dict["smsOperator"] = sms_operator
        if sim_card_used is not UNSET:
            field_dict["simCardUsed"] = sim_card_used
        if dsl_modulation_type is not UNSET:
            field_dict["dslModulationType"] = dsl_modulation_type
        if annex_type is not UNSET:
            field_dict["annexType"] = annex_type
        if line_status is not UNSET:
            field_dict["lineStatus"] = line_status
        if max_rx_rate is not UNSET:
            field_dict["maxRxRate"] = max_rx_rate
        if max_tx_rate is not UNSET:
            field_dict["maxTxRate"] = max_tx_rate
        if rx_snr_margin is not UNSET:
            field_dict["rxSnrMargin"] = rx_snr_margin
        if tx_snr_margin is not UNSET:
            field_dict["txSnrMargin"] = tx_snr_margin
        if rx_line_attenuation is not UNSET:
            field_dict["rxLineAttenuation"] = rx_line_attenuation
        if tx_line_attenuation is not UNSET:
            field_dict["txLineAttenuation"] = tx_line_attenuation
        if rx_error_pkts is not UNSET:
            field_dict["rxErrorPkts"] = rx_error_pkts
        if tx_error_pkts is not UNSET:
            field_dict["txErrorPkts"] = tx_error_pkts

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.mirrored_port import MirroredPort
        from ..models.osg_wan_port_ipv_4_config_vo import (
            OsgWanPortIpv4ConfigVO,
        )
        from ..models.osg_wan_port_ipv_6_config_vo import (
            OsgWanPortIpv6ConfigVO,
        )

        d = dict(src_dict)
        port = d.pop("port", UNSET)

        name = d.pop("name", UNSET)

        mac = d.pop("mac", UNSET)

        port_desc = d.pop("portDesc", UNSET)

        type_ = d.pop("type", UNSET)

        physical_type = d.pop("physicalType", UNSET)

        mode = d.pop("mode", UNSET)

        poe = d.pop("poe", UNSET)

        poe_power = d.pop("poePower", UNSET)

        status = d.pop("status", UNSET)

        internet_state = d.pop("internetState", UNSET)

        ip = d.pop("ip", UNSET)

        online_detection = d.pop("onlineDetection", UNSET)

        ip2 = d.pop("ip2", UNSET)

        speed = d.pop("speed", UNSET)

        duplex = d.pop("duplex", UNSET)

        rx = d.pop("rx", UNSET)

        rx_pkt = d.pop("rxPkt", UNSET)

        rx_pkt_rate = d.pop("rxPktRate", UNSET)

        rx_rate = d.pop("rxRate", UNSET)

        tx = d.pop("tx", UNSET)

        tx_pkt = d.pop("txPkt", UNSET)

        tx_pkt_rate = d.pop("txPktRate", UNSET)

        tx_rate = d.pop("txRate", UNSET)

        proto = d.pop("proto", UNSET)

        wan_ipv_6_comptent = d.pop("wanIpv6Comptent", UNSET)

        _wan_port_ipv_6_config = d.pop("wanPortIpv6Config", UNSET)
        wan_port_ipv_6_config: OsgWanPortIpv6ConfigVO | Unset
        if isinstance(_wan_port_ipv_6_config, Unset):
            wan_port_ipv_6_config = UNSET
        else:
            wan_port_ipv_6_config = OsgWanPortIpv6ConfigVO.from_dict(
                _wan_port_ipv_6_config
            )

        _wan_port_ipv_4_config = d.pop("wanPortIpv4Config", UNSET)
        wan_port_ipv_4_config: OsgWanPortIpv4ConfigVO | Unset
        if isinstance(_wan_port_ipv_4_config, Unset):
            wan_port_ipv_4_config = UNSET
        else:
            wan_port_ipv_4_config = OsgWanPortIpv4ConfigVO.from_dict(
                _wan_port_ipv_4_config
            )

        _mirrored_ports = d.pop("mirroredPorts", UNSET)
        mirrored_ports: list[MirroredPort] | Unset = UNSET
        if _mirrored_ports is not UNSET:
            mirrored_ports = []
            for mirrored_ports_item_data in _mirrored_ports:
                mirrored_ports_item = MirroredPort.from_dict(mirrored_ports_item_data)

                mirrored_ports.append(mirrored_ports_item)

        health_level = d.pop("healthLevel", UNSET)

        latency = d.pop("latency", UNSET)

        loss = d.pop("loss", UNSET)

        tx_training_rate = d.pop("txTrainingRate", UNSET)

        rx_training_rate = d.pop("rxTrainingRate", UNSET)

        isp = d.pop("isp", UNSET)

        card_status = d.pop("cardStatus", UNSET)

        internet_status = d.pop("internetStatus", UNSET)

        net_type = d.pop("netType", UNSET)

        band = d.pop("band", UNSET)

        signal = d.pop("signal", UNSET)

        rsrp = d.pop("rsrp", UNSET)

        rsrq = d.pop("rsrq", UNSET)

        snr = d.pop("snr", UNSET)

        data_usage = d.pop("dataUsage", UNSET)

        total_data = d.pop("totalData", UNSET)

        isp_version = d.pop("ispVersion", UNSET)

        roaming_status = d.pop("roamingStatus", UNSET)

        traffic_status = d.pop("trafficStatus", UNSET)

        support_sms = d.pop("supportSms", UNSET)

        sms_operator = d.pop("smsOperator", UNSET)

        sim_card_used = d.pop("simCardUsed", UNSET)

        dsl_modulation_type = d.pop("dslModulationType", UNSET)

        annex_type = d.pop("annexType", UNSET)

        line_status = d.pop("lineStatus", UNSET)

        max_rx_rate = d.pop("maxRxRate", UNSET)

        max_tx_rate = d.pop("maxTxRate", UNSET)

        rx_snr_margin = d.pop("rxSnrMargin", UNSET)

        tx_snr_margin = d.pop("txSnrMargin", UNSET)

        rx_line_attenuation = d.pop("rxLineAttenuation", UNSET)

        tx_line_attenuation = d.pop("txLineAttenuation", UNSET)

        rx_error_pkts = d.pop("rxErrorPkts", UNSET)

        tx_error_pkts = d.pop("txErrorPkts", UNSET)

        gateway_wan_status_entity = cls(
            port=port,
            name=name,
            mac=mac,
            port_desc=port_desc,
            type_=type_,
            physical_type=physical_type,
            mode=mode,
            poe=poe,
            poe_power=poe_power,
            status=status,
            internet_state=internet_state,
            ip=ip,
            online_detection=online_detection,
            ip2=ip2,
            speed=speed,
            duplex=duplex,
            rx=rx,
            rx_pkt=rx_pkt,
            rx_pkt_rate=rx_pkt_rate,
            rx_rate=rx_rate,
            tx=tx,
            tx_pkt=tx_pkt,
            tx_pkt_rate=tx_pkt_rate,
            tx_rate=tx_rate,
            proto=proto,
            wan_ipv_6_comptent=wan_ipv_6_comptent,
            wan_port_ipv_6_config=wan_port_ipv_6_config,
            wan_port_ipv_4_config=wan_port_ipv_4_config,
            mirrored_ports=mirrored_ports,
            health_level=health_level,
            latency=latency,
            loss=loss,
            tx_training_rate=tx_training_rate,
            rx_training_rate=rx_training_rate,
            isp=isp,
            card_status=card_status,
            internet_status=internet_status,
            net_type=net_type,
            band=band,
            signal=signal,
            rsrp=rsrp,
            rsrq=rsrq,
            snr=snr,
            data_usage=data_usage,
            total_data=total_data,
            isp_version=isp_version,
            roaming_status=roaming_status,
            traffic_status=traffic_status,
            support_sms=support_sms,
            sms_operator=sms_operator,
            sim_card_used=sim_card_used,
            dsl_modulation_type=dsl_modulation_type,
            annex_type=annex_type,
            line_status=line_status,
            max_rx_rate=max_rx_rate,
            max_tx_rate=max_tx_rate,
            rx_snr_margin=rx_snr_margin,
            tx_snr_margin=tx_snr_margin,
            rx_line_attenuation=rx_line_attenuation,
            tx_line_attenuation=tx_line_attenuation,
            rx_error_pkts=rx_error_pkts,
            tx_error_pkts=tx_error_pkts,
        )

        gateway_wan_status_entity.additional_properties = d
        return gateway_wan_status_entity

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
