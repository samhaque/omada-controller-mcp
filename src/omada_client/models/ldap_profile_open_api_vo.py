from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="LdapProfileOpenApiVO")


@_attrs_define
class LdapProfileOpenApiVO:
    """
    Attributes:
        ldap_profile_id (str | Unset): LDAP profile ID
        name (str | Unset): LDAP profile name
        status (bool | Unset): LDAP profile enable status
        bind_type (int | Unset): Type of LDAP bind, 0: Simple Mode；1: Anonymous Mode; 2: Regular Mode
        server (str | Unset): LDAP server address
        dst_port (int | Unset): LDAP server listening port. When SSL is not enabled, it is generally 389, and when SSL
            is enabled, it is generally 636
        use_ssl (bool | Unset): LDAP server enable ssl status
        cn (str | Unset): LDAP server common name
        base_dn (str | Unset): LDAP server base distinguish name
        group_dn (str | Unset): LDAP server group distinguish name, optional when parameter [type] is 1 or 2
        filter_ (str | Unset): Additional filter, optional when parameter [type] is 1 or 2
        regular_dn (str | Unset): Regular Dn, valid when parameter [type] is 2
        regular_password (str | Unset): Regular Password, valid when parameter [type] is 2
    """

    ldap_profile_id: str | Unset = UNSET
    name: str | Unset = UNSET
    status: bool | Unset = UNSET
    bind_type: int | Unset = UNSET
    server: str | Unset = UNSET
    dst_port: int | Unset = UNSET
    use_ssl: bool | Unset = UNSET
    cn: str | Unset = UNSET
    base_dn: str | Unset = UNSET
    group_dn: str | Unset = UNSET
    filter_: str | Unset = UNSET
    regular_dn: str | Unset = UNSET
    regular_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ldap_profile_id = self.ldap_profile_id

        name = self.name

        status = self.status

        bind_type = self.bind_type

        server = self.server

        dst_port = self.dst_port

        use_ssl = self.use_ssl

        cn = self.cn

        base_dn = self.base_dn

        group_dn = self.group_dn

        filter_ = self.filter_

        regular_dn = self.regular_dn

        regular_password = self.regular_password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ldap_profile_id is not UNSET:
            field_dict["ldapProfileId"] = ldap_profile_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if bind_type is not UNSET:
            field_dict["bindType"] = bind_type
        if server is not UNSET:
            field_dict["server"] = server
        if dst_port is not UNSET:
            field_dict["dstPort"] = dst_port
        if use_ssl is not UNSET:
            field_dict["useSsl"] = use_ssl
        if cn is not UNSET:
            field_dict["cn"] = cn
        if base_dn is not UNSET:
            field_dict["baseDn"] = base_dn
        if group_dn is not UNSET:
            field_dict["groupDn"] = group_dn
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if regular_dn is not UNSET:
            field_dict["regularDn"] = regular_dn
        if regular_password is not UNSET:
            field_dict["regularPassword"] = regular_password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        ldap_profile_id = d.pop("ldapProfileId", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        bind_type = d.pop("bindType", UNSET)

        server = d.pop("server", UNSET)

        dst_port = d.pop("dstPort", UNSET)

        use_ssl = d.pop("useSsl", UNSET)

        cn = d.pop("cn", UNSET)

        base_dn = d.pop("baseDn", UNSET)

        group_dn = d.pop("groupDn", UNSET)

        filter_ = d.pop("filter", UNSET)

        regular_dn = d.pop("regularDn", UNSET)

        regular_password = d.pop("regularPassword", UNSET)

        ldap_profile_open_api_vo = cls(
            ldap_profile_id=ldap_profile_id,
            name=name,
            status=status,
            bind_type=bind_type,
            server=server,
            dst_port=dst_port,
            use_ssl=use_ssl,
            cn=cn,
            base_dn=base_dn,
            group_dn=group_dn,
            filter_=filter_,
            regular_dn=regular_dn,
            regular_password=regular_password,
        )

        ldap_profile_open_api_vo.additional_properties = d
        return ldap_profile_open_api_vo

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
