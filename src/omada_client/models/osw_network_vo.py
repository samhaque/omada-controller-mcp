from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_dhcp_relay_vo import OswDhcpRelayVO
    from ..models.osw_dhcp_server_vo import OswDhcpServerVO
    from ..models.osw_ip_setting_vo import OswIpSettingVO
    from ..models.osw_ipv_6_setting_vo import OswIpv6SettingVO


T = TypeVar("T", bound="OswNetworkVO")


@_attrs_define
class OswNetworkVO:
    """VLAN Interface.

    Attributes:
        mode (int): DHCP mode. 0: None, mode 1: DHCP Server, mode 2: DHCP Relay.
        id (str | Unset): Network ID
        mvlan (bool | Unset): Indicate the vlan is management vlan or not.
        name (str | Unset): Switch network name.
        vlan (int | Unset): VLAN ID.
        status (int | Unset): Enable status of the network vlan. 0: disable; 1: enable.
        ip (OswIpSettingVO | Unset): Network IP setting.
        ipv_6_enable (bool | Unset): Enable IPV6 or not.
        ipv6 (OswIpv6SettingVO | Unset): Network IPV6 setting.
        dhcp_server (OswDhcpServerVO | Unset): Network DHCP server settings.
        dhcp_relay (OswDhcpRelayVO | Unset): Network DHCP relay settings.
        vrf_id (str | Unset): VRF ID
        mtu (int | Unset): MTU, MTU value should be less than or equal to the jumbo value.
    """

    mode: int
    id: str | Unset = UNSET
    mvlan: bool | Unset = UNSET
    name: str | Unset = UNSET
    vlan: int | Unset = UNSET
    status: int | Unset = UNSET
    ip: OswIpSettingVO | Unset = UNSET
    ipv_6_enable: bool | Unset = UNSET
    ipv6: OswIpv6SettingVO | Unset = UNSET
    dhcp_server: OswDhcpServerVO | Unset = UNSET
    dhcp_relay: OswDhcpRelayVO | Unset = UNSET
    vrf_id: str | Unset = UNSET
    mtu: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        id = self.id

        mvlan = self.mvlan

        name = self.name

        vlan = self.vlan

        status = self.status

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
                "mode": mode,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if mvlan is not UNSET:
            field_dict["mvlan"] = mvlan
        if name is not UNSET:
            field_dict["name"] = name
        if vlan is not UNSET:
            field_dict["vlan"] = vlan
        if status is not UNSET:
            field_dict["status"] = status
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
        from ..models.osw_dhcp_relay_vo import OswDhcpRelayVO
        from ..models.osw_dhcp_server_vo import OswDhcpServerVO
        from ..models.osw_ip_setting_vo import OswIpSettingVO
        from ..models.osw_ipv_6_setting_vo import OswIpv6SettingVO

        d = dict(src_dict)
        mode = d.pop("mode")

        id = d.pop("id", UNSET)

        mvlan = d.pop("mvlan", UNSET)

        name = d.pop("name", UNSET)

        vlan = d.pop("vlan", UNSET)

        status = d.pop("status", UNSET)

        _ip = d.pop("ip", UNSET)
        ip: OswIpSettingVO | Unset
        if isinstance(_ip, Unset):
            ip = UNSET
        else:
            ip = OswIpSettingVO.from_dict(_ip)

        ipv_6_enable = d.pop("ipv6Enable", UNSET)

        _ipv6 = d.pop("ipv6", UNSET)
        ipv6: OswIpv6SettingVO | Unset
        if isinstance(_ipv6, Unset):
            ipv6 = UNSET
        else:
            ipv6 = OswIpv6SettingVO.from_dict(_ipv6)

        _dhcp_server = d.pop("dhcpServer", UNSET)
        dhcp_server: OswDhcpServerVO | Unset
        if isinstance(_dhcp_server, Unset):
            dhcp_server = UNSET
        else:
            dhcp_server = OswDhcpServerVO.from_dict(_dhcp_server)

        _dhcp_relay = d.pop("dhcpRelay", UNSET)
        dhcp_relay: OswDhcpRelayVO | Unset
        if isinstance(_dhcp_relay, Unset):
            dhcp_relay = UNSET
        else:
            dhcp_relay = OswDhcpRelayVO.from_dict(_dhcp_relay)

        vrf_id = d.pop("vrfId", UNSET)

        mtu = d.pop("mtu", UNSET)

        osw_network_vo = cls(
            mode=mode,
            id=id,
            mvlan=mvlan,
            name=name,
            vlan=vlan,
            status=status,
            ip=ip,
            ipv_6_enable=ipv_6_enable,
            ipv6=ipv6,
            dhcp_server=dhcp_server,
            dhcp_relay=dhcp_relay,
            vrf_id=vrf_id,
            mtu=mtu,
        )

        osw_network_vo.additional_properties = d
        return osw_network_vo

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
