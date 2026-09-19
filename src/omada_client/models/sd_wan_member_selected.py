from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SdWanMemberSelected")


@_attrs_define
class SdWanMemberSelected:
    """A list of members of the SD-WAN group

    Attributes:
        device_mac (str): The device MAC of the sdWan member.
        site_id (str): The ID of the site where the sdWan member is located.
    """

    device_mac: str
    site_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        device_mac = self.device_mac

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deviceMac": device_mac,
                "siteId": site_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        device_mac = d.pop("deviceMac")

        site_id = d.pop("siteId")

        sd_wan_member_selected = cls(
            device_mac=device_mac,
            site_id=site_id,
        )

        sd_wan_member_selected.additional_properties = d
        return sd_wan_member_selected

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
