from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GeoOpenApiVO")


@_attrs_define
class GeoOpenApiVO:
    """Geo List.

    Attributes:
        country (str | Unset): Country code.
        attempts (int | Unset): Attempts.
        source (str | Unset): Source Ip, shown as Multiple when there are more than one ip.
    """

    country: str | Unset = UNSET
    attempts: int | Unset = UNSET
    source: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        country = self.country

        attempts = self.attempts

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if country is not UNSET:
            field_dict["country"] = country
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        country = d.pop("country", UNSET)

        attempts = d.pop("attempts", UNSET)

        source = d.pop("source", UNSET)

        geo_open_api_vo = cls(
            country=country,
            attempts=attempts,
            source=source,
        )

        geo_open_api_vo.additional_properties = d
        return geo_open_api_vo

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
