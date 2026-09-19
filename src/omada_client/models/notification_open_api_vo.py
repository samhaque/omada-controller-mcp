from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.alert_email_setting_vo import AlertEmailSettingVO
    from ..models.notification_configuration_open_api_vo import (
        NotificationConfigurationOpenApiVO,
    )
    from ..models.recipients_vo import RecipientsVO


T = TypeVar("T", bound="NotificationOpenApiVO")


@_attrs_define
class NotificationOpenApiVO:
    """
    Attributes:
        alert_email_setting (AlertEmailSettingVO | Unset): Abnormal Alert Email(This config applies to the Abnormal >
            Notification view).
        email (NotificationConfigurationOpenApiVO | Unset): Email Alerts List(This config applies to the Abnormal >
            Notification view).
        resource (int | Unset): The incident notifiction setting creation resource, such as: 0: new created, 1: from
            template, 2: override.
        recipients (list[RecipientsVO] | Unset): Recipients of the incident notifiction
    """

    alert_email_setting: AlertEmailSettingVO | Unset = UNSET
    email: NotificationConfigurationOpenApiVO | Unset = UNSET
    resource: int | Unset = UNSET
    recipients: list[RecipientsVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        alert_email_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.alert_email_setting, Unset):
            alert_email_setting = self.alert_email_setting.to_dict()

        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        resource = self.resource

        recipients: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recipients, Unset):
            recipients = []
            for recipients_item_data in self.recipients:
                recipients_item = recipients_item_data.to_dict()
                recipients.append(recipients_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_email_setting is not UNSET:
            field_dict["alertEmailSetting"] = alert_email_setting
        if email is not UNSET:
            field_dict["email"] = email
        if resource is not UNSET:
            field_dict["resource"] = resource
        if recipients is not UNSET:
            field_dict["recipients"] = recipients

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.alert_email_setting_vo import AlertEmailSettingVO
        from ..models.notification_configuration_open_api_vo import (
            NotificationConfigurationOpenApiVO,
        )
        from ..models.recipients_vo import RecipientsVO

        d = dict(src_dict)
        _alert_email_setting = d.pop("alertEmailSetting", UNSET)
        alert_email_setting: AlertEmailSettingVO | Unset
        if isinstance(_alert_email_setting, Unset):
            alert_email_setting = UNSET
        else:
            alert_email_setting = AlertEmailSettingVO.from_dict(_alert_email_setting)

        _email = d.pop("email", UNSET)
        email: NotificationConfigurationOpenApiVO | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = NotificationConfigurationOpenApiVO.from_dict(_email)

        resource = d.pop("resource", UNSET)

        _recipients = d.pop("recipients", UNSET)
        recipients: list[RecipientsVO] | Unset = UNSET
        if _recipients is not UNSET:
            recipients = []
            for recipients_item_data in _recipients:
                recipients_item = RecipientsVO.from_dict(recipients_item_data)

                recipients.append(recipients_item)

        notification_open_api_vo = cls(
            alert_email_setting=alert_email_setting,
            email=email,
            resource=resource,
            recipients=recipients,
        )

        notification_open_api_vo.additional_properties = d
        return notification_open_api_vo

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
