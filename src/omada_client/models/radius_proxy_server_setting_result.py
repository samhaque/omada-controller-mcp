from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusProxyServerSettingResult")


@_attrs_define
class RadiusProxyServerSettingResult:
    """
    Attributes:
        enable (bool): Whether the RADIUS proxy server is enabled.
        port (int): Server port.
        status (bool | Unset): RADIUS proxy server real running status.
        fail_reason (str | Unset): Startup failed reason, required when parameter [status] is false.
        require_message_authenticator (bool | Unset): Message-Authenticator parameter verification enable status
        limit_proxy_state (bool | Unset): Proxy-State parameter limit status
    """

    enable: bool
    port: int
    status: bool | Unset = UNSET
    fail_reason: str | Unset = UNSET
    require_message_authenticator: bool | Unset = UNSET
    limit_proxy_state: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        port = self.port

        status = self.status

        fail_reason = self.fail_reason

        require_message_authenticator = self.require_message_authenticator

        limit_proxy_state = self.limit_proxy_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "port": port,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if fail_reason is not UNSET:
            field_dict["failReason"] = fail_reason
        if require_message_authenticator is not UNSET:
            field_dict["requireMessageAuthenticator"] = require_message_authenticator
        if limit_proxy_state is not UNSET:
            field_dict["limitProxyState"] = limit_proxy_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        port = d.pop("port")

        status = d.pop("status", UNSET)

        fail_reason = d.pop("failReason", UNSET)

        require_message_authenticator = d.pop("requireMessageAuthenticator", UNSET)

        limit_proxy_state = d.pop("limitProxyState", UNSET)

        radius_proxy_server_setting_result = cls(
            enable=enable,
            port=port,
            status=status,
            fail_reason=fail_reason,
            require_message_authenticator=require_message_authenticator,
            limit_proxy_state=limit_proxy_state,
        )

        radius_proxy_server_setting_result.additional_properties = d
        return radius_proxy_server_setting_result

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
