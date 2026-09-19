from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sd_wan_linked_spoke_config import SdWanLinkedSpokeConfig
    from ..models.sd_wan_member_config import SdWanMemberConfig
    from ..models.sd_wan_nat_info_config import SdWanNatInfoConfig


T = TypeVar("T", bound="SdWanGroup")


@_attrs_define
class SdWanGroup:
    """
    Attributes:
        name (str): The name of the SD-WAN group
        member_list (list[SdWanMemberConfig]): A list of members of the SD-WAN group
        enable_nat (bool): Whether the group enable SD-WAN virtual network Map
        description (str | Unset): The description of the SD-WAN group
        ip_pool_start (str | Unset): The start of the IP pool of the SD-WAN group, it is recommended to ignore it as it
            will be generated automatically
        ip_pool_end (str | Unset): The end of the IP pool of the SD-WAN group, it is recommended to ignore it as it will
            be generated automatically
        linked_spokes (list[SdWanLinkedSpokeConfig] | Unset): A list of linked-spokes of the SD-WAN group
        nat_info (SdWanNatInfoConfig | Unset): The NAT info of the SD-WAN group
    """

    name: str
    member_list: list[SdWanMemberConfig]
    enable_nat: bool
    description: str | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    linked_spokes: list[SdWanLinkedSpokeConfig] | Unset = UNSET
    nat_info: SdWanNatInfoConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        member_list = []
        for member_list_item_data in self.member_list:
            member_list_item = member_list_item_data.to_dict()
            member_list.append(member_list_item)

        enable_nat = self.enable_nat

        description = self.description

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        linked_spokes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_spokes, Unset):
            linked_spokes = []
            for linked_spokes_item_data in self.linked_spokes:
                linked_spokes_item = linked_spokes_item_data.to_dict()
                linked_spokes.append(linked_spokes_item)

        nat_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nat_info, Unset):
            nat_info = self.nat_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "memberList": member_list,
                "enableNat": enable_nat,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if linked_spokes is not UNSET:
            field_dict["linkedSpokes"] = linked_spokes
        if nat_info is not UNSET:
            field_dict["natInfo"] = nat_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sd_wan_linked_spoke_config import (
            SdWanLinkedSpokeConfig,
        )
        from ..models.sd_wan_member_config import SdWanMemberConfig
        from ..models.sd_wan_nat_info_config import SdWanNatInfoConfig

        d = dict(src_dict)
        name = d.pop("name")

        member_list = []
        _member_list = d.pop("memberList")
        for member_list_item_data in _member_list:
            member_list_item = SdWanMemberConfig.from_dict(member_list_item_data)

            member_list.append(member_list_item)

        enable_nat = d.pop("enableNat")

        description = d.pop("description", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        _linked_spokes = d.pop("linkedSpokes", UNSET)
        linked_spokes: list[SdWanLinkedSpokeConfig] | Unset = UNSET
        if _linked_spokes is not UNSET:
            linked_spokes = []
            for linked_spokes_item_data in _linked_spokes:
                linked_spokes_item = SdWanLinkedSpokeConfig.from_dict(
                    linked_spokes_item_data
                )

                linked_spokes.append(linked_spokes_item)

        _nat_info = d.pop("natInfo", UNSET)
        nat_info: SdWanNatInfoConfig | Unset
        if isinstance(_nat_info, Unset):
            nat_info = UNSET
        else:
            nat_info = SdWanNatInfoConfig.from_dict(_nat_info)

        sd_wan_group = cls(
            name=name,
            member_list=member_list,
            enable_nat=enable_nat,
            description=description,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            linked_spokes=linked_spokes,
            nat_info=nat_info,
        )

        sd_wan_group.additional_properties = d
        return sd_wan_group

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
