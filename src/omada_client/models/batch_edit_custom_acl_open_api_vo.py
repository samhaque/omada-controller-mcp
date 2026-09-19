from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchEditCustomAclOpenApiVO")


@_attrs_define
class BatchEditCustomAclOpenApiVO:
    """
    Attributes:
        ids (list[str]): When selectType is set to all, the ids do not need to be passed and all entries are processed,
            when selectType is set to include, the id entries contained in the ids are processed, when selectType is set to
            exclude, the id entries that are not contained in the ids are processed
        log (int): log status of acl.
        status (int): enable status of acl.
        select_type (str | Unset): SelectType all, include or exclude
        search_key (str | Unset): Fuzzy query parameters, support field: voucher code
    """

    ids: list[str]
    log: int
    status: int
    select_type: str | Unset = UNSET
    search_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        log = self.log

        status = self.status

        select_type = self.select_type

        search_key = self.search_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ids": ids,
                "log": log,
                "status": status,
            }
        )
        if select_type is not UNSET:
            field_dict["selectType"] = select_type
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids"))

        log = d.pop("log")

        status = d.pop("status")

        select_type = d.pop("selectType", UNSET)

        search_key = d.pop("searchKey", UNSET)

        batch_edit_custom_acl_open_api_vo = cls(
            ids=ids,
            log=log,
            status=status,
            select_type=select_type,
            search_key=search_key,
        )

        batch_edit_custom_acl_open_api_vo.additional_properties = d
        return batch_edit_custom_acl_open_api_vo

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
