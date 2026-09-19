from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_api_webhook_message_vo import OpenApiWebhookMessageVO


T = TypeVar("T", bound="OpenApiWebhookLogMessageVO")


@_attrs_define
class OpenApiWebhookLogMessageVO:
    """Dispatch Log Message

    Attributes:
        url (str | Unset): Webhook URL
        webhook_message (OpenApiWebhookMessageVO | Unset): Webhook Message
        dispatch_time (int | Unset): Webhook Dispatch Log Time, Unit (ms)
    """

    url: str | Unset = UNSET
    webhook_message: OpenApiWebhookMessageVO | Unset = UNSET
    dispatch_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        webhook_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhook_message, Unset):
            webhook_message = self.webhook_message.to_dict()

        dispatch_time = self.dispatch_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if webhook_message is not UNSET:
            field_dict["webhookMessage"] = webhook_message
        if dispatch_time is not UNSET:
            field_dict["dispatchTime"] = dispatch_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.open_api_webhook_message_vo import (
            OpenApiWebhookMessageVO,
        )

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _webhook_message = d.pop("webhookMessage", UNSET)
        webhook_message: OpenApiWebhookMessageVO | Unset
        if isinstance(_webhook_message, Unset):
            webhook_message = UNSET
        else:
            webhook_message = OpenApiWebhookMessageVO.from_dict(_webhook_message)

        dispatch_time = d.pop("dispatchTime", UNSET)

        open_api_webhook_log_message_vo = cls(
            url=url,
            webhook_message=webhook_message,
            dispatch_time=dispatch_time,
        )

        open_api_webhook_log_message_vo.additional_properties = d
        return open_api_webhook_log_message_vo

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
