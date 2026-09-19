from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RFScanCommand")


@_attrs_define
class RFScanCommand:
    """
    Attributes:
        radio_id_list (list[int] | Unset): Parameter [radioIdList] indicates the set of frequency bands for radio
            frequency scan. The value range of each element in the list should be between 0 and 3. 0: 2.4GHz, 1: 5GHz, 2:
            5GHz-2, 3: 6GHz. This parameter takes effect only when the device supports selecting bands for radio frequency
            scan; If the device does not support selecting bands, or if this parameter is not passed or is an empty list,
            the device will perform radio frequency scan for all its frequency bands.
    """

    radio_id_list: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        radio_id_list: list[int] | Unset = UNSET
        if not isinstance(self.radio_id_list, Unset):
            radio_id_list = self.radio_id_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if radio_id_list is not UNSET:
            field_dict["radioIdList"] = radio_id_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        radio_id_list = cast(list[int], d.pop("radioIdList", UNSET))

        rf_scan_command = cls(
            radio_id_list=radio_id_list,
        )

        rf_scan_command.additional_properties = d
        return rf_scan_command

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
