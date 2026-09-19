from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wifi_device_and_client_query_vo_sorts import (
        WifiDeviceAndClientQueryVOSorts,
    )


T = TypeVar("T", bound="WifiDeviceAndClientQueryVO")


@_attrs_define
class WifiDeviceAndClientQueryVO:
    """
    Attributes:
        time (int): Time(unit:ms)
        search_key (str | Unset): Fuzzy query parameters, support field name,mac
        sorts (WifiDeviceAndClientQueryVOSorts | Unset): Sort parameter may be one of asc or desc. Optional parameter.
            If it is not carried, it means it is not sorted by this field.
        top_k (int | Unset): The topK elements, which must be less than 100
    """

    time: int
    search_key: str | Unset = UNSET
    sorts: WifiDeviceAndClientQueryVOSorts | Unset = UNSET
    top_k: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        time = self.time

        search_key = self.search_key

        sorts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = self.sorts.to_dict()

        top_k = self.top_k

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "time": time,
            }
        )
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if top_k is not UNSET:
            field_dict["topK"] = top_k

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.wifi_device_and_client_query_vo_sorts import (
            WifiDeviceAndClientQueryVOSorts,
        )

        d = dict(src_dict)
        time = d.pop("time")

        search_key = d.pop("searchKey", UNSET)

        _sorts = d.pop("sorts", UNSET)
        sorts: WifiDeviceAndClientQueryVOSorts | Unset
        if isinstance(_sorts, Unset):
            sorts = UNSET
        else:
            sorts = WifiDeviceAndClientQueryVOSorts.from_dict(_sorts)

        top_k = d.pop("topK", UNSET)

        wifi_device_and_client_query_vo = cls(
            time=time,
            search_key=search_key,
            sorts=sorts,
            top_k=top_k,
        )

        wifi_device_and_client_query_vo.additional_properties = d
        return wifi_device_and_client_query_vo

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
