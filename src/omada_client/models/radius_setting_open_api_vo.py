from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RadiusSettingOpenApiVO")


@_attrs_define
class RadiusSettingOpenApiVO:
    """It is required when parameter [authType] is 1.

    Attributes:
        radius_profile (str): Radius profile ID. RADIUS profile can be created using 'Create a new RADIUS profile'
            interface, and RADIUS profile ID can be obtained from 'Get RADIUS profile list' interface.
        default_group (str): Default user group ID for the user on the radius server. User group can be created using
            'Create SSL VPN user group' interface, and user group ID can be obtained from 'Get user group list for SSL VPN
            server' interface.
        auth_type (int): Authtype should be a value as follows: 0：PAP; 1:CHAP
        repeat_time (int): Repeat time should be within the range of 1–10
        over_time (int): Request Timeout, 1~60(s).
        nas_ip (str | Unset): NAS IP
    """

    radius_profile: str
    default_group: str
    auth_type: int
    repeat_time: int
    over_time: int
    nas_ip: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radius_profile = self.radius_profile

        default_group = self.default_group

        auth_type = self.auth_type

        repeat_time = self.repeat_time

        over_time = self.over_time

        nas_ip = self.nas_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "radiusProfile": radius_profile,
                "defaultGroup": default_group,
                "authType": auth_type,
                "repeatTime": repeat_time,
                "overTime": over_time,
            }
        )
        if nas_ip is not UNSET:
            field_dict["nasIp"] = nas_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radius_profile = d.pop("radiusProfile")

        default_group = d.pop("defaultGroup")

        auth_type = d.pop("authType")

        repeat_time = d.pop("repeatTime")

        over_time = d.pop("overTime")

        nas_ip = d.pop("nasIp", UNSET)

        radius_setting_open_api_vo = cls(
            radius_profile=radius_profile,
            default_group=default_group,
            auth_type=auth_type,
            repeat_time=repeat_time,
            over_time=over_time,
            nas_ip=nas_ip,
        )

        radius_setting_open_api_vo.additional_properties = d
        return radius_setting_open_api_vo

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
