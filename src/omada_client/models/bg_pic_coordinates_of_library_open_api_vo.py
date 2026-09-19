from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BgPicCoordinatesOfLibraryOpenApiVO")


@_attrs_define
class BgPicCoordinatesOfLibraryOpenApiVO:
    """Library mobile background picture coordinates.

    Attributes:
        width (int | Unset): Width of background picture coordinates.
        height (int | Unset): Height of background picture coordinates.
        left (int | Unset): Left of background picture coordinates.
        top (int | Unset): Top of background picture coordinates.
    """

    width: int | Unset = UNSET
    height: int | Unset = UNSET
    left: int | Unset = UNSET
    top: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        width = self.width

        height = self.height

        left = self.left

        top = self.top

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if left is not UNSET:
            field_dict["left"] = left
        if top is not UNSET:
            field_dict["top"] = top

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        left = d.pop("left", UNSET)

        top = d.pop("top", UNSET)

        bg_pic_coordinates_of_library_open_api_vo = cls(
            width=width,
            height=height,
            left=left,
            top=top,
        )

        bg_pic_coordinates_of_library_open_api_vo.additional_properties = d
        return bg_pic_coordinates_of_library_open_api_vo

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
