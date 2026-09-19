from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchOspfProcessOpenApiVO")


@_attrs_define
class BatchOspfProcessOpenApiVO:
    """
    Attributes:
        process_id_list (list[str]): List of Process ID
        select_type (int): Select Type, it should be a value as follows: 1: SELECT ALL, 2: SELECT INCLUDE, 3: SELECT
            EXCLUDE.
        search_key (str | Unset): SearchKey
    """

    process_id_list: list[str]
    select_type: int
    search_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        process_id_list = self.process_id_list

        select_type = self.select_type

        search_key = self.search_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "processIdList": process_id_list,
                "selectType": select_type,
            }
        )
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        process_id_list = cast(list[str], d.pop("processIdList"))

        select_type = d.pop("selectType")

        search_key = d.pop("searchKey", UNSET)

        batch_ospf_process_open_api_vo = cls(
            process_id_list=process_id_list,
            select_type=select_type,
            search_key=search_key,
        )

        batch_ospf_process_open_api_vo.additional_properties = d
        return batch_ospf_process_open_api_vo

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
