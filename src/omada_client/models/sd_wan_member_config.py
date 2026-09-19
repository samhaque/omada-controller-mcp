from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lan_network_brief import LanNetworkBrief
    from ..models.osg_port_stat_brief import OsgPortStatBrief


T = TypeVar("T", bound="SdWanMemberConfig")


@_attrs_define
class SdWanMemberConfig:
    """A list of members of the SD-WAN group

    Attributes:
        role (int): The role of sdWan member, hub or spoke.
        device_mac (str): The device MAC of the sdWan member.
        site_id (str): The ID of the site where the sdWan member is located.
        site_name (str | Unset): The name of the site where the sdWan member is located.
        wan_ports_info (list[OsgPortStatBrief] | Unset): A list of device port status info for SdWan Member.
        lan_network_info (list[LanNetworkBrief] | Unset): A list of lan network info for SdWan Member.
        public_ip (bool | Unset): Whether the sdWan member has a public IP.
    """

    role: int
    device_mac: str
    site_id: str
    site_name: str | Unset = UNSET
    wan_ports_info: list[OsgPortStatBrief] | Unset = UNSET
    lan_network_info: list[LanNetworkBrief] | Unset = UNSET
    public_ip: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        device_mac = self.device_mac

        site_id = self.site_id

        site_name = self.site_name

        wan_ports_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wan_ports_info, Unset):
            wan_ports_info = []
            for wan_ports_info_item_data in self.wan_ports_info:
                wan_ports_info_item = wan_ports_info_item_data.to_dict()
                wan_ports_info.append(wan_ports_info_item)

        lan_network_info: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lan_network_info, Unset):
            lan_network_info = []
            for lan_network_info_item_data in self.lan_network_info:
                lan_network_info_item = lan_network_info_item_data.to_dict()
                lan_network_info.append(lan_network_info_item)

        public_ip = self.public_ip

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "deviceMac": device_mac,
                "siteId": site_id,
            }
        )
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if wan_ports_info is not UNSET:
            field_dict["wanPortsInfo"] = wan_ports_info
        if lan_network_info is not UNSET:
            field_dict["lanNetworkInfo"] = lan_network_info
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_brief import LanNetworkBrief
        from ..models.osg_port_stat_brief import OsgPortStatBrief

        d = dict(src_dict)
        role = d.pop("role")

        device_mac = d.pop("deviceMac")

        site_id = d.pop("siteId")

        site_name = d.pop("siteName", UNSET)

        _wan_ports_info = d.pop("wanPortsInfo", UNSET)
        wan_ports_info: list[OsgPortStatBrief] | Unset = UNSET
        if _wan_ports_info is not UNSET:
            wan_ports_info = []
            for wan_ports_info_item_data in _wan_ports_info:
                wan_ports_info_item = OsgPortStatBrief.from_dict(
                    wan_ports_info_item_data
                )

                wan_ports_info.append(wan_ports_info_item)

        _lan_network_info = d.pop("lanNetworkInfo", UNSET)
        lan_network_info: list[LanNetworkBrief] | Unset = UNSET
        if _lan_network_info is not UNSET:
            lan_network_info = []
            for lan_network_info_item_data in _lan_network_info:
                lan_network_info_item = LanNetworkBrief.from_dict(
                    lan_network_info_item_data
                )

                lan_network_info.append(lan_network_info_item)

        public_ip = d.pop("publicIp", UNSET)

        sd_wan_member_config = cls(
            role=role,
            device_mac=device_mac,
            site_id=site_id,
            site_name=site_name,
            wan_ports_info=wan_ports_info,
            lan_network_info=lan_network_info,
            public_ip=public_ip,
        )

        sd_wan_member_config.additional_properties = d
        return sd_wan_member_config

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
