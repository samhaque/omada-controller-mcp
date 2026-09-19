from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExternalServerPortalSetting")


@_attrs_define
class ExternalServerPortalSetting:
    """External Server Portal Setting.

    Attributes:
        host_type (int): Host type, should be a value as follows: 1: IP; 2: URL
        server_ip (str | Unset): Server IP, required when [hostType] is 1, pattern as "xx.xx.xx.xx".
        server_port (int | Unset): Server port, required when [hostType] is 1, from 1 to 65535.
        server_url_scheme (str | Unset): Server url scheme, required when [hostType] is 2, value is http or https.
        server_url (str | Unset): Server url, required when [hostType] is 2.
    """

    host_type: int
    server_ip: str | Unset = UNSET
    server_port: int | Unset = UNSET
    server_url_scheme: str | Unset = UNSET
    server_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        host_type = self.host_type

        server_ip = self.server_ip

        server_port = self.server_port

        server_url_scheme = self.server_url_scheme

        server_url = self.server_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostType": host_type,
            }
        )
        if server_ip is not UNSET:
            field_dict["serverIp"] = server_ip
        if server_port is not UNSET:
            field_dict["serverPort"] = server_port
        if server_url_scheme is not UNSET:
            field_dict["serverUrlScheme"] = server_url_scheme
        if server_url is not UNSET:
            field_dict["serverUrl"] = server_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        host_type = d.pop("hostType")

        server_ip = d.pop("serverIp", UNSET)

        server_port = d.pop("serverPort", UNSET)

        server_url_scheme = d.pop("serverUrlScheme", UNSET)

        server_url = d.pop("serverUrl", UNSET)

        external_server_portal_setting = cls(
            host_type=host_type,
            server_ip=server_ip,
            server_port=server_port,
            server_url_scheme=server_url_scheme,
            server_url=server_url,
        )

        external_server_portal_setting.additional_properties = d
        return external_server_portal_setting

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
