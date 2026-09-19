from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeviceAccessManagementSetting")


@_attrs_define
class DeviceAccessManagementSetting:
    """Device Access Management Setting.

    Attributes:
        web_control_http (bool): Control device web http accessing.
        web_control_https (bool): Control device web https accessing.
        app_discovery (bool): Control device app discovery, bind with device web https access, if appDiscvoery is
            enabled, webControlHttps must be enabled.
    """

    web_control_http: bool
    web_control_https: bool
    app_discovery: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_control_http = self.web_control_http

        web_control_https = self.web_control_https

        app_discovery = self.app_discovery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webControlHttp": web_control_http,
                "webControlHttps": web_control_https,
                "appDiscovery": app_discovery,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        web_control_http = d.pop("webControlHttp")

        web_control_https = d.pop("webControlHttps")

        app_discovery = d.pop("appDiscovery")

        device_access_management_setting = cls(
            web_control_http=web_control_http,
            web_control_https=web_control_https,
            app_discovery=app_discovery,
        )

        device_access_management_setting.additional_properties = d
        return device_access_management_setting

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
