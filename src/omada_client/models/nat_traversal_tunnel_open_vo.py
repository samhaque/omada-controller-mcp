from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="NatTraversalTunnelOpenVO")


@_attrs_define
class NatTraversalTunnelOpenVO:
    """
    Attributes:
        open_status (bool | Unset): Enable/Disable existing remote access tunnel. True: Enable, False: Disable
    """

    open_status: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_status = self.open_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_status is not UNSET:
            field_dict["openStatus"] = open_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        open_status = d.pop("openStatus", UNSET)

        nat_traversal_tunnel_open_vo = cls(
            open_status=open_status,
        )

        nat_traversal_tunnel_open_vo.additional_properties = d
        return nat_traversal_tunnel_open_vo

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
