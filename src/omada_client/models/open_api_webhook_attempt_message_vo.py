from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenApiWebhookAttemptMessageVO")


@_attrs_define
class OpenApiWebhookAttemptMessageVO:
    """Attempt Message of Dispatch Log Detail

    Attributes:
        status (int | Unset): Webhook Attempt Push Status: 0/1 (Success/Failed)
        message_code (int | Unset): Http Message Code of Webhook Attempt Push
        attempt_time (int | Unset): Webhook Attempt Push Time, Unit (ms)
    """

    status: int | Unset = UNSET
    message_code: int | Unset = UNSET
    attempt_time: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message_code = self.message_code

        attempt_time = self.attempt_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if message_code is not UNSET:
            field_dict["messageCode"] = message_code
        if attempt_time is not UNSET:
            field_dict["attemptTime"] = attempt_time

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        message_code = d.pop("messageCode", UNSET)

        attempt_time = d.pop("attemptTime", UNSET)

        open_api_webhook_attempt_message_vo = cls(
            status=status,
            message_code=message_code,
            attempt_time=attempt_time,
        )

        open_api_webhook_attempt_message_vo.additional_properties = d
        return open_api_webhook_attempt_message_vo

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
