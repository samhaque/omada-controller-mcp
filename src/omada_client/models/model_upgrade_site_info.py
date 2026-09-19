from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_basic_info import SiteBasicInfo


T = TypeVar("T", bound="ModelUpgradeSiteInfo")


@_attrs_define
class ModelUpgradeSiteInfo:
    """
    Attributes:
        current_page (int | Unset): Start page number. Start from 1.
        current_page_size (int | Unset): Number of entries per page. It should be within the range of 1–100.
        total_rows (int | Unset): Total rows.
        all_site_ids (list[str] | Unset): All siteIDs in the query result.
        data (list[SiteBasicInfo] | Unset): Site basic information on one page.
    """

    current_page: int | Unset = UNSET
    current_page_size: int | Unset = UNSET
    total_rows: int | Unset = UNSET
    all_site_ids: list[str] | Unset = UNSET
    data: list[SiteBasicInfo] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        current_page_size = self.current_page_size

        total_rows = self.total_rows

        all_site_ids: list[str] | Unset = UNSET
        if not isinstance(self.all_site_ids, Unset):
            all_site_ids = self.all_site_ids

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if current_page_size is not UNSET:
            field_dict["currentPageSize"] = current_page_size
        if total_rows is not UNSET:
            field_dict["totalRows"] = total_rows
        if all_site_ids is not UNSET:
            field_dict["allSiteIds"] = all_site_ids
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.site_basic_info import SiteBasicInfo

        d = dict(src_dict)
        current_page = d.pop("currentPage", UNSET)

        current_page_size = d.pop("currentPageSize", UNSET)

        total_rows = d.pop("totalRows", UNSET)

        all_site_ids = cast(list[str], d.pop("allSiteIds", UNSET))

        _data = d.pop("data", UNSET)
        data: list[SiteBasicInfo] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = SiteBasicInfo.from_dict(data_item_data)

                data.append(data_item)

        model_upgrade_site_info = cls(
            current_page=current_page,
            current_page_size=current_page_size,
            total_rows=total_rows,
            all_site_ids=all_site_ids,
            data=data,
        )

        model_upgrade_site_info.additional_properties = d
        return model_upgrade_site_info

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
