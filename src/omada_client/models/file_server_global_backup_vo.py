from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_server_open_api_vo import FileServerOpenApiVO


T = TypeVar("T", bound="FileServerGlobalBackupVO")


@_attrs_define
class FileServerGlobalBackupVO:
    """
    Attributes:
        server_config (FileServerOpenApiVO): File server configuration.
        file_path (str): Saving directory path for backup file. Parameter [filePath] should be 1 - 128 ASCII characters.
        retain_user (bool | Unset): Whether need retain user info.
        retain_auth_record (bool | Unset): Whether need retain auth record.
        retain_firmware_log (bool | Unset): Whether need retain firmware log.
        retention (int | Unset): Backup data retention, values are as follows: 0 :no limit others:7，30，60，90，180，365.
    """

    server_config: FileServerOpenApiVO
    file_path: str
    retain_user: bool | Unset = UNSET
    retain_auth_record: bool | Unset = UNSET
    retain_firmware_log: bool | Unset = UNSET
    retention: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_config = self.server_config.to_dict()

        file_path = self.file_path

        retain_user = self.retain_user

        retain_auth_record = self.retain_auth_record

        retain_firmware_log = self.retain_firmware_log

        retention = self.retention

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverConfig": server_config,
                "filePath": file_path,
            }
        )
        if retain_user is not UNSET:
            field_dict["retainUser"] = retain_user
        if retain_auth_record is not UNSET:
            field_dict["retainAuthRecord"] = retain_auth_record
        if retain_firmware_log is not UNSET:
            field_dict["retainFirmwareLog"] = retain_firmware_log
        if retention is not UNSET:
            field_dict["retention"] = retention

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.file_server_open_api_vo import (
            FileServerOpenApiVO,
        )

        d = dict(src_dict)
        server_config = FileServerOpenApiVO.from_dict(d.pop("serverConfig"))

        file_path = d.pop("filePath")

        retain_user = d.pop("retainUser", UNSET)

        retain_auth_record = d.pop("retainAuthRecord", UNSET)

        retain_firmware_log = d.pop("retainFirmwareLog", UNSET)

        retention = d.pop("retention", UNSET)

        file_server_global_backup_vo = cls(
            server_config=server_config,
            file_path=file_path,
            retain_user=retain_user,
            retain_auth_record=retain_auth_record,
            retain_firmware_log=retain_firmware_log,
            retention=retention,
        )

        file_server_global_backup_vo.additional_properties = d
        return file_server_global_backup_vo

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
