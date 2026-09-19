from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="DeviceBindBriefOpenApiVO")


@_attrs_define
class DeviceBindBriefOpenApiVO:
    """
    Attributes:
        mac (str): The mac address of device, like AA-BB-CC-DD-EE-FF.
        site_id (str): The ID of target site.
    """

    mac: str
    site_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "siteId": site_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        site_id = d.pop("siteId")

        device_bind_brief_open_api_vo = cls(
            mac=mac,
            site_id=site_id,
        )

        device_bind_brief_open_api_vo.additional_properties = d
        return device_bind_brief_open_api_vo

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
