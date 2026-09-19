from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from typing_extensions import Self

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdpMetadataOpenApiVO")


@_attrs_define
class IdpMetadataOpenApiVO:
    """
    Attributes:
        name (str): IdP name should contain 1 to 32 characters.
        entity_id (str): The IdP entity id which must be unique in same Omadac.
        login_url (str): Login url
        x_509_certificate (str): BASE64 encoded string of x509 certificate.
        description (str | Unset): IdP description should contain 0 to 128 characters.
    """

    name: str
    entity_id: str
    login_url: str
    x_509_certificate: str
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        entity_id = self.entity_id

        login_url = self.login_url

        x_509_certificate = self.x_509_certificate

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "entityId": entity_id,
                "loginUrl": login_url,
                "x509Certificate": x_509_certificate,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls, src_dict: Mapping[str, Any]) -> Self:
        d = dict(src_dict)
        name = d.pop("name")

        entity_id = d.pop("entityId")

        login_url = d.pop("loginUrl")

        x_509_certificate = d.pop("x509Certificate")

        description = d.pop("description", UNSET)

        idp_metadata_open_api_vo = cls(
            name=name,
            entity_id=entity_id,
            login_url=login_url,
            x_509_certificate=x_509_certificate,
            description=description,
        )

        idp_metadata_open_api_vo.additional_properties = d
        return idp_metadata_open_api_vo

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
