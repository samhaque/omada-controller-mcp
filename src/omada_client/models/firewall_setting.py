from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="FirewallSetting")


@_attrs_define
class FirewallSetting:
    """
    Attributes:
        icmp (int): ICMP should be within the range of 1–2097151.
        other (int): Other should be within the range of 1–2097151.
        tcp_close (int): TCP close should be within the range of 1–2097151.
        tcp_close_wait (int): TCP close wait should be within the range of 1–2097151.
        tcp_established (int): TCP established should be within the range of 1–2097151.
        tcp_fin_wait (int): TCP FIN wait should be within the range of 1–2097151.
        tcp_last_ack (int): TCP last ACK should be within the range of 1–2097151.
        tcp_syn_receive (int): TCP SYN receive should be within the range of 1–2097151.
        tcp_syn_sent (int): TCP SYN sent should be within the range of 1–2097151.
        tcp_time_wait (int): TCP time wait should be within the range of 1–2097151.
        udp_other (int): UDP other should be within the range of 1–2097151.
        udp_stream (int): UDP stream should be within the range of 1–2097151.
        broadcast_ping (bool): Broadcast ping of the firewall setting.
        receive_redirects (bool): Receive redirects of the firewall setting.
        send_redirects (bool): Send redirects of the firewall setting.
        syn_cookies (bool): SYN Cookies of the firewall setting.
    """

    icmp: int
    other: int
    tcp_close: int
    tcp_close_wait: int
    tcp_established: int
    tcp_fin_wait: int
    tcp_last_ack: int
    tcp_syn_receive: int
    tcp_syn_sent: int
    tcp_time_wait: int
    udp_other: int
    udp_stream: int
    broadcast_ping: bool
    receive_redirects: bool
    send_redirects: bool
    syn_cookies: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icmp = self.icmp

        other = self.other

        tcp_close = self.tcp_close

        tcp_close_wait = self.tcp_close_wait

        tcp_established = self.tcp_established

        tcp_fin_wait = self.tcp_fin_wait

        tcp_last_ack = self.tcp_last_ack

        tcp_syn_receive = self.tcp_syn_receive

        tcp_syn_sent = self.tcp_syn_sent

        tcp_time_wait = self.tcp_time_wait

        udp_other = self.udp_other

        udp_stream = self.udp_stream

        broadcast_ping = self.broadcast_ping

        receive_redirects = self.receive_redirects

        send_redirects = self.send_redirects

        syn_cookies = self.syn_cookies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icmp": icmp,
                "other": other,
                "tcpClose": tcp_close,
                "tcpCloseWait": tcp_close_wait,
                "tcpEstablished": tcp_established,
                "tcpFinWait": tcp_fin_wait,
                "tcpLastAck": tcp_last_ack,
                "tcpSynReceive": tcp_syn_receive,
                "tcpSynSent": tcp_syn_sent,
                "tcpTimeWait": tcp_time_wait,
                "udpOther": udp_other,
                "udpStream": udp_stream,
                "broadcastPing": broadcast_ping,
                "receiveRedirects": receive_redirects,
                "sendRedirects": send_redirects,
                "synCookies": syn_cookies,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        icmp = d.pop("icmp")

        other = d.pop("other")

        tcp_close = d.pop("tcpClose")

        tcp_close_wait = d.pop("tcpCloseWait")

        tcp_established = d.pop("tcpEstablished")

        tcp_fin_wait = d.pop("tcpFinWait")

        tcp_last_ack = d.pop("tcpLastAck")

        tcp_syn_receive = d.pop("tcpSynReceive")

        tcp_syn_sent = d.pop("tcpSynSent")

        tcp_time_wait = d.pop("tcpTimeWait")

        udp_other = d.pop("udpOther")

        udp_stream = d.pop("udpStream")

        broadcast_ping = d.pop("broadcastPing")

        receive_redirects = d.pop("receiveRedirects")

        send_redirects = d.pop("sendRedirects")

        syn_cookies = d.pop("synCookies")

        firewall_setting = cls(
            icmp=icmp,
            other=other,
            tcp_close=tcp_close,
            tcp_close_wait=tcp_close_wait,
            tcp_established=tcp_established,
            tcp_fin_wait=tcp_fin_wait,
            tcp_last_ack=tcp_last_ack,
            tcp_syn_receive=tcp_syn_receive,
            tcp_syn_sent=tcp_syn_sent,
            tcp_time_wait=tcp_time_wait,
            udp_other=udp_other,
            udp_stream=udp_stream,
            broadcast_ping=broadcast_ping,
            receive_redirects=receive_redirects,
            send_redirects=send_redirects,
            syn_cookies=syn_cookies,
        )

        firewall_setting.additional_properties = d
        return firewall_setting

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
