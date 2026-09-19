from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osg_mac_filter_address_open_api_vo import OsgMacFilterAddressOpenApiVO


T = TypeVar("T", bound="MacFiltering")


@_attrs_define
class MacFiltering:
    """
    Attributes:
        name (str): Name of the MAC filtering entity.
        filter_mode (int): Filter mode should be a value as follows: 0: allow; 1: deny.
        type_ (int): Type should be a value as follows: 0: macAddresses; 1: macGroupIds.
        id (str | Unset): ID of the MAC filtering entity.
        mac_addresses (list[OsgMacFilterAddressOpenApiVO] | Unset): MAC addresses of the MAC filtering entity.
        mac_group_ids (list[str] | Unset): MAC groups of the MAC filtering entity. MAC group can be created using
            'Create a new group profile' interface, and MAC group ID can be obtained from 'Get group profile list'
            interface.
    """

    name: str
    filter_mode: int
    type_: int
    id: str | Unset = UNSET
    mac_addresses: list[OsgMacFilterAddressOpenApiVO] | Unset = UNSET
    mac_group_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        filter_mode = self.filter_mode

        type_ = self.type_

        id = self.id

        mac_addresses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mac_addresses, Unset):
            mac_addresses = []
            for mac_addresses_item_data in self.mac_addresses:
                mac_addresses_item = mac_addresses_item_data.to_dict()
                mac_addresses.append(mac_addresses_item)

        mac_group_ids: list[str] | Unset = UNSET
        if not isinstance(self.mac_group_ids, Unset):
            mac_group_ids = self.mac_group_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "filterMode": filter_mode,
                "type": type_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if mac_addresses is not UNSET:
            field_dict["macAddresses"] = mac_addresses
        if mac_group_ids is not UNSET:
            field_dict["macGroupIds"] = mac_group_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osg_mac_filter_address_open_api_vo import (
            OsgMacFilterAddressOpenApiVO,
        )

        d = dict(src_dict)
        name = d.pop("name")

        filter_mode = d.pop("filterMode")

        type_ = d.pop("type")

        id = d.pop("id", UNSET)

        _mac_addresses = d.pop("macAddresses", UNSET)
        mac_addresses: list[OsgMacFilterAddressOpenApiVO] | Unset = UNSET
        if _mac_addresses is not UNSET:
            mac_addresses = []
            for mac_addresses_item_data in _mac_addresses:
                mac_addresses_item = OsgMacFilterAddressOpenApiVO.from_dict(
                    mac_addresses_item_data
                )

                mac_addresses.append(mac_addresses_item)

        mac_group_ids = cast(list[str], d.pop("macGroupIds", UNSET))

        mac_filtering = cls(
            name=name,
            filter_mode=filter_mode,
            type_=type_,
            id=id,
            mac_addresses=mac_addresses,
            mac_group_ids=mac_group_ids,
        )

        mac_filtering.additional_properties = d
        return mac_filtering

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
