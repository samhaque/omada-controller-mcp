from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_alert_email_open_api_vo import LogAlertEmailOpenApiVO
    from ..models.log_notification_edit_open_api_v2vo import (
        LogNotificationEditOpenApiV2VO,
    )
    from ..models.webhook_config_edit_open_api_vo import WebhookConfigEditOpenApiVO


T = TypeVar("T", bound="LogNotificationSettingEditOpenApiV2VO")


@_attrs_define
class LogNotificationSettingEditOpenApiV2VO:
    """
    Attributes:
        webhook_config (WebhookConfigEditOpenApiVO | Unset): Log Notification Webhook Config (This config applies to the
            Omada Pro Controller only)
        alert_notifications (list[LogNotificationEditOpenApiV2VO] | Unset): Alert Notification List
        event_notifications (list[LogNotificationEditOpenApiV2VO] | Unset): Event Notification List
        alert_email_setting (LogAlertEmailOpenApiVO | Unset): Log Event Email (This config applies to the log site view)
        event_email_setting (LogAlertEmailOpenApiVO | Unset): Log Event Email (This config applies to the log site view)
    """

    webhook_config: WebhookConfigEditOpenApiVO | Unset = UNSET
    alert_notifications: list[LogNotificationEditOpenApiV2VO] | Unset = UNSET
    event_notifications: list[LogNotificationEditOpenApiV2VO] | Unset = UNSET
    alert_email_setting: LogAlertEmailOpenApiVO | Unset = UNSET
    event_email_setting: LogAlertEmailOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_config, Unset):
            webhook_config = self.webhook_config.to_dict()

        alert_notifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.alert_notifications, Unset):
            alert_notifications = []
            for alert_notifications_item_data in self.alert_notifications:
                alert_notifications_item = alert_notifications_item_data.to_dict()
                alert_notifications.append(alert_notifications_item)

        event_notifications: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.event_notifications, Unset):
            event_notifications = []
            for event_notifications_item_data in self.event_notifications:
                event_notifications_item = event_notifications_item_data.to_dict()
                event_notifications.append(event_notifications_item)

        alert_email_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_email_setting, Unset):
            alert_email_setting = self.alert_email_setting.to_dict()

        event_email_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.event_email_setting, Unset):
            event_email_setting = self.event_email_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if webhook_config is not UNSET:
            field_dict["webhookConfig"] = webhook_config
        if alert_notifications is not UNSET:
            field_dict["alertNotifications"] = alert_notifications
        if event_notifications is not UNSET:
            field_dict["eventNotifications"] = event_notifications
        if alert_email_setting is not UNSET:
            field_dict["alertEmailSetting"] = alert_email_setting
        if event_email_setting is not UNSET:
            field_dict["eventEmailSetting"] = event_email_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.log_alert_email_open_api_vo import (
            LogAlertEmailOpenApiVO,
        )
        from ..models.log_notification_edit_open_api_v2vo import (
            LogNotificationEditOpenApiV2VO,
        )
        from ..models.webhook_config_edit_open_api_vo import (
            WebhookConfigEditOpenApiVO,
        )

        d = dict(src_dict)
        _webhook_config = d.pop("webhookConfig", UNSET)
        webhook_config: WebhookConfigEditOpenApiVO | Unset
        if isinstance(_webhook_config, Unset):
            webhook_config = UNSET
        else:
            webhook_config = WebhookConfigEditOpenApiVO.from_dict(_webhook_config)

        _alert_notifications = d.pop("alertNotifications", UNSET)
        alert_notifications: list[LogNotificationEditOpenApiV2VO] | Unset = UNSET
        if _alert_notifications is not UNSET:
            alert_notifications = []
            for alert_notifications_item_data in _alert_notifications:
                alert_notifications_item = LogNotificationEditOpenApiV2VO.from_dict(
                    alert_notifications_item_data
                )

                alert_notifications.append(alert_notifications_item)

        _event_notifications = d.pop("eventNotifications", UNSET)
        event_notifications: list[LogNotificationEditOpenApiV2VO] | Unset = UNSET
        if _event_notifications is not UNSET:
            event_notifications = []
            for event_notifications_item_data in _event_notifications:
                event_notifications_item = LogNotificationEditOpenApiV2VO.from_dict(
                    event_notifications_item_data
                )

                event_notifications.append(event_notifications_item)

        _alert_email_setting = d.pop("alertEmailSetting", UNSET)
        alert_email_setting: LogAlertEmailOpenApiVO | Unset
        if isinstance(_alert_email_setting, Unset):
            alert_email_setting = UNSET
        else:
            alert_email_setting = LogAlertEmailOpenApiVO.from_dict(_alert_email_setting)

        _event_email_setting = d.pop("eventEmailSetting", UNSET)
        event_email_setting: LogAlertEmailOpenApiVO | Unset
        if isinstance(_event_email_setting, Unset):
            event_email_setting = UNSET
        else:
            event_email_setting = LogAlertEmailOpenApiVO.from_dict(_event_email_setting)

        log_notification_setting_edit_open_api_v2vo = cls(
            webhook_config=webhook_config,
            alert_notifications=alert_notifications,
            event_notifications=event_notifications,
            alert_email_setting=alert_email_setting,
            event_email_setting=event_email_setting,
        )

        log_notification_setting_edit_open_api_v2vo.additional_properties = d
        return log_notification_setting_edit_open_api_v2vo

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
