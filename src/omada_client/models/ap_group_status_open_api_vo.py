from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApGroupStatusOpenApiVO")


@_attrs_define
class ApGroupStatusOpenApiVO:
    """
    Attributes:
        exceeded (bool | Unset): whether the number of AP Groups exceeds the limit
        ap_group_num (int | Unset): the number of AP Groups
    """

    exceeded: bool | Unset = UNSET
    ap_group_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exceeded = self.exceeded

        ap_group_num = self.ap_group_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exceeded is not UNSET:
            field_dict["exceeded"] = exceeded
        if ap_group_num is not UNSET:
            field_dict["apGroupNum"] = ap_group_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        exceeded = d.pop("exceeded", UNSET)

        ap_group_num = d.pop("apGroupNum", UNSET)

        ap_group_status_open_api_vo = cls(
            exceeded=exceeded,
            ap_group_num=ap_group_num,
        )

        ap_group_status_open_api_vo.additional_properties = d
        return ap_group_status_open_api_vo

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
