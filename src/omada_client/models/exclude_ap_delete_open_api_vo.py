from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExcludeApDeleteOpenApiVO")


@_attrs_define
class ExcludeApDeleteOpenApiVO:
    """
    Attributes:
        select_type (str | Unset): The value of parameter [selectType] must be in [all, include, exclude].
        macs (list[str] | Unset): MAC list. When parameter [selectType] is 'all', it should be null.When parameter
            [selectType] is 'include', it means the MAC list that needs to be included.When parameter [selectType] is
            'exclude', it means the MAC list that needs to be excluded.
    """

    select_type: str | Unset = UNSET
    macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_type = self.select_type

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if select_type is not UNSET:
            field_dict["selectType"] = select_type
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        select_type = d.pop("selectType", UNSET)

        macs = cast(list[str], d.pop("macs", UNSET))

        exclude_ap_delete_open_api_vo = cls(
            select_type=select_type,
            macs=macs,
        )

        exclude_ap_delete_open_api_vo.additional_properties = d
        return exclude_ap_delete_open_api_vo

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
