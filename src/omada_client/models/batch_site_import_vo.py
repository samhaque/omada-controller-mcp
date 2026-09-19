from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

if TYPE_CHECKING:
    from ..models.file_server_open_api_vo import FileServerOpenApiVO
    from ..models.site_import_open_api_vo import SiteImportOpenApiVO


T = TypeVar("T", bound="BatchSiteImportVO")


@_attrs_define
class BatchSiteImportVO:
    """
    Attributes:
        file_server_config (FileServerOpenApiVO): File server configuration.
        site_import_config_list (list[SiteImportOpenApiVO]): Site import config list. max size 300.
    """

    file_server_config: FileServerOpenApiVO
    site_import_config_list: list[SiteImportOpenApiVO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_server_config = self.file_server_config.to_dict()

        site_import_config_list = []
        for site_import_config_list_item_data in self.site_import_config_list:
            site_import_config_list_item = site_import_config_list_item_data.to_dict()
            site_import_config_list.append(site_import_config_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileServerConfig": file_server_config,
                "siteImportConfigList": site_import_config_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.file_server_open_api_vo import (
            FileServerOpenApiVO,
        )
        from ..models.site_import_open_api_vo import (
            SiteImportOpenApiVO,
        )

        d = dict(src_dict)
        file_server_config = FileServerOpenApiVO.from_dict(d.pop("fileServerConfig"))

        site_import_config_list = []
        _site_import_config_list = d.pop("siteImportConfigList")
        for site_import_config_list_item_data in _site_import_config_list:
            site_import_config_list_item = SiteImportOpenApiVO.from_dict(
                site_import_config_list_item_data
            )

            site_import_config_list.append(site_import_config_list_item)

        batch_site_import_vo = cls(
            file_server_config=file_server_config,
            site_import_config_list=site_import_config_list,
        )

        batch_site_import_vo.additional_properties = d
        return batch_site_import_vo

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
