from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ipv_4_connection_2_open_api_vo import Ipv4Connection2OpenApiVO


T = TypeVar("T", bound="Ipv4PptpOpenApiVO")


@_attrs_define
class Ipv4PptpOpenApiVO:
    """It is required when [protoType] is 4.

    Attributes:
        user_name (str):
        password (str):
        ip_from_isp (bool): Get IP address from ISP.
        connection_mode (int): It should be a value as follows: 0: Connect Automatically; 1: Connect Manually; 2: Time-
            based.
        mtu (int): 576-1500, default:1420
        ipv_4_connection_2 (Ipv4Connection2OpenApiVO):
        primary_dns (str | Unset): Primary DNS
        secondary_dns (str | Unset): Secondary DNS
        redial_interval (int | Unset): It is required when [linkType] is 0. Unit: Second
        start_time (str | Unset): It is required when [linkType] is 2. For example, 12:30.
        end_time (str | Unset): It is required when [linkType] is 2. For example, 12:30.
        mss_clamping_type (int | Unset): 0: Disable, 1: Auto, 2: Custom
        mss_clamping_value (int | Unset): (Optional) It is required when [mssClampingType] is 2, which ranges from 532 ~
            1452.
    """

    user_name: str
    password: str
    ip_from_isp: bool
    connection_mode: int
    mtu: int
    ipv_4_connection_2: Ipv4Connection2OpenApiVO
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    redial_interval: int | Unset = UNSET
    start_time: str | Unset = UNSET
    end_time: str | Unset = UNSET
    mss_clamping_type: int | Unset = UNSET
    mss_clamping_value: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_name = self.user_name

        password = self.password

        ip_from_isp = self.ip_from_isp

        connection_mode = self.connection_mode

        mtu = self.mtu

        ipv_4_connection_2 = self.ipv_4_connection_2.to_dict()

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        redial_interval = self.redial_interval

        start_time = self.start_time

        end_time = self.end_time

        mss_clamping_type = self.mss_clamping_type

        mss_clamping_value = self.mss_clamping_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userName": user_name,
                "password": password,
                "ipFromIsp": ip_from_isp,
                "connectionMode": connection_mode,
                "mtu": mtu,
                "ipv4Connection2": ipv_4_connection_2,
            }
        )
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if redial_interval is not UNSET:
            field_dict["redialInterval"] = redial_interval
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if mss_clamping_type is not UNSET:
            field_dict["mssClampingType"] = mss_clamping_type
        if mss_clamping_value is not UNSET:
            field_dict["mssClampingValue"] = mss_clamping_value

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ipv_4_connection_2_open_api_vo import (
            Ipv4Connection2OpenApiVO,
        )

        d = dict(src_dict)
        user_name = d.pop("userName")

        password = d.pop("password")

        ip_from_isp = d.pop("ipFromIsp")

        connection_mode = d.pop("connectionMode")

        mtu = d.pop("mtu")

        ipv_4_connection_2 = Ipv4Connection2OpenApiVO.from_dict(
            d.pop("ipv4Connection2")
        )

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        redial_interval = d.pop("redialInterval", UNSET)

        start_time = d.pop("startTime", UNSET)

        end_time = d.pop("endTime", UNSET)

        mss_clamping_type = d.pop("mssClampingType", UNSET)

        mss_clamping_value = d.pop("mssClampingValue", UNSET)

        ipv_4_pptp_open_api_vo = cls(
            user_name=user_name,
            password=password,
            ip_from_isp=ip_from_isp,
            connection_mode=connection_mode,
            mtu=mtu,
            ipv_4_connection_2=ipv_4_connection_2,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            redial_interval=redial_interval,
            start_time=start_time,
            end_time=end_time,
            mss_clamping_type=mss_clamping_type,
            mss_clamping_value=mss_clamping_value,
        )

        ipv_4_pptp_open_api_vo.additional_properties = d
        return ipv_4_pptp_open_api_vo

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
