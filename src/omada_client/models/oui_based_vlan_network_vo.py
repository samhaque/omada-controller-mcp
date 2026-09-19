from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="OuiBasedVlanNetworkVO")


@_attrs_define
class OuiBasedVlanNetworkVO:
    """The network configured in the osw port.

    Attributes:
        oui_based_vlan_id (str | Unset): The id of the oui based vlan rule.
        oui_based_vlan_name (str | Unset): The name of the oui based vlan rule.
        rule_mode (int | Unset): The mode of the oui based vlan rule. 0 represents all device ports ,1 represents
            custom.
        network_id (str | Unset): The id for the network.
        network_name (str | Unset): The name of the network.
        vlan_type (int | Unset): 0:Single, 1:Multiple(Bridge Vlan)
        vlan (int | Unset): The vlan of one network that multicast config used.
    """

    oui_based_vlan_id: str | Unset = UNSET
    oui_based_vlan_name: str | Unset = UNSET
    rule_mode: int | Unset = UNSET
    network_id: str | Unset = UNSET
    network_name: str | Unset = UNSET
    vlan_type: int | Unset = UNSET
    vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        oui_based_vlan_id = self.oui_based_vlan_id

        oui_based_vlan_name = self.oui_based_vlan_name

        rule_mode = self.rule_mode

        network_id = self.network_id

        network_name = self.network_name

        vlan_type = self.vlan_type

        vlan = self.vlan

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oui_based_vlan_id is not UNSET:
            field_dict["ouiBasedVlanId"] = oui_based_vlan_id
        if oui_based_vlan_name is not UNSET:
            field_dict["ouiBasedVlanName"] = oui_based_vlan_name
        if rule_mode is not UNSET:
            field_dict["ruleMode"] = rule_mode
        if network_id is not UNSET:
            field_dict["networkId"] = network_id
        if network_name is not UNSET:
            field_dict["networkName"] = network_name
        if vlan_type is not UNSET:
            field_dict["vlanType"] = vlan_type
        if vlan is not UNSET:
            field_dict["vlan"] = vlan

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        oui_based_vlan_id = d.pop("ouiBasedVlanId", UNSET)

        oui_based_vlan_name = d.pop("ouiBasedVlanName", UNSET)

        rule_mode = d.pop("ruleMode", UNSET)

        network_id = d.pop("networkId", UNSET)

        network_name = d.pop("networkName", UNSET)

        vlan_type = d.pop("vlanType", UNSET)

        vlan = d.pop("vlan", UNSET)

        oui_based_vlan_network_vo = cls(
            oui_based_vlan_id=oui_based_vlan_id,
            oui_based_vlan_name=oui_based_vlan_name,
            rule_mode=rule_mode,
            network_id=network_id,
            network_name=network_name,
            vlan_type=vlan_type,
            vlan=vlan,
        )

        oui_based_vlan_network_vo.additional_properties = d
        return oui_based_vlan_network_vo

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
