from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateLdapProfileOpenApiVO")


@_attrs_define
class CreateLdapProfileOpenApiVO:
    """
    Attributes:
        name (str): LDAP profile name. Name should contain 1 to 64 characters
        status (bool): LDAP profile enable status
        bind_type (int): Type of LDAP bind. BindType should be a value as follows: 0: Simple Mode; 1: Anonymous Mode; 2:
            Regular Mode
        server (str): LDAP server address
        dst_port (int): LDAP server listening port. dstPort should be within the range of 0-65535. When SSL is not
            enabled, it is generally 389, and when SSL is enabled, it is generally 636
        use_ssl (bool): LDAP server enable ssl status
        cn (str): LDAP server common name, for example: cn, uid. Cn should contain 1 to 64 characters
        base_dn (str): LDAP server base distinguish name, for example: dc=xxx,dc=com. BaseDn should contain 1 to 512
            characters.
        group_dn (str | Unset): LDAP server group distinguish name, optional when parameter [type] is 1 or 2. For
            example: ou=xxx,dc=xxx,dc=com. GroupDn should contain 1 to 512 characters
        filter_ (str | Unset): Additional filter, optional when parameter [type] is 1 or 2. For example: ou=xxx. Filter
            should contain 1 to 512 characters
        regular_dn (str | Unset): Regular Dn, required when parameter [type] is 2. RegularDn should contain 1 to 256
            characters
        regular_password (str | Unset): Regular Password, required when parameter [type] is 2. RegularPassword should
            contain 1 to 256 characters
    """

    name: str
    status: bool
    bind_type: int
    server: str
    dst_port: int
    use_ssl: bool
    cn: str
    base_dn: str
    group_dn: str | Unset = UNSET
    filter_: str | Unset = UNSET
    regular_dn: str | Unset = UNSET
    regular_password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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
        field_dict.update(
            {
                "name": name,
                "status": status,
                "bindType": bind_type,
                "server": server,
                "dstPort": dst_port,
                "useSsl": use_ssl,
                "cn": cn,
                "baseDn": base_dn,
            }
        )
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
        name = d.pop("name")

        status = d.pop("status")

        bind_type = d.pop("bindType")

        server = d.pop("server")

        dst_port = d.pop("dstPort")

        use_ssl = d.pop("useSsl")

        cn = d.pop("cn")

        base_dn = d.pop("baseDn")

        group_dn = d.pop("groupDn", UNSET)

        filter_ = d.pop("filter", UNSET)

        regular_dn = d.pop("regularDn", UNSET)

        regular_password = d.pop("regularPassword", UNSET)

        create_ldap_profile_open_api_vo = cls(
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

        create_ldap_profile_open_api_vo.additional_properties = d
        return create_ldap_profile_open_api_vo

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
