from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivePairMultiSiteOpenApiDTO")


@_attrs_define
class ActivePairMultiSiteOpenApiDTO:
    """
    Attributes:
        device_mac (str): Device MAC address, like AA-BB-CC-DD-EE-FF
        license_type (str): License type should be a value as follows: Cloud Based Controller(1year, 2years, 3years,
            4years, 5years, others, trial); Local Controller(trial, permanent);
        site_id (str | Unset): Site ID
        license_id (str | Unset): License ID
    """

    device_mac: str
    license_type: str
    site_id: str | Unset = UNSET
    license_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        license_type = self.license_type

        site_id = self.site_id

        license_id = self.license_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceMac": device_mac,
                "licenseType": license_type,
            }
        )
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if license_id is not UNSET:
            field_dict["licenseId"] = license_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac = d.pop("deviceMac")

        license_type = d.pop("licenseType")

        site_id = d.pop("siteId", UNSET)

        license_id = d.pop("licenseId", UNSET)

        active_pair_multi_site_open_api_dto = cls(
            device_mac=device_mac,
            license_type=license_type,
            site_id=site_id,
            license_id=license_id,
        )

        active_pair_multi_site_open_api_dto.additional_properties = d
        return active_pair_multi_site_open_api_dto

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
