from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApInterference")


@_attrs_define
class ApInterference:
    """
    Attributes:
        interferences2g (list[ApInterference] | Unset): List of 2G interferences.
        interferences5g (list[ApInterference] | Unset): List of 5G interferences.
        interferences6g (list[ApInterference] | Unset): List of 6G interferences.
    """

    interferences2g: list[ApInterference] | Unset = UNSET
    interferences5g: list[ApInterference] | Unset = UNSET
    interferences6g: list[ApInterference] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interferences2g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interferences2g, Unset):
            interferences2g = []
            for interferences2g_item_data in self.interferences2g:
                interferences2g_item = interferences2g_item_data.to_dict()
                interferences2g.append(interferences2g_item)

        interferences5g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interferences5g, Unset):
            interferences5g = []
            for interferences5g_item_data in self.interferences5g:
                interferences5g_item = interferences5g_item_data.to_dict()
                interferences5g.append(interferences5g_item)

        interferences6g: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.interferences6g, Unset):
            interferences6g = []
            for interferences6g_item_data in self.interferences6g:
                interferences6g_item = interferences6g_item_data.to_dict()
                interferences6g.append(interferences6g_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if interferences2g is not UNSET:
            field_dict["interferences2g"] = interferences2g
        if interferences5g is not UNSET:
            field_dict["interferences5g"] = interferences5g
        if interferences6g is not UNSET:
            field_dict["interferences6g"] = interferences6g

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        _interferences2g = d.pop("interferences2g", UNSET)
        interferences2g: list[ApInterference] | Unset = UNSET
        if _interferences2g is not UNSET:
            interferences2g = []
            for interferences2g_item_data in _interferences2g:
                interferences2g_item = ApInterference.from_dict(
                    interferences2g_item_data
                )

                interferences2g.append(interferences2g_item)

        _interferences5g = d.pop("interferences5g", UNSET)
        interferences5g: list[ApInterference] | Unset = UNSET
        if _interferences5g is not UNSET:
            interferences5g = []
            for interferences5g_item_data in _interferences5g:
                interferences5g_item = ApInterference.from_dict(
                    interferences5g_item_data
                )

                interferences5g.append(interferences5g_item)

        _interferences6g = d.pop("interferences6g", UNSET)
        interferences6g: list[ApInterference] | Unset = UNSET
        if _interferences6g is not UNSET:
            interferences6g = []
            for interferences6g_item_data in _interferences6g:
                interferences6g_item = ApInterference.from_dict(
                    interferences6g_item_data
                )

                interferences6g.append(interferences6g_item)

        ap_interference = cls(
            interferences2g=interferences2g,
            interferences5g=interferences5g,
            interferences6g=interferences6g,
        )

        ap_interference.additional_properties = d
        return ap_interference

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
