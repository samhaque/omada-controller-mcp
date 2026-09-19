from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MailServerOpenApiModifyVO")


@_attrs_define
class MailServerOpenApiModifyVO:
    """
    Attributes:
        sender (str): The email address of the sender.
        receiver (str): The email address of the receiver, which can be the same as or different from the sender's email
            address.
        ssl (bool): Enable this feature, and the data will be transmitted based on the SSL protocol.
        auth (bool): Enable this feature if the login of the mailbox requires a username and authorization code.
        smtp_server (str | Unset): Enter the domain name or IP address of the SMTP server.
        smtp_port (int | Unset): Enter the port used by the SMTP server according to the instructions of your email
            service provider.
        username (str | Unset): When Authentication is enabled, enter your email address as the username.
        auth_code (str | Unset): When Authentication is enabled, enter the authorization code that enables a third party
            to log in to the mailbox. Note that the authorization code is not the mailbox's password.
    """

    sender: str
    receiver: str
    ssl: bool
    auth: bool
    smtp_server: str | Unset = UNSET
    smtp_port: int | Unset = UNSET
    username: str | Unset = UNSET
    auth_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sender = self.sender

        receiver = self.receiver

        ssl = self.ssl

        auth = self.auth

        smtp_server = self.smtp_server

        smtp_port = self.smtp_port

        username = self.username

        auth_code = self.auth_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sender": sender,
                "receiver": receiver,
                "ssl": ssl,
                "auth": auth,
            }
        )
        if smtp_server is not UNSET:
            field_dict["smtpServer"] = smtp_server
        if smtp_port is not UNSET:
            field_dict["smtpPort"] = smtp_port
        if username is not UNSET:
            field_dict["username"] = username
        if auth_code is not UNSET:
            field_dict["authCode"] = auth_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        sender = d.pop("sender")

        receiver = d.pop("receiver")

        ssl = d.pop("ssl")

        auth = d.pop("auth")

        smtp_server = d.pop("smtpServer", UNSET)

        smtp_port = d.pop("smtpPort", UNSET)

        username = d.pop("username", UNSET)

        auth_code = d.pop("authCode", UNSET)

        mail_server_open_api_modify_vo = cls(
            sender=sender,
            receiver=receiver,
            ssl=ssl,
            auth=auth,
            smtp_server=smtp_server,
            smtp_port=smtp_port,
            username=username,
            auth_code=auth_code,
        )

        mail_server_open_api_modify_vo.additional_properties = d
        return mail_server_open_api_modify_vo

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
