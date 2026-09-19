from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="SnmpSettingOpenApiVO")


@_attrs_define
class SnmpSettingOpenApiVO:
    """
    Attributes:
        snmp_v1v2c_enable (bool): SNMPv1 & SNMPv2c enable status
        snmp_v3_enable (bool): SNMPv3 enable status
        community_string (str | Unset): Community string, valid when parameter [snmpV1V2CEnable] is true. The
            communityString should contain at least 10 characters, using a combination of numbers, letters or special
            characters.
            The communityString should not contain consecutive identical characters.
        username (str | Unset): Username, valid when parameter [snmpV3Enable] is true. Username should contain 1 to 30
            characters
        password (str | Unset): The password should contain at least 10 characters, using a combination of numbers,
            letters or special characters.
            The password should not contain consecutive identical characters.
            Username and Password should not be the same.
        security_level (int | Unset): Security Level should be a value as follows: 0: NoAuthNoPriv; 1: AuthNoPriv; 2:
            AuthPriv
        auth_mode (int | Unset): Authentication Mode should be a value as follows: 1: MD5; 2: SHA. When Security Level
            is AuthNoPriv or AuthPriv, this field is required
        privacy_mode (int | Unset): Privacy Mode should be a value as follows: 1: DES; 2: AES. When Security Level is
            AuthPriv, this field is required
        privacy_password (str | Unset): The privacy password should contain at least 10 characters, using a combination
            of numbers, letters or special characters.
            The privacy password should not contain consecutive identical characters.
            Username and privacy password should not be the same.
        location (str | Unset): Location
        contact (str | Unset): Contact
    """

    snmp_v1v2c_enable: bool
    snmp_v3_enable: bool
    community_string: str | Unset = UNSET
    username: str | Unset = UNSET
    password: str | Unset = UNSET
    security_level: int | Unset = UNSET
    auth_mode: int | Unset = UNSET
    privacy_mode: int | Unset = UNSET
    privacy_password: str | Unset = UNSET
    location: str | Unset = UNSET
    contact: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        snmp_v1v2c_enable = self.snmp_v1v2c_enable

        snmp_v3_enable = self.snmp_v3_enable

        community_string = self.community_string

        username = self.username

        password = self.password

        security_level = self.security_level

        auth_mode = self.auth_mode

        privacy_mode = self.privacy_mode

        privacy_password = self.privacy_password

        location = self.location

        contact = self.contact

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "snmpV1V2CEnable": snmp_v1v2c_enable,
                "snmpV3Enable": snmp_v3_enable,
            }
        )
        if community_string is not UNSET:
            field_dict["communityString"] = community_string
        if username is not UNSET:
            field_dict["username"] = username
        if password is not UNSET:
            field_dict["password"] = password
        if security_level is not UNSET:
            field_dict["securityLevel"] = security_level
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if privacy_mode is not UNSET:
            field_dict["privacyMode"] = privacy_mode
        if privacy_password is not UNSET:
            field_dict["privacyPassword"] = privacy_password
        if location is not UNSET:
            field_dict["location"] = location
        if contact is not UNSET:
            field_dict["contact"] = contact

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        snmp_v1v2c_enable = d.pop("snmpV1V2CEnable")

        snmp_v3_enable = d.pop("snmpV3Enable")

        community_string = d.pop("communityString", UNSET)

        username = d.pop("username", UNSET)

        password = d.pop("password", UNSET)

        security_level = d.pop("securityLevel", UNSET)

        auth_mode = d.pop("authMode", UNSET)

        privacy_mode = d.pop("privacyMode", UNSET)

        privacy_password = d.pop("privacyPassword", UNSET)

        location = d.pop("location", UNSET)

        contact = d.pop("contact", UNSET)

        snmp_setting_open_api_vo = cls(
            snmp_v1v2c_enable=snmp_v1v2c_enable,
            snmp_v3_enable=snmp_v3_enable,
            community_string=community_string,
            username=username,
            password=password,
            security_level=security_level,
            auth_mode=auth_mode,
            privacy_mode=privacy_mode,
            privacy_password=privacy_password,
            location=location,
            contact=contact,
        )

        snmp_setting_open_api_vo.additional_properties = d
        return snmp_setting_open_api_vo

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
