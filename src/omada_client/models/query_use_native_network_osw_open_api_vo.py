from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryUseNativeNetworkOswOpenApiVO")


@_attrs_define
class QueryUseNativeNetworkOswOpenApiVO:
    """QueryUseNativeNetworkOswOpenApiVO

    Attributes:
        page (int): Start from 1.
        page_size (int): It should be within the range of 1–1000.
        select_all (bool | Unset): Select all VLAN networks
        ids (list[str] | Unset): List of VLAN and Interface network IDs. The valid network IDs can be obtained from "Get
            LAN network list". When selectAll is true, it means select all except specified IDs; When selectAll is false, it
            means select specified IDs.
    """

    page: int
    page_size: int
    select_all: bool | Unset = UNSET
    ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        page_size = self.page_size

        select_all = self.select_all

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pageSize": page_size,
            }
        )
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        page = d.pop("page")

        page_size = d.pop("pageSize")

        select_all = d.pop("selectAll", UNSET)

        ids = cast(list[str], d.pop("ids", UNSET))

        query_use_native_network_osw_open_api_vo = cls(
            page=page,
            page_size=page_size,
            select_all=select_all,
            ids=ids,
        )

        query_use_native_network_osw_open_api_vo.additional_properties = d
        return query_use_native_network_osw_open_api_vo

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
