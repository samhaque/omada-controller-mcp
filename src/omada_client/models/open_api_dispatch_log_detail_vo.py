from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenApiDispatchLogDetailVO")


@_attrs_define
class OpenApiDispatchLogDetailVO:
    """Dispatch Log Detail

    Attributes:
        headers (str | Unset): Http Headers of Webhook Push
        content (str | Unset): Webhook Push Content
        attempt_number (int | Unset): Webhook Attempt Number
    """

    headers: str | Unset = UNSET
    content: str | Unset = UNSET
    attempt_number: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers = self.headers

        content = self.content

        attempt_number = self.attempt_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if headers is not UNSET:
            field_dict["headers"] = headers
        if content is not UNSET:
            field_dict["content"] = content
        if attempt_number is not UNSET:
            field_dict["attemptNumber"] = attempt_number

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        headers = d.pop("headers", UNSET)

        content = d.pop("content", UNSET)

        attempt_number = d.pop("attemptNumber", UNSET)

        open_api_dispatch_log_detail_vo = cls(
            headers=headers,
            content=content,
            attempt_number=attempt_number,
        )

        open_api_dispatch_log_detail_vo.additional_properties = d
        return open_api_dispatch_log_detail_vo

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
