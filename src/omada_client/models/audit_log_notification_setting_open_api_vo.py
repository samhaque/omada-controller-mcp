from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_log_notification_open_api_vo import (
        AuditLogNotificationOpenApiVO,
    )
    from ..models.webhook_config_open_api_vo import WebhookConfigOpenApiVO


T = TypeVar("T", bound="AuditLogNotificationSettingOpenApiVO")


@_attrs_define
class AuditLogNotificationSettingOpenApiVO:
    """
    Attributes:
        webhook_config (WebhookConfigOpenApiVO | Unset): Log Notification Webhook Config (This config applies to the
            Omada Pro Controller only)
        audit_log_notifications (list[AuditLogNotificationOpenApiVO] | Unset): Audit Log Notification List
    """

    webhook_config: WebhookConfigOpenApiVO | Unset = UNSET
    audit_log_notifications: list[AuditLogNotificationOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_config, Unset):
            webhook_config = self.webhook_config.to_dict()

        audit_log_notifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.audit_log_notifications, Unset):
            audit_log_notifications = []
            for audit_log_notifications_item_data in self.audit_log_notifications:
                audit_log_notifications_item = (
                    audit_log_notifications_item_data.to_dict()
                )
                audit_log_notifications.append(audit_log_notifications_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_config is not UNSET:
            field_dict["webhookConfig"] = webhook_config
        if audit_log_notifications is not UNSET:
            field_dict["auditLogNotifications"] = audit_log_notifications

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.audit_log_notification_open_api_vo import (
            AuditLogNotificationOpenApiVO,
        )
        from ..models.webhook_config_open_api_vo import (
            WebhookConfigOpenApiVO,
        )

        d = dict(src_dict)
        _webhook_config = d.pop("webhookConfig", UNSET)
        webhook_config: WebhookConfigOpenApiVO | Unset
        if isinstance(_webhook_config, Unset):
            webhook_config = UNSET
        else:
            webhook_config = WebhookConfigOpenApiVO.from_dict(_webhook_config)

        _audit_log_notifications = d.pop("auditLogNotifications", UNSET)
        audit_log_notifications: list[AuditLogNotificationOpenApiVO] | Unset = UNSET
        if _audit_log_notifications is not UNSET:
            audit_log_notifications = []
            for audit_log_notifications_item_data in _audit_log_notifications:
                audit_log_notifications_item = AuditLogNotificationOpenApiVO.from_dict(
                    audit_log_notifications_item_data
                )

                audit_log_notifications.append(audit_log_notifications_item)

        audit_log_notification_setting_open_api_vo = cls(
            webhook_config=webhook_config,
            audit_log_notifications=audit_log_notifications,
        )

        audit_log_notification_setting_open_api_vo.additional_properties = d
        return audit_log_notification_setting_open_api_vo

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
