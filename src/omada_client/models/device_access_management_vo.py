from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceAccessManagementVO")


@_attrs_define
class DeviceAccessManagementVO:
    """
    Attributes:
        web_control_http (bool | Unset): Web Control HTTP access switch, default to true.
        web_control_https (bool | Unset): Web Control HTTPS access switch, default to true.
        app_discovery (bool | Unset): Device app management discovery switch, default to true.
    """

    web_control_http: bool | Unset = UNSET
    web_control_https: bool | Unset = UNSET
    app_discovery: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        web_control_http = self.web_control_http

        web_control_https = self.web_control_https

        app_discovery = self.app_discovery

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if web_control_http is not UNSET:
            field_dict["webControlHttp"] = web_control_http
        if web_control_https is not UNSET:
            field_dict["webControlHttps"] = web_control_https
        if app_discovery is not UNSET:
            field_dict["appDiscovery"] = app_discovery

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        web_control_http = d.pop("webControlHttp", UNSET)

        web_control_https = d.pop("webControlHttps", UNSET)

        app_discovery = d.pop("appDiscovery", UNSET)

        device_access_management_vo = cls(
            web_control_http=web_control_http,
            web_control_https=web_control_https,
            app_discovery=app_discovery,
        )

        device_access_management_vo.additional_properties = d
        return device_access_management_vo

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
