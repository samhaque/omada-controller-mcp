from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteImportOpenApiVO")


@_attrs_define
class SiteImportOpenApiVO:
    """Site import config list. max size 300.

    Attributes:
        file_path (str): File path of site backup config file.
        site_name (str): Target site name. It should contain 1 to 64 characters.
        skip_device (bool | Unset): Whether skip device info(if true: skip import device; if false: import device in
            config file; default for false
    """

    file_path: str
    site_name: str
    skip_device: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_path = self.file_path

        site_name = self.site_name

        skip_device = self.skip_device

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filePath": file_path,
                "siteName": site_name,
            }
        )
        if skip_device is not UNSET:
            field_dict["skipDevice"] = skip_device

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file_path = d.pop("filePath")

        site_name = d.pop("siteName")

        skip_device = d.pop("skipDevice", UNSET)

        site_import_open_api_vo = cls(
            file_path=file_path,
            site_name=site_name,
            skip_device=skip_device,
        )

        site_import_open_api_vo.additional_properties = d
        return site_import_open_api_vo

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
