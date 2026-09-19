from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapSetting")


@_attrs_define
class LdapSetting:
    """Ldap Portal Setting.

    Attributes:
        ldap_profile_id (str): LDAP profile ID. Ldap profile can be  created using 'Create a new LDAP profile' ('Create
            a new LDAP profile template') interface, and LDAP profile ID can be obtained from 'Get LDAP profile list' ('Get
            LDAP profile template list') interface
        portal_custom (int): Portal customization, should be a value as follows: 1: use local; 2: use external
        external_url_scheme (str | Unset): External URL scheme, should be a value as follows: http ; https. Required
            when portalCustom is 2.
        external_url (str | Unset): External URL. Required when portalCustom is 2.
    """

    ldap_profile_id: str
    portal_custom: int
    external_url_scheme: str | Unset = UNSET
    external_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ldap_profile_id = self.ldap_profile_id

        portal_custom = self.portal_custom

        external_url_scheme = self.external_url_scheme

        external_url = self.external_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ldapProfileId": ldap_profile_id,
                "portalCustom": portal_custom,
            }
        )
        if external_url_scheme is not UNSET:
            field_dict["externalUrlScheme"] = external_url_scheme
        if external_url is not UNSET:
            field_dict["externalUrl"] = external_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ldap_profile_id = d.pop("ldapProfileId")

        portal_custom = d.pop("portalCustom")

        external_url_scheme = d.pop("externalUrlScheme", UNSET)

        external_url = d.pop("externalUrl", UNSET)

        ldap_setting = cls(
            ldap_profile_id=ldap_profile_id,
            portal_custom=portal_custom,
            external_url_scheme=external_url_scheme,
            external_url=external_url,
        )

        ldap_setting.additional_properties = d
        return ldap_setting

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
