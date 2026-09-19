from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

T = TypeVar("T", bound="SelfSiteRestoreVO")


@_attrs_define
class SelfSiteRestoreVO:
    """Site restore info list to restore. Up to 300 entries are allowed for the site restore info list.

    Attributes:
        file_name (str): Site backup file name. Parameter [fileName] should be 1 - 128 ASCII characters.
        site_id (str): Site ID to restore
    """

    file_name: str
    site_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        file_name = self.file_name

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fileName": file_name,
                "siteId": site_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        file_name = d.pop("fileName")

        site_id = d.pop("siteId")

        self_site_restore_vo = cls(
            file_name=file_name,
            site_id=site_id,
        )

        self_site_restore_vo.additional_properties = d
        return self_site_restore_vo

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
