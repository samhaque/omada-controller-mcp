from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="GlobalOverViewOpenApiVO")


@_attrs_define
class GlobalOverViewOpenApiVO:
    """
    Attributes:
        total_gateway_num (int | Unset): total number of gateways
        connected_gateway_num (int | Unset): total number of connected gateways
        disconnected_gateway_num (int | Unset): total number of disconnected gateways
        total_switch_num (int | Unset): total number of switch
        connected_switch_num (int | Unset): total number of connected switch
        disconnected_switch_num (int | Unset): total number of disconnected switch
        total_ap_num (int | Unset): total number of ap
        connected_ap_num (int | Unset): total number of connected ap
        isolated_ap_num (int | Unset): total number of isolated ap
        disconnected_ap_num (int | Unset): total number of disconnected ap
        total_olt_num (int | Unset): total number of olt
        connected_olt_num (int | Unset): total number of connected olt
        disconnected_olt_num (int | Unset): total number of disconnected olt
        total_client_num (int | Unset): total number of client
        wired_client_num (int | Unset): total number of wired client
        wireless_client_num (int | Unset): total number of wireless client
        guest_num (int | Unset): total number of wireless guest
        site_num (int | Unset): total number of site
        country_num (int | Unset): total number of country
        cloud_access_status (int | Unset): the status of cloud access. -1: disabled  0: disconneted  1: conneted
        pre_config_osg_num (int | Unset): the number of preconfig gateway.
        pre_config_osw_num (int | Unset): the number of preconfig switch.
        pre_config_ap_num (int | Unset): the number of preconfig ap.
        pre_config_olt_num (int | Unset): the number of preconfig olt.
        total_connected_num (int | Unset): total number of connected devices
    """

    total_gateway_num: int | Unset = UNSET
    connected_gateway_num: int | Unset = UNSET
    disconnected_gateway_num: int | Unset = UNSET
    total_switch_num: int | Unset = UNSET
    connected_switch_num: int | Unset = UNSET
    disconnected_switch_num: int | Unset = UNSET
    total_ap_num: int | Unset = UNSET
    connected_ap_num: int | Unset = UNSET
    isolated_ap_num: int | Unset = UNSET
    disconnected_ap_num: int | Unset = UNSET
    total_olt_num: int | Unset = UNSET
    connected_olt_num: int | Unset = UNSET
    disconnected_olt_num: int | Unset = UNSET
    total_client_num: int | Unset = UNSET
    wired_client_num: int | Unset = UNSET
    wireless_client_num: int | Unset = UNSET
    guest_num: int | Unset = UNSET
    site_num: int | Unset = UNSET
    country_num: int | Unset = UNSET
    cloud_access_status: int | Unset = UNSET
    pre_config_osg_num: int | Unset = UNSET
    pre_config_osw_num: int | Unset = UNSET
    pre_config_ap_num: int | Unset = UNSET
    pre_config_olt_num: int | Unset = UNSET
    total_connected_num: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_gateway_num = self.total_gateway_num

        connected_gateway_num = self.connected_gateway_num

        disconnected_gateway_num = self.disconnected_gateway_num

        total_switch_num = self.total_switch_num

        connected_switch_num = self.connected_switch_num

        disconnected_switch_num = self.disconnected_switch_num

        total_ap_num = self.total_ap_num

        connected_ap_num = self.connected_ap_num

        isolated_ap_num = self.isolated_ap_num

        disconnected_ap_num = self.disconnected_ap_num

        total_olt_num = self.total_olt_num

        connected_olt_num = self.connected_olt_num

        disconnected_olt_num = self.disconnected_olt_num

        total_client_num = self.total_client_num

        wired_client_num = self.wired_client_num

        wireless_client_num = self.wireless_client_num

        guest_num = self.guest_num

        site_num = self.site_num

        country_num = self.country_num

        cloud_access_status = self.cloud_access_status

        pre_config_osg_num = self.pre_config_osg_num

        pre_config_osw_num = self.pre_config_osw_num

        pre_config_ap_num = self.pre_config_ap_num

        pre_config_olt_num = self.pre_config_olt_num

        total_connected_num = self.total_connected_num

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_gateway_num is not UNSET:
            field_dict["totalGatewayNum"] = total_gateway_num
        if connected_gateway_num is not UNSET:
            field_dict["connectedGatewayNum"] = connected_gateway_num
        if disconnected_gateway_num is not UNSET:
            field_dict["disconnectedGatewayNum"] = disconnected_gateway_num
        if total_switch_num is not UNSET:
            field_dict["totalSwitchNum"] = total_switch_num
        if connected_switch_num is not UNSET:
            field_dict["connectedSwitchNum"] = connected_switch_num
        if disconnected_switch_num is not UNSET:
            field_dict["disconnectedSwitchNum"] = disconnected_switch_num
        if total_ap_num is not UNSET:
            field_dict["totalApNum"] = total_ap_num
        if connected_ap_num is not UNSET:
            field_dict["connectedApNum"] = connected_ap_num
        if isolated_ap_num is not UNSET:
            field_dict["isolatedApNum"] = isolated_ap_num
        if disconnected_ap_num is not UNSET:
            field_dict["disconnectedApNum"] = disconnected_ap_num
        if total_olt_num is not UNSET:
            field_dict["totalOltNum"] = total_olt_num
        if connected_olt_num is not UNSET:
            field_dict["connectedOltNum"] = connected_olt_num
        if disconnected_olt_num is not UNSET:
            field_dict["disconnectedOltNum"] = disconnected_olt_num
        if total_client_num is not UNSET:
            field_dict["totalClientNum"] = total_client_num
        if wired_client_num is not UNSET:
            field_dict["wiredClientNum"] = wired_client_num
        if wireless_client_num is not UNSET:
            field_dict["wirelessClientNum"] = wireless_client_num
        if guest_num is not UNSET:
            field_dict["guestNum"] = guest_num
        if site_num is not UNSET:
            field_dict["siteNum"] = site_num
        if country_num is not UNSET:
            field_dict["countryNum"] = country_num
        if cloud_access_status is not UNSET:
            field_dict["cloudAccessStatus"] = cloud_access_status
        if pre_config_osg_num is not UNSET:
            field_dict["preConfigOsgNum"] = pre_config_osg_num
        if pre_config_osw_num is not UNSET:
            field_dict["preConfigOswNum"] = pre_config_osw_num
        if pre_config_ap_num is not UNSET:
            field_dict["preConfigApNum"] = pre_config_ap_num
        if pre_config_olt_num is not UNSET:
            field_dict["preConfigOltNum"] = pre_config_olt_num
        if total_connected_num is not UNSET:
            field_dict["totalConnectedNum"] = total_connected_num

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        total_gateway_num = d.pop("totalGatewayNum", UNSET)

        connected_gateway_num = d.pop("connectedGatewayNum", UNSET)

        disconnected_gateway_num = d.pop("disconnectedGatewayNum", UNSET)

        total_switch_num = d.pop("totalSwitchNum", UNSET)

        connected_switch_num = d.pop("connectedSwitchNum", UNSET)

        disconnected_switch_num = d.pop("disconnectedSwitchNum", UNSET)

        total_ap_num = d.pop("totalApNum", UNSET)

        connected_ap_num = d.pop("connectedApNum", UNSET)

        isolated_ap_num = d.pop("isolatedApNum", UNSET)

        disconnected_ap_num = d.pop("disconnectedApNum", UNSET)

        total_olt_num = d.pop("totalOltNum", UNSET)

        connected_olt_num = d.pop("connectedOltNum", UNSET)

        disconnected_olt_num = d.pop("disconnectedOltNum", UNSET)

        total_client_num = d.pop("totalClientNum", UNSET)

        wired_client_num = d.pop("wiredClientNum", UNSET)

        wireless_client_num = d.pop("wirelessClientNum", UNSET)

        guest_num = d.pop("guestNum", UNSET)

        site_num = d.pop("siteNum", UNSET)

        country_num = d.pop("countryNum", UNSET)

        cloud_access_status = d.pop("cloudAccessStatus", UNSET)

        pre_config_osg_num = d.pop("preConfigOsgNum", UNSET)

        pre_config_osw_num = d.pop("preConfigOswNum", UNSET)

        pre_config_ap_num = d.pop("preConfigApNum", UNSET)

        pre_config_olt_num = d.pop("preConfigOltNum", UNSET)

        total_connected_num = d.pop("totalConnectedNum", UNSET)

        global_over_view_open_api_vo = cls(
            total_gateway_num=total_gateway_num,
            connected_gateway_num=connected_gateway_num,
            disconnected_gateway_num=disconnected_gateway_num,
            total_switch_num=total_switch_num,
            connected_switch_num=connected_switch_num,
            disconnected_switch_num=disconnected_switch_num,
            total_ap_num=total_ap_num,
            connected_ap_num=connected_ap_num,
            isolated_ap_num=isolated_ap_num,
            disconnected_ap_num=disconnected_ap_num,
            total_olt_num=total_olt_num,
            connected_olt_num=connected_olt_num,
            disconnected_olt_num=disconnected_olt_num,
            total_client_num=total_client_num,
            wired_client_num=wired_client_num,
            wireless_client_num=wireless_client_num,
            guest_num=guest_num,
            site_num=site_num,
            country_num=country_num,
            cloud_access_status=cloud_access_status,
            pre_config_osg_num=pre_config_osg_num,
            pre_config_osw_num=pre_config_osw_num,
            pre_config_ap_num=pre_config_ap_num,
            pre_config_olt_num=pre_config_olt_num,
            total_connected_num=total_connected_num,
        )

        global_over_view_open_api_vo.additional_properties = d
        return global_over_view_open_api_vo

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
