from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookConfigEditOpenApiVO")


@_attrs_define
class WebhookConfigEditOpenApiVO:
    """Log Notification Webhook Config (This config applies to the Omada Pro Controller only)

    Attributes:
        webhook_enable (bool): Audit or Omada Log Notification Enable for Disable Webhook Example: False.
        webhook_id (str | Unset): Webhook ID (Webhook ID should be configured in webhook setting, when Webhook Enable is
            true)
    """

    webhook_enable: bool
    webhook_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        webhook_enable = self.webhook_enable

        webhook_id = self.webhook_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "webhookEnable": webhook_enable,
            }
        )
        if webhook_id is not UNSET:
            field_dict["webhookId"] = webhook_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        webhook_enable = d.pop("webhookEnable")

        webhook_id = d.pop("webhookId", UNSET)

        webhook_config_edit_open_api_vo = cls(
            webhook_enable=webhook_enable,
            webhook_id=webhook_id,
        )

        webhook_config_edit_open_api_vo.additional_properties = d
        return webhook_config_edit_open_api_vo

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
