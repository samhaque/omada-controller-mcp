from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAutoCheckResInfo")


@_attrs_define
class CreateAutoCheckResInfo:
    """
    Attributes:
        auto_check_id (str | Unset): AutoCheck ID
    """

    auto_check_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_check_id = self.auto_check_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_check_id is not UNSET:
            field_dict["autoCheckId"] = auto_check_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        auto_check_id = d.pop("autoCheckId", UNSET)

        create_auto_check_res_info = cls(
            auto_check_id=auto_check_id,
        )

        create_auto_check_res_info.additional_properties = d
        return create_auto_check_res_info

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
