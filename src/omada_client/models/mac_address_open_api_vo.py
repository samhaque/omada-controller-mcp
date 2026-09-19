from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MacAddressOpenApiVO")


@_attrs_define
class MacAddressOpenApiVO:
    """MAC address list. Valid when [type] is 2

    Attributes:
        rule_id (int | Unset): ID of MAC address info
        name (str | Unset): MAC address name
        mac_address (str | Unset): MAC address
    """

    rule_id: int | Unset = UNSET
    name: str | Unset = UNSET
    mac_address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        rule_id = self.rule_id

        name = self.name

        mac_address = self.mac_address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rule_id is not UNSET:
            field_dict["ruleId"] = rule_id
        if name is not UNSET:
            field_dict["name"] = name
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        rule_id = d.pop("ruleId", UNSET)

        name = d.pop("name", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        mac_address_open_api_vo = cls(
            rule_id=rule_id,
            name=name,
            mac_address=mac_address,
        )

        mac_address_open_api_vo.additional_properties = d
        return mac_address_open_api_vo

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
