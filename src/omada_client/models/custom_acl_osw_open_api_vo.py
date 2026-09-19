from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomAclOswOpenApiVO")


@_attrs_define
class CustomAclOswOpenApiVO:
    """Only for bindingType is custom switch vlan, list of selected device

    Attributes:
        mac (str): MAC
        vrf (str): VRF should be 1 to 15 characters consisting of numbers (0 to 9), uppercase and lowercase letters (A
            to Z, a to z), and symbols -_@.+ but cannot be . or .. only.
        stack_id (str | Unset): Stack ID
        vrf_id (str | Unset): VRF ID
    """

    mac: str
    vrf: str
    stack_id: str | Unset = UNSET
    vrf_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        vrf = self.vrf

        stack_id = self.stack_id

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "vrf": vrf,
            }
        )
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        vrf = d.pop("vrf")

        stack_id = d.pop("stackId", UNSET)

        vrf_id = d.pop("vrfId", UNSET)

        custom_acl_osw_open_api_vo = cls(
            mac=mac,
            vrf=vrf,
            stack_id=stack_id,
            vrf_id=vrf_id,
        )

        custom_acl_osw_open_api_vo.additional_properties = d
        return custom_acl_osw_open_api_vo

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
