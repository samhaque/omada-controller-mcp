from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectIdsOpenApiVO")


@_attrs_define
class SelectIdsOpenApiVO:
    """
    Attributes:
        type_ (int): Select type. It should be a value as follows: 0: Represents selecting all vouchers in the voucher
            group, this selection does not pass parameter [ids]. 1: Parameter [ids] includes the IDs of vouchers in the
            voucher group to be selected. 2: Parameter [ids] includes the IDs of vouchers in the voucher group not to be
            selected
        group_id (str): Voucher Group ID. Voucher group can be created using 'Create Voucher Group' interface, and
            Voucher Group ID can be obtained from 'Get Voucher Group list' interface
        ids (list[str] | Unset): ID list of vouchers. Voucher can be created using 'Create Voucher Group' interface, and
            Voucher ID can be obtained from 'Get Voucher Group Detail' interface
        search_key (str | Unset): Fuzzy query parameters, support field: voucher code
        status (int | Unset): voucher status filter query parameters. It should be a value as follows: 0: Unused
            vouchers, 1: In use vouchers, 2: Expired vouchers
    """

    type_: int
    group_id: str
    ids: list[str] | Unset = UNSET
    search_key: str | Unset = UNSET
    status: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        group_id = self.group_id

        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        search_key = self.search_key

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "groupId": group_id,
            }
        )
        if ids is not UNSET:
            field_dict["ids"] = ids
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        type_ = d.pop("type")

        group_id = d.pop("groupId")

        ids = cast(list[str], d.pop("ids", UNSET))

        search_key = d.pop("searchKey", UNSET)

        status = d.pop("status", UNSET)

        select_ids_open_api_vo = cls(
            type_=type_,
            group_id=group_id,
            ids=ids,
            search_key=search_key,
            status=status,
        )

        select_ids_open_api_vo.additional_properties = d
        return select_ids_open_api_vo

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
