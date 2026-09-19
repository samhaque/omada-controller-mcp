from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationStatVO")


@_attrs_define
class ApplicationStatVO:
    """
    Attributes:
        allow_apps (int | Unset):
        block_apps (int | Unset):
    """

    allow_apps: int | Unset = UNSET
    block_apps: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_apps = self.allow_apps

        block_apps = self.block_apps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allow_apps is not UNSET:
            field_dict["allowApps"] = allow_apps
        if block_apps is not UNSET:
            field_dict["blockApps"] = block_apps

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        allow_apps = d.pop("allowApps", UNSET)

        block_apps = d.pop("blockApps", UNSET)

        application_stat_vo = cls(
            allow_apps=allow_apps,
            block_apps=block_apps,
        )

        application_stat_vo.additional_properties = d
        return application_stat_vo

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
