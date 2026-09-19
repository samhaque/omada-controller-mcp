from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BackupFileResultVO")


@_attrs_define
class BackupFileResultVO:
    """File list of backup files.

    Attributes:
        file_name (str | Unset): File name of backup file. Parameter [fileName] should be 1 - 128 ASCII characters.
        backup_time (int | Unset): Backup time(ms).
        size (int | Unset): Size of backup file(Byte).
    """

    file_name: str | Unset = UNSET
    backup_time: int | Unset = UNSET
    size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        backup_time = self.backup_time

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if backup_time is not UNSET:
            field_dict["backupTime"] = backup_time
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file_name = d.pop("fileName", UNSET)

        backup_time = d.pop("backupTime", UNSET)

        size = d.pop("size", UNSET)

        backup_file_result_vo = cls(
            file_name=file_name,
            backup_time=backup_time,
            size=size,
        )

        backup_file_result_vo.additional_properties = d
        return backup_file_result_vo

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
