from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.osw_dhcp_server_range_open_api_vo import OswDhcpServerRangeOpenApiVO
    from ..models.switch_custom_dhcp_options import SwitchCustomDHCPOptions


T = TypeVar("T", bound="OswDhcpServerOpenApiVO")


@_attrs_define
class OswDhcpServerOpenApiVO:
    """Network DHCP server settings. Only valid when deviceType is 2 and mode is 1.

    Attributes:
        leasetime (int): Lease time should be within the range of 2–2880
        ip (str | Unset): DHCP Server IP, like 192.168.0.1.
        netmask (str | Unset): Parameter [netmask] should be within the range of 1-31
        ip_range_pool (list[OswDhcpServerRangeOpenApiVO] | Unset): The list of DHCP Range
        pri_dns (str | Unset): Primary DNS, like 192.0.0.1
        snd_dns (str | Unset): Second DNS, like 8.8.8.8
        gateway (str | Unset): Gateway IP, like 192.168.0.1
        option138 (str | Unset): option138 ip, like 192.168.0.1
        dhcp_pool_mask (int | Unset): DHCP pool mask, value is from 1 to 31.
        options (list[SwitchCustomDHCPOptions] | Unset): Custom DHCP options.
        vrf_id (str | Unset): VRF ID
    """

    leasetime: int
    ip: str | Unset = UNSET
    netmask: str | Unset = UNSET
    ip_range_pool: list[OswDhcpServerRangeOpenApiVO] | Unset = UNSET
    pri_dns: str | Unset = UNSET
    snd_dns: str | Unset = UNSET
    gateway: str | Unset = UNSET
    option138: str | Unset = UNSET
    dhcp_pool_mask: int | Unset = UNSET
    options: list[SwitchCustomDHCPOptions] | Unset = UNSET
    vrf_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        leasetime = self.leasetime

        ip = self.ip

        netmask = self.netmask

        ip_range_pool: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ip_range_pool, Unset):
            ip_range_pool = []
            for ip_range_pool_item_data in self.ip_range_pool:
                ip_range_pool_item = ip_range_pool_item_data.to_dict()
                ip_range_pool.append(ip_range_pool_item)

        pri_dns = self.pri_dns

        snd_dns = self.snd_dns

        gateway = self.gateway

        option138 = self.option138

        dhcp_pool_mask = self.dhcp_pool_mask

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        vrf_id = self.vrf_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "leasetime": leasetime,
            }
        )
        if ip is not UNSET:
            field_dict["ip"] = ip
        if netmask is not UNSET:
            field_dict["netmask"] = netmask
        if ip_range_pool is not UNSET:
            field_dict["ipRangePool"] = ip_range_pool
        if pri_dns is not UNSET:
            field_dict["priDns"] = pri_dns
        if snd_dns is not UNSET:
            field_dict["sndDns"] = snd_dns
        if gateway is not UNSET:
            field_dict["gateway"] = gateway
        if option138 is not UNSET:
            field_dict["option138"] = option138
        if dhcp_pool_mask is not UNSET:
            field_dict["dhcpPoolMask"] = dhcp_pool_mask
        if options is not UNSET:
            field_dict["options"] = options
        if vrf_id is not UNSET:
            field_dict["vrfId"] = vrf_id

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.osw_dhcp_server_range_open_api_vo import (
            OswDhcpServerRangeOpenApiVO,
        )
        from ..models.switch_custom_dhcp_options import (
            SwitchCustomDHCPOptions,
        )

        d = dict(src_dict)
        leasetime = d.pop("leasetime")

        ip = d.pop("ip", UNSET)

        netmask = d.pop("netmask", UNSET)

        _ip_range_pool = d.pop("ipRangePool", UNSET)
        ip_range_pool: list[OswDhcpServerRangeOpenApiVO] | Unset = UNSET
        if _ip_range_pool is not UNSET:
            ip_range_pool = []
            for ip_range_pool_item_data in _ip_range_pool:
                ip_range_pool_item = OswDhcpServerRangeOpenApiVO.from_dict(
                    ip_range_pool_item_data
                )

                ip_range_pool.append(ip_range_pool_item)

        pri_dns = d.pop("priDns", UNSET)

        snd_dns = d.pop("sndDns", UNSET)

        gateway = d.pop("gateway", UNSET)

        option138 = d.pop("option138", UNSET)

        dhcp_pool_mask = d.pop("dhcpPoolMask", UNSET)

        _options = d.pop("options", UNSET)
        options: list[SwitchCustomDHCPOptions] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = SwitchCustomDHCPOptions.from_dict(options_item_data)

                options.append(options_item)

        vrf_id = d.pop("vrfId", UNSET)

        osw_dhcp_server_open_api_vo = cls(
            leasetime=leasetime,
            ip=ip,
            netmask=netmask,
            ip_range_pool=ip_range_pool,
            pri_dns=pri_dns,
            snd_dns=snd_dns,
            gateway=gateway,
            option138=option138,
            dhcp_pool_mask=dhcp_pool_mask,
            options=options,
            vrf_id=vrf_id,
        )

        osw_dhcp_server_open_api_vo.additional_properties = d
        return osw_dhcp_server_open_api_vo

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
