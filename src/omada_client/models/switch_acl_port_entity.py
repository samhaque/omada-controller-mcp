from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SwitchACLPortEntity")


@_attrs_define
class SwitchACLPortEntity:
    """only for bindingType custom ports

    Attributes:
        mac (str): MAC
        custom_port_ids (list[int]): Custom port IDs
        custom_lag_ids (list[int]): Custom lag IDs
        vrf (str): VRF should be 1 to 15 characters consisting of numbers (0 to 9), uppercase and lowercase letters (A
            to Z, a to z), and symbols -_@.+ but cannot be . or .. only.
        stack_id (str | Unset): Stack ID
        standard_custom_port_ids (list[str] | Unset): Custom standard port IDs
        vrf_id (str | Unset): VRF ID
    """

    mac: str
    custom_port_ids: list[int]
    custom_lag_ids: list[int]
    vrf: str
    stack_id: str | Unset = UNSET
    standard_custom_port_ids: list[str] | Unset = UNSET
    vrf_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        custom_port_ids = self.custom_port_ids

        custom_lag_ids = self.custom_lag_ids

        vrf = self.vrf

        stack_id = self.stack_id

        standard_custom_port_ids: list[str] | Unset = UNSET
        if not isinstance(self.standard_custom_port_ids, Unset):
            standard_custom_port_ids = self.standard_custom_port_ids

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mac": mac,
                "customPortIds": custom_port_ids,
                "customLagIds": custom_lag_ids,
                "vrf": vrf,
            }
        )
        if stack_id is not UNSET:
            field_dict["stackId"] = stack_id
        if standard_custom_port_ids is not UNSET:
            field_dict["standardCustomPortIds"] = standard_custom_port_ids
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac")

        custom_port_ids = cast(list[int], d.pop("customPortIds"))

        custom_lag_ids = cast(list[int], d.pop("customLagIds"))

        vrf = d.pop("vrf")

        stack_id = d.pop("stackId", UNSET)

        standard_custom_port_ids = cast(
            list[str], d.pop("standardCustomPortIds", UNSET)
        )

        vrf_id = d.pop("vrfId", UNSET)

        switch_acl_port_entity = cls(
            mac=mac,
            custom_port_ids=custom_port_ids,
            custom_lag_ids=custom_lag_ids,
            vrf=vrf,
            stack_id=stack_id,
            standard_custom_port_ids=standard_custom_port_ids,
            vrf_id=vrf_id,
        )

        switch_acl_port_entity.additional_properties = d
        return switch_acl_port_entity

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
