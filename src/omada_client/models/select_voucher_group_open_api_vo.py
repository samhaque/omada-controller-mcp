from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectVoucherGroupOpenApiVO")


@_attrs_define
class SelectVoucherGroupOpenApiVO:
    """
    Attributes:
        type_ (int): Select type. It should be a value as follows: 0: Represents selecting all voucher groups, this
            selection does not pass parameter [groupIds]. 1: Parameter [groupIds] includes the IDs of the voucher groups to
            be selected. 2: Parameter [groupIds] includes the IDs of the voucher groups not to be selected
        group_ids (list[str] | Unset): ID list of voucher groups. Voucher group can be created using 'Create Voucher
            Group' interface, and Voucher Group ID can be obtained from 'Get Voucher Group list' interface
        search_key (str | Unset): Fuzzy query parameters, support field: voucher group name, voucher code
        time_start (int | Unset): End timestamp filter query parameters, unit: MS
    """

    type_: int
    group_ids: list[str] | Unset = UNSET
    search_key: str | Unset = UNSET
    time_start: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        group_ids: list[str] | Unset = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        search_key = self.search_key

        time_start = self.time_start

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if time_start is not UNSET:
            field_dict["timeStart"] = time_start

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        search_key = d.pop("searchKey", UNSET)

        time_start = d.pop("timeStart", UNSET)

        select_voucher_group_open_api_vo = cls(
            type_=type_,
            group_ids=group_ids,
            search_key=search_key,
            time_start=time_start,
        )

        select_voucher_group_open_api_vo.additional_properties = d
        return select_voucher_group_open_api_vo

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
