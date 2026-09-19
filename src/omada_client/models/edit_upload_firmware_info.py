from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="EditUploadFirmwareInfo")


@_attrs_define
class EditUploadFirmwareInfo:
    """
    Attributes:
        description (str | Unset): Description of firmware
        target_enable (bool | Unset): Do the sites set up specified firmware, it should be a value as follows: true,
            false
        target_sites (list[str] | Unset): Target sites ID, it exists when "targetEnable" is true
    """

    description: str | Unset = UNSET
    target_enable: bool | Unset = UNSET
    target_sites: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        target_enable = self.target_enable

        target_sites: list[str] | Unset = UNSET
        if not isinstance(self.target_sites, Unset):
            target_sites = self.target_sites

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if target_enable is not UNSET:
            field_dict["targetEnable"] = target_enable
        if target_sites is not UNSET:
            field_dict["targetSites"] = target_sites

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        target_enable = d.pop("targetEnable", UNSET)

        target_sites = cast(list[str], d.pop("targetSites", UNSET))

        edit_upload_firmware_info = cls(
            description=description,
            target_enable=target_enable,
            target_sites=target_sites,
        )

        edit_upload_firmware_info.additional_properties = d
        return edit_upload_firmware_info

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
