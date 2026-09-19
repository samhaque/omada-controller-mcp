from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessItem")


@_attrs_define
class AccessItem:
    """
    Attributes:
        phone (str): Allowed phone numbers.
        country_code (str | Unset): Country code should contain 2 characters. Country code must be entered when entering
            the calling code. For the values of Country code, refer to section 5.4.1 of the Open API Access Guide.
        calling_code (str | Unset): Calling code should contain 2 to 5 characters. Calling code must be entered when
            entering the country code. For the values of Calling code, refer to section 5.4.1 of the Open API Access Guide.
    """

    phone: str
    country_code: str | Unset = UNSET
    calling_code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        country_code = self.country_code

        calling_code = self.calling_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "phone": phone,
            }
        )
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if calling_code is not UNSET:
            field_dict["callingCode"] = calling_code

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        phone = d.pop("phone")

        country_code = d.pop("countryCode", UNSET)

        calling_code = d.pop("callingCode", UNSET)

        access_item = cls(
            phone=phone,
            country_code=country_code,
            calling_code=calling_code,
        )

        access_item.additional_properties = d
        return access_item

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
