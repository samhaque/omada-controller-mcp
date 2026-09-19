from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sd_wan_links_to_hub import SdWanLinksToHub


T = TypeVar("T", bound="SdWanGroupTunnelStatus")


@_attrs_define
class SdWanGroupTunnelStatus:
    """
    Attributes:
        first_check (bool | Unset): Whether the first check has been completed.
        linked_spokes (list[SdWanLinksToHub] | Unset): A list of hub-spokes of the sdWan group
    """

    first_check: bool | Unset = UNSET
    linked_spokes: list[SdWanLinksToHub] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_check = self.first_check

        linked_spokes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_spokes, Unset):
            linked_spokes = []
            for linked_spokes_item_data in self.linked_spokes:
                linked_spokes_item = linked_spokes_item_data.to_dict()
                linked_spokes.append(linked_spokes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_check is not UNSET:
            field_dict["firstCheck"] = first_check
        if linked_spokes is not UNSET:
            field_dict["linkedSpokes"] = linked_spokes

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sd_wan_links_to_hub import SdWanLinksToHub

        d = dict(src_dict)
        first_check = d.pop("firstCheck", UNSET)

        _linked_spokes = d.pop("linkedSpokes", UNSET)
        linked_spokes: list[SdWanLinksToHub] | Unset = UNSET
        if _linked_spokes is not UNSET:
            linked_spokes = []
            for linked_spokes_item_data in _linked_spokes:
                linked_spokes_item = SdWanLinksToHub.from_dict(linked_spokes_item_data)

                linked_spokes.append(linked_spokes_item)

        sd_wan_group_tunnel_status = cls(
            first_check=first_check,
            linked_spokes=linked_spokes,
        )

        sd_wan_group_tunnel_status.additional_properties = d
        return sd_wan_group_tunnel_status

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
