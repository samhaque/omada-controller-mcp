from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_schedule_time_vo import BaseScheduleTimeVO
    from ..models.file_server_open_api_vo import FileServerOpenApiVO


T = TypeVar("T", bound="AutoBackupOpenApiVO")


@_attrs_define
class AutoBackupOpenApiVO:
    """
    Attributes:
        enable (bool): Whether enable backup schedule task
        occurrence (BaseScheduleTimeVO | Unset): Backup schedule time occurrence
        max_number_of_file (int | Unset): Max number of schedule backup files
        retention (int | Unset): Retention setting for data, values are as follows: -1 retention settings only, 0 backup
            all data, only for software controller, 7 retention backup data for 7 days, 30 retention backup data for 30
            days, 60 retention backup data for 60 days, 90 retention backup data for 90 days, 180 retention backup data for
            180 days, 365 retention backup data for 365 days
        saving_path (str | Unset): Saving path for backup schedule
        available_paths (list[str] | Unset): Available paths for backup schedule
        file_server_config (FileServerOpenApiVO | Unset): File server configuration.
        storage_type (int | Unset): Storage type, values are as follows: 0 for file server, 1 for cloud server(only for
            Cloud based controller), 2 for local disk, null for default path
        data_sheets (list[str] | Unset): Data to backup, values are as follows: knowClient, omadaLog, auditLog.
        retain_setting (bool | Unset): Whether retain setting when backup.
        retain_user (bool | Unset): Whether retain user when backup.
        retain_auth_record (bool | Unset): Whether retain auth record when backup.
        retain_firmware_log (bool | Unset): Whether retain firmware log when backup.
    """

    enable: bool
    occurrence: BaseScheduleTimeVO | Unset = UNSET
    max_number_of_file: int | Unset = UNSET
    retention: int | Unset = UNSET
    saving_path: str | Unset = UNSET
    available_paths: list[str] | Unset = UNSET
    file_server_config: FileServerOpenApiVO | Unset = UNSET
    storage_type: int | Unset = UNSET
    data_sheets: list[str] | Unset = UNSET
    retain_setting: bool | Unset = UNSET
    retain_user: bool | Unset = UNSET
    retain_auth_record: bool | Unset = UNSET
    retain_firmware_log: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        occurrence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occurrence, Unset):
            occurrence = self.occurrence.to_dict()

        max_number_of_file = self.max_number_of_file

        retention = self.retention

        saving_path = self.saving_path

        available_paths: list[str] | Unset = UNSET
        if not isinstance(self.available_paths, Unset):
            available_paths = self.available_paths

        file_server_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_server_config, Unset):
            file_server_config = self.file_server_config.to_dict()

        storage_type = self.storage_type

        data_sheets: list[str] | Unset = UNSET
        if not isinstance(self.data_sheets, Unset):
            data_sheets = self.data_sheets

        retain_setting = self.retain_setting

        retain_user = self.retain_user

        retain_auth_record = self.retain_auth_record

        retain_firmware_log = self.retain_firmware_log

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enable": enable,
            }
        )
        if occurrence is not UNSET:
            field_dict["occurrence"] = occurrence
        if max_number_of_file is not UNSET:
            field_dict["maxNumberOfFile"] = max_number_of_file
        if retention is not UNSET:
            field_dict["retention"] = retention
        if saving_path is not UNSET:
            field_dict["savingPath"] = saving_path
        if available_paths is not UNSET:
            field_dict["availablePaths"] = available_paths
        if file_server_config is not UNSET:
            field_dict["fileServerConfig"] = file_server_config
        if storage_type is not UNSET:
            field_dict["storageType"] = storage_type
        if data_sheets is not UNSET:
            field_dict["dataSheets"] = data_sheets
        if retain_setting is not UNSET:
            field_dict["retainSetting"] = retain_setting
        if retain_user is not UNSET:
            field_dict["retainUser"] = retain_user
        if retain_auth_record is not UNSET:
            field_dict["retainAuthRecord"] = retain_auth_record
        if retain_firmware_log is not UNSET:
            field_dict["retainFirmwareLog"] = retain_firmware_log

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.base_schedule_time_vo import BaseScheduleTimeVO
        from ..models.file_server_open_api_vo import (
            FileServerOpenApiVO,
        )

        d = dict(src_dict)
        enable = d.pop("enable")

        _occurrence = d.pop("occurrence", UNSET)
        occurrence: BaseScheduleTimeVO | Unset
        if isinstance(_occurrence, Unset):
            occurrence = UNSET
        else:
            occurrence = BaseScheduleTimeVO.from_dict(_occurrence)

        max_number_of_file = d.pop("maxNumberOfFile", UNSET)

        retention = d.pop("retention", UNSET)

        saving_path = d.pop("savingPath", UNSET)

        available_paths = cast(list[str], d.pop("availablePaths", UNSET))

        _file_server_config = d.pop("fileServerConfig", UNSET)
        file_server_config: FileServerOpenApiVO | Unset
        if isinstance(_file_server_config, Unset):
            file_server_config = UNSET
        else:
            file_server_config = FileServerOpenApiVO.from_dict(_file_server_config)

        storage_type = d.pop("storageType", UNSET)

        data_sheets = cast(list[str], d.pop("dataSheets", UNSET))

        retain_setting = d.pop("retainSetting", UNSET)

        retain_user = d.pop("retainUser", UNSET)

        retain_auth_record = d.pop("retainAuthRecord", UNSET)

        retain_firmware_log = d.pop("retainFirmwareLog", UNSET)

        auto_backup_open_api_vo = cls(
            enable=enable,
            occurrence=occurrence,
            max_number_of_file=max_number_of_file,
            retention=retention,
            saving_path=saving_path,
            available_paths=available_paths,
            file_server_config=file_server_config,
            storage_type=storage_type,
            data_sheets=data_sheets,
            retain_setting=retain_setting,
            retain_user=retain_user,
            retain_auth_record=retain_auth_record,
            retain_firmware_log=retain_firmware_log,
        )

        auto_backup_open_api_vo.additional_properties = d
        return auto_backup_open_api_vo

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
