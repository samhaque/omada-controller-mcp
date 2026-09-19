from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenApiWebhookMessageVO")


@_attrs_define
class OpenApiWebhookMessageVO:
    """Webhook Message

    Attributes:
        status (int | Unset): Webhook Push Status. It should be a value as follows: 0: Success; 1: Failed
        message_code (int | Unset): Http Message Code of Webhook Push
    """

    status: int | Unset = UNSET
    message_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message_code = self.message_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if message_code is not UNSET:
            field_dict["messageCode"] = message_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        message_code = d.pop("messageCode", UNSET)

        open_api_webhook_message_vo = cls(
            status=status,
            message_code=message_code,
        )

        open_api_webhook_message_vo.additional_properties = d
        return open_api_webhook_message_vo

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
