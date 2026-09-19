from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OsgMacFilterAddressOpenApiVO")


@_attrs_define
class OsgMacFilterAddressOpenApiVO:
    """MAC addresses of the MAC filtering entity.

    Attributes:
        mac_address (str): MAC address of the MAC filtering address.
        name (str | Unset): Name of the MAC filtering address.
    """

    mac_address: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac_address = self.mac_address

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "macAddress": mac_address,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac_address = d.pop("macAddress")

        name = d.pop("name", UNSET)

        osg_mac_filter_address_open_api_vo = cls(
            mac_address=mac_address,
            name=name,
        )

        osg_mac_filter_address_open_api_vo.additional_properties = d
        return osg_mac_filter_address_open_api_vo

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
