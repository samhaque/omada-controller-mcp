from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_dhcp_options import CustomDHCPOptions


T = TypeVar("T", bound="VirtualWanIpv4DhcpOpenApiVO")


@_attrs_define
class VirtualWanIpv4DhcpOpenApiVO:
    """VirtualWanIpv4DhcpOpenApiVO

    Attributes:
        mtu (int): Parameter [mtu] should be a value between 576 and 1500.
        unicast (str | Unset): Subnet mask of virtual WAN.
        dns1 (str | Unset): Primary DNS server.
        dns2 (str | Unset): Secondary DNS server.
        hostname (str | Unset): Host name. Parameter [hostname] should be up to 63 characters long and can only use
            numbers, letters, and hyphen.
        dhcp_options (list[CustomDHCPOptions] | Unset): Virtual WAN custom DHCP options.
    """

    mtu: int
    unicast: str | Unset = UNSET
    dns1: str | Unset = UNSET
    dns2: str | Unset = UNSET
    hostname: str | Unset = UNSET
    dhcp_options: list[CustomDHCPOptions] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mtu = self.mtu

        unicast = self.unicast

        dns1 = self.dns1

        dns2 = self.dns2

        hostname = self.hostname

        dhcp_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dhcp_options, Unset):
            dhcp_options = []
            for dhcp_options_item_data in self.dhcp_options:
                dhcp_options_item = dhcp_options_item_data.to_dict()
                dhcp_options.append(dhcp_options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mtu": mtu,
            }
        )
        if unicast is not UNSET:
            field_dict["unicast"] = unicast
        if dns1 is not UNSET:
            field_dict["dns1"] = dns1
        if dns2 is not UNSET:
            field_dict["dns2"] = dns2
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if dhcp_options is not UNSET:
            field_dict["dhcpOptions"] = dhcp_options

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.custom_dhcp_options import CustomDHCPOptions

        d = dict(src_dict)
        mtu = d.pop("mtu")

        unicast = d.pop("unicast", UNSET)

        dns1 = d.pop("dns1", UNSET)

        dns2 = d.pop("dns2", UNSET)

        hostname = d.pop("hostname", UNSET)

        _dhcp_options = d.pop("dhcpOptions", UNSET)
        dhcp_options: list[CustomDHCPOptions] | Unset = UNSET
        if _dhcp_options is not UNSET:
            dhcp_options = []
            for dhcp_options_item_data in _dhcp_options:
                dhcp_options_item = CustomDHCPOptions.from_dict(dhcp_options_item_data)

                dhcp_options.append(dhcp_options_item)

        virtual_wan_ipv_4_dhcp_open_api_vo = cls(
            mtu=mtu,
            unicast=unicast,
            dns1=dns1,
            dns2=dns2,
            hostname=hostname,
            dhcp_options=dhcp_options,
        )

        virtual_wan_ipv_4_dhcp_open_api_vo.additional_properties = d
        return virtual_wan_ipv_4_dhcp_open_api_vo

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
