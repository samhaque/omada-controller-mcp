from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_group_detail_vo import ApGroupDetailVO


T = TypeVar("T", bound="ApGroupDetailOpenApiVO")


@_attrs_define
class ApGroupDetailOpenApiVO:
    """
    Attributes:
        ap_groups (list[ApGroupDetailVO] | Unset):
        max_ssids_2g (int | Unset): 2G radio max Ssid number in group
        max_ssids_5g (int | Unset): 5G radio max Ssid number in group
        max_ssids_6g (int | Unset): 6G radio max Ssid number in group
        max_ssids_mlo (int | Unset): max Mlo Ssid number in group
    """

    ap_groups: list[ApGroupDetailVO] | Unset = UNSET
    max_ssids_2g: int | Unset = UNSET
    max_ssids_5g: int | Unset = UNSET
    max_ssids_6g: int | Unset = UNSET
    max_ssids_mlo: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ap_groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ap_groups, Unset):
            ap_groups = []
            for ap_groups_item_data in self.ap_groups:
                ap_groups_item = ap_groups_item_data.to_dict()
                ap_groups.append(ap_groups_item)

        max_ssids_2g = self.max_ssids_2g

        max_ssids_5g = self.max_ssids_5g

        max_ssids_6g = self.max_ssids_6g

        max_ssids_mlo = self.max_ssids_mlo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ap_groups is not UNSET:
            field_dict["apGroups"] = ap_groups
        if max_ssids_2g is not UNSET:
            field_dict["maxSsids2G"] = max_ssids_2g
        if max_ssids_5g is not UNSET:
            field_dict["maxSsids5G"] = max_ssids_5g
        if max_ssids_6g is not UNSET:
            field_dict["maxSsids6G"] = max_ssids_6g
        if max_ssids_mlo is not UNSET:
            field_dict["maxSsidsMlo"] = max_ssids_mlo

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_group_detail_vo import ApGroupDetailVO

        d = dict(src_dict)
        _ap_groups = d.pop("apGroups", UNSET)
        ap_groups: list[ApGroupDetailVO] | Unset = UNSET
        if _ap_groups is not UNSET:
            ap_groups = []
            for ap_groups_item_data in _ap_groups:
                ap_groups_item = ApGroupDetailVO.from_dict(ap_groups_item_data)

                ap_groups.append(ap_groups_item)

        max_ssids_2g = d.pop("maxSsids2G", UNSET)

        max_ssids_5g = d.pop("maxSsids5G", UNSET)

        max_ssids_6g = d.pop("maxSsids6G", UNSET)

        max_ssids_mlo = d.pop("maxSsidsMlo", UNSET)

        ap_group_detail_open_api_vo = cls(
            ap_groups=ap_groups,
            max_ssids_2g=max_ssids_2g,
            max_ssids_5g=max_ssids_5g,
            max_ssids_6g=max_ssids_6g,
            max_ssids_mlo=max_ssids_mlo,
        )

        ap_group_detail_open_api_vo.additional_properties = d
        return ap_group_detail_open_api_vo

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
