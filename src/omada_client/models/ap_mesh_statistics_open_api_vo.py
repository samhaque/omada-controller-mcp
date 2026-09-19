from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_wireless_uplink import ApWirelessUplink
    from ..models.candidate_parent_open_api_vo import CandidateParentOpenApiVO
    from ..models.child_ap_open_api_vo import ChildApOpenApiVO


T = TypeVar("T", bound="ApMeshStatisticsOpenApiVO")


@_attrs_define
class ApMeshStatisticsOpenApiVO:
    """
    Attributes:
        status (int | Unset): ap status
        status_category (int | Unset): ap status category
        wireless_linked (bool | Unset): whether ap is wireless linked
        scan_status (int | Unset): 0-init; 1-scanning; 2-scan success; 3-fail
        child_aps (list[ChildApOpenApiVO] | Unset): List of child aps
        wireless_uplink (ApWirelessUplink | Unset): Wireless uplink info
        candidate_parents (list[CandidateParentOpenApiVO] | Unset): candidate parent aps info
    """

    status: int | Unset = UNSET
    status_category: int | Unset = UNSET
    wireless_linked: bool | Unset = UNSET
    scan_status: int | Unset = UNSET
    child_aps: list[ChildApOpenApiVO] | Unset = UNSET
    wireless_uplink: ApWirelessUplink | Unset = UNSET
    candidate_parents: list[CandidateParentOpenApiVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        status_category = self.status_category

        wireless_linked = self.wireless_linked

        scan_status = self.scan_status

        child_aps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.child_aps, Unset):
            child_aps = []
            for child_aps_item_data in self.child_aps:
                child_aps_item = child_aps_item_data.to_dict()
                child_aps.append(child_aps_item)

        wireless_uplink: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_uplink, Unset):
            wireless_uplink = self.wireless_uplink.to_dict()

        candidate_parents: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.candidate_parents, Unset):
            candidate_parents = []
            for candidate_parents_item_data in self.candidate_parents:
                candidate_parents_item = candidate_parents_item_data.to_dict()
                candidate_parents.append(candidate_parents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if status_category is not UNSET:
            field_dict["statusCategory"] = status_category
        if wireless_linked is not UNSET:
            field_dict["wirelessLinked"] = wireless_linked
        if scan_status is not UNSET:
            field_dict["scanStatus"] = scan_status
        if child_aps is not UNSET:
            field_dict["childAps"] = child_aps
        if wireless_uplink is not UNSET:
            field_dict["wirelessUplink"] = wireless_uplink
        if candidate_parents is not UNSET:
            field_dict["candidateParents"] = candidate_parents

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_wireless_uplink import ApWirelessUplink
        from ..models.candidate_parent_open_api_vo import (
            CandidateParentOpenApiVO,
        )
        from ..models.child_ap_open_api_vo import ChildApOpenApiVO

        d = dict(src_dict)
        status = d.pop("status", UNSET)

        status_category = d.pop("statusCategory", UNSET)

        wireless_linked = d.pop("wirelessLinked", UNSET)

        scan_status = d.pop("scanStatus", UNSET)

        _child_aps = d.pop("childAps", UNSET)
        child_aps: list[ChildApOpenApiVO] | Unset = UNSET
        if _child_aps is not UNSET:
            child_aps = []
            for child_aps_item_data in _child_aps:
                child_aps_item = ChildApOpenApiVO.from_dict(child_aps_item_data)

                child_aps.append(child_aps_item)

        _wireless_uplink = d.pop("wirelessUplink", UNSET)
        wireless_uplink: ApWirelessUplink | Unset
        if isinstance(_wireless_uplink, Unset):
            wireless_uplink = UNSET
        else:
            wireless_uplink = ApWirelessUplink.from_dict(_wireless_uplink)

        _candidate_parents = d.pop("candidateParents", UNSET)
        candidate_parents: list[CandidateParentOpenApiVO] | Unset = UNSET
        if _candidate_parents is not UNSET:
            candidate_parents = []
            for candidate_parents_item_data in _candidate_parents:
                candidate_parents_item = CandidateParentOpenApiVO.from_dict(
                    candidate_parents_item_data
                )

                candidate_parents.append(candidate_parents_item)

        ap_mesh_statistics_open_api_vo = cls(
            status=status,
            status_category=status_category,
            wireless_linked=wireless_linked,
            scan_status=scan_status,
            child_aps=child_aps,
            wireless_uplink=wireless_uplink,
            candidate_parents=candidate_parents,
        )

        ap_mesh_statistics_open_api_vo.additional_properties = d
        return ap_mesh_statistics_open_api_vo

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
