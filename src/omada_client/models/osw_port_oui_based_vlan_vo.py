from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oui_based_vlan_network_vo import OuiBasedVlanNetworkVO


T = TypeVar("T", bound="OswPortOuiBasedVlanVO")


@_attrs_define
class OswPortOuiBasedVlanVO:
    """Vlans configured in oui based rules.

    Attributes:
        networks (list[OuiBasedVlanNetworkVO] | Unset): The network configured in the osw port.
    """

    networks: list[OuiBasedVlanNetworkVO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if networks is not UNSET:
            field_dict["networks"] = networks

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.oui_based_vlan_network_vo import (
            OuiBasedVlanNetworkVO,
        )

        d = dict(src_dict)
        _networks = d.pop("networks", UNSET)
        networks: list[OuiBasedVlanNetworkVO] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = OuiBasedVlanNetworkVO.from_dict(networks_item_data)

                networks.append(networks_item)

        osw_port_oui_based_vlan_vo = cls(
            networks=networks,
        )

        osw_port_oui_based_vlan_vo.additional_properties = d
        return osw_port_oui_based_vlan_vo

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
