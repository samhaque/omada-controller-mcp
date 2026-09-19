from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdpMetadataDetailOpenApiVO")


@_attrs_define
class IdpMetadataDetailOpenApiVO:
    """
    Attributes:
        idp_id (str | Unset): IdP ID(resource ID).
        name (str | Unset): IdP name.
        description (str | Unset): Description.
        entity_id (str | Unset): The IdP entity ID which must be unique in same Omadac.
        login_url (str | Unset): Login url.
        x_509_certificate (str | Unset): BASE64 encoded string of x509 certificate.
        entity_url (str | Unset): Entity url.
        sign_on_url (str | Unset): Sign On url.
    """

    idp_id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    entity_id: str | Unset = UNSET
    login_url: str | Unset = UNSET
    x_509_certificate: str | Unset = UNSET
    entity_url: str | Unset = UNSET
    sign_on_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        idp_id = self.idp_id

        name = self.name

        description = self.description

        entity_id = self.entity_id

        login_url = self.login_url

        x_509_certificate = self.x_509_certificate

        entity_url = self.entity_url

        sign_on_url = self.sign_on_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idp_id is not UNSET:
            field_dict["idpId"] = idp_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if login_url is not UNSET:
            field_dict["loginUrl"] = login_url
        if x_509_certificate is not UNSET:
            field_dict["x509Certificate"] = x_509_certificate
        if entity_url is not UNSET:
            field_dict["entityUrl"] = entity_url
        if sign_on_url is not UNSET:
            field_dict["signOnUrl"] = sign_on_url

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        idp_id = d.pop("idpId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        entity_id = d.pop("entityId", UNSET)

        login_url = d.pop("loginUrl", UNSET)

        x_509_certificate = d.pop("x509Certificate", UNSET)

        entity_url = d.pop("entityUrl", UNSET)

        sign_on_url = d.pop("signOnUrl", UNSET)

        idp_metadata_detail_open_api_vo = cls(
            idp_id=idp_id,
            name=name,
            description=description,
            entity_id=entity_id,
            login_url=login_url,
            x_509_certificate=x_509_certificate,
            entity_url=entity_url,
            sign_on_url=sign_on_url,
        )

        idp_metadata_detail_open_api_vo.additional_properties = d
        return idp_metadata_detail_open_api_vo

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
