from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MoveSiteIdOpenApiVO")


@_attrs_define
class MoveSiteIdOpenApiVO:
    """
    Attributes:
        move_site_id (str | Unset): For batch move site operations, use the "Get batch move site" interface to query the
            result of this operation.
    """

    move_site_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        move_site_id = self.move_site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if move_site_id is not UNSET:
            field_dict["moveSiteId"] = move_site_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        move_site_id = d.pop("moveSiteId", UNSET)

        move_site_id_open_api_vo = cls(
            move_site_id=move_site_id,
        )

        move_site_id_open_api_vo.additional_properties = d
        return move_site_id_open_api_vo

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
