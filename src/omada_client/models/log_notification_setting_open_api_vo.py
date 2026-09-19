from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_alert_email_open_api_vo import LogAlertEmailOpenApiVO
    from ..models.log_notification_open_api_vo import LogNotificationOpenApiVO
    from ..models.webhook_config_open_api_vo import WebhookConfigOpenApiVO


T = TypeVar("T", bound="LogNotificationSettingOpenApiVO")


@_attrs_define
class LogNotificationSettingOpenApiVO:
    """
    Attributes:
        webhook_config (WebhookConfigOpenApiVO | Unset): Log Notification Webhook Config (This config applies to the
            Omada Pro Controller only)
        log_notifications (list[LogNotificationOpenApiVO] | Unset): Log Notification List
        alert_email_setting (LogAlertEmailOpenApiVO | Unset): Log Event Email (This config applies to the log site view)
    """

    webhook_config: WebhookConfigOpenApiVO | Unset = UNSET
    log_notifications: list[LogNotificationOpenApiVO] | Unset = UNSET
    alert_email_setting: LogAlertEmailOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_config, Unset):
            webhook_config = self.webhook_config.to_dict()

        log_notifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.log_notifications, Unset):
            log_notifications = []
            for log_notifications_item_data in self.log_notifications:
                log_notifications_item = log_notifications_item_data.to_dict()
                log_notifications.append(log_notifications_item)

        alert_email_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_email_setting, Unset):
            alert_email_setting = self.alert_email_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_config is not UNSET:
            field_dict["webhookConfig"] = webhook_config
        if log_notifications is not UNSET:
            field_dict["logNotifications"] = log_notifications
        if alert_email_setting is not UNSET:
            field_dict["alertEmailSetting"] = alert_email_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.log_alert_email_open_api_vo import (
            LogAlertEmailOpenApiVO,
        )
        from ..models.log_notification_open_api_vo import (
            LogNotificationOpenApiVO,
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

        _log_notifications = d.pop("logNotifications", UNSET)
        log_notifications: list[LogNotificationOpenApiVO] | Unset = UNSET
        if _log_notifications is not UNSET:
            log_notifications = []
            for log_notifications_item_data in _log_notifications:
                log_notifications_item = LogNotificationOpenApiVO.from_dict(
                    log_notifications_item_data
                )

                log_notifications.append(log_notifications_item)

        _alert_email_setting = d.pop("alertEmailSetting", UNSET)
        alert_email_setting: LogAlertEmailOpenApiVO | Unset
        if isinstance(_alert_email_setting, Unset):
            alert_email_setting = UNSET
        else:
            alert_email_setting = LogAlertEmailOpenApiVO.from_dict(_alert_email_setting)

        log_notification_setting_open_api_vo = cls(
            webhook_config=webhook_config,
            log_notifications=log_notifications,
            alert_email_setting=alert_email_setting,
        )

        log_notification_setting_open_api_vo.additional_properties = d
        return log_notification_setting_open_api_vo

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
