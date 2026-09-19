from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthTimeoutSetting")


@_attrs_define
class AuthTimeoutSetting:
    """Auth Timeout Setting.

    Attributes:
        custom_timeout (int | Unset): Custom timeout should be within the range of 1 - 1,000,000 min or 1 - 10,000 hour
            or 1 - 1,000 day.
        custom_timeout_unit (int | Unset): Timeout unit, should be a value as follows: 1: min; 2: hour; 3: day.
    """

    custom_timeout: int | Unset = UNSET
    custom_timeout_unit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom_timeout = self.custom_timeout

        custom_timeout_unit = self.custom_timeout_unit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom_timeout is not UNSET:
            field_dict["customTimeout"] = custom_timeout
        if custom_timeout_unit is not UNSET:
            field_dict["customTimeoutUnit"] = custom_timeout_unit

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        custom_timeout = d.pop("customTimeout", UNSET)

        custom_timeout_unit = d.pop("customTimeoutUnit", UNSET)

        auth_timeout_setting = cls(
            custom_timeout=custom_timeout,
            custom_timeout_unit=custom_timeout_unit,
        )

        auth_timeout_setting.additional_properties = d
        return auth_timeout_setting

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
