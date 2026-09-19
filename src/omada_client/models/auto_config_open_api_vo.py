from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="AutoConfigOpenApiVO")


@_attrs_define
class AutoConfigOpenApiVO:
    """It is required when [configType] is 0.

    Attributes:
        location (int): Location index, which refers to "Get location and ISP info".
        mobile_isp (int): MobileISP index, which refers to "Get location and ISP info".
    """

    location: int
    mobile_isp: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location

        mobile_isp = self.mobile_isp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "mobileISP": mobile_isp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        location = d.pop("location")

        mobile_isp = d.pop("mobileISP")

        auto_config_open_api_vo = cls(
            location=location,
            mobile_isp=mobile_isp,
        )

        auto_config_open_api_vo.additional_properties = d
        return auto_config_open_api_vo

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
