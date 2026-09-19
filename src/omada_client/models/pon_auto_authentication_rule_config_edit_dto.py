from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="PonAutoAuthenticationRuleConfigEditDTO")


@_attrs_define
class PonAutoAuthenticationRuleConfigEditDTO:
    """
    Attributes:
        key (str): Identifier of entry
        pon_port (str): Pon port.e.g.GPON 1/0/1
        rule_id (int): Rule ID should be within the range of 1 to 128
        line_profile (str): Line profile id
        service_profile (str): Service profile id
        equip_id (str | Unset): Matched ONT ID.EquipId should contain 1 to 20 characters in ASCII (from \\x21 to \\x7e).
        vendor_id (str | Unset): Matched ONU vendor ID.VendorId should contain 1 to 4 characters in ASCII (from \\x21 to
            \\x7e).
        software_version (str | Unset): Software version should contain 1 to 14 characters, consisting of:Uppercase and
            lowercase letters,Digits,Special characters: -, @, _, :, /, .
        line_profile_name (str | Unset): Line profile name
        service_profile_name (str | Unset): Service profile name
        service_port_profile (str | Unset): Service port profile id bound to the ONU
    """

    key: str
    pon_port: str
    rule_id: int
    line_profile: str
    service_profile: str
    equip_id: str | Unset = UNSET
    vendor_id: str | Unset = UNSET
    software_version: str | Unset = UNSET
    line_profile_name: str | Unset = UNSET
    service_profile_name: str | Unset = UNSET
    service_port_profile: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        pon_port = self.pon_port

        rule_id = self.rule_id

        line_profile = self.line_profile

        service_profile = self.service_profile

        equip_id = self.equip_id

        vendor_id = self.vendor_id

        software_version = self.software_version

        line_profile_name = self.line_profile_name

        service_profile_name = self.service_profile_name

        service_port_profile = self.service_port_profile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "ponPort": pon_port,
                "ruleId": rule_id,
                "lineProfile": line_profile,
                "serviceProfile": service_profile,
            }
        )
        if equip_id is not UNSET:
            field_dict["equipId"] = equip_id
        if vendor_id is not UNSET:
            field_dict["vendorId"] = vendor_id
        if software_version is not UNSET:
            field_dict["softwareVersion"] = software_version
        if line_profile_name is not UNSET:
            field_dict["lineProfileName"] = line_profile_name
        if service_profile_name is not UNSET:
            field_dict["serviceProfileName"] = service_profile_name
        if service_port_profile is not UNSET:
            field_dict["servicePortProfile"] = service_port_profile

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        key = d.pop("key")

        pon_port = d.pop("ponPort")

        rule_id = d.pop("ruleId")

        line_profile = d.pop("lineProfile")

        service_profile = d.pop("serviceProfile")

        equip_id = d.pop("equipId", UNSET)

        vendor_id = d.pop("vendorId", UNSET)

        software_version = d.pop("softwareVersion", UNSET)

        line_profile_name = d.pop("lineProfileName", UNSET)

        service_profile_name = d.pop("serviceProfileName", UNSET)

        service_port_profile = d.pop("servicePortProfile", UNSET)

        pon_auto_authentication_rule_config_edit_dto = cls(
            key=key,
            pon_port=pon_port,
            rule_id=rule_id,
            line_profile=line_profile,
            service_profile=service_profile,
            equip_id=equip_id,
            vendor_id=vendor_id,
            software_version=software_version,
            line_profile_name=line_profile_name,
            service_profile_name=service_profile_name,
            service_port_profile=service_port_profile,
        )

        pon_auto_authentication_rule_config_edit_dto.additional_properties = d
        return pon_auto_authentication_rule_config_edit_dto

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
