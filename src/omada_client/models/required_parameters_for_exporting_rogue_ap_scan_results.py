from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequiredParametersForExportingRogueAPScanResults")


@_attrs_define
class RequiredParametersForExportingRogueAPScanResults:
    """
    Attributes:
        site_ids (list[str] | Unset): Parameter [siteIds] indicates site IDs that need to export rogue AP scan results.
        format_ (int | Unset): Parameter [format] indicates the type of the exported file. 0: CSV, 1: xlsx.
    """

    site_ids: list[str] | Unset = UNSET
    format_: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_ids: list[str] | Unset = UNSET
        if not isinstance(self.site_ids, Unset):
            site_ids = self.site_ids

        format_ = self.format_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_ids is not UNSET:
            field_dict["siteIds"] = site_ids
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        site_ids = cast(list[str], d.pop("siteIds", UNSET))

        format_ = d.pop("format", UNSET)

        required_parameters_for_exporting_rogue_ap_scan_results = cls(
            site_ids=site_ids,
            format_=format_,
        )

        required_parameters_for_exporting_rogue_ap_scan_results.additional_properties = d
        return required_parameters_for_exporting_rogue_ap_scan_results

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
