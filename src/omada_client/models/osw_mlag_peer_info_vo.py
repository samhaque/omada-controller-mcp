from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OswMlagPeerInfoVO")


@_attrs_define
class OswMlagPeerInfoVO:
    """M-LAG Peer device info

    Attributes:
        mac (str | Unset): M-LAG Peer device mac
        name (str | Unset): M-LAG Peer device name
        port_num (int | Unset): Number of ports in the M-LAG group
        max_lag_num (int | Unset): Maximum number of LAG groups
        max_lag_member (int | Unset): Maximum number of ports in a LAG group
        used_lag_ids (list[int] | Unset): List of used lag IDs
    """

    mac: str | Unset = UNSET
    name: str | Unset = UNSET
    port_num: int | Unset = UNSET
    max_lag_num: int | Unset = UNSET
    max_lag_member: int | Unset = UNSET
    used_lag_ids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mac = self.mac

        name = self.name

        port_num = self.port_num

        max_lag_num = self.max_lag_num

        max_lag_member = self.max_lag_member

        used_lag_ids: list[int] | Unset = UNSET
        if not isinstance(self.used_lag_ids, Unset):
            used_lag_ids = self.used_lag_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mac is not UNSET:
            field_dict["mac"] = mac
        if name is not UNSET:
            field_dict["name"] = name
        if port_num is not UNSET:
            field_dict["portNum"] = port_num
        if max_lag_num is not UNSET:
            field_dict["maxLagNum"] = max_lag_num
        if max_lag_member is not UNSET:
            field_dict["maxLagMember"] = max_lag_member
        if used_lag_ids is not UNSET:
            field_dict["usedLagIds"] = used_lag_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mac = d.pop("mac", UNSET)

        name = d.pop("name", UNSET)

        port_num = d.pop("portNum", UNSET)

        max_lag_num = d.pop("maxLagNum", UNSET)

        max_lag_member = d.pop("maxLagMember", UNSET)

        used_lag_ids = cast(list[int], d.pop("usedLagIds", UNSET))

        osw_mlag_peer_info_vo = cls(
            mac=mac,
            name=name,
            port_num=port_num,
            max_lag_num=max_lag_num,
            max_lag_member=max_lag_member,
            used_lag_ids=used_lag_ids,
        )

        osw_mlag_peer_info_vo.additional_properties = d
        return osw_mlag_peer_info_vo

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
