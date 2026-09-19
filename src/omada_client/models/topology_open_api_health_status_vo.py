from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopologyOpenApiHealthStatusVO")


@_attrs_define
class TopologyOpenApiHealthStatusVO:
    """Topology Health Status

    Attributes:
        good (int | Unset): Devices Count In Good Health Status
        fair (int | Unset): Devices Count In Fair/Average Health Status
        poor (int | Unset): Devices Count In Poor Health Status
        no_data (int | Unset): Devices Count With No Health Status
        disconnected (int | Unset): Disconnected Devices Count
        total (int | Unset): Total Devices Count
    """

    good: int | Unset = UNSET
    fair: int | Unset = UNSET
    poor: int | Unset = UNSET
    no_data: int | Unset = UNSET
    disconnected: int | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        good = self.good

        fair = self.fair

        poor = self.poor

        no_data = self.no_data

        disconnected = self.disconnected

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if good is not UNSET:
            field_dict["good"] = good
        if fair is not UNSET:
            field_dict["fair"] = fair
        if poor is not UNSET:
            field_dict["poor"] = poor
        if no_data is not UNSET:
            field_dict["noData"] = no_data
        if disconnected is not UNSET:
            field_dict["disconnected"] = disconnected
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        good = d.pop("good", UNSET)

        fair = d.pop("fair", UNSET)

        poor = d.pop("poor", UNSET)

        no_data = d.pop("noData", UNSET)

        disconnected = d.pop("disconnected", UNSET)

        total = d.pop("total", UNSET)

        topology_open_api_health_status_vo = cls(
            good=good,
            fair=fair,
            poor=poor,
            no_data=no_data,
            disconnected=disconnected,
            total=total,
        )

        topology_open_api_health_status_vo.additional_properties = d
        return topology_open_api_health_status_vo

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
