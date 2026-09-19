from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthTypeDistributionVO")


@_attrs_define
class AuthTypeDistributionVO:
    """
    Attributes:
        no_auth (int | Unset):
        simple_password (int | Unset):
        hotspot (int | Unset):
        facebook (int | Unset):
        external_radius (int | Unset):
        external_portal (int | Unset):
        ldap (int | Unset):
        google (int | Unset):
    """

    no_auth: int | Unset = UNSET
    simple_password: int | Unset = UNSET
    hotspot: int | Unset = UNSET
    facebook: int | Unset = UNSET
    external_radius: int | Unset = UNSET
    external_portal: int | Unset = UNSET
    ldap: int | Unset = UNSET
    google: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        no_auth = self.no_auth

        simple_password = self.simple_password

        hotspot = self.hotspot

        facebook = self.facebook

        external_radius = self.external_radius

        external_portal = self.external_portal

        ldap = self.ldap

        google = self.google

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_auth is not UNSET:
            field_dict["noAuth"] = no_auth
        if simple_password is not UNSET:
            field_dict["simplePassword"] = simple_password
        if hotspot is not UNSET:
            field_dict["hotspot"] = hotspot
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if external_radius is not UNSET:
            field_dict["externalRadius"] = external_radius
        if external_portal is not UNSET:
            field_dict["externalPortal"] = external_portal
        if ldap is not UNSET:
            field_dict["ldap"] = ldap
        if google is not UNSET:
            field_dict["google"] = google

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        no_auth = d.pop("noAuth", UNSET)

        simple_password = d.pop("simplePassword", UNSET)

        hotspot = d.pop("hotspot", UNSET)

        facebook = d.pop("facebook", UNSET)

        external_radius = d.pop("externalRadius", UNSET)

        external_portal = d.pop("externalPortal", UNSET)

        ldap = d.pop("ldap", UNSET)

        google = d.pop("google", UNSET)

        auth_type_distribution_vo = cls(
            no_auth=no_auth,
            simple_password=simple_password,
            hotspot=hotspot,
            facebook=facebook,
            external_radius=external_radius,
            external_portal=external_portal,
            ldap=ldap,
            google=google,
        )

        auth_type_distribution_vo.additional_properties = d
        return auth_type_distribution_vo

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
