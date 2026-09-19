from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RestrictionEntity")


@_attrs_define
class RestrictionEntity:
    """
    Attributes:
        network_name (str): Network name. It should be the name of LAN network, can be obtained from 'Get LAN network
            list' interface.
        filter_id (int): Filter ID can be obtained from 'Get filter list' interface.
        network_id (str | Unset): Network ID. It should be the ID of lan network. It can be queried by request: Get LAN
            network list.
    """

    network_name: str
    filter_id: int
    network_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        network_name = self.network_name

        filter_id = self.filter_id

        network_id = self.network_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "networkName": network_name,
                "filterId": filter_id,
            }
        )
        if network_id is not UNSET:
            field_dict["networkId"] = network_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        network_name = d.pop("networkName")

        filter_id = d.pop("filterId")

        network_id = d.pop("networkId", UNSET)

        restriction_entity = cls(
            network_name=network_name,
            filter_id=filter_id,
            network_id=network_id,
        )

        restriction_entity.additional_properties = d
        return restriction_entity

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
