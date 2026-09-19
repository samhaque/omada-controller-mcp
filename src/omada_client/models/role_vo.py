from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleVO")


@_attrs_define
class RoleVO:
    """Role privilege

    Attributes:
        msp_dashboard (int | Unset): msp dashboard, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_device (int | Unset): msp device, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_log (int | Unset): msp log, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_license (int | Unset): msp license, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_license_bind (int | Unset): msp license bind, it should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_users (int | Unset): msp user, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_roles (int | Unset): msp role, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_saml_users (int | Unset): saml users in msp view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_saml_roles (int | Unset): saml roles in msp view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_saml_ssos (int | Unset): saml ssos in msp view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_setting (int | Unset): msp setting, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_export_data (int | Unset): export data in msp view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_adopt (int | Unset): msp adopt in msp view, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_add_devices (int | Unset): msp add devices in msp view, it should be a value as follows: 0:block; 1:view
            only; 2:modify
        msp_add_adopt_device (int | Unset): msp add and adopt devices in msp view, it should be a value as follows:
            0:block; 1:view only; 2:modify
        msp_webhook (int | Unset): msp webhook in msp view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_sites (int | Unset): msp sites in msp view, it should be a value as follows: 0:block; 1:view only; 2:modify
        msp_cluster (int | Unset): msp cluster, it should be a value as follows: 0:block; 1:view only; 2:modify
        global_dashboard (int | Unset): dashboard in global view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        dashboard (int | Unset): dashboard, it should be a value as follows: 0:block; 1:view only; 2:modify
        devices (int | Unset): devices, it should be a value as follows: 0:block; 1:view only; 2:modify
        adopt (int | Unset): adopt, it should be a value as follows: 0:block; 1:view only; 2:modify
        add_devices (int | Unset): add devices in global/customer view, it should be a value as follows: 0:block; 1:view
            only; 2:modify
        add_adopt_device (int | Unset): add and adopt devices in global/customer view, it should be a value as follows:
            0:block; 1:view only; 2:modify
        global_log (int | Unset): log in global view, it should be a value as follows: 0:block; 1:view only; 2:modify
        manual_upgrade (int | Unset): manual upgrade in global view, it should be a value as follows: 0:block; 1:view
            only; 2:modify
        log (int | Unset): log in site view, it should be a value as follows: 0:block; 1:view only; 2:modify
        license_ (int | Unset): license, it should be a value as follows: 0:block; 1:view only; 2:modify
        license_bind (int | Unset): license bind, it should be a value as follows: 0:block; 1:view only; 2:modify
        users (int | Unset): users in global view, it should be a value as follows: 0:block; 1:view only; 2:modify
        roles (int | Unset): roles in global view, it should be a value as follows: 0:block; 1:view only; 2:modify
        saml_users (int | Unset): saml users in global view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        saml_roles (int | Unset): saml roles in global view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        saml_ssos (int | Unset): saml ssos in global view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        global_setting (int | Unset): settings in global view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        export_data (int | Unset): export data in site view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        global_export_data (int | Unset): export data in global view, it should be a value as follows: 0:block; 1:view
            only; 2:modify
        export_global_log (int | Unset): export global log data in global view, it should be a value as follows:
            0:block; 1:view only; 2:modify
        global_cluster (int | Unset): cluster in global view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        hotspot (int | Unset): hotspot, it should be a value as follows: 0:block; 1:view only; 2:modify
        statics (int | Unset): statics, it should be a value as follows: 0:block; 1:view only; 2:modify
        map_ (int | Unset): map, it should be a value as follows: 0:block; 1:view only; 2:modify
        clients (int | Unset): clients, it should be a value as follows: 0:block; 1:view only; 2:modify
        insight (int | Unset): insight, it should be a value as follows: 0:block; 1:view only; 2:modify
        report (int | Unset): network report, it should be a value as follows: 0:block; 1:view only; 2:modify
        network (int | Unset): site network settings, it should be a value as follows: 0:block; 1:view only; 2:modify
        device_account (int | Unset): device account, it should be a value as follows: 0:block; 1:view only; 2:modify
        anomaly (int | Unset): anomaly, it should be a value as follows: 0:block; 1:view only; 2:modify
        analyze (int | Unset): analyze, it should be a value as follows: 0:block; 1:view only; 2:modify
        site_analyze (int | Unset): analyze in site view, it should be a value as follows: 0:block; 1:view only;
            2:modify
        global_security (int | Unset): security, it should be a value as follows: 0:block; 1:view only; 2:modify
        global_webhook (int | Unset): Webhook, it should be a value as follows: 0:block; 1:view only; 2:modify
        global_map_token (int | Unset): Map Token, it should be a value as follows: 0:block; 1:view only; 2:modify
        site_template (int | Unset): Site Template, it should be a value as follows: 0:block; 1:view only; 2:modify
        global_firmware (int | Unset): Firmware Manager, it should be a value as follows: 0:block; 1:view only; 2:modify
        sd_wan (int | Unset): SD-WAN, it should be a value as follows: 0:block; 1:view only; 2:modify
        site_home (int | Unset): Site Home Manager
        device_recovery (int | Unset): Device Recovery, it should be a value as follows: 0:block; 1:view only; 2:modify
        site_network (int | Unset): Network Config Page, it should be a value as follows: 0:block; 1:view only; 2:modify
        site_device (int | Unset): Device Config Page, it should be a value as follows: 0:block; 1:view only; 2:modify
        site_maintain (int | Unset): Maintenance Page, it should be a value as follows: 0:block; 1:view only; 2:modify
        ai_assi (int | Unset): AI Assistant, it should be a value as follows: 0:block; 1:view only; 2:modify
    """

    msp_dashboard: int | Unset = UNSET
    msp_device: int | Unset = UNSET
    msp_log: int | Unset = UNSET
    msp_license: int | Unset = UNSET
    msp_license_bind: int | Unset = UNSET
    msp_users: int | Unset = UNSET
    msp_roles: int | Unset = UNSET
    msp_saml_users: int | Unset = UNSET
    msp_saml_roles: int | Unset = UNSET
    msp_saml_ssos: int | Unset = UNSET
    msp_setting: int | Unset = UNSET
    msp_export_data: int | Unset = UNSET
    msp_adopt: int | Unset = UNSET
    msp_add_devices: int | Unset = UNSET
    msp_add_adopt_device: int | Unset = UNSET
    msp_webhook: int | Unset = UNSET
    msp_sites: int | Unset = UNSET
    msp_cluster: int | Unset = UNSET
    global_dashboard: int | Unset = UNSET
    dashboard: int | Unset = UNSET
    devices: int | Unset = UNSET
    adopt: int | Unset = UNSET
    add_devices: int | Unset = UNSET
    add_adopt_device: int | Unset = UNSET
    global_log: int | Unset = UNSET
    manual_upgrade: int | Unset = UNSET
    log: int | Unset = UNSET
    license_: int | Unset = UNSET
    license_bind: int | Unset = UNSET
    users: int | Unset = UNSET
    roles: int | Unset = UNSET
    saml_users: int | Unset = UNSET
    saml_roles: int | Unset = UNSET
    saml_ssos: int | Unset = UNSET
    global_setting: int | Unset = UNSET
    export_data: int | Unset = UNSET
    global_export_data: int | Unset = UNSET
    export_global_log: int | Unset = UNSET
    global_cluster: int | Unset = UNSET
    hotspot: int | Unset = UNSET
    statics: int | Unset = UNSET
    map_: int | Unset = UNSET
    clients: int | Unset = UNSET
    insight: int | Unset = UNSET
    report: int | Unset = UNSET
    network: int | Unset = UNSET
    device_account: int | Unset = UNSET
    anomaly: int | Unset = UNSET
    analyze: int | Unset = UNSET
    site_analyze: int | Unset = UNSET
    global_security: int | Unset = UNSET
    global_webhook: int | Unset = UNSET
    global_map_token: int | Unset = UNSET
    site_template: int | Unset = UNSET
    global_firmware: int | Unset = UNSET
    sd_wan: int | Unset = UNSET
    site_home: int | Unset = UNSET
    device_recovery: int | Unset = UNSET
    site_network: int | Unset = UNSET
    site_device: int | Unset = UNSET
    site_maintain: int | Unset = UNSET
    ai_assi: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        msp_dashboard = self.msp_dashboard

        msp_device = self.msp_device

        msp_log = self.msp_log

        msp_license = self.msp_license

        msp_license_bind = self.msp_license_bind

        msp_users = self.msp_users

        msp_roles = self.msp_roles

        msp_saml_users = self.msp_saml_users

        msp_saml_roles = self.msp_saml_roles

        msp_saml_ssos = self.msp_saml_ssos

        msp_setting = self.msp_setting

        msp_export_data = self.msp_export_data

        msp_adopt = self.msp_adopt

        msp_add_devices = self.msp_add_devices

        msp_add_adopt_device = self.msp_add_adopt_device

        msp_webhook = self.msp_webhook

        msp_sites = self.msp_sites

        msp_cluster = self.msp_cluster

        global_dashboard = self.global_dashboard

        dashboard = self.dashboard

        devices = self.devices

        adopt = self.adopt

        add_devices = self.add_devices

        add_adopt_device = self.add_adopt_device

        global_log = self.global_log

        manual_upgrade = self.manual_upgrade

        log = self.log

        license_ = self.license_

        license_bind = self.license_bind

        users = self.users

        roles = self.roles

        saml_users = self.saml_users

        saml_roles = self.saml_roles

        saml_ssos = self.saml_ssos

        global_setting = self.global_setting

        export_data = self.export_data

        global_export_data = self.global_export_data

        export_global_log = self.export_global_log

        global_cluster = self.global_cluster

        hotspot = self.hotspot

        statics = self.statics

        map_ = self.map_

        clients = self.clients

        insight = self.insight

        report = self.report

        network = self.network

        device_account = self.device_account

        anomaly = self.anomaly

        analyze = self.analyze

        site_analyze = self.site_analyze

        global_security = self.global_security

        global_webhook = self.global_webhook

        global_map_token = self.global_map_token

        site_template = self.site_template

        global_firmware = self.global_firmware

        sd_wan = self.sd_wan

        site_home = self.site_home

        device_recovery = self.device_recovery

        site_network = self.site_network

        site_device = self.site_device

        site_maintain = self.site_maintain

        ai_assi = self.ai_assi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if msp_dashboard is not UNSET:
            field_dict["mspDashboard"] = msp_dashboard
        if msp_device is not UNSET:
            field_dict["mspDevice"] = msp_device
        if msp_log is not UNSET:
            field_dict["mspLog"] = msp_log
        if msp_license is not UNSET:
            field_dict["mspLicense"] = msp_license
        if msp_license_bind is not UNSET:
            field_dict["mspLicenseBind"] = msp_license_bind
        if msp_users is not UNSET:
            field_dict["mspUsers"] = msp_users
        if msp_roles is not UNSET:
            field_dict["mspRoles"] = msp_roles
        if msp_saml_users is not UNSET:
            field_dict["mspSamlUsers"] = msp_saml_users
        if msp_saml_roles is not UNSET:
            field_dict["mspSamlRoles"] = msp_saml_roles
        if msp_saml_ssos is not UNSET:
            field_dict["mspSamlSsos"] = msp_saml_ssos
        if msp_setting is not UNSET:
            field_dict["mspSetting"] = msp_setting
        if msp_export_data is not UNSET:
            field_dict["mspExportData"] = msp_export_data
        if msp_adopt is not UNSET:
            field_dict["mspAdopt"] = msp_adopt
        if msp_add_devices is not UNSET:
            field_dict["mspAddDevices"] = msp_add_devices
        if msp_add_adopt_device is not UNSET:
            field_dict["mspAddAdoptDevice"] = msp_add_adopt_device
        if msp_webhook is not UNSET:
            field_dict["mspWebhook"] = msp_webhook
        if msp_sites is not UNSET:
            field_dict["mspSites"] = msp_sites
        if msp_cluster is not UNSET:
            field_dict["mspCluster"] = msp_cluster
        if global_dashboard is not UNSET:
            field_dict["globalDashboard"] = global_dashboard
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if devices is not UNSET:
            field_dict["devices"] = devices
        if adopt is not UNSET:
            field_dict["adopt"] = adopt
        if add_devices is not UNSET:
            field_dict["addDevices"] = add_devices
        if add_adopt_device is not UNSET:
            field_dict["addAdoptDevice"] = add_adopt_device
        if global_log is not UNSET:
            field_dict["globalLog"] = global_log
        if manual_upgrade is not UNSET:
            field_dict["manualUpgrade"] = manual_upgrade
        if log is not UNSET:
            field_dict["log"] = log
        if license_ is not UNSET:
            field_dict["license"] = license_
        if license_bind is not UNSET:
            field_dict["licenseBind"] = license_bind
        if users is not UNSET:
            field_dict["users"] = users
        if roles is not UNSET:
            field_dict["roles"] = roles
        if saml_users is not UNSET:
            field_dict["samlUsers"] = saml_users
        if saml_roles is not UNSET:
            field_dict["samlRoles"] = saml_roles
        if saml_ssos is not UNSET:
            field_dict["samlSsos"] = saml_ssos
        if global_setting is not UNSET:
            field_dict["globalSetting"] = global_setting
        if export_data is not UNSET:
            field_dict["exportData"] = export_data
        if global_export_data is not UNSET:
            field_dict["globalExportData"] = global_export_data
        if export_global_log is not UNSET:
            field_dict["exportGlobalLog"] = export_global_log
        if global_cluster is not UNSET:
            field_dict["globalCluster"] = global_cluster
        if hotspot is not UNSET:
            field_dict["hotspot"] = hotspot
        if statics is not UNSET:
            field_dict["statics"] = statics
        if map_ is not UNSET:
            field_dict["map"] = map_
        if clients is not UNSET:
            field_dict["clients"] = clients
        if insight is not UNSET:
            field_dict["insight"] = insight
        if report is not UNSET:
            field_dict["report"] = report
        if network is not UNSET:
            field_dict["network"] = network
        if device_account is not UNSET:
            field_dict["deviceAccount"] = device_account
        if anomaly is not UNSET:
            field_dict["anomaly"] = anomaly
        if analyze is not UNSET:
            field_dict["analyze"] = analyze
        if site_analyze is not UNSET:
            field_dict["siteAnalyze"] = site_analyze
        if global_security is not UNSET:
            field_dict["globalSecurity"] = global_security
        if global_webhook is not UNSET:
            field_dict["globalWebhook"] = global_webhook
        if global_map_token is not UNSET:
            field_dict["globalMapToken"] = global_map_token
        if site_template is not UNSET:
            field_dict["siteTemplate"] = site_template
        if global_firmware is not UNSET:
            field_dict["globalFirmware"] = global_firmware
        if sd_wan is not UNSET:
            field_dict["sdWan"] = sd_wan
        if site_home is not UNSET:
            field_dict["siteHome"] = site_home
        if device_recovery is not UNSET:
            field_dict["deviceRecovery"] = device_recovery
        if site_network is not UNSET:
            field_dict["siteNetwork"] = site_network
        if site_device is not UNSET:
            field_dict["siteDevice"] = site_device
        if site_maintain is not UNSET:
            field_dict["siteMaintain"] = site_maintain
        if ai_assi is not UNSET:
            field_dict["aiAssi"] = ai_assi

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        msp_dashboard = d.pop("mspDashboard", UNSET)

        msp_device = d.pop("mspDevice", UNSET)

        msp_log = d.pop("mspLog", UNSET)

        msp_license = d.pop("mspLicense", UNSET)

        msp_license_bind = d.pop("mspLicenseBind", UNSET)

        msp_users = d.pop("mspUsers", UNSET)

        msp_roles = d.pop("mspRoles", UNSET)

        msp_saml_users = d.pop("mspSamlUsers", UNSET)

        msp_saml_roles = d.pop("mspSamlRoles", UNSET)

        msp_saml_ssos = d.pop("mspSamlSsos", UNSET)

        msp_setting = d.pop("mspSetting", UNSET)

        msp_export_data = d.pop("mspExportData", UNSET)

        msp_adopt = d.pop("mspAdopt", UNSET)

        msp_add_devices = d.pop("mspAddDevices", UNSET)

        msp_add_adopt_device = d.pop("mspAddAdoptDevice", UNSET)

        msp_webhook = d.pop("mspWebhook", UNSET)

        msp_sites = d.pop("mspSites", UNSET)

        msp_cluster = d.pop("mspCluster", UNSET)

        global_dashboard = d.pop("globalDashboard", UNSET)

        dashboard = d.pop("dashboard", UNSET)

        devices = d.pop("devices", UNSET)

        adopt = d.pop("adopt", UNSET)

        add_devices = d.pop("addDevices", UNSET)

        add_adopt_device = d.pop("addAdoptDevice", UNSET)

        global_log = d.pop("globalLog", UNSET)

        manual_upgrade = d.pop("manualUpgrade", UNSET)

        log = d.pop("log", UNSET)

        license_ = d.pop("license", UNSET)

        license_bind = d.pop("licenseBind", UNSET)

        users = d.pop("users", UNSET)

        roles = d.pop("roles", UNSET)

        saml_users = d.pop("samlUsers", UNSET)

        saml_roles = d.pop("samlRoles", UNSET)

        saml_ssos = d.pop("samlSsos", UNSET)

        global_setting = d.pop("globalSetting", UNSET)

        export_data = d.pop("exportData", UNSET)

        global_export_data = d.pop("globalExportData", UNSET)

        export_global_log = d.pop("exportGlobalLog", UNSET)

        global_cluster = d.pop("globalCluster", UNSET)

        hotspot = d.pop("hotspot", UNSET)

        statics = d.pop("statics", UNSET)

        map_ = d.pop("map", UNSET)

        clients = d.pop("clients", UNSET)

        insight = d.pop("insight", UNSET)

        report = d.pop("report", UNSET)

        network = d.pop("network", UNSET)

        device_account = d.pop("deviceAccount", UNSET)

        anomaly = d.pop("anomaly", UNSET)

        analyze = d.pop("analyze", UNSET)

        site_analyze = d.pop("siteAnalyze", UNSET)

        global_security = d.pop("globalSecurity", UNSET)

        global_webhook = d.pop("globalWebhook", UNSET)

        global_map_token = d.pop("globalMapToken", UNSET)

        site_template = d.pop("siteTemplate", UNSET)

        global_firmware = d.pop("globalFirmware", UNSET)

        sd_wan = d.pop("sdWan", UNSET)

        site_home = d.pop("siteHome", UNSET)

        device_recovery = d.pop("deviceRecovery", UNSET)

        site_network = d.pop("siteNetwork", UNSET)

        site_device = d.pop("siteDevice", UNSET)

        site_maintain = d.pop("siteMaintain", UNSET)

        ai_assi = d.pop("aiAssi", UNSET)

        role_vo = cls(
            msp_dashboard=msp_dashboard,
            msp_device=msp_device,
            msp_log=msp_log,
            msp_license=msp_license,
            msp_license_bind=msp_license_bind,
            msp_users=msp_users,
            msp_roles=msp_roles,
            msp_saml_users=msp_saml_users,
            msp_saml_roles=msp_saml_roles,
            msp_saml_ssos=msp_saml_ssos,
            msp_setting=msp_setting,
            msp_export_data=msp_export_data,
            msp_adopt=msp_adopt,
            msp_add_devices=msp_add_devices,
            msp_add_adopt_device=msp_add_adopt_device,
            msp_webhook=msp_webhook,
            msp_sites=msp_sites,
            msp_cluster=msp_cluster,
            global_dashboard=global_dashboard,
            dashboard=dashboard,
            devices=devices,
            adopt=adopt,
            add_devices=add_devices,
            add_adopt_device=add_adopt_device,
            global_log=global_log,
            manual_upgrade=manual_upgrade,
            log=log,
            license_=license_,
            license_bind=license_bind,
            users=users,
            roles=roles,
            saml_users=saml_users,
            saml_roles=saml_roles,
            saml_ssos=saml_ssos,
            global_setting=global_setting,
            export_data=export_data,
            global_export_data=global_export_data,
            export_global_log=export_global_log,
            global_cluster=global_cluster,
            hotspot=hotspot,
            statics=statics,
            map_=map_,
            clients=clients,
            insight=insight,
            report=report,
            network=network,
            device_account=device_account,
            anomaly=anomaly,
            analyze=analyze,
            site_analyze=site_analyze,
            global_security=global_security,
            global_webhook=global_webhook,
            global_map_token=global_map_token,
            site_template=site_template,
            global_firmware=global_firmware,
            sd_wan=sd_wan,
            site_home=site_home,
            device_recovery=device_recovery,
            site_network=site_network,
            site_device=site_device,
            site_maintain=site_maintain,
            ai_assi=ai_assi,
        )

        role_vo.additional_properties = d
        return role_vo

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
