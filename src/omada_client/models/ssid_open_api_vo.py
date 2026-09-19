from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SsidOpenApiVO")


@_attrs_define
class SsidOpenApiVO:
    """
    Attributes:
        ssid_id (str | Unset): SSID ID, kept for backward compatibility and equivalent to id. This field will be removed
            in a future release; use id instead.
        id (str | Unset): SSID ID
        name (str | Unset): SSID name. It should contain 1 to 32 UTF-8 characters.
        description (bool | Unset): SSID Enable status.
        choose_devices (int | Unset):
        band (int | Unset): SSID band. The lowest bit indicates whether 2.4G is included; the second lowest bit
            indicates whether 5G is included; the third lowest bit indicates whether 6G is included; 1 means included while
            0 means not included. For example, 7(111) means that 2G/5G/6G are enabled; 1(001) means that 2G is enabled.
            (When 5G is included，it means 5G/5G1/5G2 are enabled.)
        guest_net_enable (bool | Unset): SSID guest network config status. True: enable, false: disable.
        security (int | Unset): SSID security mode; Security should be a value as follows: 0: None; 2: WPA-Enterprise;
            3: WPA-Personal; 4: PPSK without RADIUS; 5: PPSK with RADIUS.
        broadcast (bool | Unset): SSID broadcast config status. True: enable, false: disable.
        vlan_enable (bool | Unset): SSID VLAN config status. True: enable, false: disable.
        vlan_id (int | Unset): SSID VLAN ID. This field is required when Parameter [vlanEnable] is true; It should be
            within the range of 1–4094.
        vlan_pool_ids (str | Unset): SSID VLAN POOL IDs. This field is required when Parameter [vlanEnable] is true; The
            numbers contain in it should be within the range of 1–4094.
    """

    ssid_id: str | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: bool | Unset = UNSET
    choose_devices: int | Unset = UNSET
    band: int | Unset = UNSET
    guest_net_enable: bool | Unset = UNSET
    security: int | Unset = UNSET
    broadcast: bool | Unset = UNSET
    vlan_enable: bool | Unset = UNSET
    vlan_id: int | Unset = UNSET
    vlan_pool_ids: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ssid_id = self.ssid_id

        id = self.id

        name = self.name

        description = self.description

        choose_devices = self.choose_devices

        band = self.band

        guest_net_enable = self.guest_net_enable

        security = self.security

        broadcast = self.broadcast

        vlan_enable = self.vlan_enable

        vlan_id = self.vlan_id

        vlan_pool_ids = self.vlan_pool_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ssid_id is not UNSET:
            field_dict["ssidId"] = ssid_id
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if choose_devices is not UNSET:
            field_dict["chooseDevices"] = choose_devices
        if band is not UNSET:
            field_dict["band"] = band
        if guest_net_enable is not UNSET:
            field_dict["guestNetEnable"] = guest_net_enable
        if security is not UNSET:
            field_dict["security"] = security
        if broadcast is not UNSET:
            field_dict["broadcast"] = broadcast
        if vlan_enable is not UNSET:
            field_dict["vlanEnable"] = vlan_enable
        if vlan_id is not UNSET:
            field_dict["vlanId"] = vlan_id
        if vlan_pool_ids is not UNSET:
            field_dict["vlanPoolIds"] = vlan_pool_ids

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ssid_id = d.pop("ssidId", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        choose_devices = d.pop("chooseDevices", UNSET)

        band = d.pop("band", UNSET)

        guest_net_enable = d.pop("guestNetEnable", UNSET)

        security = d.pop("security", UNSET)

        broadcast = d.pop("broadcast", UNSET)

        vlan_enable = d.pop("vlanEnable", UNSET)

        vlan_id = d.pop("vlanId", UNSET)

        vlan_pool_ids = d.pop("vlanPoolIds", UNSET)

        ssid_open_api_vo = cls(
            ssid_id=ssid_id,
            id=id,
            name=name,
            description=description,
            choose_devices=choose_devices,
            band=band,
            guest_net_enable=guest_net_enable,
            security=security,
            broadcast=broadcast,
            vlan_enable=vlan_enable,
            vlan_id=vlan_id,
            vlan_pool_ids=vlan_pool_ids,
        )

        ssid_open_api_vo.additional_properties = d
        return ssid_open_api_vo

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
