from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlagLocateOpenApiVO")


@_attrs_define
class MlagLocateOpenApiVO:
    """
    Attributes:
        select_all (bool): Indicates whether to select the entire M-LAG group
        locate_enable (bool): Indicates whether locate is enabled
        macs (list[str] | Unset): Selected Devices Mac List. When selectAll is false, it cannot be empty.
    """

    select_all: bool
    locate_enable: bool
    macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_all = self.select_all

        locate_enable = self.locate_enable

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selectAll": select_all,
                "locateEnable": locate_enable,
            }
        )
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        select_all = d.pop("selectAll")

        locate_enable = d.pop("locateEnable")

        macs = cast(list[str], d.pop("macs", UNSET))

        mlag_locate_open_api_vo = cls(
            select_all=select_all,
            locate_enable=locate_enable,
            macs=macs,
        )

        mlag_locate_open_api_vo.additional_properties = d
        return mlag_locate_open_api_vo

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
