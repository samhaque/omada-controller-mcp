from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="MspRoleVO")


@_attrs_define
class MspRoleVO:
    """Role privilege.

    Attributes:
        msp_dashboard (int | Unset): Msp dashboard permission. It should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_device (int | Unset): Msp device. It should be a value as follows: 0:block; 1:view only; 2:modify
        msp_log (int | Unset): Msp log. It should be a value as follows: 0:block; 1:view only; 2:modify
        msp_license (int | Unset): Msp license. It should be a value as follows: 0:block; 1:view only; 2:modify
        msp_license_bind (int | Unset): msp license bind
        msp_adopt (int | Unset): Msp adopt. It should be a value as follows: 0:block; 2:access
        msp_add_devices (int | Unset): Msp add devices. It should be a value as follows: 0:block; 2:access
        msp_add_adopt_device (int | Unset): Msp add and adopt devices. It should be a value as follows: 0:block;
            2:access
        msp_users (int | Unset): Msp users. It should be a value as follows: 0:block; 1:view only; 2:modify
        msp_roles (int | Unset): Msp roles. It should be a value as follows: 0:block; 1:view only; 2:modify
        msp_saml_users (int | Unset): Saml users in msp view. It should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_saml_roles (int | Unset): Saml roles in msp view. It should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_saml_ssos (int | Unset): Saml ssos in msp view. It should be a value as follows: 0:block; 1:view only;
            2:modify
        msp_setting (int | Unset): Msp setting. It should be a value as follows: 0:block; 1:view only; 2:modify
        msp_export_data (int | Unset): Export data in msp view. It should be a value as follows: 0:block; 2:access
        msp_webhook (int | Unset): Msp webhook. It should be a value as follows: 0:block; 1:view only; 2:modify
        msp_sites (int | Unset): Msp sites. It should be a value as follows: 0:block; 2:access
        msp_cluster (int | Unset): msp cluster, 0:block; 1:view only; 2:modify
        ai_assi (int | Unset): AI Assistant, it should be a value as follows: 0:block; 1:view only; 2:modify
    """

    msp_dashboard: int | Unset = UNSET
    msp_device: int | Unset = UNSET
    msp_log: int | Unset = UNSET
    msp_license: int | Unset = UNSET
    msp_license_bind: int | Unset = UNSET
    msp_adopt: int | Unset = UNSET
    msp_add_devices: int | Unset = UNSET
    msp_add_adopt_device: int | Unset = UNSET
    msp_users: int | Unset = UNSET
    msp_roles: int | Unset = UNSET
    msp_saml_users: int | Unset = UNSET
    msp_saml_roles: int | Unset = UNSET
    msp_saml_ssos: int | Unset = UNSET
    msp_setting: int | Unset = UNSET
    msp_export_data: int | Unset = UNSET
    msp_webhook: int | Unset = UNSET
    msp_sites: int | Unset = UNSET
    msp_cluster: int | Unset = UNSET
    ai_assi: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        msp_dashboard = self.msp_dashboard

        msp_device = self.msp_device

        msp_log = self.msp_log

        msp_license = self.msp_license

        msp_license_bind = self.msp_license_bind

        msp_adopt = self.msp_adopt

        msp_add_devices = self.msp_add_devices

        msp_add_adopt_device = self.msp_add_adopt_device

        msp_users = self.msp_users

        msp_roles = self.msp_roles

        msp_saml_users = self.msp_saml_users

        msp_saml_roles = self.msp_saml_roles

        msp_saml_ssos = self.msp_saml_ssos

        msp_setting = self.msp_setting

        msp_export_data = self.msp_export_data

        msp_webhook = self.msp_webhook

        msp_sites = self.msp_sites

        msp_cluster = self.msp_cluster

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
        if msp_adopt is not UNSET:
            field_dict["mspAdopt"] = msp_adopt
        if msp_add_devices is not UNSET:
            field_dict["mspAddDevices"] = msp_add_devices
        if msp_add_adopt_device is not UNSET:
            field_dict["mspAddAdoptDevice"] = msp_add_adopt_device
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
        if msp_webhook is not UNSET:
            field_dict["mspWebhook"] = msp_webhook
        if msp_sites is not UNSET:
            field_dict["mspSites"] = msp_sites
        if msp_cluster is not UNSET:
            field_dict["mspCluster"] = msp_cluster
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

        msp_adopt = d.pop("mspAdopt", UNSET)

        msp_add_devices = d.pop("mspAddDevices", UNSET)

        msp_add_adopt_device = d.pop("mspAddAdoptDevice", UNSET)

        msp_users = d.pop("mspUsers", UNSET)

        msp_roles = d.pop("mspRoles", UNSET)

        msp_saml_users = d.pop("mspSamlUsers", UNSET)

        msp_saml_roles = d.pop("mspSamlRoles", UNSET)

        msp_saml_ssos = d.pop("mspSamlSsos", UNSET)

        msp_setting = d.pop("mspSetting", UNSET)

        msp_export_data = d.pop("mspExportData", UNSET)

        msp_webhook = d.pop("mspWebhook", UNSET)

        msp_sites = d.pop("mspSites", UNSET)

        msp_cluster = d.pop("mspCluster", UNSET)

        ai_assi = d.pop("aiAssi", UNSET)

        msp_role_vo = cls(
            msp_dashboard=msp_dashboard,
            msp_device=msp_device,
            msp_log=msp_log,
            msp_license=msp_license,
            msp_license_bind=msp_license_bind,
            msp_adopt=msp_adopt,
            msp_add_devices=msp_add_devices,
            msp_add_adopt_device=msp_add_adopt_device,
            msp_users=msp_users,
            msp_roles=msp_roles,
            msp_saml_users=msp_saml_users,
            msp_saml_roles=msp_saml_roles,
            msp_saml_ssos=msp_saml_ssos,
            msp_setting=msp_setting,
            msp_export_data=msp_export_data,
            msp_webhook=msp_webhook,
            msp_sites=msp_sites,
            msp_cluster=msp_cluster,
            ai_assi=ai_assi,
        )

        msp_role_vo.additional_properties = d
        return msp_role_vo

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
