from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswVrfConfigOpenApiVO")


@_attrs_define
class OswVrfConfigOpenApiVO:
    """
    Attributes:
        ipv_6_enable (bool): Whether to enable ipv6
        vrf (str | Unset): VRF name: 1 to 15 characters consisting of numbers (0 to 9), uppercase and lowercase letters
            (A to Z, a to z), and symbols -_@.+; cannot be '.' or '..' only. This parameter is required when creating a VRF
            and is not needed when modifying a VRF.
        ipv_4_enable (bool | Unset): Whether to enable ipv4. Ipv4Enable should be true. This parameter is required when
            creating a VRF and is not needed when modifying a VRF.
    """

    ipv_6_enable: bool
    vrf: str | Unset = UNSET
    ipv_4_enable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ipv_6_enable = self.ipv_6_enable

        vrf = self.vrf

        ipv_4_enable = self.ipv_4_enable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ipv6Enable": ipv_6_enable,
            }
        )
        if vrf is not UNSET:
            field_dict["vrf"] = vrf
        if ipv_4_enable is not UNSET:
            field_dict["ipv4Enable"] = ipv_4_enable

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ipv_6_enable = d.pop("ipv6Enable")

        vrf = d.pop("vrf", UNSET)

        ipv_4_enable = d.pop("ipv4Enable", UNSET)

        osw_vrf_config_open_api_vo = cls(
            ipv_6_enable=ipv_6_enable,
            vrf=vrf,
            ipv_4_enable=ipv_4_enable,
        )

        osw_vrf_config_open_api_vo.additional_properties = d
        return osw_vrf_config_open_api_vo

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
