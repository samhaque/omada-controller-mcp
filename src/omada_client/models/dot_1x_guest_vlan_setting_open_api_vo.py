from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="Dot1XGuestVlanSettingOpenApiVO")


@_attrs_define
class Dot1XGuestVlanSettingOpenApiVO:
    """Guest VLAN configuration used for EAP 802.1x authentication. Supports three modes: 0 = None, 1 = By Network, 2 = By
    VLAN ID. Parameter [guestVlanSetting] should not be null when [enable] is TRUE.

        Attributes:
            mode (int): Guest VLAN application mode. Valid values: 0 = None (Disable Guest Vlan), 1 = By Network (select a
                LAN network), 2 = By VLAN ID (specify a VLAN ID directly).
            lan_network_id (str | Unset): LAN network ID used when [mode] = 1 (By Network). Specifies the target LAN network
                to which the Guest VLAN is mapped. The LAN network ID can be obtained from the 'Get LAN network list V3'
                interface.
            bridge_vlan (int | Unset): Actual VLAN ID to apply when the selected LAN network is a Multi-VLAN network. Valid
                range: 1-4094.
            vlan_id (int | Unset): Guest VLAN ID used when [mode] = 2 (By VLAN ID). Valid range: 1-4094.
    """

    mode: int
    lan_network_id: str | Unset = UNSET
    bridge_vlan: int | Unset = UNSET
    vlan_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        lan_network_id = self.lan_network_id

        bridge_vlan = self.bridge_vlan

        vlan_id = self.vlan_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if lan_network_id is not UNSET:
            field_dict["lanNetworkId"] = lan_network_id
        if bridge_vlan is not UNSET:
            field_dict["bridgeVlan"] = bridge_vlan
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        lan_network_id = d.pop("lanNetworkId", UNSET)

        bridge_vlan = d.pop("bridgeVlan", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        dot_1x_guest_vlan_setting_open_api_vo = cls(
            mode=mode,
            lan_network_id=lan_network_id,
            bridge_vlan=bridge_vlan,
            vlan_id=vlan_id,
        )

        dot_1x_guest_vlan_setting_open_api_vo.additional_properties = d
        return dot_1x_guest_vlan_setting_open_api_vo

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
