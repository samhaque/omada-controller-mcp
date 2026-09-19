from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dhcp_options import CustomDHCPOptions
    from ..models.dhcp_range_open_api_vo import DhcpRangeOpenApiVO


T = TypeVar("T", bound="DhcpSettingsTemplateOpenApiVO")


@_attrs_define
class DhcpSettingsTemplateOpenApiVO:
    """Configure DHCP settings

    Attributes:
        enable (bool | Unset): When value is true, DHCP server is enabled
        ip_range_pool (list[DhcpRangeOpenApiVO] | Unset): The list of DHCP Range, which size can't be more than
            "dhcpRangePoolSize", "dhcpRangePoolSize" can be obtained from 'Get LAN network template list' interface.
        ip_range_start (int | Unset): The specific format value of Gateway Subnet start IP
        ip_range_end (int | Unset): The specific format value of Gateway Subnet End IP
        dhcpns (str | Unset): Setup DHCP server: "auto" or "manual"
        pri_dns (str | Unset): When DHCPs are "manual", primary DNS Server.
        snd_dns (str | Unset): When DHCPs are "manual", second DNS Server.
        leasetime (int | Unset): Leasetime should be within the range of 2-10080
        gateway (str | Unset): Manual Setup of DHCP Gateway IP
        dhcp_next_server (str | Unset): The dhcpNextServer should be valid IP address, which is used in optional set
            next DHCP server.
        dhcp_pool_mask (int | Unset):
        options (list[CustomDHCPOptions] | Unset): User custom DHCP options
    """

    enable: bool | Unset = UNSET
    ip_range_pool: list[DhcpRangeOpenApiVO] | Unset = UNSET
    ip_range_start: int | Unset = UNSET
    ip_range_end: int | Unset = UNSET
    dhcpns: str | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    leasetime: int | Unset = UNSET
    gateway: str | Unset = UNSET
    dhcp_next_server: str | Unset = UNSET
    dhcp_pool_mask: int | Unset = UNSET
    options: list[CustomDHCPOptions] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        ip_range_pool: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip_range_pool, Unset):
            ip_range_pool = []
            for ip_range_pool_item_data in self.ip_range_pool:
                ip_range_pool_item = ip_range_pool_item_data.to_dict()
                ip_range_pool.append(ip_range_pool_item)

        ip_range_start = self.ip_range_start

        ip_range_end = self.ip_range_end

        dhcpns = self.dhcpns

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        leasetime = self.leasetime

        gateway = self.gateway

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
        if ip_range_pool is not UNSET:
            field_dict["ipRangePool"] = ip_range_pool
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
        from ..models.dhcp_range_open_api_vo import DhcpRangeOpenApiVO

        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        _ip_range_pool = d.pop("ipRangePool", UNSET)
        ip_range_pool: list[DhcpRangeOpenApiVO] | Unset = UNSET
        if _ip_range_pool is not UNSET:
            ip_range_pool = []
            for ip_range_pool_item_data in _ip_range_pool:
                ip_range_pool_item = DhcpRangeOpenApiVO.from_dict(
                    ip_range_pool_item_data
                )

                ip_range_pool.append(ip_range_pool_item)

        ip_range_start = d.pop("ipRangeStart", UNSET)

        ip_range_end = d.pop("ipRangeEnd", UNSET)

        dhcpns = d.pop("dhcpns", UNSET)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        leasetime = d.pop("leasetime", UNSET)

        gateway = d.pop("gateway", UNSET)

        dhcp_next_server = d.pop("dhcpNextServer", UNSET)

        dhcp_pool_mask = d.pop("dhcpPoolMask", UNSET)

        _options = d.pop("options", UNSET)
        options: list[CustomDHCPOptions] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = CustomDHCPOptions.from_dict(options_item_data)

                options.append(options_item)

        dhcp_settings_template_open_api_vo = cls(
            enable=enable,
            ip_range_pool=ip_range_pool,
            ip_range_start=ip_range_start,
            ip_range_end=ip_range_end,
            dhcpns=dhcpns,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            leasetime=leasetime,
            gateway=gateway,
            dhcp_next_server=dhcp_next_server,
            dhcp_pool_mask=dhcp_pool_mask,
            options=options,
        )

        dhcp_settings_template_open_api_vo.additional_properties = d
        return dhcp_settings_template_open_api_vo

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
