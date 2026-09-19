from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApVoipVlanSettingOpenApiVO")


@_attrs_define
class ApVoipVlanSettingOpenApiVO:
    """VoIP VLAN setting.

    Attributes:
        mode (int): VoIP VLAN mode. 0 : Follow Management VLAN. 1: Custom.
        lan_network_id (str | Unset): LAN network ID. Parameter [lanNetworkId] should not be null, and should not be the
            same as the lanNetworkId of management VLAN when parameter [mode] is 1.
        voip_bridge_vlan (int | Unset): VoIP bridge vlan. Parameter [voipBridgeVlan] should not be null and be between 1
            and 4090 when parameter [lanNetworkId] corresponds to a multiple VLAN LAN network.
        ip_type (int | Unset): VoIP VLAN IP Type. 0: Static IP. 1: DHCP.
        ip (str | Unset): VoIP VLAN IP. Parameter [ip] should not be null when [ipType] is 0.
        ip_mask (str | Unset): VoIP VLAN IP mask. Parameter [ipMask] should not be null when [ipType] is 0.
        ip_gateway (str | Unset): VoIP VLAN IP gateway. Parameter [ipGateway] should not be null when [ipType] is 0.
        ip_dns_1 (str | Unset): IP DNS1.
        ip_dns_2 (str | Unset): IP DNS2.
    """

    mode: int
    lan_network_id: str | Unset = UNSET
    voip_bridge_vlan: int | Unset = UNSET
    ip_type: int | Unset = UNSET
    ip: str | Unset = UNSET
    ip_mask: str | Unset = UNSET
    ip_gateway: str | Unset = UNSET
    ip_dns_1: str | Unset = UNSET
    ip_dns_2: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        lan_network_id = self.lan_network_id

        voip_bridge_vlan = self.voip_bridge_vlan

        ip_type = self.ip_type

        ip = self.ip

        ip_mask = self.ip_mask

        ip_gateway = self.ip_gateway

        ip_dns_1 = self.ip_dns_1

        ip_dns_2 = self.ip_dns_2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
            }
        )
        if lan_network_id is not UNSET:
            field_dict["lanNetworkId"] = lan_network_id
        if voip_bridge_vlan is not UNSET:
            field_dict["voipBridgeVlan"] = voip_bridge_vlan
        if ip_type is not UNSET:
            field_dict["ipType"] = ip_type
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ip_mask is not UNSET:
            field_dict["ipMask"] = ip_mask
        if ip_gateway is not UNSET:
            field_dict["ipGateway"] = ip_gateway
        if ip_dns_1 is not UNSET:
            field_dict["ipDns1"] = ip_dns_1
        if ip_dns_2 is not UNSET:
            field_dict["ipDns2"] = ip_dns_2

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        mode = d.pop("mode")

        lan_network_id = d.pop("lanNetworkId", UNSET)

        voip_bridge_vlan = d.pop("voipBridgeVlan", UNSET)

        ip_type = d.pop("ipType", UNSET)

        ip = d.pop("ip", UNSET)

        ip_mask = d.pop("ipMask", UNSET)

        ip_gateway = d.pop("ipGateway", UNSET)

        ip_dns_1 = d.pop("ipDns1", UNSET)

        ip_dns_2 = d.pop("ipDns2", UNSET)

        ap_voip_vlan_setting_open_api_vo = cls(
            mode=mode,
            lan_network_id=lan_network_id,
            voip_bridge_vlan=voip_bridge_vlan,
            ip_type=ip_type,
            ip=ip,
            ip_mask=ip_mask,
            ip_gateway=ip_gateway,
            ip_dns_1=ip_dns_1,
            ip_dns_2=ip_dns_2,
        )

        ap_voip_vlan_setting_open_api_vo.additional_properties = d
        return ap_voip_vlan_setting_open_api_vo

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
