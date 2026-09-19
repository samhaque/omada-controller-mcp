from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PortalPort")


@_attrs_define
class PortalPort:
    """
    Attributes:
        portal_http_port (int | Unset): Portal HTTP Port should be 80 or between 1024 and 65535
        portal_https_port (int | Unset): Portal HTTPS Port should be between 1024 and 65535
        auto_portal_ip_enable (bool | Unset): Auto portal IP enable status
        portal_https_redirect (bool | Unset): Portal HTTPS redirect status
        portal_host (str | Unset): Portal Host should be a domain name or IP address
    """

    portal_http_port: int | Unset = UNSET
    portal_https_port: int | Unset = UNSET
    auto_portal_ip_enable: bool | Unset = UNSET
    portal_https_redirect: bool | Unset = UNSET
    portal_host: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        portal_http_port = self.portal_http_port

        portal_https_port = self.portal_https_port

        auto_portal_ip_enable = self.auto_portal_ip_enable

        portal_https_redirect = self.portal_https_redirect

        portal_host = self.portal_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if portal_http_port is not UNSET:
            field_dict["portalHttpPort"] = portal_http_port
        if portal_https_port is not UNSET:
            field_dict["portalHttpsPort"] = portal_https_port
        if auto_portal_ip_enable is not UNSET:
            field_dict["autoPortalIpEnable"] = auto_portal_ip_enable
        if portal_https_redirect is not UNSET:
            field_dict["portalHttpsRedirect"] = portal_https_redirect
        if portal_host is not UNSET:
            field_dict["portalHost"] = portal_host

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        portal_http_port = d.pop("portalHttpPort", UNSET)

        portal_https_port = d.pop("portalHttpsPort", UNSET)

        auto_portal_ip_enable = d.pop("autoPortalIpEnable", UNSET)

        portal_https_redirect = d.pop("portalHttpsRedirect", UNSET)

        portal_host = d.pop("portalHost", UNSET)

        portal_port = cls(
            portal_http_port=portal_http_port,
            portal_https_port=portal_https_port,
            auto_portal_ip_enable=auto_portal_ip_enable,
            portal_https_redirect=portal_https_redirect,
            portal_host=portal_host,
        )

        portal_port.additional_properties = d
        return portal_port

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
