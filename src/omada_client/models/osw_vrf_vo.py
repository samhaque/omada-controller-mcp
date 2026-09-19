from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswVrfVO")


@_attrs_define
class OswVrfVO:
    """
    Attributes:
        vrf (str): VRF name, it should be 1 to 15 characters consisting of numbers (0 to 9), uppercase and lowercase
            letters (A to Z, a to z), and symbols -_@.+ but cannot be . or .. only.
        ipv_4_enable (bool): Whether to enable ipv4. Ipv4Enable should be true
        ipv_6_enable (bool): Whether to enable ipv6
        id (str | Unset): VRF ID. This parameter is not required for creation or modification.
    """

    vrf: str
    ipv_4_enable: bool
    ipv_6_enable: bool
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vrf = self.vrf

        ipv_4_enable = self.ipv_4_enable

        ipv_6_enable = self.ipv_6_enable

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vrf": vrf,
                "ipv4Enable": ipv_4_enable,
                "ipv6Enable": ipv_6_enable,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        vrf = d.pop("vrf")

        ipv_4_enable = d.pop("ipv4Enable")

        ipv_6_enable = d.pop("ipv6Enable")

        id = d.pop("id", UNSET)

        osw_vrf_vo = cls(
            vrf=vrf,
            ipv_4_enable=ipv_4_enable,
            ipv_6_enable=ipv_6_enable,
            id=id,
        )

        osw_vrf_vo.additional_properties = d
        return osw_vrf_vo

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
