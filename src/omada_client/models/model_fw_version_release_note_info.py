from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelFwVersionReleaseNoteInfo")


@_attrs_define
class ModelFwVersionReleaseNoteInfo:
    """Release Notes information for a firmware series

    Attributes:
        current_version (str | Unset): Current version number, such as "2.5.0 Build 20190118 Rel. 64821"
        release_note (str | Unset): Current version of releaseNote
        previous_version (str | Unset): Previous version number
        next_version (str | Unset): The version number of the subsequent version
    """

    current_version: str | Unset = UNSET
    release_note: str | Unset = UNSET
    previous_version: str | Unset = UNSET
    next_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_version = self.current_version

        release_note = self.release_note

        previous_version = self.previous_version

        next_version = self.next_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_version is not UNSET:
            field_dict["currentVersion"] = current_version
        if release_note is not UNSET:
            field_dict["releaseNote"] = release_note
        if previous_version is not UNSET:
            field_dict["previousVersion"] = previous_version
        if next_version is not UNSET:
            field_dict["nextVersion"] = next_version

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        current_version = d.pop("currentVersion", UNSET)

        release_note = d.pop("releaseNote", UNSET)

        previous_version = d.pop("previousVersion", UNSET)

        next_version = d.pop("nextVersion", UNSET)

        model_fw_version_release_note_info = cls(
            current_version=current_version,
            release_note=release_note,
            previous_version=previous_version,
            next_version=next_version,
        )

        model_fw_version_release_note_info.additional_properties = d
        return model_fw_version_release_note_info

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
