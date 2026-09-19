from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NatTraversalSingleTunnelStatusVO")


@_attrs_define
class NatTraversalSingleTunnelStatusVO:
    """
    Attributes:
        tunnel_id (int | Unset):
        status (int | Unset): Status of the remote access tunnel. 0: Disconnected, 1: Connected, 2: Opening, -1:
            Heartbeat Missed, -2: Expired.
        open_status (bool | Unset): The open and closed status of the remote access tunnel.
        name (str | Unset): Name of the remote access tunnel.
    """

    tunnel_id: int | Unset = UNSET
    status: int | Unset = UNSET
    open_status: bool | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tunnel_id = self.tunnel_id

        status = self.status

        open_status = self.open_status

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tunnel_id is not UNSET:
            field_dict["tunnelId"] = tunnel_id
        if status is not UNSET:
            field_dict["status"] = status
        if open_status is not UNSET:
            field_dict["openStatus"] = open_status
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        tunnel_id = d.pop("tunnelId", UNSET)

        status = d.pop("status", UNSET)

        open_status = d.pop("openStatus", UNSET)

        name = d.pop("name", UNSET)

        nat_traversal_single_tunnel_status_vo = cls(
            tunnel_id=tunnel_id,
            status=status,
            open_status=open_status,
            name=name,
        )

        nat_traversal_single_tunnel_status_vo.additional_properties = d
        return nat_traversal_single_tunnel_status_vo

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
