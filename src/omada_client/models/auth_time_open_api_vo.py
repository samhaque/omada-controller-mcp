from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthTimeOpenApiVO")


@_attrs_define
class AuthTimeOpenApiVO:
    """Authentication timeout time. Display when enabled, otherwise no display.

    Attributes:
        auth_timeout (int): Validity period should be a value as follows: 0: Custom; 1: 30 Minutes; 2: 1 Hour; 3: 2
            Hours; 4: 4 Hours; 5: 8 Hours; 6: 1 Day; 7: 7 Days integer.
        custom_timeout (int | Unset): Custom timeout should be within the range of 1 ~ 1,000,000 minutes(when
            parameter[customTimeoutUnit] value is 1), or 1 ~ 10,000 hours(when parameter[customTimeoutUnit] value is 2), or
            1 ~ 1,000 days(when parameter[customTimeoutUnit] value is 3).
        custom_timeout_unit (int | Unset): Custom timeout unit should be a value as follows: 1: min; 2: hour; 3: day.
    """

    auth_timeout: int
    custom_timeout: int | Unset = UNSET
    custom_timeout_unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_timeout = self.auth_timeout

        custom_timeout = self.custom_timeout

        custom_timeout_unit = self.custom_timeout_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authTimeout": auth_timeout,
            }
        )
        if custom_timeout is not UNSET:
            field_dict["customTimeout"] = custom_timeout
        if custom_timeout_unit is not UNSET:
            field_dict["customTimeoutUnit"] = custom_timeout_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        auth_timeout = d.pop("authTimeout")

        custom_timeout = d.pop("customTimeout", UNSET)

        custom_timeout_unit = d.pop("customTimeoutUnit", UNSET)

        auth_time_open_api_vo = cls(
            auth_timeout=auth_timeout,
            custom_timeout=custom_timeout,
            custom_timeout_unit=custom_timeout_unit,
        )

        auth_time_open_api_vo.additional_properties = d
        return auth_time_open_api_vo

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
