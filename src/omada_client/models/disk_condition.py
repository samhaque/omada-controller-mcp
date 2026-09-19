from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiskCondition")


@_attrs_define
class DiskCondition:
    """Hardware Storage

    Attributes:
        name (str | Unset): Disk condition name
        total_storage (float | Unset): Total storage of disk
        used_storage (float | Unset): Used storage of disk
        oc_storage (bool | Unset): OC storage of disk
    """

    name: str | Unset = UNSET
    total_storage: float | Unset = UNSET
    used_storage: float | Unset = UNSET
    oc_storage: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        total_storage = self.total_storage

        used_storage = self.used_storage

        oc_storage = self.oc_storage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if total_storage is not UNSET:
            field_dict["totalStorage"] = total_storage
        if used_storage is not UNSET:
            field_dict["usedStorage"] = used_storage
        if oc_storage is not UNSET:
            field_dict["ocStorage"] = oc_storage

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        total_storage = d.pop("totalStorage", UNSET)

        used_storage = d.pop("usedStorage", UNSET)

        oc_storage = d.pop("ocStorage", UNSET)

        disk_condition = cls(
            name=name,
            total_storage=total_storage,
            used_storage=used_storage,
            oc_storage=oc_storage,
        )

        disk_condition.additional_properties = d
        return disk_condition

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
