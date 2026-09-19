from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IpsBlockListEntry")


@_attrs_define
class IpsBlockListEntry:
    """
    Attributes:
        id (str | Unset): Block list entry ID.
        name (str | Unset): The name of the defined blocked or isolated policy.
        source_ip (str | Unset): Source IP in defined blocked or isolated policy.
        destination (str | Unset): The destination IP in defined blocked or isolated policy.
        source_location (str | Unset): The region code of the source IP.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    source_ip: str | Unset = UNSET
    destination: str | Unset = UNSET
    source_location: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        source_ip = self.source_ip

        destination = self.destination

        source_location = self.source_location

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if source_ip is not UNSET:
            field_dict["sourceIp"] = source_ip
        if destination is not UNSET:
            field_dict["destination"] = destination
        if source_location is not UNSET:
            field_dict["sourceLocation"] = source_location

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        source_ip = d.pop("sourceIp", UNSET)

        destination = d.pop("destination", UNSET)

        source_location = d.pop("sourceLocation", UNSET)

        ips_block_list_entry = cls(
            id=id,
            name=name,
            source_ip=source_ip,
            destination=destination,
            source_location=source_location,
        )

        ips_block_list_entry.additional_properties = d
        return ips_block_list_entry

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
