from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_account_setting_vo import DeviceAccountSettingVO
    from ..models.health_stat_vo import HealthStatVO
    from ..models.site_setting_anomaly_stat_vo import SiteSettingAnomalyStatVO
    from ..models.wan_health_stat_vo import WanHealthStatVO


T = TypeVar("T", bound="SiteStatisticInfo")


@_attrs_define
class SiteStatisticInfo:
    """
    Attributes:
        id (str | Unset):
        gateway_status (int | Unset):
        pre_config_osg_num (int | Unset):
        pre_config_osw_num (int | Unset):
        pre_config_ap_num (int | Unset):
        pre_config_olt_num (int | Unset):
        lan (bool | Unset):
        wlan (bool | Unset):
        lan_device_connected_num (int | Unset):
        lan_device_disconnected_num (int | Unset):
        wlan_device_connected_num (int | Unset):
        wlan_device_disconnected_num (int | Unset):
        wlan_device_isolated_num (int | Unset):
        olt_device_connected_num (int | Unset):
        olt_device_disconnected_num (int | Unset):
        lan_user_num (int | Unset):
        wlan_user_num (int | Unset):
        lan_guest_num (int | Unset):
        wlan_guest_num (int | Unset):
        device_account (DeviceAccountSettingVO | Unset):
        wireless_upgrade (bool | Unset):
        wired_upgrade (bool | Unset):
        issue_event (SiteSettingAnomalyStatVO | Unset): Statistics of incidents for site.
        wan_health (WanHealthStatVO | Unset):
        wlan_health (int | Unset):
        gateway_health (int | Unset):
        switch_health (HealthStatVO | Unset):
        eap_health (HealthStatVO | Unset):
        wireless_client_health (HealthStatVO | Unset):
        wired_client_health (HealthStatVO | Unset):
    """

    id: str | Unset = UNSET
    gateway_status: int | Unset = UNSET
    pre_config_osg_num: int | Unset = UNSET
    pre_config_osw_num: int | Unset = UNSET
    pre_config_ap_num: int | Unset = UNSET
    pre_config_olt_num: int | Unset = UNSET
    lan: bool | Unset = UNSET
    wlan: bool | Unset = UNSET
    lan_device_connected_num: int | Unset = UNSET
    lan_device_disconnected_num: int | Unset = UNSET
    wlan_device_connected_num: int | Unset = UNSET
    wlan_device_disconnected_num: int | Unset = UNSET
    wlan_device_isolated_num: int | Unset = UNSET
    olt_device_connected_num: int | Unset = UNSET
    olt_device_disconnected_num: int | Unset = UNSET
    lan_user_num: int | Unset = UNSET
    wlan_user_num: int | Unset = UNSET
    lan_guest_num: int | Unset = UNSET
    wlan_guest_num: int | Unset = UNSET
    device_account: DeviceAccountSettingVO | Unset = UNSET
    wireless_upgrade: bool | Unset = UNSET
    wired_upgrade: bool | Unset = UNSET
    issue_event: SiteSettingAnomalyStatVO | Unset = UNSET
    wan_health: WanHealthStatVO | Unset = UNSET
    wlan_health: int | Unset = UNSET
    gateway_health: int | Unset = UNSET
    switch_health: HealthStatVO | Unset = UNSET
    eap_health: HealthStatVO | Unset = UNSET
    wireless_client_health: HealthStatVO | Unset = UNSET
    wired_client_health: HealthStatVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        gateway_status = self.gateway_status

        pre_config_osg_num = self.pre_config_osg_num

        pre_config_osw_num = self.pre_config_osw_num

        pre_config_ap_num = self.pre_config_ap_num

        pre_config_olt_num = self.pre_config_olt_num

        lan = self.lan

        wlan = self.wlan

        lan_device_connected_num = self.lan_device_connected_num

        lan_device_disconnected_num = self.lan_device_disconnected_num

        wlan_device_connected_num = self.wlan_device_connected_num

        wlan_device_disconnected_num = self.wlan_device_disconnected_num

        wlan_device_isolated_num = self.wlan_device_isolated_num

        olt_device_connected_num = self.olt_device_connected_num

        olt_device_disconnected_num = self.olt_device_disconnected_num

        lan_user_num = self.lan_user_num

        wlan_user_num = self.wlan_user_num

        lan_guest_num = self.lan_guest_num

        wlan_guest_num = self.wlan_guest_num

        device_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.device_account, Unset):
            device_account = self.device_account.to_dict()

        wireless_upgrade = self.wireless_upgrade

        wired_upgrade = self.wired_upgrade

        issue_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_event, Unset):
            issue_event = self.issue_event.to_dict()

        wan_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wan_health, Unset):
            wan_health = self.wan_health.to_dict()

        wlan_health = self.wlan_health

        gateway_health = self.gateway_health

        switch_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.switch_health, Unset):
            switch_health = self.switch_health.to_dict()

        eap_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.eap_health, Unset):
            eap_health = self.eap_health.to_dict()

        wireless_client_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wireless_client_health, Unset):
            wireless_client_health = self.wireless_client_health.to_dict()

        wired_client_health: dict[str, Any] | Unset = UNSET
        if not isinstance(self.wired_client_health, Unset):
            wired_client_health = self.wired_client_health.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if gateway_status is not UNSET:
            field_dict["gatewayStatus"] = gateway_status
        if pre_config_osg_num is not UNSET:
            field_dict["preConfigOsgNum"] = pre_config_osg_num
        if pre_config_osw_num is not UNSET:
            field_dict["preConfigOswNum"] = pre_config_osw_num
        if pre_config_ap_num is not UNSET:
            field_dict["preConfigApNum"] = pre_config_ap_num
        if pre_config_olt_num is not UNSET:
            field_dict["preConfigOltNum"] = pre_config_olt_num
        if lan is not UNSET:
            field_dict["lan"] = lan
        if wlan is not UNSET:
            field_dict["wlan"] = wlan
        if lan_device_connected_num is not UNSET:
            field_dict["lanDeviceConnectedNum"] = lan_device_connected_num
        if lan_device_disconnected_num is not UNSET:
            field_dict["lanDeviceDisconnectedNum"] = lan_device_disconnected_num
        if wlan_device_connected_num is not UNSET:
            field_dict["wlanDeviceConnectedNum"] = wlan_device_connected_num
        if wlan_device_disconnected_num is not UNSET:
            field_dict["wlanDeviceDisconnectedNum"] = wlan_device_disconnected_num
        if wlan_device_isolated_num is not UNSET:
            field_dict["wlanDeviceIsolatedNum"] = wlan_device_isolated_num
        if olt_device_connected_num is not UNSET:
            field_dict["oltDeviceConnectedNum"] = olt_device_connected_num
        if olt_device_disconnected_num is not UNSET:
            field_dict["oltDeviceDisconnectedNum"] = olt_device_disconnected_num
        if lan_user_num is not UNSET:
            field_dict["lanUserNum"] = lan_user_num
        if wlan_user_num is not UNSET:
            field_dict["wlanUserNum"] = wlan_user_num
        if lan_guest_num is not UNSET:
            field_dict["lanGuestNum"] = lan_guest_num
        if wlan_guest_num is not UNSET:
            field_dict["wlanGuestNum"] = wlan_guest_num
        if device_account is not UNSET:
            field_dict["deviceAccount"] = device_account
        if wireless_upgrade is not UNSET:
            field_dict["wirelessUpgrade"] = wireless_upgrade
        if wired_upgrade is not UNSET:
            field_dict["wiredUpgrade"] = wired_upgrade
        if issue_event is not UNSET:
            field_dict["issueEvent"] = issue_event
        if wan_health is not UNSET:
            field_dict["wanHealth"] = wan_health
        if wlan_health is not UNSET:
            field_dict["wlanHealth"] = wlan_health
        if gateway_health is not UNSET:
            field_dict["gatewayHealth"] = gateway_health
        if switch_health is not UNSET:
            field_dict["switchHealth"] = switch_health
        if eap_health is not UNSET:
            field_dict["eapHealth"] = eap_health
        if wireless_client_health is not UNSET:
            field_dict["wirelessClientHealth"] = wireless_client_health
        if wired_client_health is not UNSET:
            field_dict["wiredClientHealth"] = wired_client_health

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.device_account_setting_vo import (
            DeviceAccountSettingVO,
        )
        from ..models.health_stat_vo import HealthStatVO
        from ..models.site_setting_anomaly_stat_vo import (
            SiteSettingAnomalyStatVO,
        )
        from ..models.wan_health_stat_vo import WanHealthStatVO

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        gateway_status = d.pop("gatewayStatus", UNSET)

        pre_config_osg_num = d.pop("preConfigOsgNum", UNSET)

        pre_config_osw_num = d.pop("preConfigOswNum", UNSET)

        pre_config_ap_num = d.pop("preConfigApNum", UNSET)

        pre_config_olt_num = d.pop("preConfigOltNum", UNSET)

        lan = d.pop("lan", UNSET)

        wlan = d.pop("wlan", UNSET)

        lan_device_connected_num = d.pop("lanDeviceConnectedNum", UNSET)

        lan_device_disconnected_num = d.pop("lanDeviceDisconnectedNum", UNSET)

        wlan_device_connected_num = d.pop("wlanDeviceConnectedNum", UNSET)

        wlan_device_disconnected_num = d.pop("wlanDeviceDisconnectedNum", UNSET)

        wlan_device_isolated_num = d.pop("wlanDeviceIsolatedNum", UNSET)

        olt_device_connected_num = d.pop("oltDeviceConnectedNum", UNSET)

        olt_device_disconnected_num = d.pop("oltDeviceDisconnectedNum", UNSET)

        lan_user_num = d.pop("lanUserNum", UNSET)

        wlan_user_num = d.pop("wlanUserNum", UNSET)

        lan_guest_num = d.pop("lanGuestNum", UNSET)

        wlan_guest_num = d.pop("wlanGuestNum", UNSET)

        _device_account = d.pop("deviceAccount", UNSET)
        device_account: DeviceAccountSettingVO | Unset
        if isinstance(_device_account, Unset):
            device_account = UNSET
        else:
            device_account = DeviceAccountSettingVO.from_dict(_device_account)

        wireless_upgrade = d.pop("wirelessUpgrade", UNSET)

        wired_upgrade = d.pop("wiredUpgrade", UNSET)

        _issue_event = d.pop("issueEvent", UNSET)
        issue_event: SiteSettingAnomalyStatVO | Unset
        if isinstance(_issue_event, Unset):
            issue_event = UNSET
        else:
            issue_event = SiteSettingAnomalyStatVO.from_dict(_issue_event)

        _wan_health = d.pop("wanHealth", UNSET)
        wan_health: WanHealthStatVO | Unset
        if isinstance(_wan_health, Unset):
            wan_health = UNSET
        else:
            wan_health = WanHealthStatVO.from_dict(_wan_health)

        wlan_health = d.pop("wlanHealth", UNSET)

        gateway_health = d.pop("gatewayHealth", UNSET)

        _switch_health = d.pop("switchHealth", UNSET)
        switch_health: HealthStatVO | Unset
        if isinstance(_switch_health, Unset):
            switch_health = UNSET
        else:
            switch_health = HealthStatVO.from_dict(_switch_health)

        _eap_health = d.pop("eapHealth", UNSET)
        eap_health: HealthStatVO | Unset
        if isinstance(_eap_health, Unset):
            eap_health = UNSET
        else:
            eap_health = HealthStatVO.from_dict(_eap_health)

        _wireless_client_health = d.pop("wirelessClientHealth", UNSET)
        wireless_client_health: HealthStatVO | Unset
        if isinstance(_wireless_client_health, Unset):
            wireless_client_health = UNSET
        else:
            wireless_client_health = HealthStatVO.from_dict(_wireless_client_health)

        _wired_client_health = d.pop("wiredClientHealth", UNSET)
        wired_client_health: HealthStatVO | Unset
        if isinstance(_wired_client_health, Unset):
            wired_client_health = UNSET
        else:
            wired_client_health = HealthStatVO.from_dict(_wired_client_health)

        site_statistic_info = cls(
            id=id,
            gateway_status=gateway_status,
            pre_config_osg_num=pre_config_osg_num,
            pre_config_osw_num=pre_config_osw_num,
            pre_config_ap_num=pre_config_ap_num,
            pre_config_olt_num=pre_config_olt_num,
            lan=lan,
            wlan=wlan,
            lan_device_connected_num=lan_device_connected_num,
            lan_device_disconnected_num=lan_device_disconnected_num,
            wlan_device_connected_num=wlan_device_connected_num,
            wlan_device_disconnected_num=wlan_device_disconnected_num,
            wlan_device_isolated_num=wlan_device_isolated_num,
            olt_device_connected_num=olt_device_connected_num,
            olt_device_disconnected_num=olt_device_disconnected_num,
            lan_user_num=lan_user_num,
            wlan_user_num=wlan_user_num,
            lan_guest_num=lan_guest_num,
            wlan_guest_num=wlan_guest_num,
            device_account=device_account,
            wireless_upgrade=wireless_upgrade,
            wired_upgrade=wired_upgrade,
            issue_event=issue_event,
            wan_health=wan_health,
            wlan_health=wlan_health,
            gateway_health=gateway_health,
            switch_health=switch_health,
            eap_health=eap_health,
            wireless_client_health=wireless_client_health,
            wired_client_health=wired_client_health,
        )

        site_statistic_info.additional_properties = d
        return site_statistic_info

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
