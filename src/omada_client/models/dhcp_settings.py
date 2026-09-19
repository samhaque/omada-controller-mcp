from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dhcp_options import CustomDHCPOptions


T = TypeVar("T", bound="DhcpSettings")


@_attrs_define
class DhcpSettings:
    """Configure DHCP settings

    Attributes:
        enable (bool | Unset): When value is true, DHCP server is enabled
        ipaddr_start (str | Unset): DHCP Range Start IP. Must use ipRangePool field If want to configure multiple DHCP
            Ranges.
        ipaddr_end (str | Unset): DHCP Range End IP. Must use ipRangePool field If want to configure multiple DHCP
            Ranges.
        ip_range_start (int | Unset): The specific format value of Gateway Subnet start IP
        ip_range_end (int | Unset): The specific format value of Gateway Subnet End IP
        dhcpns (str | Unset): Setup DHCP server: "auto" or "manual"
        pri_dns (str | Unset): When DHCPs are "manual", primary DNS Server.
        snd_dns (str | Unset): When DHCPs are "manual", second DNS Server.
        leasetime (int | Unset): Valid value is from 2 to 2880
        gateway (str | Unset): Manual Setup of DHCP Gateway IP
        host_ip (str | Unset): DHCP Omada Controller IP
        option60 (str | Unset): Option60 should be between 0 and 50, which is used to optionally identify the vendor
            type and configuration of a DHCP client.
        option66 (str | Unset): The Option66 should be between 0 and 128, which specifies the TFTP server information
            and supports a single TFTP server IP address.
        option138 (str | Unset): The option138 should be valid IP address, which is used in discovering the devices by
            the Omada controller.
        dhcp_next_server (str | Unset): The dhcpNextServer should be valid IP address, which is used in optional set
            next DHCP server.
        dhcp_pool_mask (int | Unset):
        options (list[CustomDHCPOptions] | Unset): User custom DHCP options
    """

    enable: bool | Unset = UNSET
    ipaddr_start: str | Unset = UNSET
    ipaddr_end: str | Unset = UNSET
    ip_range_start: int | Unset = UNSET
    ip_range_end: int | Unset = UNSET
    dhcpns: str | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    leasetime: int | Unset = UNSET
    gateway: str | Unset = UNSET
    host_ip: str | Unset = UNSET
    option60: str | Unset = UNSET
    option66: str | Unset = UNSET
    option138: str | Unset = UNSET
    dhcp_next_server: str | Unset = UNSET
    dhcp_pool_mask: int | Unset = UNSET
    options: list[CustomDHCPOptions] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        ipaddr_start = self.ipaddr_start

        ipaddr_end = self.ipaddr_end

        ip_range_start = self.ip_range_start

        ip_range_end = self.ip_range_end

        dhcpns = self.dhcpns

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        leasetime = self.leasetime

        gateway = self.gateway

        host_ip = self.host_ip

        option60 = self.option60

        option66 = self.option66

        option138 = self.option138

        dhcp_next_server = self.dhcp_next_server

        dhcp_pool_mask = self.dhcp_pool_mask

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["enable"] = enable
        if ipaddr_start is not UNSET:
            field_dict["ipaddrStart"] = ipaddr_start
        if ipaddr_end is not UNSET:
            field_dict["ipaddrEnd"] = ipaddr_end
        if ip_range_start is not UNSET:
            field_dict["ipRangeStart"] = ip_range_start
        if ip_range_end is not UNSET:
            field_dict["ipRangeEnd"] = ip_range_end
        if dhcpns is not UNSET:
            field_dict["dhcpns"] = dhcpns
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns
        if leasetime is not UNSET:
            field_dict["leasetime"] = leasetime
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if host_ip is not UNSET:
            field_dict["hostIP"] = host_ip
        if option60 is not UNSET:
            field_dict["option60"] = option60
        if option66 is not UNSET:
            field_dict["option66"] = option66
        if option138 is not UNSET:
            field_dict["option138"] = option138
        if dhcp_next_server is not UNSET:
            field_dict["dhcpNextServer"] = dhcp_next_server
        if dhcp_pool_mask is not UNSET:
            field_dict["dhcpPoolMask"] = dhcp_pool_mask
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_dhcp_options import CustomDHCPOptions

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        ipaddr_start = d.pop("ipaddrStart", UNSET)

        ipaddr_end = d.pop("ipaddrEnd", UNSET)

        ip_range_start = d.pop("ipRangeStart", UNSET)

        ip_range_end = d.pop("ipRangeEnd", UNSET)

        dhcpns = d.pop("dhcpns", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        leasetime = d.pop("leasetime", UNSET)

        gateway = d.pop("gateway", UNSET)

        host_ip = d.pop("hostIP", UNSET)

        option60 = d.pop("option60", UNSET)

        option66 = d.pop("option66", UNSET)

        option138 = d.pop("option138", UNSET)

        dhcp_next_server = d.pop("dhcpNextServer", UNSET)

        dhcp_pool_mask = d.pop("dhcpPoolMask", UNSET)

        _options = d.pop("options", UNSET)
        options: list[CustomDHCPOptions] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CustomDHCPOptions.from_dict(options_item_data)

                options.append(options_item)

        dhcp_settings = cls(
            enable=enable,
            ipaddr_start=ipaddr_start,
            ipaddr_end=ipaddr_end,
            ip_range_start=ip_range_start,
            ip_range_end=ip_range_end,
            dhcpns=dhcpns,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            leasetime=leasetime,
            gateway=gateway,
            host_ip=host_ip,
            option60=option60,
            option66=option66,
            option138=option138,
            dhcp_next_server=dhcp_next_server,
            dhcp_pool_mask=dhcp_pool_mask,
            options=options,
        )

        dhcp_settings.additional_properties = d
        return dhcp_settings

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
