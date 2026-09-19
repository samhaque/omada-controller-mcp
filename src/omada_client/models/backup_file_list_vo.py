from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.backup_file_result_vo import BackupFileResultVO


T = TypeVar("T", bound="BackupFileListVO")


@_attrs_define
class BackupFileListVO:
    """
    Attributes:
        file_list (list[BackupFileResultVO] | Unset): File list of backup files.
    """

    file_list: list[BackupFileResultVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_list, Unset):
            file_list = []
            for file_list_item_data in self.file_list:
                file_list_item = file_list_item_data.to_dict()
                file_list.append(file_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if file_list is not UNSET:
            field_dict["fileList"] = file_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.backup_file_result_vo import BackupFileResultVO

        d = dict(src_dict)
        _file_list = d.pop("fileList", UNSET)
        file_list: list[BackupFileResultVO] | Unset = UNSET
        if _file_list is not UNSET:
            file_list = []
            for file_list_item_data in _file_list:
                file_list_item = BackupFileResultVO.from_dict(file_list_item_data)

                file_list.append(file_list_item)

        backup_file_list_vo = cls(
            file_list=file_list,
        )

        backup_file_list_vo.additional_properties = d
        return backup_file_list_vo

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
