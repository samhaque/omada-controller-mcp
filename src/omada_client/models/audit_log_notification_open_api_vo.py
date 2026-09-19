from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditLogNotificationOpenApiVO")


@_attrs_define
class AuditLogNotificationOpenApiVO:
    """Audit Log Notification List

    Attributes:
        key (str | Unset): Audit Log Notification Category Key Example: DASHBOARD.
        short_msg (str | Unset): Audit Log Notification Category Short Message Example: Dashboard.
        webhook (bool | Unset): Audit Log Notification Category Enable or Disable Webhook Example: False.
    """

    key: str | Unset = UNSET
    short_msg: str | Unset = UNSET
    webhook: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        short_msg = self.short_msg

        webhook = self.webhook

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if short_msg is not UNSET:
            field_dict["shortMsg"] = short_msg
        if webhook is not UNSET:
            field_dict["webhook"] = webhook

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        short_msg = d.pop("shortMsg", UNSET)

        webhook = d.pop("webhook", UNSET)

        audit_log_notification_open_api_vo = cls(
            key=key,
            short_msg=short_msg,
            webhook=webhook,
        )

        audit_log_notification_open_api_vo.additional_properties = d
        return audit_log_notification_open_api_vo

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
