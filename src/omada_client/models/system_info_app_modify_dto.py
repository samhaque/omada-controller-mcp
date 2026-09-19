from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemInfoAppModifyDTO")


@_attrs_define
class SystemInfoAppModifyDTO:
    """
    Attributes:
        device_name (str | Unset): Device name should contain 1-32 bits numbers, Upper and lower letters, -@_:/. .
        device_location (str | Unset): Device location should contain 1-32 bits numbers, Upper and lower letters, -@_:/.
            .
        contact_information (str | Unset): Contact information should contain 1-32 bits numbers, Upper and lower
            letters, -@_:/. .
    """

    device_name: str | Unset = UNSET
    device_location: str | Unset = UNSET
    contact_information: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_name = self.device_name

        device_location = self.device_location

        contact_information = self.contact_information

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if device_location is not UNSET:
            field_dict["deviceLocation"] = device_location
        if contact_information is not UNSET:
            field_dict["contactInformation"] = contact_information

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_name = d.pop("deviceName", UNSET)

        device_location = d.pop("deviceLocation", UNSET)

        contact_information = d.pop("contactInformation", UNSET)

        system_info_app_modify_dto = cls(
            device_name=device_name,
            device_location=device_location,
            contact_information=contact_information,
        )

        system_info_app_modify_dto.additional_properties = d
        return system_info_app_modify_dto

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
