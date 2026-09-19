from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcp_servers_setting import DhcpServersSetting
    from ..models.dhcpv_6_servers_setting import Dhcpv6ServersSetting


T = TypeVar("T", bound="CreateVLANs")


@_attrs_define
class CreateVLANs:
    """
    Attributes:
        name (str): LAN network name should contain 1 to 128 characters.
        vlans (str): Support batch VLAN creation. VLAN format: 200, 1-100.
        igmp_snoop_enable (bool): Enable IGMP snooping
        dhcp_l2_relay_enable (bool | Unset): The switch of DHCP L2 relay
        dhcp_guard (DhcpServersSetting | Unset): Legal DHCP Server
        mld_snoop_enable (bool | Unset): Enable MLD snooping
        dhcpv_6_guard (Dhcpv6ServersSetting | Unset): Legal DHCPv6 Server
        application (int | Unset): Effective device type should be a value as follows: 0: Gateway and Switch; 1: Switch
    """

    name: str
    vlans: str
    igmp_snoop_enable: bool
    dhcp_l2_relay_enable: bool | Unset = UNSET
    dhcp_guard: DhcpServersSetting | Unset = UNSET
    mld_snoop_enable: bool | Unset = UNSET
    dhcpv_6_guard: Dhcpv6ServersSetting | Unset = UNSET
    application: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        vlans = self.vlans

        igmp_snoop_enable = self.igmp_snoop_enable

        dhcp_l2_relay_enable = self.dhcp_l2_relay_enable

        dhcp_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcp_guard, Unset):
            dhcp_guard = self.dhcp_guard.to_dict()

        mld_snoop_enable = self.mld_snoop_enable

        dhcpv_6_guard: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcpv_6_guard, Unset):
            dhcpv_6_guard = self.dhcpv_6_guard.to_dict()

        application = self.application

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "vlans": vlans,
                "igmpSnoopEnable": igmp_snoop_enable,
            }
        )
        if dhcp_l2_relay_enable is not UNSET:
            field_dict["dhcpL2RelayEnable"] = dhcp_l2_relay_enable
        if dhcp_guard is not UNSET:
            field_dict["dhcpGuard"] = dhcp_guard
        if mld_snoop_enable is not UNSET:
            field_dict["mldSnoopEnable"] = mld_snoop_enable
        if dhcpv_6_guard is not UNSET:
            field_dict["dhcpv6Guard"] = dhcpv_6_guard
        if application is not UNSET:
            field_dict["application"] = application

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcp_servers_setting import DhcpServersSetting
        from ..models.dhcpv_6_servers_setting import (
            Dhcpv6ServersSetting,
        )

        d = dict(src_dict)
        name = d.pop("name")

        vlans = d.pop("vlans")

        igmp_snoop_enable = d.pop("igmpSnoopEnable")

        dhcp_l2_relay_enable = d.pop("dhcpL2RelayEnable", UNSET)

        _dhcp_guard = d.pop("dhcpGuard", UNSET)
        dhcp_guard: DhcpServersSetting | Unset
        if isinstance(_dhcp_guard, Unset):
            dhcp_guard = UNSET
        else:
            dhcp_guard = DhcpServersSetting.from_dict(_dhcp_guard)

        mld_snoop_enable = d.pop("mldSnoopEnable", UNSET)

        _dhcpv_6_guard = d.pop("dhcpv6Guard", UNSET)
        dhcpv_6_guard: Dhcpv6ServersSetting | Unset
        if isinstance(_dhcpv_6_guard, Unset):
            dhcpv_6_guard = UNSET
        else:
            dhcpv_6_guard = Dhcpv6ServersSetting.from_dict(_dhcpv_6_guard)

        application = d.pop("application", UNSET)

        create_vla_ns = cls(
            name=name,
            vlans=vlans,
            igmp_snoop_enable=igmp_snoop_enable,
            dhcp_l2_relay_enable=dhcp_l2_relay_enable,
            dhcp_guard=dhcp_guard,
            mld_snoop_enable=mld_snoop_enable,
            dhcpv_6_guard=dhcpv_6_guard,
            application=application,
        )

        create_vla_ns.additional_properties = d
        return create_vla_ns

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
