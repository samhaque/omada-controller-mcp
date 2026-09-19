from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApVlanConfigOpenApiVO")


@_attrs_define
class ApVlanConfigOpenApiVO:
    """
    Attributes:
        mode (int): Mode for the AP management VLAN configuration to take effect.[0:Default,1:Custom]
        lan_network_id (str | Unset): This field indicates the currently effective lanNetworkId.
        bridge_vlan (int | Unset): When mvlanNetworkId is bridge vlan, mvlanBridgeVlan has a value.
    """

    mode: int
    lan_network_id: str | Unset = UNSET
    bridge_vlan: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        lan_network_id = self.lan_network_id

        bridge_vlan = self.bridge_vlan

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

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        lan_network_id = d.pop("lanNetworkId", UNSET)

        bridge_vlan = d.pop("bridgeVlan", UNSET)

        ap_vlan_config_open_api_vo = cls(
            mode=mode,
            lan_network_id=lan_network_id,
            bridge_vlan=bridge_vlan,
        )

        ap_vlan_config_open_api_vo.additional_properties = d
        return ap_vlan_config_open_api_vo

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
