from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogNotificationEditOpenApiV2VO")


@_attrs_define
class LogNotificationEditOpenApiV2VO:
    """Event Notification List

    Attributes:
        key (str): For the values of Log Notification Key, refer to section 5.6.1 of the Open API Access Example:
            LOGIN_OK.
        enable (bool): Log Notification Enable or Disable Example: True.
        email (bool): Log Notification Enable or Disable Email Example: True.
        webhook (bool | Unset): Log Notification Category Enable or Disable Webhook (This config applies to the Omada
            Pro Controller only and should not bu null) Example: False.
    """

    key: str
    enable: bool
    email: bool
    webhook: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        enable = self.enable

        email = self.email

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "enable": enable,
                "email": email,
            }
        )
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        enable = d.pop("enable")

        email = d.pop("email")

        webhook = d.pop("webhook", UNSET)

        log_notification_edit_open_api_v2vo = cls(
            key=key,
            enable=enable,
            email=email,
            webhook=webhook,
        )

        log_notification_edit_open_api_v2vo.additional_properties = d
        return log_notification_edit_open_api_v2vo

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
