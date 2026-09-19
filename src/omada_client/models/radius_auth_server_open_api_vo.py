from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusAuthServerOpenApiVO")


@_attrs_define
class RadiusAuthServerOpenApiVO:
    """Radius authentication server list

    Attributes:
        radius_server_ip (str): Radius authentication server IP. In Pro Site of the Omada Pro Controller,
            [radiusServerIp] should be a valid IP or domain address. In Omada Controller and Basic Site of the Omada Pro
            Controller, [radiusServerIp] should be a valid IP address.
        radius_port (int): Radius authentication server port, radiusPort should be within the range of 1-65535
        radius_pwd (str): Radius authentication server password, radiusPwd should contain 1 to 64 characters,The
            question mark (?), double quote ("), percent sign (%), and backslash (\\) may cause the RADIUS function to fail
            and are not recommended.
        rad_sec_enable (bool | Unset): Radius RadSec enable status
        ca_cert (str | Unset): CA certification profile id
        client_cert (str | Unset): Client certification profile id
    """

    radius_server_ip: str
    radius_port: int
    radius_pwd: str
    rad_sec_enable: bool | Unset = UNSET
    ca_cert: str | Unset = UNSET
    client_cert: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_server_ip = self.radius_server_ip

        radius_port = self.radius_port

        radius_pwd = self.radius_pwd

        rad_sec_enable = self.rad_sec_enable

        ca_cert = self.ca_cert

        client_cert = self.client_cert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radiusServerIp": radius_server_ip,
                "radiusPort": radius_port,
                "radiusPwd": radius_pwd,
            }
        )
        if rad_sec_enable is not UNSET:
            field_dict["radSecEnable"] = rad_sec_enable
        if ca_cert is not UNSET:
            field_dict["caCert"] = ca_cert
        if client_cert is not UNSET:
            field_dict["clientCert"] = client_cert

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radius_server_ip = d.pop("radiusServerIp")

        radius_port = d.pop("radiusPort")

        radius_pwd = d.pop("radiusPwd")

        rad_sec_enable = d.pop("radSecEnable", UNSET)

        ca_cert = d.pop("caCert", UNSET)

        client_cert = d.pop("clientCert", UNSET)

        radius_auth_server_open_api_vo = cls(
            radius_server_ip=radius_server_ip,
            radius_port=radius_port,
            radius_pwd=radius_pwd,
            rad_sec_enable=rad_sec_enable,
            ca_cert=ca_cert,
            client_cert=client_cert,
        )

        radius_auth_server_open_api_vo.additional_properties = d
        return radius_auth_server_open_api_vo

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
