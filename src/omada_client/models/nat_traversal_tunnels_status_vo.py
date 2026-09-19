from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nat_traversal_single_tunnel_status_vo import (
        NatTraversalSingleTunnelStatusVO,
    )


T = TypeVar("T", bound="NatTraversalTunnelsStatusVO")


@_attrs_define
class NatTraversalTunnelsStatusVO:
    """
    Attributes:
        tunnels_status (list[NatTraversalSingleTunnelStatusVO] | Unset):
    """

    tunnels_status: list[NatTraversalSingleTunnelStatusVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tunnels_status: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tunnels_status, Unset):
            tunnels_status = []
            for tunnels_status_item_data in self.tunnels_status:
                tunnels_status_item = tunnels_status_item_data.to_dict()
                tunnels_status.append(tunnels_status_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tunnels_status is not UNSET:
            field_dict["tunnelsStatus"] = tunnels_status

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.nat_traversal_single_tunnel_status_vo import (
            NatTraversalSingleTunnelStatusVO,
        )

        d = dict(src_dict)
        _tunnels_status = d.pop("tunnelsStatus", UNSET)
        tunnels_status: list[NatTraversalSingleTunnelStatusVO] | Unset = UNSET
        if _tunnels_status is not UNSET:
            tunnels_status = []
            for tunnels_status_item_data in _tunnels_status:
                tunnels_status_item = NatTraversalSingleTunnelStatusVO.from_dict(
                    tunnels_status_item_data
                )

                tunnels_status.append(tunnels_status_item)

        nat_traversal_tunnels_status_vo = cls(
            tunnels_status=tunnels_status,
        )

        nat_traversal_tunnels_status_vo.additional_properties = d
        return nat_traversal_tunnels_status_vo

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
