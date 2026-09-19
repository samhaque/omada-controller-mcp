from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetTagOpenApiVO")


@_attrs_define
class SetTagOpenApiVO:
    """
    Attributes:
        tag_ids (list[str]): Tag ID list
        macs (list[str] | Unset): Device MAC list, like AA-BB-CC-DD-EE-FF
    """

    tag_ids: list[str]
    macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tag_ids = self.tag_ids

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tagIds": tag_ids,
            }
        )
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tag_ids = cast(list[str], d.pop("tagIds"))

        macs = cast(list[str], d.pop("macs", UNSET))

        set_tag_open_api_vo = cls(
            tag_ids=tag_ids,
            macs=macs,
        )

        set_tag_open_api_vo.additional_properties = d
        return set_tag_open_api_vo

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
