from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlacedSite")


@_attrs_define
class PlacedSite:
    """
    Attributes:
        id (str | Unset): site id
        region (str | Unset): site region
        name (str | Unset): site name
        longitude (float | Unset): site longitude
        latitude (float | Unset): site latitude
        address (str | Unset): site address
    """

    id: str | Unset = UNSET
    region: str | Unset = UNSET
    name: str | Unset = UNSET
    longitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    address: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        region = self.region

        name = self.name

        longitude = self.longitude

        latitude = self.latitude

        address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if region is not UNSET:
            field_dict["region"] = region
        if name is not UNSET:
            field_dict["name"] = name
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        region = d.pop("region", UNSET)

        name = d.pop("name", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        address = d.pop("address", UNSET)

        placed_site = cls(
            id=id,
            region=region,
            name=name,
            longitude=longitude,
            latitude=latitude,
            address=address,
        )

        placed_site.additional_properties = d
        return placed_site

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
