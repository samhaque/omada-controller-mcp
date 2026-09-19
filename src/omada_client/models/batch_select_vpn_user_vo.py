from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchSelectVpnUserVO")


@_attrs_define
class BatchSelectVpnUserVO:
    """
    Attributes:
        ids (list[str] | Unset): ID list of batch selected VPN users.
        search_key (str | Unset): The keywords of the searchIt is effected when [selectAll] is 'true'.
        select_all (bool | Unset): Indicates whether to select all VPN users for deletion. The behavior depends on the
            combination with 'ids': 1: If selectAll is true and ids is not empty: perform a reverse selection (excluding the
            specified IDs). 2: If selectAll is true and ids is empty: select all VPN users. 3: If selectAll is false and ids
            is not empty: select only the specified VPN users in the ID list.
        protocol (int | Unset): Protocol should be a value as follows: 0: L2TP or PPTP; 1: OpenVPN, 2: SSL VPN.
    """

    ids: list[str] | Unset = UNSET
    search_key: str | Unset = UNSET
    select_all: bool | Unset = UNSET
    protocol: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ids: list[str] | Unset = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        search_key = self.search_key

        select_all = self.select_all

        protocol = self.protocol

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ids is not UNSET:
            field_dict["ids"] = ids
        if search_key is not UNSET:
            field_dict["searchKey"] = search_key
        if select_all is not UNSET:
            field_dict["selectAll"] = select_all
        if protocol is not UNSET:
            field_dict["protocol"] = protocol

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ids = cast(list[str], d.pop("ids", UNSET))

        search_key = d.pop("searchKey", UNSET)

        select_all = d.pop("selectAll", UNSET)

        protocol = d.pop("protocol", UNSET)

        batch_select_vpn_user_vo = cls(
            ids=ids,
            search_key=search_key,
            select_all=select_all,
            protocol=protocol,
        )

        batch_select_vpn_user_vo.additional_properties = d
        return batch_select_vpn_user_vo

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
