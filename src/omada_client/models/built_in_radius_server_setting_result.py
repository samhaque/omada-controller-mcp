from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.radius_server_certificate_setting import (
        RADIUSServerCertificateSetting,
    )


T = TypeVar("T", bound="BuiltInRADIUSServerSettingResult")


@_attrs_define
class BuiltInRADIUSServerSettingResult:
    """
    Attributes:
        enable (bool): Whether the Built-In RADIUS server is enabled.
        auth_server_port (int): Server port.
        secret (str): Server secrect.
        tunnel_reply_enable (bool): Whether the Tunneled Reply is enabled.
        server_address_type (int): Built In RADIUS server address type, 0: Auto generated, 1: Custom
        status (bool | Unset): Built-In RADIUS server real running status.
        fail_reason (str | Unset): Startup failed reason, required when parameter [status] is false.
        custom_address (str | Unset): Customize server address, required when parameter [serverAddressType] is 1.
        radius_server_certificate (RADIUSServerCertificateSetting | Unset): RADIUS server certificate
        require_message_authenticator (bool | Unset): Message-Authenticator parameter verification enable status
        limit_proxy_state (bool | Unset): Proxy-State parameter limit status
    """

    enable: bool
    auth_server_port: int
    secret: str
    tunnel_reply_enable: bool
    server_address_type: int
    status: bool | Unset = UNSET
    fail_reason: str | Unset = UNSET
    custom_address: str | Unset = UNSET
    radius_server_certificate: RADIUSServerCertificateSetting | Unset = UNSET
    require_message_authenticator: bool | Unset = UNSET
    limit_proxy_state: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        auth_server_port = self.auth_server_port

        secret = self.secret

        tunnel_reply_enable = self.tunnel_reply_enable

        server_address_type = self.server_address_type

        status = self.status

        fail_reason = self.fail_reason

        custom_address = self.custom_address

        radius_server_certificate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius_server_certificate, Unset):
            radius_server_certificate = self.radius_server_certificate.to_dict()

        require_message_authenticator = self.require_message_authenticator

        limit_proxy_state = self.limit_proxy_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
                "authServerPort": auth_server_port,
                "secret": secret,
                "tunnelReplyEnable": tunnel_reply_enable,
                "serverAddressType": server_address_type,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if fail_reason is not UNSET:
            field_dict["failReason"] = fail_reason
        if custom_address is not UNSET:
            field_dict["customAddress"] = custom_address
        if radius_server_certificate is not UNSET:
            field_dict["radiusServerCertificate"] = radius_server_certificate
        if require_message_authenticator is not UNSET:
            field_dict["requireMessageAuthenticator"] = require_message_authenticator
        if limit_proxy_state is not UNSET:
            field_dict["limitProxyState"] = limit_proxy_state

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.radius_server_certificate_setting import (
            RADIUSServerCertificateSetting,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        auth_server_port = d.pop("authServerPort")

        secret = d.pop("secret")

        tunnel_reply_enable = d.pop("tunnelReplyEnable")

        server_address_type = d.pop("serverAddressType")

        status = d.pop("status", UNSET)

        fail_reason = d.pop("failReason", UNSET)

        custom_address = d.pop("customAddress", UNSET)

        _radius_server_certificate = d.pop("radiusServerCertificate", UNSET)
        radius_server_certificate: RADIUSServerCertificateSetting | Unset
        if isinstance(_radius_server_certificate, Unset):
            radius_server_certificate = UNSET
        else:
            radius_server_certificate = RADIUSServerCertificateSetting.from_dict(
                _radius_server_certificate
            )

        require_message_authenticator = d.pop("requireMessageAuthenticator", UNSET)

        limit_proxy_state = d.pop("limitProxyState", UNSET)

        built_in_radius_server_setting_result = cls(
            enable=enable,
            auth_server_port=auth_server_port,
            secret=secret,
            tunnel_reply_enable=tunnel_reply_enable,
            server_address_type=server_address_type,
            status=status,
            fail_reason=fail_reason,
            custom_address=custom_address,
            radius_server_certificate=radius_server_certificate,
            require_message_authenticator=require_message_authenticator,
            limit_proxy_state=limit_proxy_state,
        )

        built_in_radius_server_setting_result.additional_properties = d
        return built_in_radius_server_setting_result

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
