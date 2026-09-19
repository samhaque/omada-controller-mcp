from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.last_scan_result_vo import LastScanResultVO


T = TypeVar("T", bound="ExperienceIndex")


@_attrs_define
class ExperienceIndex:
    """
    Attributes:
        last_scan (list[LastScanResultVO] | Unset): The results of the last scan.
    """

    last_scan: list[LastScanResultVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_scan: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.last_scan, Unset):
            last_scan = []
            for last_scan_item_data in self.last_scan:
                last_scan_item = last_scan_item_data.to_dict()
                last_scan.append(last_scan_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_scan is not UNSET:
            field_dict["lastScan"] = last_scan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.last_scan_result_vo import LastScanResultVO

        d = dict(src_dict)
        _last_scan = d.pop("lastScan", UNSET)
        last_scan: list[LastScanResultVO] | Unset = UNSET
        if _last_scan is not UNSET:
            last_scan = []
            for last_scan_item_data in _last_scan:
                last_scan_item = LastScanResultVO.from_dict(last_scan_item_data)

                last_scan.append(last_scan_item)

        experience_index = cls(
            last_scan=last_scan,
        )

        experience_index.additional_properties = d
        return experience_index

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
