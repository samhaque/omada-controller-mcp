from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="ConfigIotServerOpenApiVOFilters")


@_attrs_define
class ConfigIotServerOpenApiVOFilters:
    """The keys in the [filters] map represent the filter types, while the values correspond to the specific filtering
    criteria or values associated with each filter type.<br />Note:<br />Filter type = 0, The Company Identifier must
    conform to a 4-digit or 6-digit hexadecimal encoding. It is only applicable to ibeacon devices<br />Filter type = 1,
    The Vendor should not exceed 255 bytes in length.<br />Filter type = 2, The Local Name should not exceed 120 bytes
    in length. It is only applicable to minew devices.<br />Filter type = 3, The Service UUID must conform to a 4-digit
    hexadecimal encoding. It is only applicable to minew and eddystone devices.<br />Filter type = 4, The Mac Oui must
    conform to a 6-digit hexadecimal encoding.<br />Filter type = 5, The iBeacon UUID must conform to a 32-digit
    hexadecimal encoding. It is only applicable to iBeacon devices.<br />Filter type = 6, The UID must conform to a
    20-digit or 32-digit hexadecimal encoding. It is only applicable to eddystone devices.<br />Filter type = 7, The URL
    should not include a scheme. It is only applicable to eddystone devices.<br />

    """

    additional_properties: dict[str, list[str]] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        config_iot_server_open_api_vo_filters = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = cast(list[str], prop_dict)

            additional_properties[prop_name] = additional_property

        config_iot_server_open_api_vo_filters.additional_properties = (
            additional_properties
        )
        return config_iot_server_open_api_vo_filters

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> list[str]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: list[str]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
