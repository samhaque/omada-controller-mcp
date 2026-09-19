from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sd_wan_network_map import SdWanNetworkMap


T = TypeVar("T", bound="SdWanMappedNetworkResult")


@_attrs_define
class SdWanMappedNetworkResult:
    """
    Attributes:
        mapped_networks (list[SdWanNetworkMap] | Unset): A list of the mapped network
        default_map_network_list (list[str] | Unset): A list of the default mapping network
        custom_map_network_list (list[str] | Unset): A list of the customized mapping network
    """

    mapped_networks: list[SdWanNetworkMap] | Unset = UNSET
    default_map_network_list: list[str] | Unset = UNSET
    custom_map_network_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mapped_networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mapped_networks, Unset):
            mapped_networks = []
            for mapped_networks_item_data in self.mapped_networks:
                mapped_networks_item = mapped_networks_item_data.to_dict()
                mapped_networks.append(mapped_networks_item)

        default_map_network_list: list[str] | Unset = UNSET
        if not isinstance(self.default_map_network_list, Unset):
            default_map_network_list = self.default_map_network_list

        custom_map_network_list: list[str] | Unset = UNSET
        if not isinstance(self.custom_map_network_list, Unset):
            custom_map_network_list = self.custom_map_network_list

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mapped_networks is not UNSET:
            field_dict["mappedNetworks"] = mapped_networks
        if default_map_network_list is not UNSET:
            field_dict["defaultMapNetworkList"] = default_map_network_list
        if custom_map_network_list is not UNSET:
            field_dict["customMapNetworkList"] = custom_map_network_list

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.sd_wan_network_map import SdWanNetworkMap

        d = dict(src_dict)
        _mapped_networks = d.pop("mappedNetworks", UNSET)
        mapped_networks: list[SdWanNetworkMap] | Unset = UNSET
        if _mapped_networks is not UNSET:
            mapped_networks = []
            for mapped_networks_item_data in _mapped_networks:
                mapped_networks_item = SdWanNetworkMap.from_dict(
                    mapped_networks_item_data
                )

                mapped_networks.append(mapped_networks_item)

        default_map_network_list = cast(
            list[str], d.pop("defaultMapNetworkList", UNSET)
        )

        custom_map_network_list = cast(list[str], d.pop("customMapNetworkList", UNSET))

        sd_wan_mapped_network_result = cls(
            mapped_networks=mapped_networks,
            default_map_network_list=default_map_network_list,
            custom_map_network_list=custom_map_network_list,
        )

        sd_wan_mapped_network_result.additional_properties = d
        return sd_wan_mapped_network_result

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
