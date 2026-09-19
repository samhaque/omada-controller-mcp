from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManuallyConfigOpenApiVO")


@_attrs_define
class ManuallyConfigOpenApiVO:
    """It is required when [configType] is 1.

    Attributes:
        dial_number (str):
        apn (str | Unset):
        username (str | Unset):
        password (str | Unset):
    """

    dial_number: str
    apn: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dial_number = self.dial_number

        apn = self.apn

        username = self.username

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dialNumber": dial_number,
            }
        )
        if apn is not UNSET:
            field_dict["apn"] = apn
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        dial_number = d.pop("dialNumber")

        apn = d.pop("apn", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        manually_config_open_api_vo = cls(
            dial_number=dial_number,
            apn=apn,
            username=username,
            password=password,
        )

        manually_config_open_api_vo.additional_properties = d
        return manually_config_open_api_vo

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
