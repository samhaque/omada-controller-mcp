from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualWanIpv4PppoaOpenApiVO")


@_attrs_define
class VirtualWanIpv4PppoaOpenApiVO:
    """VirtualWanIpv4PppoaOpenApiVO

    Attributes:
        user_name (str): Username. Parameter [userName] should contain 1 to 255 ASCII characters.
        password (str): Password. Parameter [password] should contain 1 to 255 ASCII characters.
        ip_from_isp (str): Get IP address from ISP.
        link_type (str): Connection Mode. Parameter [linkType] should be as follows: auto: Connect Automatically;
            demand: Connect Manually; time: Time-based.
        redial_interval (int): It is required when [linkType] is 0. Unit: Second.
        mtu (int): Parameter [mtu] should be a value between 576 and 1492.
        mru (int): Parameter [mru] should be a value between 576 and 1492.
        mss_clamping_type (int): It should be a value as follows: 0: Disable, 1: Auto, 2: Custom.
        ipaddr (str | Unset): IP address.
        gateway (str | Unset): Gateway IP.
        start_time (str | Unset): It is required when [linkType] is 2. For example, 12:30.
        end_time (str | Unset): It is required when [linkType] is 2. For example, 12:30.
        service (str | Unset): Parameter [service] should be 1 ~ 128 visible ASCII characters.
        netmask (str | Unset): Subnet mask.
        dns1 (str | Unset): Primary DNS server.
        dns2 (str | Unset): Secondary DNS server.
        connect (str | Unset):
        mss_clamping_value (int | Unset): It is required when [mssClampingType] is 2, which ranges 532 ~ 1452.
    """

    user_name: str
    password: str
    ip_from_isp: str
    link_type: str
    redial_interval: int
    mtu: int
    mru: int
    mss_clamping_type: int
    ipaddr: str | Unset = UNSET
    gateway: str | Unset = UNSET
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    service: str | Unset = UNSET
    netmask: str | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    connect: str | Unset = UNSET
    mss_clamping_value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_name = self.user_name

        password = self.password

        ip_from_isp = self.ip_from_isp

        link_type = self.link_type

        redial_interval = self.redial_interval

        mtu = self.mtu

        mru = self.mru

        mss_clamping_type = self.mss_clamping_type

        ipaddr = self.ipaddr

        gateway = self.gateway

        start_time = self.start_time

        end_time = self.end_time

        service = self.service

        netmask = self.netmask

        dns1 = self.dns1

        dns2 = self.dns2

        connect = self.connect

        mss_clamping_value = self.mss_clamping_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
                "password": password,
                "ipFromIsp": ip_from_isp,
                "linkType": link_type,
                "redialInterval": redial_interval,
                "mtu": mtu,
                "mru": mru,
                "mssClampingType": mss_clamping_type,
            }
        )
        if ipaddr is not UNSET:
            field_dict["ipaddr"] = ipaddr
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if service is not UNSET:
            field_dict["service"] = service
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2
        if connect is not UNSET:
            field_dict["connect"] = connect
        if mss_clamping_value is not UNSET:
            field_dict["mssClampingValue"] = mss_clamping_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        user_name = d.pop("userName")

        password = d.pop("password")

        ip_from_isp = d.pop("ipFromIsp")

        link_type = d.pop("linkType")

        redial_interval = d.pop("redialInterval")

        mtu = d.pop("mtu")

        mru = d.pop("mru")

        mss_clamping_type = d.pop("mssClampingType")

        ipaddr = d.pop("ipaddr", UNSET)

        gateway = d.pop("gateway", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        service = d.pop("service", UNSET)

        netmask = d.pop("netmask", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        connect = d.pop("connect", UNSET)

        mss_clamping_value = d.pop("mssClampingValue", UNSET)

        virtual_wan_ipv_4_pppoa_open_api_vo = cls(
            user_name=user_name,
            password=password,
            ip_from_isp=ip_from_isp,
            link_type=link_type,
            redial_interval=redial_interval,
            mtu=mtu,
            mru=mru,
            mss_clamping_type=mss_clamping_type,
            ipaddr=ipaddr,
            gateway=gateway,
            start_time=start_time,
            end_time=end_time,
            service=service,
            netmask=netmask,
            dns1=dns1,
            dns2=dns2,
            connect=connect,
            mss_clamping_value=mss_clamping_value,
        )

        virtual_wan_ipv_4_pppoa_open_api_vo.additional_properties = d
        return virtual_wan_ipv_4_pppoa_open_api_vo

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
