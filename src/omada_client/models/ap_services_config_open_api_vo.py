from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ap_l3_access_vo import ApL3AccessVO
    from ..models.ap_mvlan_setting_open_api_vo import ApMvlanSettingOpenApiVO
    from ..models.ap_snmp_vo import ApSnmpVO
    from ..models.ap_voip_vlan_setting_open_api_vo import ApVoipVlanSettingOpenApiVO


T = TypeVar("T", bound="ApServicesConfigOpenApiVO")


@_attrs_define
class ApServicesConfigOpenApiVO:
    """
    Attributes:
        mvlan_setting (ApMvlanSettingOpenApiVO | Unset): Management VLAN setting.
        snmp (ApSnmpVO | Unset): Snmp Setting.
        l_3_access_setting (ApL3AccessVO | Unset): EAP L3 Accessibility setting.
        lldp_enable (int | Unset): Parameter [lldpEnable] should be a value as follows: 0:off; 1:on; 2:Use Site
            Settings.
        loopback_detect_enable (bool | Unset): Whether to enable loopback detection.
        voip_vlan_setting (ApVoipVlanSettingOpenApiVO | Unset): VoIP VLAN setting.
    """

    mvlan_setting: ApMvlanSettingOpenApiVO | Unset = UNSET
    snmp: ApSnmpVO | Unset = UNSET
    l_3_access_setting: ApL3AccessVO | Unset = UNSET
    lldp_enable: int | Unset = UNSET
    loopback_detect_enable: bool | Unset = UNSET
    voip_vlan_setting: ApVoipVlanSettingOpenApiVO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mvlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mvlan_setting, Unset):
            mvlan_setting = self.mvlan_setting.to_dict()

        snmp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.snmp, Unset):
            snmp = self.snmp.to_dict()

        l_3_access_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.l_3_access_setting, Unset):
            l_3_access_setting = self.l_3_access_setting.to_dict()

        lldp_enable = self.lldp_enable

        loopback_detect_enable = self.loopback_detect_enable

        voip_vlan_setting: dict[str, Any] | Unset = UNSET
        if not isinstance(self.voip_vlan_setting, Unset):
            voip_vlan_setting = self.voip_vlan_setting.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mvlan_setting is not UNSET:
            field_dict["mvlanSetting"] = mvlan_setting
        if snmp is not UNSET:
            field_dict["snmp"] = snmp
        if l_3_access_setting is not UNSET:
            field_dict["l3AccessSetting"] = l_3_access_setting
        if lldp_enable is not UNSET:
            field_dict["lldpEnable"] = lldp_enable
        if loopback_detect_enable is not UNSET:
            field_dict["loopbackDetectEnable"] = loopback_detect_enable
        if voip_vlan_setting is not UNSET:
            field_dict["voipVlanSetting"] = voip_vlan_setting

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        from ..models.ap_l3_access_vo import ApL3AccessVO
        from ..models.ap_mvlan_setting_open_api_vo import (
            ApMvlanSettingOpenApiVO,
        )
        from ..models.ap_snmp_vo import ApSnmpVO
        from ..models.ap_voip_vlan_setting_open_api_vo import (
            ApVoipVlanSettingOpenApiVO,
        )

        d = dict(src_dict)
        _mvlan_setting = d.pop("mvlanSetting", UNSET)
        mvlan_setting: ApMvlanSettingOpenApiVO | Unset
        if isinstance(_mvlan_setting, Unset):
            mvlan_setting = UNSET
        else:
            mvlan_setting = ApMvlanSettingOpenApiVO.from_dict(_mvlan_setting)

        _snmp = d.pop("snmp", UNSET)
        snmp: ApSnmpVO | Unset
        if isinstance(_snmp, Unset):
            snmp = UNSET
        else:
            snmp = ApSnmpVO.from_dict(_snmp)

        _l_3_access_setting = d.pop("l3AccessSetting", UNSET)
        l_3_access_setting: ApL3AccessVO | Unset
        if isinstance(_l_3_access_setting, Unset):
            l_3_access_setting = UNSET
        else:
            l_3_access_setting = ApL3AccessVO.from_dict(_l_3_access_setting)

        lldp_enable = d.pop("lldpEnable", UNSET)

        loopback_detect_enable = d.pop("loopbackDetectEnable", UNSET)

        _voip_vlan_setting = d.pop("voipVlanSetting", UNSET)
        voip_vlan_setting: ApVoipVlanSettingOpenApiVO | Unset
        if isinstance(_voip_vlan_setting, Unset):
            voip_vlan_setting = UNSET
        else:
            voip_vlan_setting = ApVoipVlanSettingOpenApiVO.from_dict(_voip_vlan_setting)

        ap_services_config_open_api_vo = cls(
            mvlan_setting=mvlan_setting,
            snmp=snmp,
            l_3_access_setting=l_3_access_setting,
            lldp_enable=lldp_enable,
            loopback_detect_enable=loopback_detect_enable,
            voip_vlan_setting=voip_vlan_setting,
        )

        ap_services_config_open_api_vo.additional_properties = d
        return ap_services_config_open_api_vo

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
