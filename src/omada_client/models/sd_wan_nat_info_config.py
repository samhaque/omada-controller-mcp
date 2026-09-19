from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sd_wan_nat_item_config import SdWanNatItemConfig


T = TypeVar("T", bound="SdWanNatInfoConfig")


@_attrs_define
class SdWanNatInfoConfig:
    """The NAT info of the SD-WAN group

    Attributes:
        default_map_network_list (list[str] | Unset): A list of the default mapping network
        custom_map_network_list (list[str] | Unset): A list of the customized mapping network
        network_map_list (list[SdWanNatItemConfig] | Unset): A list of the network map item
    """

    default_map_network_list: list[str] | Unset = UNSET
    custom_map_network_list: list[str] | Unset = UNSET
    network_map_list: list[SdWanNatItemConfig] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        default_map_network_list: list[str] | Unset = UNSET
        if not isinstance(self.default_map_network_list, Unset):
            default_map_network_list = self.default_map_network_list

        custom_map_network_list: list[str] | Unset = UNSET
        if not isinstance(self.custom_map_network_list, Unset):
            custom_map_network_list = self.custom_map_network_list

        network_map_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.network_map_list, Unset):
            network_map_list = []
            for network_map_list_item_data in self.network_map_list:
                network_map_list_item = network_map_list_item_data.to_dict()
                network_map_list.append(network_map_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_map_network_list is not UNSET:
            field_dict["defaultMapNetworkList"] = default_map_network_list
        if custom_map_network_list is not UNSET:
            field_dict["customMapNetworkList"] = custom_map_network_list
        if network_map_list is not UNSET:
            field_dict["networkMapList"] = network_map_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sd_wan_nat_item_config import SdWanNatItemConfig

        d = dict(src_dict)
        default_map_network_list = cast(
            list[str], d.pop("defaultMapNetworkList", UNSET)
        )

        custom_map_network_list = cast(list[str], d.pop("customMapNetworkList", UNSET))

        _network_map_list = d.pop("networkMapList", UNSET)
        network_map_list: list[SdWanNatItemConfig] | Unset = UNSET
        if _network_map_list is not UNSET:
            network_map_list = []
            for network_map_list_item_data in _network_map_list:
                network_map_list_item = SdWanNatItemConfig.from_dict(
                    network_map_list_item_data
                )

                network_map_list.append(network_map_list_item)

        sd_wan_nat_info_config = cls(
            default_map_network_list=default_map_network_list,
            custom_map_network_list=custom_map_network_list,
            network_map_list=network_map_list,
        )

        sd_wan_nat_info_config.additional_properties = d
        return sd_wan_nat_info_config

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
