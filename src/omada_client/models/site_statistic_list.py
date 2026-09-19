from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_statistic import SiteStatistic


T = TypeVar("T", bound="SiteStatisticList")


@_attrs_define
class SiteStatisticList:
    """Site statistic list

    Attributes:
        omada_and_site_ids (list[SiteStatistic] | Unset): Omadac ID and site ID list
    """

    omada_and_site_ids: list[SiteStatistic] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        omada_and_site_ids: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.omada_and_site_ids, Unset):
            omada_and_site_ids = []
            for omada_and_site_ids_item_data in self.omada_and_site_ids:
                omada_and_site_ids_item = omada_and_site_ids_item_data.to_dict()
                omada_and_site_ids.append(omada_and_site_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if omada_and_site_ids is not UNSET:
            field_dict["omadaAndSiteIds"] = omada_and_site_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_statistic import SiteStatistic

        d = dict(src_dict)
        _omada_and_site_ids = d.pop("omadaAndSiteIds", UNSET)
        omada_and_site_ids: list[SiteStatistic] | Unset = UNSET
        if _omada_and_site_ids is not UNSET:
            omada_and_site_ids = []
            for omada_and_site_ids_item_data in _omada_and_site_ids:
                omada_and_site_ids_item = SiteStatistic.from_dict(
                    omada_and_site_ids_item_data
                )

                omada_and_site_ids.append(omada_and_site_ids_item)

        site_statistic_list = cls(
            omada_and_site_ids=omada_and_site_ids,
        )

        site_statistic_list.additional_properties = d
        return site_statistic_list

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
