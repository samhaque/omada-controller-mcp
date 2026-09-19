from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogNotificationOpenApiVO")


@_attrs_define
class LogNotificationOpenApiVO:
    """Log Notification List

    Attributes:
        key (str | Unset): Log Notification Key Example: LOGIN_OK.
        short_msg (str | Unset): Log Notification Short Message Example: User Logged In.
        alert (bool | Unset): Log Notification Enable or Disable Alert Example: False.
        event (bool | Unset): Log Notification Enable or Disable Event Example: True.
        email (bool | Unset): Log Notification Enable or Disable Email Example: True.
        webhook (bool | Unset): Log Notification Enable or Disable Webhook (This config applies to the Omada Pro
            Controller only) Example: False.
    """

    key: str | Unset = UNSET
    short_msg: str | Unset = UNSET
    alert: bool | Unset = UNSET
    event: bool | Unset = UNSET
    email: bool | Unset = UNSET
    webhook: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        short_msg = self.short_msg

        alert = self.alert

        event = self.event

        email = self.email

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if short_msg is not UNSET:
            field_dict["shortMsg"] = short_msg
        if alert is not UNSET:
            field_dict["alert"] = alert
        if event is not UNSET:
            field_dict["event"] = event
        if email is not UNSET:
            field_dict["email"] = email
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        short_msg = d.pop("shortMsg", UNSET)

        alert = d.pop("alert", UNSET)

        event = d.pop("event", UNSET)

        email = d.pop("email", UNSET)

        webhook = d.pop("webhook", UNSET)

        log_notification_open_api_vo = cls(
            key=key,
            short_msg=short_msg,
            alert=alert,
            event=event,
            email=email,
            webhook=webhook,
        )

        log_notification_open_api_vo.additional_properties = d
        return log_notification_open_api_vo

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
