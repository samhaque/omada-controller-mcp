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


T = TypeVar("T", bound="SdWanMemberInfo")


@_attrs_define
class SdWanMemberInfo:
    """A list of members of the SD-WAN group

    Attributes:
        role (int | Unset): The role of sdWan member, hub or spoke.
        device_mac (str | Unset): The device MAC of the sdWan member.
        device_name (str | Unset): The device name of the sdWan member.
        online_status (int | Unset): The device online status of the sdWan member.
        type_ (str | Unset): The device type of the sdWan member.
        model (str | Unset): The device model of the sdWan member.
        model_version (str | Unset): The device model version of the sdWan member.
        show_model (str | Unset): The device showmodel of the sdWan member.
        site_id (str | Unset): The ID of the site where the sdWan member is located.
        site_name (str | Unset): The name of the site where the sdWan member is located.
        region (str | Unset): The region where the site is located.
        longitude (float | Unset): The map longitude of the site.
        latitude (float | Unset): The map latitude of the site.
        region_longitude (float | Unset): The region longitude of the site.
        region_latitude (float | Unset): The region latitude of the site.
        unplaced (bool | Unset): Whether the site is placed on the map.
        address (str | Unset): The address where the site is located.
        wan_ports_info (list[OsgPortStatBrief] | Unset): A list of device port status info for SdWan Member.
        lan_network_info (list[LanNetworkBrief] | Unset): A list of lan network info for SdWan Member.
        public_ip (bool | Unset): Whether the sdWan member has a public IP.
        sd_wan_ip (str | Unset): The sdWan IP of the sdWan member.
        linked_to_hub (int | Unset): If a member is a spoke, the link connection to the hub is identified.
        support_sd_wan_nat (bool | Unset): Whether the device support SD-WAN NAT.
    """

    role: int | Unset = UNSET
    device_mac: str | Unset = UNSET
    device_name: str | Unset = UNSET
    online_status: int | Unset = UNSET
    type_: str | Unset = UNSET
    model: str | Unset = UNSET
    model_version: str | Unset = UNSET
    show_model: str | Unset = UNSET
    site_id: str | Unset = UNSET
    site_name: str | Unset = UNSET
    region: str | Unset = UNSET
    longitude: float | Unset = UNSET
    latitude: float | Unset = UNSET
    region_longitude: float | Unset = UNSET
    region_latitude: float | Unset = UNSET
    unplaced: bool | Unset = UNSET
    address: str | Unset = UNSET
    wan_ports_info: list[OsgPortStatBrief] | Unset = UNSET
    lan_network_info: list[LanNetworkBrief] | Unset = UNSET
    public_ip: bool | Unset = UNSET
    sd_wan_ip: str | Unset = UNSET
    linked_to_hub: int | Unset = UNSET
    support_sd_wan_nat: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        role = self.role

        device_mac = self.device_mac

        device_name = self.device_name

        online_status = self.online_status

        type_ = self.type_

        model = self.model

        model_version = self.model_version

        show_model = self.show_model

        site_id = self.site_id

        site_name = self.site_name

        region = self.region

        longitude = self.longitude

        latitude = self.latitude

        region_longitude = self.region_longitude

        region_latitude = self.region_latitude

        unplaced = self.unplaced

        address = self.address

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

        sd_wan_ip = self.sd_wan_ip

        linked_to_hub = self.linked_to_hub

        support_sd_wan_nat = self.support_sd_wan_nat

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role
        if device_mac is not UNSET:
            field_dict["deviceMac"] = device_mac
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if online_status is not UNSET:
            field_dict["onlineStatus"] = online_status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if model is not UNSET:
            field_dict["model"] = model
        if model_version is not UNSET:
            field_dict["modelVersion"] = model_version
        if show_model is not UNSET:
            field_dict["showModel"] = show_model
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site_name is not UNSET:
            field_dict["siteName"] = site_name
        if region is not UNSET:
            field_dict["region"] = region
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if region_longitude is not UNSET:
            field_dict["regionLongitude"] = region_longitude
        if region_latitude is not UNSET:
            field_dict["regionLatitude"] = region_latitude
        if unplaced is not UNSET:
            field_dict["unplaced"] = unplaced
        if address is not UNSET:
            field_dict["address"] = address
        if wan_ports_info is not UNSET:
            field_dict["wanPortsInfo"] = wan_ports_info
        if lan_network_info is not UNSET:
            field_dict["lanNetworkInfo"] = lan_network_info
        if public_ip is not UNSET:
            field_dict["publicIp"] = public_ip
        if sd_wan_ip is not UNSET:
            field_dict["sdWanIp"] = sd_wan_ip
        if linked_to_hub is not UNSET:
            field_dict["linkedToHub"] = linked_to_hub
        if support_sd_wan_nat is not UNSET:
            field_dict["supportSdWanNat"] = support_sd_wan_nat

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.lan_network_brief import LanNetworkBrief
        from ..models.osg_port_stat_brief import OsgPortStatBrief

        d = dict(src_dict)
        role = d.pop("role", UNSET)

        device_mac = d.pop("deviceMac", UNSET)

        device_name = d.pop("deviceName", UNSET)

        online_status = d.pop("onlineStatus", UNSET)

        type_ = d.pop("type", UNSET)

        model = d.pop("model", UNSET)

        model_version = d.pop("modelVersion", UNSET)

        show_model = d.pop("showModel", UNSET)

        site_id = d.pop("siteId", UNSET)

        site_name = d.pop("siteName", UNSET)

        region = d.pop("region", UNSET)

        longitude = d.pop("longitude", UNSET)

        latitude = d.pop("latitude", UNSET)

        region_longitude = d.pop("regionLongitude", UNSET)

        region_latitude = d.pop("regionLatitude", UNSET)

        unplaced = d.pop("unplaced", UNSET)

        address = d.pop("address", UNSET)

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

        sd_wan_ip = d.pop("sdWanIp", UNSET)

        linked_to_hub = d.pop("linkedToHub", UNSET)

        support_sd_wan_nat = d.pop("supportSdWanNat", UNSET)

        sd_wan_member_info = cls(
            role=role,
            device_mac=device_mac,
            device_name=device_name,
            online_status=online_status,
            type_=type_,
            model=model,
            model_version=model_version,
            show_model=show_model,
            site_id=site_id,
            site_name=site_name,
            region=region,
            longitude=longitude,
            latitude=latitude,
            region_longitude=region_longitude,
            region_latitude=region_latitude,
            unplaced=unplaced,
            address=address,
            wan_ports_info=wan_ports_info,
            lan_network_info=lan_network_info,
            public_ip=public_ip,
            sd_wan_ip=sd_wan_ip,
            linked_to_hub=linked_to_hub,
            support_sd_wan_nat=support_sd_wan_nat,
        )

        sd_wan_member_info.additional_properties = d
        return sd_wan_member_info

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
