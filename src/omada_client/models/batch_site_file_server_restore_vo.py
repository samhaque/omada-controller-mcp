from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.file_server_open_api_vo import FileServerOpenApiVO
    from ..models.file_server_site_restore_vo import FileServerSiteRestoreVO


T = TypeVar("T", bound="BatchSiteFileServerRestoreVO")


@_attrs_define
class BatchSiteFileServerRestoreVO:
    """
    Attributes:
        server_config (FileServerOpenApiVO): File server configuration.
        site_infos (list[FileServerSiteRestoreVO]): Sites to restore.
    """

    server_config: FileServerOpenApiVO
    site_infos: list[FileServerSiteRestoreVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        server_config = self.server_config.to_dict()

        site_infos = []
        for site_infos_item_data in self.site_infos:
            site_infos_item = site_infos_item_data.to_dict()
            site_infos.append(site_infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serverConfig": server_config,
                "siteInfos": site_infos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.file_server_open_api_vo import (
            FileServerOpenApiVO,
        )
        from ..models.file_server_site_restore_vo import (
            FileServerSiteRestoreVO,
        )

        d = dict(src_dict)
        server_config = FileServerOpenApiVO.from_dict(d.pop("serverConfig"))

        site_infos = []
        _site_infos = d.pop("siteInfos")
        for site_infos_item_data in _site_infos:
            site_infos_item = FileServerSiteRestoreVO.from_dict(site_infos_item_data)

            site_infos.append(site_infos_item)

        batch_site_file_server_restore_vo = cls(
            server_config=server_config,
            site_infos=site_infos,
        )

        batch_site_file_server_restore_vo.additional_properties = d
        return batch_site_file_server_restore_vo

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
