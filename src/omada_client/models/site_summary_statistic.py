from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_summary_statistic_site_statistic_map import (
        SiteSummaryStatisticSiteStatisticMap,
    )


T = TypeVar("T", bound="SiteSummaryStatistic")


@_attrs_define
class SiteSummaryStatistic:
    """Site summary statistic info

    Attributes:
        site_statistic_map (SiteSummaryStatisticSiteStatisticMap | Unset):
    """

    site_statistic_map: SiteSummaryStatisticSiteStatisticMap | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        site_statistic_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.site_statistic_map, Unset):
            site_statistic_map = self.site_statistic_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if site_statistic_map is not UNSET:
            field_dict["siteStatisticMap"] = site_statistic_map

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_summary_statistic_site_statistic_map import (
            SiteSummaryStatisticSiteStatisticMap,
        )

        d = dict(src_dict)
        _site_statistic_map = d.pop("siteStatisticMap", UNSET)
        site_statistic_map: SiteSummaryStatisticSiteStatisticMap | Unset
        if isinstance(_site_statistic_map, Unset):
            site_statistic_map = UNSET
        else:
            site_statistic_map = SiteSummaryStatisticSiteStatisticMap.from_dict(
                _site_statistic_map
            )

        site_summary_statistic = cls(
            site_statistic_map=site_statistic_map,
        )

        site_summary_statistic.additional_properties = d
        return site_summary_statistic

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
