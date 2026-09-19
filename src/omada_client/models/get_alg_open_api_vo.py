from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAlgOpenApiVO")


@_attrs_define
class GetAlgOpenApiVO:
    """
    Attributes:
        ftp (bool): Whether to enable the FTP ALG
        h323 (bool): Whether to enable the H323 ALG
        pptp (bool): Whether to enable the PPTP ALG
        sip (bool): Whether to enable the SIP ALG
        ip_sec (bool): Whether to enable the IPSec ALG
        ftp_ports (list[int] | Unset): The listening port for FTP signaling messages, the default port is 21
        sip_tcp (bool | Unset): Enable this option if your SIP signaling uses the TCP protocol and the device needs to
            modify the IP address and port in SIP messages, enabled by default.
        sip_udp (bool | Unset): Enable this option if your SIP signaling uses the UDP protocol and the device needs to
            modify the IP address and port in SIP signaling messages, enabled by default.
        sip_ports (list[int] | Unset): The listening ports for SIP signaling messages, the default ports are 5060 and
            5061
        sip_direct_signaling (bool | Unset): Enable this option if you want SIP signaling connections to only arrive
            from registered IP addresses, enabled by default.
        sip_direct_media (bool | Unset): Enable this option if you want SIP media connections to only arrive from
            registered IP addresses.
        sip_timeout (bool | Unset): Enable this option if you want to apply timeout limits to SIP signaling and media
            connections on the device.
        sip_signaling_timeout (int | Unset): Modify this item if you want to adjust the timeout duration for SIP
            signaling sessions (1 – 86,400 seconds).
        sip_media_timeout (int | Unset): Modify this item if you want to adjust the timeout duration for SIP media
            sessions (1 – 86,400 seconds).
        support_sip_alg_config (bool | Unset): Whether to support custom configuration for ALG
        exist_sip_alg_config (bool | Unset): Whether to exist custom configuration for SIP ALG
        exist_ftp_alg_config (bool | Unset): Whether to exist custom configuration for FTP ALG
    """

    ftp: bool
    h323: bool
    pptp: bool
    sip: bool
    ip_sec: bool
    ftp_ports: list[int] | Unset = UNSET
    sip_tcp: bool | Unset = UNSET
    sip_udp: bool | Unset = UNSET
    sip_ports: list[int] | Unset = UNSET
    sip_direct_signaling: bool | Unset = UNSET
    sip_direct_media: bool | Unset = UNSET
    sip_timeout: bool | Unset = UNSET
    sip_signaling_timeout: int | Unset = UNSET
    sip_media_timeout: int | Unset = UNSET
    support_sip_alg_config: bool | Unset = UNSET
    exist_sip_alg_config: bool | Unset = UNSET
    exist_ftp_alg_config: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ftp = self.ftp

        h323 = self.h323

        pptp = self.pptp

        sip = self.sip

        ip_sec = self.ip_sec

        ftp_ports: list[int] | Unset = UNSET
        if not isinstance(self.ftp_ports, Unset):
            ftp_ports = self.ftp_ports

        sip_tcp = self.sip_tcp

        sip_udp = self.sip_udp

        sip_ports: list[int] | Unset = UNSET
        if not isinstance(self.sip_ports, Unset):
            sip_ports = self.sip_ports

        sip_direct_signaling = self.sip_direct_signaling

        sip_direct_media = self.sip_direct_media

        sip_timeout = self.sip_timeout

        sip_signaling_timeout = self.sip_signaling_timeout

        sip_media_timeout = self.sip_media_timeout

        support_sip_alg_config = self.support_sip_alg_config

        exist_sip_alg_config = self.exist_sip_alg_config

        exist_ftp_alg_config = self.exist_ftp_alg_config

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ftp": ftp,
                "h323": h323,
                "pptp": pptp,
                "sip": sip,
                "ipSec": ip_sec,
            }
        )
        if ftp_ports is not UNSET:
            field_dict["ftpPorts"] = ftp_ports
        if sip_tcp is not UNSET:
            field_dict["sipTcp"] = sip_tcp
        if sip_udp is not UNSET:
            field_dict["sipUdp"] = sip_udp
        if sip_ports is not UNSET:
            field_dict["sipPorts"] = sip_ports
        if sip_direct_signaling is not UNSET:
            field_dict["sipDirectSignaling"] = sip_direct_signaling
        if sip_direct_media is not UNSET:
            field_dict["sipDirectMedia"] = sip_direct_media
        if sip_timeout is not UNSET:
            field_dict["sipTimeout"] = sip_timeout
        if sip_signaling_timeout is not UNSET:
            field_dict["sipSignalingTimeout"] = sip_signaling_timeout
        if sip_media_timeout is not UNSET:
            field_dict["sipMediaTimeout"] = sip_media_timeout
        if support_sip_alg_config is not UNSET:
            field_dict["supportSipAlgConfig"] = support_sip_alg_config
        if exist_sip_alg_config is not UNSET:
            field_dict["existSipAlgConfig"] = exist_sip_alg_config
        if exist_ftp_alg_config is not UNSET:
            field_dict["existFtpAlgConfig"] = exist_ftp_alg_config

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ftp = d.pop("ftp")

        h323 = d.pop("h323")

        pptp = d.pop("pptp")

        sip = d.pop("sip")

        ip_sec = d.pop("ipSec")

        ftp_ports = cast(list[int], d.pop("ftpPorts", UNSET))

        sip_tcp = d.pop("sipTcp", UNSET)

        sip_udp = d.pop("sipUdp", UNSET)

        sip_ports = cast(list[int], d.pop("sipPorts", UNSET))

        sip_direct_signaling = d.pop("sipDirectSignaling", UNSET)

        sip_direct_media = d.pop("sipDirectMedia", UNSET)

        sip_timeout = d.pop("sipTimeout", UNSET)

        sip_signaling_timeout = d.pop("sipSignalingTimeout", UNSET)

        sip_media_timeout = d.pop("sipMediaTimeout", UNSET)

        support_sip_alg_config = d.pop("supportSipAlgConfig", UNSET)

        exist_sip_alg_config = d.pop("existSipAlgConfig", UNSET)

        exist_ftp_alg_config = d.pop("existFtpAlgConfig", UNSET)

        get_alg_open_api_vo = cls(
            ftp=ftp,
            h323=h323,
            pptp=pptp,
            sip=sip,
            ip_sec=ip_sec,
            ftp_ports=ftp_ports,
            sip_tcp=sip_tcp,
            sip_udp=sip_udp,
            sip_ports=sip_ports,
            sip_direct_signaling=sip_direct_signaling,
            sip_direct_media=sip_direct_media,
            sip_timeout=sip_timeout,
            sip_signaling_timeout=sip_signaling_timeout,
            sip_media_timeout=sip_media_timeout,
            support_sip_alg_config=support_sip_alg_config,
            exist_sip_alg_config=exist_sip_alg_config,
            exist_ftp_alg_config=exist_ftp_alg_config,
        )

        get_alg_open_api_vo.additional_properties = d
        return get_alg_open_api_vo

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
