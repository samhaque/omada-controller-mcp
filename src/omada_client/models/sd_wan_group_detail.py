from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sd_wan_linked_spoke import SdWanLinkedSpoke
    from ..models.sd_wan_member_info import SdWanMemberInfo
    from ..models.sd_wan_nat_info import SdWanNatInfo


T = TypeVar("T", bound="SdWanGroupDetail")


@_attrs_define
class SdWanGroupDetail:
    """
    Attributes:
        id (str | Unset): The ID of the SD-WAN group
        name (str | Unset): The name of the SD-WAN group
        description (str | Unset): The description of the SD-WAN group
        ip_pool_start (str | Unset): The start of the IP pool of the SD-WAN group
        ip_pool_end (str | Unset): The end of the IP pool of the SD-WAN group
        member_list (list[SdWanMemberInfo] | Unset): A list of members of the SD-WAN group
        linked_spokes (list[SdWanLinkedSpoke] | Unset): A list of linked-spokes of the SD-WAN group
        enable_nat (bool | Unset): Whether the group enable SD-WAN virtual network Map
        nat_info (SdWanNatInfo | Unset): The NAT info of the SD-WAN group
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    member_list: list[SdWanMemberInfo] | Unset = UNSET
    linked_spokes: list[SdWanLinkedSpoke] | Unset = UNSET
    enable_nat: bool | Unset = UNSET
    nat_info: SdWanNatInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        member_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.member_list, Unset):
            member_list = []
            for member_list_item_data in self.member_list:
                member_list_item = member_list_item_data.to_dict()
                member_list.append(member_list_item)

        linked_spokes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.linked_spokes, Unset):
            linked_spokes = []
            for linked_spokes_item_data in self.linked_spokes:
                linked_spokes_item = linked_spokes_item_data.to_dict()
                linked_spokes.append(linked_spokes_item)

        enable_nat = self.enable_nat

        nat_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.nat_info, Unset):
            nat_info = self.nat_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if member_list is not UNSET:
            field_dict["memberList"] = member_list
        if linked_spokes is not UNSET:
            field_dict["linkedSpokes"] = linked_spokes
        if enable_nat is not UNSET:
            field_dict["enableNat"] = enable_nat
        if nat_info is not UNSET:
            field_dict["natInfo"] = nat_info

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sd_wan_linked_spoke import SdWanLinkedSpoke
        from ..models.sd_wan_member_info import SdWanMemberInfo
        from ..models.sd_wan_nat_info import SdWanNatInfo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        _member_list = d.pop("memberList", UNSET)
        member_list: list[SdWanMemberInfo] | Unset = UNSET
        if _member_list is not UNSET:
            member_list = []
            for member_list_item_data in _member_list:
                member_list_item = SdWanMemberInfo.from_dict(member_list_item_data)

                member_list.append(member_list_item)

        _linked_spokes = d.pop("linkedSpokes", UNSET)
        linked_spokes: list[SdWanLinkedSpoke] | Unset = UNSET
        if _linked_spokes is not UNSET:
            linked_spokes = []
            for linked_spokes_item_data in _linked_spokes:
                linked_spokes_item = SdWanLinkedSpoke.from_dict(linked_spokes_item_data)

                linked_spokes.append(linked_spokes_item)

        enable_nat = d.pop("enableNat", UNSET)

        _nat_info = d.pop("natInfo", UNSET)
        nat_info: SdWanNatInfo | Unset
        if isinstance(_nat_info, Unset):
            nat_info = UNSET
        else:
            nat_info = SdWanNatInfo.from_dict(_nat_info)

        sd_wan_group_detail = cls(
            id=id,
            name=name,
            description=description,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            member_list=member_list,
            linked_spokes=linked_spokes,
            enable_nat=enable_nat,
            nat_info=nat_info,
        )

        sd_wan_group_detail.additional_properties = d
        return sd_wan_group_detail

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
