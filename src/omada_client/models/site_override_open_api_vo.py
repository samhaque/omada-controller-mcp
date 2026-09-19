from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteOverrideOpenApiVO")


@_attrs_define
class SiteOverrideOpenApiVO:
    """sites with override module

    Attributes:
        site_id (str | Unset): site id
        overrides (list[str] | Unset): override module
    """

    site_id: str | Unset = UNSET
    overrides: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_id = self.site_id

        overrides: list[str] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_id = d.pop("siteId", UNSET)

        overrides = cast(list[str], d.pop("overrides", UNSET))

        site_override_open_api_vo = cls(
            site_id=site_id,
            overrides=overrides,
        )

        site_override_open_api_vo.additional_properties = d
        return site_override_open_api_vo

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
