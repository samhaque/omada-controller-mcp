from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_select_wan_port_req import AutoSelectWanPortReq


T = TypeVar("T", bound="BatchAutoSelectWanPortReq")


@_attrs_define
class BatchAutoSelectWanPortReq:
    """
    Attributes:
        member_list (list[AutoSelectWanPortReq] | Unset): A list of the SD-WAN devices which use auto select.
    """

    member_list: list[AutoSelectWanPortReq] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member_list, Unset):
            member_list = []
            for member_list_item_data in self.member_list:
                member_list_item = member_list_item_data.to_dict()
                member_list.append(member_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if member_list is not UNSET:
            field_dict["memberList"] = member_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.auto_select_wan_port_req import (
            AutoSelectWanPortReq,
        )

        d = dict(src_dict)
        _member_list = d.pop("memberList", UNSET)
        member_list: list[AutoSelectWanPortReq] | Unset = UNSET
        if _member_list is not UNSET:
            member_list = []
            for member_list_item_data in _member_list:
                member_list_item = AutoSelectWanPortReq.from_dict(member_list_item_data)

                member_list.append(member_list_item)

        batch_auto_select_wan_port_req = cls(
            member_list=member_list,
        )

        batch_auto_select_wan_port_req.additional_properties = d
        return batch_auto_select_wan_port_req

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
