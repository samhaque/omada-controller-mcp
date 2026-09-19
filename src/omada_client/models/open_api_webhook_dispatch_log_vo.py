from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.open_api_dispatch_log_detail_vo import OpenApiDispatchLogDetailVO
    from ..models.open_api_webhook_attempt_message_vo import (
        OpenApiWebhookAttemptMessageVO,
    )
    from ..models.open_api_webhook_log_message_vo import OpenApiWebhookLogMessageVO


T = TypeVar("T", bound="OpenApiWebhookDispatchLogVO")


@_attrs_define
class OpenApiWebhookDispatchLogVO:
    """
    Attributes:
        dispatch_message (OpenApiWebhookLogMessageVO | Unset): Dispatch Log Message
        dispatch_detail (OpenApiDispatchLogDetailVO | Unset): Dispatch Log Detail
        attempt_messages (list[OpenApiWebhookAttemptMessageVO] | Unset): Attempt Message of Dispatch Log Detail
    """

    dispatch_message: OpenApiWebhookLogMessageVO | Unset = UNSET
    dispatch_detail: OpenApiDispatchLogDetailVO | Unset = UNSET
    attempt_messages: list[OpenApiWebhookAttemptMessageVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dispatch_message: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dispatch_message, Unset):
            dispatch_message = self.dispatch_message.to_dict()

        dispatch_detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dispatch_detail, Unset):
            dispatch_detail = self.dispatch_detail.to_dict()

        attempt_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attempt_messages, Unset):
            attempt_messages = []
            for attempt_messages_item_data in self.attempt_messages:
                attempt_messages_item = attempt_messages_item_data.to_dict()
                attempt_messages.append(attempt_messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dispatch_message is not UNSET:
            field_dict["dispatchMessage"] = dispatch_message
        if dispatch_detail is not UNSET:
            field_dict["dispatchDetail"] = dispatch_detail
        if attempt_messages is not UNSET:
            field_dict["attemptMessages"] = attempt_messages

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.open_api_dispatch_log_detail_vo import (
            OpenApiDispatchLogDetailVO,
        )
        from ..models.open_api_webhook_attempt_message_vo import (
            OpenApiWebhookAttemptMessageVO,
        )
        from ..models.open_api_webhook_log_message_vo import (
            OpenApiWebhookLogMessageVO,
        )

        d = dict(src_dict)
        _dispatch_message = d.pop("dispatchMessage", UNSET)
        dispatch_message: OpenApiWebhookLogMessageVO | Unset
        if isinstance(_dispatch_message, Unset):
            dispatch_message = UNSET
        else:
            dispatch_message = OpenApiWebhookLogMessageVO.from_dict(_dispatch_message)

        _dispatch_detail = d.pop("dispatchDetail", UNSET)
        dispatch_detail: OpenApiDispatchLogDetailVO | Unset
        if isinstance(_dispatch_detail, Unset):
            dispatch_detail = UNSET
        else:
            dispatch_detail = OpenApiDispatchLogDetailVO.from_dict(_dispatch_detail)

        _attempt_messages = d.pop("attemptMessages", UNSET)
        attempt_messages: list[OpenApiWebhookAttemptMessageVO] | Unset = UNSET
        if _attempt_messages is not UNSET:
            attempt_messages = []
            for attempt_messages_item_data in _attempt_messages:
                attempt_messages_item = OpenApiWebhookAttemptMessageVO.from_dict(
                    attempt_messages_item_data
                )

                attempt_messages.append(attempt_messages_item)

        open_api_webhook_dispatch_log_vo = cls(
            dispatch_message=dispatch_message,
            dispatch_detail=dispatch_detail,
            attempt_messages=attempt_messages,
        )

        open_api_webhook_dispatch_log_vo.additional_properties = d
        return open_api_webhook_dispatch_log_vo

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
