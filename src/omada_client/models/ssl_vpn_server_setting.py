from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ldap_setting_open_api_vo import LdapSettingOpenApiVO
    from ..models.lock_setting_open_api_vo import LockSettingOpenApiVO
    from ..models.radius_setting_open_api_vo import RadiusSettingOpenApiVO


T = TypeVar("T", bound="SslVpnServerSetting")


@_attrs_define
class SslVpnServerSetting:
    """
    Attributes:
        status (bool): Status of the SSL VPN server.
        id (str | Unset): ID of the SSL VPN server.
        wan_port (str | Unset): WAN port of the SSL VPN server. WAN port ID can be obtained from 'Get internet basic
            info' interface
        wan_ip (str | Unset): WAP IP of the SSL VPN server.
        ip_pool_start (str | Unset): The start IP of the IP pool.
        ip_pool_end (str | Unset): The end IP of the IP pool.
        primary_dns (str | Unset): Primary DNS Server of the SSL VPN server.
        secondary_dns (str | Unset): Secondary DNS Server of the SSL VPN server.
        service_port (int | Unset): Service port of the SSL VPN server should be within the range of 1–65535
        auth_type (int | Unset): Authentication type of the SSL VPN server should be a value as follows: 0: local; 1:
            radius; 2: LDAP.
        radius_setting (RadiusSettingOpenApiVO | Unset): It is required when parameter [authType] is 1.
        ldap_setting (LdapSettingOpenApiVO | Unset): It is required when parameter [authType] is 2.
        name_lock_setting (LockSettingOpenApiVO | Unset): IP lock config. It is required when parameter [status] is
            true.
        ip_lock_setting (LockSettingOpenApiVO | Unset): IP lock config. It is required when parameter [status] is true.
        exit_at_idle (bool | Unset): Whether to exit when idle
        exit_time (int | Unset): Exit time should be within the range of 5–3600(s). It is required when parameter
            [exitAtIdle] is true.
        total_traffic (bool | Unset): Whether to proxy all traffic.
        support_radius (bool | Unset): Whether the adopted gateway supports Radius.
        exist_radius (bool | Unset): Whether RADIUS Authentication has been configured in SSL VPN Server.
        support_ldap (bool | Unset): Whether the adopted gateway supports LDAP.
        exist_ldap (bool | Unset): Whether LDAP Authentication has been configured in SSL VPN Server.
        support_by_ds_lite_and_map_e (bool | Unset): Whether this feature is supported for the DS-Lite or Map-E WAN
            connection types.
    """

    status: bool
    id: str | Unset = UNSET
    wan_port: str | Unset = UNSET
    wan_ip: str | Unset = UNSET
    ip_pool_start: str | Unset = UNSET
    ip_pool_end: str | Unset = UNSET
    primary_dns: str | Unset = UNSET
    secondary_dns: str | Unset = UNSET
    service_port: int | Unset = UNSET
    auth_type: int | Unset = UNSET
    radius_setting: RadiusSettingOpenApiVO | Unset = UNSET
    ldap_setting: LdapSettingOpenApiVO | Unset = UNSET
    name_lock_setting: LockSettingOpenApiVO | Unset = UNSET
    ip_lock_setting: LockSettingOpenApiVO | Unset = UNSET
    exit_at_idle: bool | Unset = UNSET
    exit_time: int | Unset = UNSET
    total_traffic: bool | Unset = UNSET
    support_radius: bool | Unset = UNSET
    exist_radius: bool | Unset = UNSET
    support_ldap: bool | Unset = UNSET
    exist_ldap: bool | Unset = UNSET
    support_by_ds_lite_and_map_e: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        id = self.id

        wan_port = self.wan_port

        wan_ip = self.wan_ip

        ip_pool_start = self.ip_pool_start

        ip_pool_end = self.ip_pool_end

        primary_dns = self.primary_dns

        secondary_dns = self.secondary_dns

        service_port = self.service_port

        auth_type = self.auth_type

        radius_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.radius_setting, Unset):
            radius_setting = self.radius_setting.to_dict()

        ldap_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap_setting, Unset):
            ldap_setting = self.ldap_setting.to_dict()

        name_lock_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_lock_setting, Unset):
            name_lock_setting = self.name_lock_setting.to_dict()

        ip_lock_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ip_lock_setting, Unset):
            ip_lock_setting = self.ip_lock_setting.to_dict()

        exit_at_idle = self.exit_at_idle

        exit_time = self.exit_time

        total_traffic = self.total_traffic

        support_radius = self.support_radius

        exist_radius = self.exist_radius

        support_ldap = self.support_ldap

        exist_ldap = self.exist_ldap

        support_by_ds_lite_and_map_e = self.support_by_ds_lite_and_map_e

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if wan_port is not UNSET:
            field_dict["wanPort"] = wan_port
        if wan_ip is not UNSET:
            field_dict["wanIp"] = wan_ip
        if ip_pool_start is not UNSET:
            field_dict["ipPoolStart"] = ip_pool_start
        if ip_pool_end is not UNSET:
            field_dict["ipPoolEnd"] = ip_pool_end
        if primary_dns is not UNSET:
            field_dict["primaryDns"] = primary_dns
        if secondary_dns is not UNSET:
            field_dict["secondaryDns"] = secondary_dns
        if service_port is not UNSET:
            field_dict["servicePort"] = service_port
        if auth_type is not UNSET:
            field_dict["authType"] = auth_type
        if radius_setting is not UNSET:
            field_dict["radiusSetting"] = radius_setting
        if ldap_setting is not UNSET:
            field_dict["LDAPSetting"] = ldap_setting
        if name_lock_setting is not UNSET:
            field_dict["nameLockSetting"] = name_lock_setting
        if ip_lock_setting is not UNSET:
            field_dict["ipLockSetting"] = ip_lock_setting
        if exit_at_idle is not UNSET:
            field_dict["exitAtIdle"] = exit_at_idle
        if exit_time is not UNSET:
            field_dict["exitTime"] = exit_time
        if total_traffic is not UNSET:
            field_dict["totalTraffic"] = total_traffic
        if support_radius is not UNSET:
            field_dict["supportRadius"] = support_radius
        if exist_radius is not UNSET:
            field_dict["existRadius"] = exist_radius
        if support_ldap is not UNSET:
            field_dict["supportLDAP"] = support_ldap
        if exist_ldap is not UNSET:
            field_dict["existLdap"] = exist_ldap
        if support_by_ds_lite_and_map_e is not UNSET:
            field_dict["supportByDsLiteAndMapE"] = support_by_ds_lite_and_map_e

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ldap_setting_open_api_vo import (
            LdapSettingOpenApiVO,
        )
        from ..models.lock_setting_open_api_vo import (
            LockSettingOpenApiVO,
        )
        from ..models.radius_setting_open_api_vo import (
            RadiusSettingOpenApiVO,
        )

        d = dict(src_dict)
        status = d.pop("status")

        id = d.pop("id", UNSET)

        wan_port = d.pop("wanPort", UNSET)

        wan_ip = d.pop("wanIp", UNSET)

        ip_pool_start = d.pop("ipPoolStart", UNSET)

        ip_pool_end = d.pop("ipPoolEnd", UNSET)

        primary_dns = d.pop("primaryDns", UNSET)

        secondary_dns = d.pop("secondaryDns", UNSET)

        service_port = d.pop("servicePort", UNSET)

        auth_type = d.pop("authType", UNSET)

        _radius_setting = d.pop("radiusSetting", UNSET)
        radius_setting: RadiusSettingOpenApiVO | Unset
        if isinstance(_radius_setting, Unset):
            radius_setting = UNSET
        else:
            radius_setting = RadiusSettingOpenApiVO.from_dict(_radius_setting)

        _ldap_setting = d.pop("LDAPSetting", UNSET)
        ldap_setting: LdapSettingOpenApiVO | Unset
        if isinstance(_ldap_setting, Unset):
            ldap_setting = UNSET
        else:
            ldap_setting = LdapSettingOpenApiVO.from_dict(_ldap_setting)

        _name_lock_setting = d.pop("nameLockSetting", UNSET)
        name_lock_setting: LockSettingOpenApiVO | Unset
        if isinstance(_name_lock_setting, Unset):
            name_lock_setting = UNSET
        else:
            name_lock_setting = LockSettingOpenApiVO.from_dict(_name_lock_setting)

        _ip_lock_setting = d.pop("ipLockSetting", UNSET)
        ip_lock_setting: LockSettingOpenApiVO | Unset
        if isinstance(_ip_lock_setting, Unset):
            ip_lock_setting = UNSET
        else:
            ip_lock_setting = LockSettingOpenApiVO.from_dict(_ip_lock_setting)

        exit_at_idle = d.pop("exitAtIdle", UNSET)

        exit_time = d.pop("exitTime", UNSET)

        total_traffic = d.pop("totalTraffic", UNSET)

        support_radius = d.pop("supportRadius", UNSET)

        exist_radius = d.pop("existRadius", UNSET)

        support_ldap = d.pop("supportLDAP", UNSET)

        exist_ldap = d.pop("existLdap", UNSET)

        support_by_ds_lite_and_map_e = d.pop("supportByDsLiteAndMapE", UNSET)

        ssl_vpn_server_setting = cls(
            status=status,
            id=id,
            wan_port=wan_port,
            wan_ip=wan_ip,
            ip_pool_start=ip_pool_start,
            ip_pool_end=ip_pool_end,
            primary_dns=primary_dns,
            secondary_dns=secondary_dns,
            service_port=service_port,
            auth_type=auth_type,
            radius_setting=radius_setting,
            ldap_setting=ldap_setting,
            name_lock_setting=name_lock_setting,
            ip_lock_setting=ip_lock_setting,
            exit_at_idle=exit_at_idle,
            exit_time=exit_time,
            total_traffic=total_traffic,
            support_radius=support_radius,
            exist_radius=exist_radius,
            support_ldap=support_ldap,
            exist_ldap=exist_ldap,
            support_by_ds_lite_and_map_e=support_by_ds_lite_and_map_e,
        )

        ssl_vpn_server_setting.additional_properties = d
        return ssl_vpn_server_setting

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
