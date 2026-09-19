from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MlagMsgVO")


@_attrs_define
class MlagMsgVO:
    """M-LAG Message

    Attributes:
        mlag_id (str | Unset): M-LAG ID
        mlag_name (str | Unset): M-LAG Group Name
        role (int | Unset): M-LAG Role, 0: Unknown, 1: Primary, 2: Secondary
        priority (int | Unset): M-LAG Priority
        dad_link_port (list[int] | Unset): Set of DAD Link Ports
        peer_link_port (list[int] | Unset): Set of Peer Link Ports
    """

    mlag_id: str | Unset = UNSET
    mlag_name: str | Unset = UNSET
    role: int | Unset = UNSET
    priority: int | Unset = UNSET
    dad_link_port: list[int] | Unset = UNSET
    peer_link_port: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mlag_id = self.mlag_id

        mlag_name = self.mlag_name

        role = self.role

        priority = self.priority

        dad_link_port: list[int] | Unset = UNSET
        if not isinstance(self.dad_link_port, Unset):
            dad_link_port = self.dad_link_port

        peer_link_port: list[int] | Unset = UNSET
        if not isinstance(self.peer_link_port, Unset):
            peer_link_port = self.peer_link_port

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mlag_id is not UNSET:
            field_dict["mlagId"] = mlag_id
        if mlag_name is not UNSET:
            field_dict["mlagName"] = mlag_name
        if role is not UNSET:
            field_dict["role"] = role
        if priority is not UNSET:
            field_dict["priority"] = priority
        if dad_link_port is not UNSET:
            field_dict["dadLinkPort"] = dad_link_port
        if peer_link_port is not UNSET:
            field_dict["peerLinkPort"] = peer_link_port

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mlag_id = d.pop("mlagId", UNSET)

        mlag_name = d.pop("mlagName", UNSET)

        role = d.pop("role", UNSET)

        priority = d.pop("priority", UNSET)

        dad_link_port = cast(list[int], d.pop("dadLinkPort", UNSET))

        peer_link_port = cast(list[int], d.pop("peerLinkPort", UNSET))

        mlag_msg_vo = cls(
            mlag_id=mlag_id,
            mlag_name=mlag_name,
            role=role,
            priority=priority,
            dad_link_port=dad_link_port,
            peer_link_port=peer_link_port,
        )

        mlag_msg_vo.additional_properties = d
        return mlag_msg_vo

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
