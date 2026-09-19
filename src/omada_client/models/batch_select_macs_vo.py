from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchSelectMacsVO")


@_attrs_define
class BatchSelectMacsVO:
    """Selected Macs

    Attributes:
        select_type (str): SelectType all, include or exclude
        macs (list[str] | Unset): When selectType is set to all, the macs do not need to be passed and all entries are
            processed, when selectType is set to include, the mac entries contained in the macs are processed, when
            selectType is set to exclude, the mac entries that are not contained in the macs are processed
    """

    select_type: str
    macs: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        select_type = self.select_type

        macs: list[str] | Unset = UNSET
        if not isinstance(self.macs, Unset):
            macs = self.macs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "selectType": select_type,
            }
        )
        if macs is not UNSET:
            field_dict["macs"] = macs

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        select_type = d.pop("selectType")

        macs = cast(list[str], d.pop("macs", UNSET))

        batch_select_macs_vo = cls(
            select_type=select_type,
            macs=macs,
        )

        batch_select_macs_vo.additional_properties = d
        return batch_select_macs_vo

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
