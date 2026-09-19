from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_dhcp_relay_open_api_vo import OswDhcpRelayOpenApiVO
    from ..models.osw_dhcp_server_open_api_vo import OswDhcpServerOpenApiVO
    from ..models.osw_ip_setting_open_api_vo import OswIpSettingOpenApiVO
    from ..models.osw_ipv_6_setting_open_api_vo import OswIpv6SettingOpenApiVO


T = TypeVar("T", bound="OswNetworkOpenApi")


@_attrs_define
class OswNetworkOpenApi:
    """
    Attributes:
        id (str): Network ID
        vlan (int): VLAN ID.
        mvlan (bool): Indicate the vlan is management vlan or not.
        mode (int): DHCP mode. 0: None, mode 1: DHCP Server, mode 2: DHCP Relay
        status (bool | Unset): Enable status of the network vlan. Note: this field only takes effect when toggling
            switch status on the Interface list page and is ignored by other switch network edit APIs.
        name (str | Unset): Switch network name.
        ip (OswIpSettingOpenApiVO | Unset): Network IP setting.
        ipv_6_enable (bool | Unset): Enable IPV6 or not.
        ipv6 (OswIpv6SettingOpenApiVO | Unset): Network IPV6 setting.
        dhcp_server (OswDhcpServerOpenApiVO | Unset): Network DHCP server settings. Only valid when deviceType is 2 and
            mode is 1.
        dhcp_relay (OswDhcpRelayOpenApiVO | Unset): Network DHCP relay settings. Only valid when deviceType is 2 and
            mode is 2
        vrf_id (str | Unset): VRF ID
        mtu (int | Unset): MTU, MTU value should be less than or equal to the jumbo value
    """

    id: str
    vlan: int
    mvlan: bool
    mode: int
    status: bool | Unset = UNSET
    name: str | Unset = UNSET
    ip: OswIpSettingOpenApiVO | Unset = UNSET
    ipv_6_enable: bool | Unset = UNSET
    ipv6: OswIpv6SettingOpenApiVO | Unset = UNSET
    dhcp_server: OswDhcpServerOpenApiVO | Unset = UNSET
    dhcp_relay: OswDhcpRelayOpenApiVO | Unset = UNSET
    vrf_id: str | Unset = UNSET
    mtu: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        vlan = self.vlan

        mvlan = self.mvlan

        mode = self.mode

        status = self.status

        name = self.name

        ip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip, Unset):
            ip = self.ip.to_dict()

        ipv_6_enable = self.ipv_6_enable

        ipv6: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ipv6, Unset):
            ipv6 = self.ipv6.to_dict()

        dhcp_server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_server, Unset):
            dhcp_server = self.dhcp_server.to_dict()

        dhcp_relay: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_relay, Unset):
            dhcp_relay = self.dhcp_relay.to_dict()

        vrf_id = self.vrf_id

        mtu = self.mtu

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "vlan": vlan,
                "mvlan": mvlan,
                "mode": mode,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if name is not UNSET:
            field_dict["name"] = name
        if ip is not UNSET:
            field_dict["ip"] = ip
        if ipv_6_enable is not UNSET:
            field_dict["ipv6Enable"] = ipv_6_enable
        if ipv6 is not UNSET:
            field_dict["ipv6"] = ipv6
        if dhcp_server is not UNSET:
            field_dict["dhcpServer"] = dhcp_server
        if dhcp_relay is not UNSET:
            field_dict["dhcpRelay"] = dhcp_relay
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id
        if mtu is not UNSET:
            field_dict["mtu"] = mtu

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_dhcp_relay_open_api_vo import (
            OswDhcpRelayOpenApiVO,
        )
        from ..models.osw_dhcp_server_open_api_vo import (
            OswDhcpServerOpenApiVO,
        )
        from ..models.osw_ip_setting_open_api_vo import (
            OswIpSettingOpenApiVO,
        )
        from ..models.osw_ipv_6_setting_open_api_vo import (
            OswIpv6SettingOpenApiVO,
        )

        d = dict(src_dict)
        id = d.pop("id")

        vlan = d.pop("vlan")

        mvlan = d.pop("mvlan")

        mode = d.pop("mode")

        status = d.pop("status", UNSET)

        name = d.pop("name", UNSET)

        _ip = d.pop("ip", UNSET)
        ip: OswIpSettingOpenApiVO | Unset
        if isinstance(_ip, Unset):
            ip = UNSET
        else:
            ip = OswIpSettingOpenApiVO.from_dict(_ip)

        ipv_6_enable = d.pop("ipv6Enable", UNSET)

        _ipv6 = d.pop("ipv6", UNSET)
        ipv6: OswIpv6SettingOpenApiVO | Unset
        if isinstance(_ipv6, Unset):
            ipv6 = UNSET
        else:
            ipv6 = OswIpv6SettingOpenApiVO.from_dict(_ipv6)

        _dhcp_server = d.pop("dhcpServer", UNSET)
        dhcp_server: OswDhcpServerOpenApiVO | Unset
        if isinstance(_dhcp_server, Unset):
            dhcp_server = UNSET
        else:
            dhcp_server = OswDhcpServerOpenApiVO.from_dict(_dhcp_server)

        _dhcp_relay = d.pop("dhcpRelay", UNSET)
        dhcp_relay: OswDhcpRelayOpenApiVO | Unset
        if isinstance(_dhcp_relay, Unset):
            dhcp_relay = UNSET
        else:
            dhcp_relay = OswDhcpRelayOpenApiVO.from_dict(_dhcp_relay)

        vrf_id = d.pop("vrfId", UNSET)

        mtu = d.pop("mtu", UNSET)

        osw_network_open_api = cls(
            id=id,
            vlan=vlan,
            mvlan=mvlan,
            mode=mode,
            status=status,
            name=name,
            ip=ip,
            ipv_6_enable=ipv_6_enable,
            ipv6=ipv6,
            dhcp_server=dhcp_server,
            dhcp_relay=dhcp_relay,
            vrf_id=vrf_id,
            mtu=mtu,
        )

        osw_network_open_api.additional_properties = d
        return osw_network_open_api

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
