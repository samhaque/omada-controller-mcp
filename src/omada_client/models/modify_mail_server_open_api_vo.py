from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyMailServerOpenApiVO")


@_attrs_define
class ModifyMailServerOpenApiVO:
    """
    Attributes:
        smtp_server (str): The domain name of the SMTP mailbox server.
        port (int): The port of the SMTP mailbox server,xxxx  should be within the range of 1-65535
        ssl_enable (bool): Whether the SMTP mailbox server uses SSL encryption.
        auth_enable (bool): Whether the SMTP email server uses basic authentication.
        smtp_enable (bool | Unset): Enable SMTP mail server
        username (str | Unset): The user's email address used for authentication.
        password (str | Unset): The user's email password used for authentication.
        sender_address (str | Unset): The email address from which the message was sent.
        receiver (str | Unset): The email address where the message will be received.
    """

    smtp_server: str
    port: int
    ssl_enable: bool
    auth_enable: bool
    smtp_enable: bool | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    sender_address: str | Unset = UNSET
    receiver: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        smtp_server = self.smtp_server

        port = self.port

        ssl_enable = self.ssl_enable

        auth_enable = self.auth_enable

        smtp_enable = self.smtp_enable

        username = self.username

        password = self.password

        sender_address = self.sender_address

        receiver = self.receiver

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "smtpServer": smtp_server,
                "port": port,
                "sslEnable": ssl_enable,
                "authEnable": auth_enable,
            }
        )
        if smtp_enable is not UNSET:
            field_dict["smtpEnable"] = smtp_enable
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if sender_address is not UNSET:
            field_dict["senderAddress"] = sender_address
        if receiver is not UNSET:
            field_dict["receiver"] = receiver

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        smtp_server = d.pop("smtpServer")

        port = d.pop("port")

        ssl_enable = d.pop("sslEnable")

        auth_enable = d.pop("authEnable")

        smtp_enable = d.pop("smtpEnable", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        sender_address = d.pop("senderAddress", UNSET)

        receiver = d.pop("receiver", UNSET)

        modify_mail_server_open_api_vo = cls(
            smtp_server=smtp_server,
            port=port,
            ssl_enable=ssl_enable,
            auth_enable=auth_enable,
            smtp_enable=smtp_enable,
            username=username,
            password=password,
            sender_address=sender_address,
            receiver=receiver,
        )

        modify_mail_server_open_api_vo.additional_properties = d
        return modify_mail_server_open_api_vo

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
