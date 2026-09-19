from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sd_wan_member_selected import SdWanMemberSelected


T = TypeVar("T", bound="CheckMappedNetwork")


@_attrs_define
class CheckMappedNetwork:
    """
    Attributes:
        modified_network (str): The IP Subnet of the modified network
        member_list (list[SdWanMemberSelected]): A list of members of the SD-WAN group
        mapped_networks (list[str] | Unset): A list of current mapped network of the SD-WAN group
    """

    modified_network: str
    member_list: list[SdWanMemberSelected]
    mapped_networks: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        modified_network = self.modified_network

        member_list = []
        for member_list_item_data in self.member_list:
            member_list_item = member_list_item_data.to_dict()
            member_list.append(member_list_item)

        mapped_networks: list[str] | Unset = UNSET
        if not isinstance(self.mapped_networks, Unset):
            mapped_networks = self.mapped_networks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "modifiedNetwork": modified_network,
                "memberList": member_list,
            }
        )
        if mapped_networks is not UNSET:
            field_dict["mappedNetworks"] = mapped_networks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sd_wan_member_selected import SdWanMemberSelected

        d = dict(src_dict)
        modified_network = d.pop("modifiedNetwork")

        member_list = []
        _member_list = d.pop("memberList")
        for member_list_item_data in _member_list:
            member_list_item = SdWanMemberSelected.from_dict(member_list_item_data)

            member_list.append(member_list_item)

        mapped_networks = cast(list[str], d.pop("mappedNetworks", UNSET))

        check_mapped_network = cls(
            modified_network=modified_network,
            member_list=member_list,
            mapped_networks=mapped_networks,
        )

        check_mapped_network.additional_properties = d
        return check_mapped_network

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
