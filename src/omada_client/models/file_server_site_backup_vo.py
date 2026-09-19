from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.file_server_open_api_vo import FileServerOpenApiVO


T = TypeVar("T", bound="FileServerSiteBackupVO")


@_attrs_define
class FileServerSiteBackupVO:
    """
    Attributes:
        server_config (FileServerOpenApiVO): File server configuration.
        file_path (str): Saving path of directory for all backup config files, example: /backup. Parameter [filePath]
            should be 1 - 128 ASCII characters.
        site_ids (list[str]): Site ID list to backup, up to 300 entries are allowed for the site ID list.
    """

    server_config: FileServerOpenApiVO
    file_path: str
    site_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_config = self.server_config.to_dict()

        file_path = self.file_path

        site_ids = self.site_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverConfig": server_config,
                "filePath": file_path,
                "siteIds": site_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.file_server_open_api_vo import (
            FileServerOpenApiVO,
        )

        d = dict(src_dict)
        server_config = FileServerOpenApiVO.from_dict(d.pop("serverConfig"))

        file_path = d.pop("filePath")

        site_ids = cast(list[str], d.pop("siteIds"))

        file_server_site_backup_vo = cls(
            server_config=server_config,
            file_path=file_path,
            site_ids=site_ids,
        )

        file_server_site_backup_vo.additional_properties = d
        return file_server_site_backup_vo

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
