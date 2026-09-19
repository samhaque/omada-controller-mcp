from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnbindDeviceRespVO")


@_attrs_define
class UnbindDeviceRespVO:
    """
    Attributes:
        mac (str | Unset):
        status (int | Unset): Unbind device status should be a value as follows: 0: success;-1: failed
        license_id (str | Unset): License ID
        license_type (str | Unset): License type should be a value as follows: 1year; 2years; 3years; 4years; 5years;
            others; trial(Cloud Based Controller), permanent; trial(Local Controller)
        category (str | Unset): Category should be a value as follows: ap; l2Switch; l3Switch; gateway
    """

    mac: str | Unset = UNSET
    status: int | Unset = UNSET
    license_id: str | Unset = UNSET
    license_type: str | Unset = UNSET
    category: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        status = self.status

        license_id = self.license_id

        license_type = self.license_type

        category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if status is not UNSET:
            field_dict["status"] = status
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id
        if license_type is not UNSET:
            field_dict["licenseType"] = license_type
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        status = d.pop("status", UNSET)

        license_id = d.pop("licenseId", UNSET)

        license_type = d.pop("licenseType", UNSET)

        category = d.pop("category", UNSET)

        unbind_device_resp_vo = cls(
            mac=mac,
            status=status,
            license_id=license_id,
            license_type=license_type,
            category=category,
        )

        unbind_device_resp_vo.additional_properties = d
        return unbind_device_resp_vo

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
