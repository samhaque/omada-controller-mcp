from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsInfo")


@_attrs_define
class IpsInfo:
    """IPS config entity

    Attributes:
        enable (bool): Whether to enable IDS/IPS config. If parameter[enable] is true, parameter[ipsMode] and
            parameter[dplevel] are needed
        ips_mode (int | Unset): IpsMode should be a value as follows: 0: detect only; 1: detect and block Example: 1.
        geo_enable (bool | Unset): Whether to enable identifying the source country and destination country of attack ip
            addresses. Example: False.
        dp_level (int | Unset): DpLevel should be a value as follows: 0: Low; 1: Medium; 2: High; 3: Custom Example: 0.
        custom_categories (list[int] | Unset): Custom IDS/IPS categories list, if parameter[Dplevel] is 3,
            customCategories is needed.CustomCategories should be a list as follow: 1: Botcc, 2: Worm, 3: Malware, 4:
            Mobile_Malware, 6: P2P, 7: Tor, 8: Exploit, 9: Shellcode, 14: Activex, 15: DNS, 18: User Agents, 24: DShield
        time_range_id (str | Unset): This field represents Time Range ID. Time Range can be created using 'Create time
            range profile' interface, and Time Range ID can be obtained from 'Get time range profile list' interface. If
            parameter[timeRangeId] is null, IDS/IPS will be effective in all time ranges.
    """

    enable: bool
    ips_mode: int | Unset = UNSET
    geo_enable: bool | Unset = UNSET
    dp_level: int | Unset = UNSET
    custom_categories: list[int] | Unset = UNSET
    time_range_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        ips_mode = self.ips_mode

        geo_enable = self.geo_enable

        dp_level = self.dp_level

        custom_categories: list[int] | Unset = UNSET
        if not isinstance(self.custom_categories, Unset):
            custom_categories = self.custom_categories

        time_range_id = self.time_range_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if ips_mode is not UNSET:
            field_dict["ipsMode"] = ips_mode
        if geo_enable is not UNSET:
            field_dict["geoEnable"] = geo_enable
        if dp_level is not UNSET:
            field_dict["dpLevel"] = dp_level
        if custom_categories is not UNSET:
            field_dict["customCategories"] = custom_categories
        if time_range_id is not UNSET:
            field_dict["timeRangeId"] = time_range_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        enable = d.pop("enable")

        ips_mode = d.pop("ipsMode", UNSET)

        geo_enable = d.pop("geoEnable", UNSET)

        dp_level = d.pop("dpLevel", UNSET)

        custom_categories = cast(list[int], d.pop("customCategories", UNSET))

        time_range_id = d.pop("timeRangeId", UNSET)

        ips_info = cls(
            enable=enable,
            ips_mode=ips_mode,
            geo_enable=geo_enable,
            dp_level=dp_level,
            custom_categories=custom_categories,
            time_range_id=time_range_id,
        )

        ips_info.additional_properties = d
        return ips_info

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
