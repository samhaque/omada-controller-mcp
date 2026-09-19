from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="IptvCustomOpenApiVO")


@_attrs_define
class IptvCustomOpenApiVO:
    """Required when parameter[mode] is 1

    Attributes:
        ip_phone_vlan_id (int): IP Phone VLAN ID should be within the range of 1–4094.
        ip_phone_vlan_priority (int): IP Phone VLAN priority should be within the range of 0–7.
        iptv_vlan_id (int): IPTV VLAN ID should be within the range of 1–4094.
        iptv_vlan_priority (int): IPTV VLAN priority should be within the range of 0–7.
    """

    ip_phone_vlan_id: int
    ip_phone_vlan_priority: int
    iptv_vlan_id: int
    iptv_vlan_priority: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ip_phone_vlan_id = self.ip_phone_vlan_id

        ip_phone_vlan_priority = self.ip_phone_vlan_priority

        iptv_vlan_id = self.iptv_vlan_id

        iptv_vlan_priority = self.iptv_vlan_priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipPhoneVlanId": ip_phone_vlan_id,
                "ipPhoneVlanPriority": ip_phone_vlan_priority,
                "iptvVlanId": iptv_vlan_id,
                "iptvVlanPriority": iptv_vlan_priority,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ip_phone_vlan_id = d.pop("ipPhoneVlanId")

        ip_phone_vlan_priority = d.pop("ipPhoneVlanPriority")

        iptv_vlan_id = d.pop("iptvVlanId")

        iptv_vlan_priority = d.pop("iptvVlanPriority")

        iptv_custom_open_api_vo = cls(
            ip_phone_vlan_id=ip_phone_vlan_id,
            ip_phone_vlan_priority=ip_phone_vlan_priority,
            iptv_vlan_id=iptv_vlan_id,
            iptv_vlan_priority=iptv_vlan_priority,
        )

        iptv_custom_open_api_vo.additional_properties = d
        return iptv_custom_open_api_vo

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
