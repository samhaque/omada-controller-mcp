from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusAcctServerOpenApiVO")


@_attrs_define
class RadiusAcctServerOpenApiVO:
    """Radius accounting server list, valid when parameter [radiusAccountingEnable] is true

    Attributes:
        accounting_server_ip (str): Radius Accounting Server IP.In Pro Site of the Omada Pro Controller,
            [accountingServerIp] should be a valid IP or domain address. In Omada Controller and Basic Site of the Omada Pro
            Controller, [accountingServerIp] should be a valid IP address.
        accounting_server_port (int): Radius Accounting port. AccountingServerPort should be within the range of 1-65535
        accounting_server_pwd (str): Radius Accounting password,The question mark (?), double quote ("), percent sign
            (%), and backslash (\\) may cause the RADIUS function to fail and are not recommended.
        rad_sec_enable (bool | Unset): Radius RadSec enable status
        ca_cert (str | Unset): CA certification profile id
        client_cert (str | Unset): Client certification profile id
    """

    accounting_server_ip: str
    accounting_server_port: int
    accounting_server_pwd: str
    rad_sec_enable: bool | Unset = UNSET
    ca_cert: str | Unset = UNSET
    client_cert: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accounting_server_ip = self.accounting_server_ip

        accounting_server_port = self.accounting_server_port

        accounting_server_pwd = self.accounting_server_pwd

        rad_sec_enable = self.rad_sec_enable

        ca_cert = self.ca_cert

        client_cert = self.client_cert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountingServerIp": accounting_server_ip,
                "accountingServerPort": accounting_server_port,
                "accountingServerPwd": accounting_server_pwd,
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
        accounting_server_ip = d.pop("accountingServerIp")

        accounting_server_port = d.pop("accountingServerPort")

        accounting_server_pwd = d.pop("accountingServerPwd")

        rad_sec_enable = d.pop("radSecEnable", UNSET)

        ca_cert = d.pop("caCert", UNSET)

        client_cert = d.pop("clientCert", UNSET)

        radius_acct_server_open_api_vo = cls(
            accounting_server_ip=accounting_server_ip,
            accounting_server_port=accounting_server_port,
            accounting_server_pwd=accounting_server_pwd,
            rad_sec_enable=rad_sec_enable,
            ca_cert=ca_cert,
            client_cert=client_cert,
        )

        radius_acct_server_open_api_vo.additional_properties = d
        return radius_acct_server_open_api_vo

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
