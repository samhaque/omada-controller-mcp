from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateGoogleLdapProfileOpenApiVO")


@_attrs_define
class CreateGoogleLdapProfileOpenApiVO:
    """Configuration of google LDAP profile, need to specify Content-Type of this form part as application/json.

    Attributes:
        name (str): Google LDAP profile name. Name should contain 1 to 64 characters.
        status (bool): LDAP profile enable status.
        bind_type (int): Type of LDAP bind. BindType should be a value as follows: 0: Simple Mode; 2: Regular Mode.
        server (str): LDAP server address.
        port (int): LDAP server listening port. dstPort should be within the range of 0-65535. It is generally 636.
        cn (str): LDAP server common name, for example: cn, uid. Cn should contain 1 to 64 characters.
        base_dn (str): LDAP server base distinguish name, for example: dc=xxx,dc=com. BaseDn should contain 1 to 512
            characters.
        filter_ (str | Unset): Additional filter, optional when parameter [type] is 1 or 2. For example: ou=xxx. Filter
            should contain 1 to 512 characters.
        account (str | Unset): Account, required when parameter [type] is 2. account should contain 1 to 256 characters.
        password (str | Unset): Password, required when parameter [type] is 2. password should contain 6 to 256
            characters.
    """

    name: str
    status: bool
    bind_type: int
    server: str
    port: int
    cn: str
    base_dn: str
    filter_: str | Unset = UNSET
    account: str | Unset = UNSET
    password: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status

        bind_type = self.bind_type

        server = self.server

        port = self.port

        cn = self.cn

        base_dn = self.base_dn

        filter_ = self.filter_

        account = self.account

        password = self.password

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
                "bindType": bind_type,
                "server": server,
                "port": port,
                "cn": cn,
                "baseDn": base_dn,
            }
        )
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if account is not UNSET:
            field_dict["account"] = account
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        status = d.pop("status")

        bind_type = d.pop("bindType")

        server = d.pop("server")

        port = d.pop("port")

        cn = d.pop("cn")

        base_dn = d.pop("baseDn")

        filter_ = d.pop("filter", UNSET)

        account = d.pop("account", UNSET)

        password = d.pop("password", UNSET)

        create_google_ldap_profile_open_api_vo = cls(
            name=name,
            status=status,
            bind_type=bind_type,
            server=server,
            port=port,
            cn=cn,
            base_dn=base_dn,
            filter_=filter_,
            account=account,
            password=password,
        )

        create_google_ldap_profile_open_api_vo.additional_properties = d
        return create_google_ldap_profile_open_api_vo

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
