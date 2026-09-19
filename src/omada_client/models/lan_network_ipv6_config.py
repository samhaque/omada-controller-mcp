from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dhcpv_6_setting import Dhcpv6Setting
    from ..models.lan_network_proto_pass_through_mode import (
        LanNetworkProtoPassThroughMode,
    )
    from ..models.lan_network_proto_slaac_stateless_dhcp_mode_or_slaacrdnss_mode import (
        LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode,
    )
    from ..models.ra_setting import RaSetting


T = TypeVar("T", bound="LanNetworkIPV6Config")


@_attrs_define
class LanNetworkIPV6Config:
    """LAN network IPv6 config

    Attributes:
        proto (int): The IPv6 Connection Type of LAN port. Proto should be a value as follows:  0: "none" (Default); 1:
            "DHCPv6"; 2: "SLAAC+Stateless DHCP"; 3: "SLAAC+RDNSS"; 4: "passthrough"
        enable (int): IPv6 enable should be a value as follows: 0: Disable (Default); 1: Enable
        dhcpv6 (Dhcpv6Setting | Unset): Dhcpv6 Setting
        slaac (LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode | Unset): Lan network proto: SLAAC+Stateless DHCP
            mode or SLAAC+RDNSS mode
        rdnss (LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode | Unset): Lan network proto: SLAAC+Stateless DHCP
            mode or SLAAC+RDNSS mode
        passthrough (LanNetworkProtoPassThroughMode | Unset): Lan network proto: Pass-Through mode
        ra (RaSetting | Unset): Ra Setting
    """

    proto: int
    enable: int
    dhcpv6: Dhcpv6Setting | Unset = UNSET
    slaac: LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode | Unset = UNSET
    rdnss: LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode | Unset = UNSET
    passthrough: LanNetworkProtoPassThroughMode | Unset = UNSET
    ra: RaSetting | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proto = self.proto

        enable = self.enable

        dhcpv6: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dhcpv6, Unset):
            dhcpv6 = self.dhcpv6.to_dict()

        slaac: dict[str, Any] | Unset = UNSET
        if not isinstance(self.slaac, Unset):
            slaac = self.slaac.to_dict()

        rdnss: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rdnss, Unset):
            rdnss = self.rdnss.to_dict()

        passthrough: dict[str, Any] | Unset = UNSET
        if not isinstance(self.passthrough, Unset):
            passthrough = self.passthrough.to_dict()

        ra: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ra, Unset):
            ra = self.ra.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proto": proto,
                "enable": enable,
            }
        )
        if dhcpv6 is not UNSET:
            field_dict["dhcpv6"] = dhcpv6
        if slaac is not UNSET:
            field_dict["slaac"] = slaac
        if rdnss is not UNSET:
            field_dict["rdnss"] = rdnss
        if passthrough is not UNSET:
            field_dict["passthrough"] = passthrough
        if ra is not UNSET:
            field_dict["ra"] = ra

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.dhcpv_6_setting import Dhcpv6Setting
        from ..models.lan_network_proto_pass_through_mode import (
            LanNetworkProtoPassThroughMode,
        )
        from ..models.lan_network_proto_slaac_stateless_dhcp_mode_or_slaacrdnss_mode import (
            LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode,
        )
        from ..models.ra_setting import RaSetting

        d = dict(src_dict)
        proto = d.pop("proto")

        enable = d.pop("enable")

        _dhcpv6 = d.pop("dhcpv6", UNSET)
        dhcpv6: Dhcpv6Setting | Unset
        if isinstance(_dhcpv6, Unset):
            dhcpv6 = UNSET
        else:
            dhcpv6 = Dhcpv6Setting.from_dict(_dhcpv6)

        _slaac = d.pop("slaac", UNSET)
        slaac: LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode | Unset
        if isinstance(_slaac, Unset):
            slaac = UNSET
        else:
            slaac = LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode.from_dict(
                _slaac
            )

        _rdnss = d.pop("rdnss", UNSET)
        rdnss: LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode | Unset
        if isinstance(_rdnss, Unset):
            rdnss = UNSET
        else:
            rdnss = LanNetworkProtoSLAACStatelessDHCPModeOrSLAACRDNSSMode.from_dict(
                _rdnss
            )

        _passthrough = d.pop("passthrough", UNSET)
        passthrough: LanNetworkProtoPassThroughMode | Unset
        if isinstance(_passthrough, Unset):
            passthrough = UNSET
        else:
            passthrough = LanNetworkProtoPassThroughMode.from_dict(_passthrough)

        _ra = d.pop("ra", UNSET)
        ra: RaSetting | Unset
        if isinstance(_ra, Unset):
            ra = UNSET
        else:
            ra = RaSetting.from_dict(_ra)

        lan_network_ipv6_config = cls(
            proto=proto,
            enable=enable,
            dhcpv6=dhcpv6,
            slaac=slaac,
            rdnss=rdnss,
            passthrough=passthrough,
            ra=ra,
        )

        lan_network_ipv6_config.additional_properties = d
        return lan_network_ipv6_config

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
