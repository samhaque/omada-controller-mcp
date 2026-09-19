from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.model_fw_version_release_note_info import (
        ModelFwVersionReleaseNoteInfo,
    )


T = TypeVar("T", bound="ModelFwOemReleaseNoteInfo")


@_attrs_define
class ModelFwOemReleaseNoteInfo:
    """
    Attributes:
        release_notes (list[ModelFwVersionReleaseNoteInfo] | Unset): Release Notes information for a firmware series
    """

    release_notes: list[ModelFwVersionReleaseNoteInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        release_notes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.release_notes, Unset):
            release_notes = []
            for release_notes_item_data in self.release_notes:
                release_notes_item = release_notes_item_data.to_dict()
                release_notes.append(release_notes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if release_notes is not UNSET:
            field_dict["releaseNotes"] = release_notes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.model_fw_version_release_note_info import (
            ModelFwVersionReleaseNoteInfo,
        )

        d = dict(src_dict)
        _release_notes = d.pop("releaseNotes", UNSET)
        release_notes: list[ModelFwVersionReleaseNoteInfo] | Unset = UNSET
        if _release_notes is not UNSET:
            release_notes = []
            for release_notes_item_data in _release_notes:
                release_notes_item = ModelFwVersionReleaseNoteInfo.from_dict(
                    release_notes_item_data
                )

                release_notes.append(release_notes_item)

        model_fw_oem_release_note_info = cls(
            release_notes=release_notes,
        )

        model_fw_oem_release_note_info.additional_properties = d
        return model_fw_oem_release_note_info

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
