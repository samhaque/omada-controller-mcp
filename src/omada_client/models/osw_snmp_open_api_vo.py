from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswSnmpOpenApiVO")


@_attrs_define
class OswSnmpOpenApiVO:
    """SNMP setting

    Attributes:
        location (str | Unset): Location, location should contain 0 to 128 ASCII characters, spaces are allowed, and
            leading and trailing spaces are not allowed.
        contact (str | Unset): Contact, contact should contain 0 to 128 ASCII characters, spaces are not allowed.
        type_ (int | Unset): SNMP config type, 0: Use Site Settings; 1: Custom.
    """

    location: str | Unset = UNSET
    contact: str | Unset = UNSET
    type_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        contact = self.contact

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location is not UNSET:
            field_dict["location"] = location
        if contact is not UNSET:
            field_dict["contact"] = contact
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        location = d.pop("location", UNSET)

        contact = d.pop("contact", UNSET)

        type_ = d.pop("type", UNSET)

        osw_snmp_open_api_vo = cls(
            location=location,
            contact=contact,
            type_=type_,
        )

        osw_snmp_open_api_vo.additional_properties = d
        return osw_snmp_open_api_vo

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
